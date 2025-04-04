"""Read and parse NIMS file.

----------
TODO
----------

----------

Notes
-----
* NIMS Data Packet Breakdown - 1 Hz:
Byte 1      h'01    SOH - Start of Packet
Byte 2      h'19    Packet Length (d'25)
Byte 3              Status Byte:
b'0     (LSB) General Alarm Bit
b'1     X-ranging: The X-component has changed bins at the beginning
of this data block.
b'2     Y-ranging: The X-component has changed bins at the beginning
of this data block.
b'3     Z-ranging: The X-component has changed bins at the beginning
of this data block.
b'4     X-out of range: magnetometer cannot home
b'5     Y-out of range: magnetometer cannot home
b'6     Z-out of range: magnetometer cannot home
b'7     1 Hz clock not valid for this data block
Byte 4              GPS Byte or Telluric Amplifier Gain:
h'00    Power-on initialization prior to first GPS lock and sync
h'C7    Power has been applied to the GPS receiver for a NIMS resync
h'D3    Power has been applied to the GPS receiver
h'C8    High gain, both telluric channels
h'CC    Low gain, both telluric channels
h'D8    High gain on X, low gain on Y
h'D9    Low gain on X, high gain on Y
Byte 5              Sequence byte (h'00 - h'FF)
Byte 6,7            Electronics unit temperature - twos compliment
Byte 8,9            Head temperature - twos compliment
Byte 10-12          Hx sample, twos compliment, MSB - LSB
Byte 13-15          Hy sample, twos compliment, MSB - LSB
Byte 16-18          Hz sample, twos compliment, MSB - LSB
Byte 19-21          Ex sample, twos compliment, MSB - LSB
Byte 22-24          Ey sample, twos compliment, MSB - LSB
Byte 25     h'04    EOH - End of Packet
"""

import re
import sys
from datetime import timedelta
from multiprocessing import Queue
from pathlib import Path
from timeit import default_timer as timer
from typing import Optional

import numpy as np
import polars as pl

from mttools_lib.utils import nmea

from ..base import EMDataBase
from ..utils import StatusFlags, dump
from .errors import NimsGeneralError, NimsHeaderError


class HeaderParser:
    """Class to parse NIMS files.

    Typical header example:

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #>>>user field>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    SITE NAME: Budweiser Spring
    STATE/PROVINCE: CA
    COUNTRY: USA
    #>>> The following code in double quotes is REQUIRED to start the NIMS <<
    #>>> The next 3 lines contain values required for processing <<<<<<<<<<<<
    #>>> The lines after that are optional <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    "CAV09d"  <-- 2 CHAR EXPERIMENT CODE + 3 CHAR SITE CODE + RUN LETTER
    2612-01; 2612-01  <-- SYSTEM BOX I.D.; MAG HEAD ID (if different)
    106  0 <-- N-S Ex WIRE LENGTH (m); HEADING (deg E mag N)
    109  90 <-- E-W Ey WIRE LENGTH (m); HEADING (deg E mag N)
    1         <-- N ELECTRODE ID
    3          <-- E ELECTRODE ID
    2          <-- S ELECTRODE ID
    4          <-- W ELECTRODE ID
    Cu          <-- GROUND ELECTRODE INFO
    GPS INFO: 01/10/19 16:16:42 1616.7000 3443.6088 115.7350 W 946.6
    OPERATOR: KP
    COMMENT: N/S CRS: .95/.96 DCV: 3.5 ACV:1
    E/W CRS: .85/.86 DCV: 1.5 ACV: 1
    Redeployed site for run b because possible animal disturbance
    """

    MAX_LENGTH = 5_000
    BLOCK_LENGTH = 2_500
    PACKET_FLAG = {  # noqa: RUF012
        "1HZ": b"\x01\x19",
        "8HZ": b"\x01\x81",
    }

    @staticmethod
    def read_header(buffer: bytes, flag: str = "1HZ") -> str:
        """Read the header from a NIMS file.

        Parameters
        ----------
        buffer : bytes
            Buffer to read the header from.
        flag : str, optional
            Flag to indicate the type of NIMS file, by default '1HZ'

        Returns
        -------
        str
            Header from the NIMS file.
        """
        index = buffer.find(HeaderParser.PACKET_FLAG[flag])

        if index == -1:
            raise NimsHeaderError("Can't find start of time series")

        header = buffer[:index]

        return header.decode("utf-8", errors="ignore")

    @staticmethod
    def temperature_conversion(ts: np.ndarray) -> np.ndarray:
        """Convert the temperature samples to degrees Celsius."""
        return (ts - 18_048) / 70

    @staticmethod
    def shift_temperature(ts: np.ndarray) -> np.ndarray:
        """Shift the temperature samples to the correct digitizer value.

        Temperature (C) = (sample - 18,048) / 70
        """
        return ts - 18_048

    @staticmethod
    def search(buff: str, pattern: str) -> str:
        """Search for a pattern in the buffer."""
        try:
            result = re.findall(pattern, buff, re.MULTILINE)[0]
        except IndexError:
            result = ""

        return str(result.strip())

    @staticmethod
    def parse_electrode_layout(buff: str, pattern: str) -> tuple[float, float]:
        """Parse data from metadata.

        ^ match start of line
        () capture the expression inside the parentheses
        .*? match anything, non-greedily
        """
        result = HeaderParser.search(buff, pattern)
        length = HeaderParser.search(result, r"^(.*?)\s")
        azimuth = HeaderParser.search(result, r"\s(.*?)$")

        return float(azimuth), float(length)


class Nims(EMDataBase):
    """Class to parse NIMS files."""

    PACKET_FLAG = {  # noqa: RUF012
        "1HZ": b"\x01\x19",
        "8HZ": b"\x01\x81",
    }
    PACKET_SIZE = {  # noqa: RUF012
        "1HZ": 25,
        "8HZ": 200,
    }  # TODO: Change 8Hz to correct size
    SAMPLE_RATE = {  # noqa: RUF012
        "1HZ": 1,
        "8HZ": 8,
    }
    MISSING_VALUE = 44_444_444

    def __init__(self, file_path: Path | None = None):
        super().__init__()
        self.metadata.system = "NIMS"
        self._file_path = file_path

        self._packet_flag: bytes = b"\x01\x19"
        self._packet_size: int = 25
        self._header_size: int = 0
        self._sample_rate: int = 1

    def _determine_sample_rate(self, buff: bytes) -> None:
        """Determine the sample rate of the data file.

        Parameters
        ----------
        buff : bytes
            The data block from the file

        """
        index = -1
        for key in self.PACKET_FLAG:
            index = buff.find(self.PACKET_FLAG[key])
            if index != -1:
                self._packet_flag = self.PACKET_FLAG[key]
                self._packet_size = self.PACKET_SIZE[key]
                self._sample_rate = self.SAMPLE_RATE[key]
                self._header_size = index
                return

        if index == -1:
            raise NimsHeaderError("Can't find start of time series")

    def parse_metadata(self) -> None:
        """Parse the metadata from the file header."""
        station_pattern = r"\"(.*)\".*<-- 2"
        site_name_pattern = r"SITE NAME:(.*?)$"
        state_province_pattern = r"STATE/PROVINCE:(.*?)$"
        country_pattern = r"COUNTRY:(.*?)$"
        box_sn_pattern = r"^(.*?);.*<-- SYS"
        mag_sn_pattern = r"^.*;(.*?)<-- SYS"
        ex_layout_pattern = r"^(.*?)<-- N-S"
        ey_layout_pattern = r"^(.*?)<-- E-W"
        operator_pattern = r"(?:OPERATOR: |OPERATOR: )(.*?)$"
        comments_pattern = r"COMMENTS: ((?:.*\s*)*)"

        component_order = {
            "Hx": 0,
            "Hy": 1,
            "Hz": 2,
            "Ex": 3,
            "Ey": 4,
            "TB": 5,
            "TH": 6,
        }
        self.metadata.component_order = component_order

        if self._file_path is None:
            raise NimsGeneralError("No file path provided.")

        with open(self._file_path, "rb") as fle:
            buff = fle.read()

        # Read file and determine if it is 1Hz or 8Hz
        self._determine_sample_rate(buff)
        self.metadata.sample_rate = self._sample_rate

        # Set up default parameters
        self.metadata.components_present = ["Hx", "Hy", "Hz", "Ex", "Ey", "TB", "TH"]
        self.metadata.gain = {
            "Hx": 1,
            "Hy": 1,
            "Hz": 1,
            "Ex": 10,
            "Ey": 10,
            "TB": 1,
            "TH": 1,
        }
        self.metadata.adc_conversion_factor = {
            "Hx": 0.01,
            "Hy": 0.01,
            "Hz": 0.01,
            "Ex": 2.44141221047903e-04,
            "Ey": 2.44141221047903e-04,
            "TB": 1 / 70,
            "TH": 1 / 70,
        }
        self.metadata.data_logger_firmware_version = "Unknown"

        search = HeaderParser.search
        header = buff[: self._header_size].decode("utf-8")
        self.metadata.run_id = search(header, station_pattern)
        self.metadata.station = self.metadata.run_id[:-1]
        self.ts_plot.title = self.metadata.station
        self.metadata.station_name = search(header, site_name_pattern)
        self.metadata.state_province = search(header, state_province_pattern)
        self.metadata.country = search(header, country_pattern)
        self.metadata.data_logger_serial_number = search(header, box_sn_pattern)
        self.metadata.run_operator = search(header, operator_pattern)
        self.metadata.comments = search(header, comments_pattern)

        mag_sn = search(header, mag_sn_pattern)
        self.metadata.serial_numbers["Hx"] = mag_sn
        self.metadata.serial_numbers["Hy"] = mag_sn
        self.metadata.serial_numbers["Hz"] = mag_sn
        self.metadata.azimuth["Hx"] = 0.0
        self.metadata.azimuth["Hy"] = 90.0
        self.metadata.azimuth["Hz"] = 0.0

        (
            self.metadata.azimuth["Ex"],
            self.metadata.dipole_length["Ex"],
        ) = HeaderParser.parse_electrode_layout(header, ex_layout_pattern)
        (
            self.metadata.azimuth["Ey"],
            self.metadata.dipole_length["Ey"],
        ) = HeaderParser.parse_electrode_layout(header, ey_layout_pattern)

    def set_gui_time_series_params(self) -> None:
        """Set time series parameters for gui plotting."""
        self.ts_plot.title = self.metadata.run_id
        self.ts_plot.number_of_plots = 7
        self.ts_plot.key_order = ["Hx", "Hy", "Hz", "Ex", "Ey", "TB", "TH"]
        # b, g, r, c, m, y, k, w
        self.ts_plot.line_colors = {
            "Hx": self.ts_plot.colors.next(),
            "Hy": self.ts_plot.colors.next(),
            "Hz": self.ts_plot.colors.next(),
            "Ex": self.ts_plot.colors.next(),
            "Ey": self.ts_plot.colors.next(),
            "TB": self.ts_plot.colors.next(),
            "TH": self.ts_plot.colors.next(),
        }
        self.ts_plot.labels = {
            "Hx": "$H_{x}$",
            "Hy": "$H_{y}$",
            "Hz": "$H_{z}$",
            "Ex": "$E_{x}$",
            "Ey": "$E_{y}$",
            "TB": "$T_{box}$",
            "TH": "$T_{head}$",
        }
        self.ts_plot.units = {
            "Hx": "nT",
            "Hy": "nT",
            "Hz": "nT",
            "Ex": "mV",
            "Ey": "mV",
            "TB": "°C",
            "TH": "°C",
        }

    def set_gui_spectra_params(self) -> None:
        """Set the parameters to plot the spectra."""
        self.sp_plot.title = self.metadata.run_id
        self.sp_plot.number_of_components = 5
        self.sp_plot.key_order = ["Hx", "Hy", "Hz", "Ex", "Ey"]
        self.sp_plot.line_colors = {
            "Hx": self.sp_plot.colors.next(),
            "Hy": self.sp_plot.colors.next(),
            "Hz": self.sp_plot.colors.next(),
            "Ex": self.sp_plot.colors.next(),
            "Ey": self.sp_plot.colors.next(),
        }

    def set_emtf_params(self) -> None:
        """Set the EMTF parameters."""
        box_sn = self.metadata.data_logger_serial_number
        mag_sn = self.metadata.serial_numbers["Hx"]
        self.emtf.component_order = ["Hx", "Hy", "Hz", "Ex", "Ey"]
        self.emtf.number_of_filters = {"Hx": 2, "Hy": 2, "Hz": 2, "Ex": 3, "Ey": 3}
        self.emtf.filter_serial_numbers = {
            "Hx": mag_sn,
            "Hy": mag_sn,
            "Hz": mag_sn,
            "Ex": box_sn,
            "Ey": box_sn,
        }
        self.emtf.missing_sample_value = self.MISSING_VALUE
        self.emtf.number_of_components = 5
        self.emtf.config_type = "lp"

    def parse_time_series(self) -> None:
        """Parse the time series data from the NIMS file."""
        if self._file_path is None:
            raise ValueError("No file path provided.")

        with open(self._file_path, "rb") as fle:
            fle.seek(self._header_size)
            data = fle.read()

        status, gain, sequence, r_temp, m_temp, hx, hy, hz, ex, ey = self._parse_nims_bytes(data)

        # ----------------------------------------------------------------------
        # Find and remove spikes from the data
        print(f"\n{'*' * 80}")
        print(f"Remove Spike Glitches: {'-' * 63}")
        spike_indexes = self._find_spike_indexes(sequence, status)
        print(f"Spikes: {spike_indexes}")
        for ind in spike_indexes[::-1]:
            status = np.delete(status, ind)
            gain = np.delete(gain, ind)
            sequence = np.delete(sequence, ind)
            r_temp = np.delete(r_temp, ind)
            m_temp = np.delete(m_temp, ind)
            hx = np.delete(hx, ind)
            hy = np.delete(hy, ind)
            hz = np.delete(hz, ind)
            ex = np.delete(ex, ind)
            ey = np.delete(ey, ind)
        print(f"{'-' * 80}")

        # ----------------------------------------------------------------------
        # Check for data gaps
        # Check for data gaps and unroll the sequence
        print(f"\n{'*' * 80}")
        print(f"Unroll Sequence: {'-' * 63}")
        sequence, gaps, duplicates = self._unroll_sequence(sequence)
        print(f"Duplicates: {duplicates}")
        print(f"Gaps: {gaps}")
        print(f"{'-' * 80}")

        number_of_packets = len(sequence)
        delta: timedelta = timedelta(seconds=number_of_packets - 1)
        time_stamp = pl.datetime_range(
            start=self.metadata.start,
            end=self.metadata.start + delta,
            interval="1s",
            time_unit="ms",
            eager=True,
        )
        ts_valid = np.zeros(number_of_packets, dtype=bool)

        df = pl.DataFrame(
            {
                "Timestamp": time_stamp,
                # "UnixTimestamp": np.array([x.timestamp() for x in time_stamp]),
                "TsValid": ts_valid,
                "Status": status,
                "Gain": gain,
                "Sequence": sequence,
                "ReceiverTemp": r_temp,
                "MagnetometerTemp": m_temp,
                # Multiply by -1, I don't know why, it is this way in MATLAB SS
                "Ex": -ex,
                "Ey": -ey,
                "Hx": hx,
                "Hy": hy,
                "Hz": hz,
            }
        )

        # ----------------------------------------------------------------------
        # Remove duplicates
        print(f"\n{'*' * 80}")
        print(f"Remove Duplicates: {'-' * 61}")
        gaps, duplicates, errors = self._remove_duplicates(df, duplicates, gaps)
        print(f"Duplicates: {duplicates}")
        print(f"Gaps: {gaps}")
        print(f"Errors: {errors}")
        self.metadata.duplicate_indexes = duplicates
        self.metadata.gap_indexes = gaps
        self.metadata.number_of_gaps = len(gaps)
        self.metadata.processing_errors["Duplicates"] = errors
        print(f"{'-' * 80}")

        # ----------------------------------------------------------------------
        print(f"\n{'*' * 80}")
        print(f"Parse Gain: {'-' * 68}")
        ex_gain, ey_gain, errors = self._parse_gain(df)
        print(f"Gains: {ex_gain}, {ey_gain}")
        self.metadata.gain["Ex"] = ex_gain
        self.metadata.gain["Ey"] = ey_gain
        self.metadata.processing_errors["Gain"] = errors
        print(errors)
        print(f"{'-' * 80}")
        print(df)

        # ----------------------------------------------------------------------
        print(f"\n{'*' * 80}")
        print(f"Parse GNSS: {'-' * 68}")
        index, time, lat, lon, elev, decl, wmm, errors = self._parse_gnss(df)
        self.metadata.latitude = lat
        self.metadata.longitude = lon
        self.metadata.elevation = elev
        self.metadata.declination = decl
        self.metadata.declination_model = wmm
        self.metadata.processing_errors["NMEA"] = errors
        print(errors)
        print(f"{'-' * 80}")

        # ----------------------------------------------------------------------
        print(f"\n{'*' * 80}")
        print(f"Parse Timestamp: {'-' * 63}")
        # df, errors = self._parse_timestamp(df, gaps, index, time)
        # self.metadata.processing_errors['Timestamp'] = errors
        print(errors)
        print(f"{'-' * 80}")

        # ----------------------------------------------------------------------
        print(f"\n{'*' * 80}")
        print(f"Calculate Data Gap Lengths: {'-' * 52}")
        # gap_lengths, errors = self._gap_lengths(df, gaps)
        # self.metadata.gap_lengths = gap_lengths
        # self.metadata.processing_errors['Gaps'] = errors
        print(f"{'-' * 80}")

        # ----------------------------------------------------------------------
        print(f"\n{'*' * 80}")
        print(f"Calculate Unknown Timestamp: {'-' * 51}")
        # df, errors = self._unknown_timestamps(df, gaps)
        # self.metadata.processing_errors['Gap Lengths'] = errors
        print(f"{'-' * 80}")

        # ----------------------------------------------------------------------
        print(f"\n{'*' * 80}")
        print(f"Extract Start/End Times: {'-' * 55}")
        self.metadata.start = df["Timestamp"][0]
        self.metadata.end = df["Timestamp"][-1]
        print(f"{'-' * 80}")

        # ----------------------------------------------------------------------
        print(f"\n{'*' * 80}")
        print(f"Run Metadata: {'-' * 66}")
        print(f"Start Time: {self.metadata.start}")
        print(f"End Time: {self.metadata.end}")
        print(f"{'-' * 80}")

        # ----------------------------------------------------------------------
        print(f"\n{'*' * 80}")
        print(f"Processing Errors: {'-' * 61}")
        for key in self.metadata.processing_errors:
            print(f"{key}: {self.metadata.processing_errors[key]}")
        print(f"{'-' * 80}")

    @staticmethod
    def _parse_nims_bytes(data: bytes) -> tuple[np.ndarray, ...]:
        """Parse the NIMS data from the bytes.

        Args:
            data (bytes): NIMS data bytes.

        Returns
        -------
            tuple(np.ndarray, ...): Parsed NIMS data.
        """
        # Use numpy to parse the data as a structured array
        dtype = np.dtype(
            [
                ("header", "u1"),  # Header byte
                ("length", "u1"),  # Length of the packet
                ("status", "u1"),  # Status byte
                ("gain", "u1"),  # Gain/GPS byte
                ("sequence", "u1"),  # Sequence byte
                (
                    "r_temp",
                    "i2",
                ),  # Signed 2-byte integer for electronics unit temperature
                ("m_temp", "i2"),  # Signed 2-byte integer for magnetometer temperature
                ("hx", "u1", (3,)),  # Signed 3-byte integer for Hx
                ("hy", "u1", (3,)),  # Signed 3-byte integer for Hy
                ("hz", "u1", (3,)),  # Signed 3-byte integer for Hz
                ("ex", "u1", (3,)),  # Signed 3-byte integer for Ex
                ("ey", "u1", (3,)),  # Signed 3-byte integer for Ey
                ("tail", "u1"),  # Tail byte
            ]
        )

        # Read the data as structured array using bulk processing
        parsed_data = np.frombuffer(data, dtype=dtype)

        # Helper function to convert 3-byte integers to signed values
        def convert_3byte_int(byte_array: np.ndarray) -> int:
            """Convert a 3-byte array to a signed integer."""
            # Join bytes and interpret as a signed 4-byte integer
            # (with leading 0 byte for sign)
            return int.from_bytes(byte_array, byteorder="big", signed=True)

        # Extract individual fields
        status = parsed_data["status"]
        gain = parsed_data["gain"]
        sequence = parsed_data["sequence"]
        r_temp = parsed_data["r_temp"]
        m_temp = parsed_data["m_temp"]
        hx = np.array([convert_3byte_int(row) for row in parsed_data["hx"]])
        hy = np.array([convert_3byte_int(row) for row in parsed_data["hy"]])
        hz = np.array([convert_3byte_int(row) for row in parsed_data["hz"]])
        ex = np.array([convert_3byte_int(row) for row in parsed_data["ex"]])
        ey = np.array([convert_3byte_int(row) for row in parsed_data["ey"]])

        # The data is in big-endian byte order, so we need to convert it to native
        # byte order if the native byte order is little-endian, otherwise polars
        # will through an error when trying to convert the data to a DataFrame
        if sys.byteorder == "little":
            r_temp = r_temp.byteswap()
            m_temp = m_temp.byteswap()

        return status, gain, sequence, r_temp, m_temp, hx, hy, hz, ex, ey

    @staticmethod
    def _find_spike_indexes(sequence: np.ndarray, status: np.ndarray) -> list[int]:
        """Find the index numbers of the spikes in the data caused by a glitch.

        Defined by the following 2 conditions:
        1. Two consecutive breaks in the sequence number continuity such that
           the sum total of difference between the spike gaps are 256.
           Ex: diff(sequence[i:i + 1]) + diff(sequence[i - 1:i]) == 256
        2. The status value is an error code: != 129

        Parameters
        ----------
        sequence : np.ndarray
            NIMS packet circular sequence numbers, 0 - 255
        status : np.ndarray
            NIMS packet status values, see top of file documentation

        Returns
        -------
        list
            Spike indexes
        """
        prev_ind = -1
        spike_indexes = []
        indexes = np.where(np.diff(sequence) != 1)[0]
        for ind in indexes[1:]:
            # Various conditions to test:
            # 1. The 'spike' status value is not 129
            # 2. There is two consecutive gaps in the sequence numbers
            if status[ind] != 129 and ind - prev_ind == 1:
                spike_indexes.append(ind)
            prev_ind = ind

        return spike_indexes

    def _unroll_sequence(self, sequence: np.ndarray) -> tuple[np.ndarray, list, list]:
        """Unroll the sequence numbers, check for gaps or duplicates.

        Parameters
        ----------
        sequence : np.ndarray
            Packet sequence numbers ranging from 0 to 255. The sequence number is
            circular, so it will wrap around from 255 to 0. The sequence number starts
            at whatever sequence number was embedded in the NIMS packet when the user
            started the run. It isn't reset when the run starts or stops.

        Returns
        -------
        np.ndarray
            Unrolled sequence numbers
        list
            Indexes of duplicate starts
        list
            Indexes of data gaps
        """
        top: int = 255
        top_interval: int = 256
        gaps: list[int] = []
        possible_duplicates: list[int] = []
        sequence_length: int = len(sequence)

        # Find every index where sequence == 255
        tops = np.where(sequence == top)[0]

        # Make sure there are no gaps before first tops index
        # tops[0] != 0 is an edge case where the sequence + top would equal 255
        # If the first sequence number + the first rollover index == 255, then
        # there is no gap.
        start_gap: bool = True
        if tops[0] != 0:
            start_gap = sequence[0] + tops[0] == top
        # Make sure there are no gaps after the last tops index
        # tops[-1] != sequence_length - 1 is an edge case where the last sequence
        # number is equal to 255. Subtract 1 from the sequence_length to account
        # for 0 indexed tops.
        # Add 1 to the last sequence number to account for the 0 sequence number
        # Subtract 1 from the length of the sequence to account for the 0 index
        end_gap: bool = True
        if tops[-1] != sequence_length - 1:
            end_gap = sequence[-1] + tops[-1] + 1 == sequence_length - 1

        # Verify start, end, and each tops index is 256 counts apart
        if (np.diff(tops) == top_interval).all() and start_gap and end_gap:
            return (
                np.full((len(sequence)), range(0, len(sequence))),
                gaps,
                possible_duplicates,
            )
        else:
            print("Warning: Sequence numbers are not continuous, unrolling slowly.")
            return self._unroll_slow(sequence)

    @staticmethod
    def _unroll_slow(sequence: np.ndarray) -> tuple[np.ndarray, list, list]:
        n = len(sequence)
        gaps = []
        duplicates = []
        unrolled_seq = np.zeros(n, dtype=np.int32)
        current_value = 0
        unrolled_seq[0] = current_value

        for i in range(1, n):
            diff = (sequence[i].astype(np.int32) - sequence[i - 1].astype(np.int32)) % 256
            if diff == 0:  # duplicate, no increment
                duplicates.append(i - 1)
            elif diff == 1:  # regular increase
                current_value += 1
            else:  # gap or wrap-around
                if diff > 1:  # gap
                    gaps.append(i - 1)
                current_value += diff
            unrolled_seq[i] = current_value

        return unrolled_seq, gaps, duplicates

    @staticmethod
    def _remove_duplicates(
        ts: pl.DataFrame, duplicates: list[int], gaps: list[int], sps: int = 1
    ) -> tuple[list[int], list[int], str]:
        """Find and remove duplicate blocks. The check is slightly convoluted.

        refer to SS, removeDuplicates.m, for more information.

        Parameters
        ----------
        ts : pl.DataFrame
            Containing all data
        duplicates : list
            Index numbers of possible duplicates
        gaps : list
            Index numbers of gaps
        sps : int, optional
            Data sampling rate

        Returns
        -------
        list
            Adjusted list of data gap indexes
        list
            Refined list of removed duplicate packets
        """
        real_gaps: list[int] = []
        real_duplicates: list[int] = []
        errors: str = ""

        # If no duplicates, return
        if not duplicates:
            return real_gaps, real_duplicates, errors

        # Check for duplicates values in the channels by comparing the field values
        for i in duplicates:
            dup = True
            dup &= min(ts["Hx"][sps * i : sps * (i + 1)] == ts["Hx"][sps * (i - 1) : sps * i])
            dup &= min(ts["Hy"][sps * i : sps * (i + 1)] == ts["Hy"][sps * (i - 1) : sps * i])
            dup &= min(ts["Hz"][sps * i : sps * (i + 1)] == ts["Hz"][sps * (i - 1) : sps * i])
            dup &= ts["Gain"][i] == ts["Gain"][i - 1] and ts["Gain"][i - 1] == 199
            dup &= ts["ReceiverTemp"][i] == ts["ReceiverTemp"][i - 1]
            dup &= ts["MagnetometerTemp"][i] == ts["MagnetometerTemp"][i - 1]
            dup &= ts["Status"][i] == ts["Status"][i - 1]
            if bool(dup) is True:
                print(f"Duplicate at {i}")
                real_duplicates.append(i)

        # Remove duplicates
        # for i in real_duplicates:
        #     ts = ts.drop(ts.index[i])

        # Change non-duplicates into data gaps
        duplicates = [i for i in duplicates if i not in real_duplicates]
        # TODO: Increase sequence numbers
        # for d in duplicates:
        #     ts["Sequence"][d:] = ts["Sequence"][d:] + 1
        # Adjust index to start of gap not 2nd duplicate number
        real_gaps = list(set(gaps + [i - 1 for i in duplicates]))
        real_gaps.sort()

        # Reset the index numbers after dropping rows
        # ts = ts.reset_index(drop=True)

        # Adjust gap index numbers by number of deleted duplicate rows
        for dupl in real_duplicates:
            for x, real_gap in enumerate(real_gaps):
                if real_gap > dupl:
                    real_gaps[x] = real_gap - 1

        # Shift values base on removing rows before them
        real_duplicates = [i - real_duplicates.index(i) for i in real_duplicates]

        if real_duplicates:
            errors = (
                f"Deleted {len(real_duplicates)} "
                f"duplicate packets from {real_duplicates} position(s)"
            )
            print(errors)

        return real_gaps, real_duplicates, errors

    @staticmethod
    def _parse_gain(ts: pl.DataFrame) -> tuple[int, int, str]:
        """Find the gain value of the electrode channels.

        Verify gain didn't change.

        Parameters
        ----------
        ts : pl.DataFrame
            Data

        Returns
        -------
        list
            Ex and Ex gain values
        """
        low_gain: int = 10
        high_gain: int = 100
        ex_low_ey_low = 204  # hex: CC
        ex_high_ey_low: int = 216  # hex: D8
        ex_low_ey_high: int = 217  # hex: D9
        ex_high_ey_high: int = 200  # hex: C8
        ex_gain: int = low_gain
        ey_gain: int = low_gain
        error: str = ""

        # Check in any of the expressions are True
        ll = (ts["Gain"] == ex_low_ey_low).any()
        hl = (ts["Gain"] == ex_high_ey_low).any()
        lh = (ts["Gain"] == ex_low_ey_high).any()
        hh = (ts["Gain"] == ex_high_ey_high).any()

        # if more than one gain value is found, gain switch during run
        if not (bool(ll) ^ bool(hl) ^ bool(lh) ^ bool(hh)):
            error = "Possible gain switch during run, setting to low gain."
        elif bool(hl):
            ex_gain = high_gain
        elif bool(lh):
            ey_gain = high_gain
        elif bool(hh):
            ex_gain = high_gain
            ey_gain = high_gain

        return ex_gain, ey_gain, error

    @staticmethod
    def _parse_gnss(
        ts: pl.DataFrame,
    ) -> tuple[list, list, float, float, float, float, str, str]:
        """Parse the embedded NMEA sentences and extract position and time information.

        Parameters
        ----------
        ts : pl.DataFrame
            Data

        Returns
        -------
        tuple[list, list, float, float, float, float, str, str]
            Extracted values on position
        """
        # The Buffer size in the NIMS to save the NMEA sentences, truncates if
        # the sentences are longer than 138 characters.
        buffer_length: int = 138
        time = []
        lat = 0.0
        lon = 0.0
        elev = 0.0
        decl = 0.0
        wmm = ""
        error = ""
        valid_indexes = []
        gprmc = []
        gpgga = []

        # Extract the NMEA sentences start indexes
        indexes: pl.DataFrame = ts.select((pl.col("Gain") == ord("$")).arg_true())

        # Get valid NMEA sentences, each NIMS buffer has 2 sentences written in
        # the data; $GPRMC then $GPGGA. The indexes above, point to the start of
        # each sentence. This loop will ignore every other index because we read
        # the buffer in 138 bytes and check that is starts with $GPRMC.
        for i in indexes["Gain"]:
            buffer = "".join(map(chr, ts["Gain"].slice(i, buffer_length)))
            try:
                if buffer.startswith("$GPRMC") and buffer.split(",")[2] == "A":
                    try:
                        rmc, gga, *_ = buffer.split("\r\n")
                    except ValueError:
                        continue

                    if nmea.valid_nmea(rmc):
                        valid_indexes.append(i)
                        gprmc.append(rmc)
                        gpgga.append(gga)
            except IndexError:
                continue

        if not valid_indexes:
            error = "No valid NMEA sentences. Can't compute timestamps."
        else:
            time = nmea.parse_time(gprmc)
            lat = nmea.median_latitude(gprmc)
            lon = nmea.median_longitude(gprmc)
            elev = nmea.median_elevation(gpgga)
            decl, wmm = nmea.compute_declination(time[0].year, lat, lon, elev)

        return valid_indexes, time, lat, lon, elev, decl, wmm, error

    def _parse_timestamp(
        self, ts: pl.DataFrame, gaps: list, index: list, time: list
    ) -> tuple[pl.DataFrame, str]:
        """Apply extracted timestamps to time series.

        TODO: Check to see if the timestamp is late or early

        Parameters
        ----------
        ts : pl.DataFrame
            DataFrame of data
        gaps : list
            Indexes of data gaps
        index : list
            Indexes of valid timestamps
        time : list
            Date times at valid timestamps

        Returns
        -------
        Tuple[pl.DataFrame, str]
            DataFrame with embedded UTC timestamps, errors
        """
        errors = ""

        # Cycle through gaps and determine time stamps
        prev_gap = 0
        for gap in [*gaps, ts.height - 1]:
            gap += 1
            # Cycle through embedded time stamps in sections
            for stamp in {i for i in index if prev_gap < i < gap}:
                lock_index = self._find_lock_index(ts, stamp)

                # Determine start time of gap section
                timestamp = time[index.index(stamp)]
                start = timestamp - timedelta(seconds=lock_index - prev_gap)

                # Create new data range and valid timestamps arrays
                timestamps = pl.timedate_range(start, periods=gap - prev_gap, freq="s")
                ts_valid = np.ones((gap - prev_gap), dtype=bool)

                # Create a temporary row number column if needed
                ts = ts.with_row_count("row_nr")

                # For Timestamp: update rows where row_nr is between
                # prev_gap and gap - 1
                ts = ts.with_columns(
                    pl.when(pl.col("row_nr").is_between(prev_gap, gap - 1, closed="left"))
                    .then(pl.lit(timestamps.to_series()))
                    .otherwise(pl.col("Timestamp"))
                    .alias("Timestamp")
                )

                # Similarly for TsValid:
                ts = ts.with_columns(
                    pl.when(pl.col("row_nr").is_between(prev_gap, gap - 1, closed="left"))
                    .then(pl.lit(ts_valid.tolist()))
                    .otherwise(pl.col("TsValid"))
                    .alias("TsValid")
                )

                # Optionally, remove the temporary row number column if no longer needed
                ts = ts.drop("row_nr")

                # ts["Timestamp"][prev_gap : gap - 1] = timestamps
                # ts["TsValid"][prev_gap : gap - 1] = ts_valid

                # TODO: Used when verifying section isn't late or early
                break

            # Check for invalid data section
            if ts["TsValid"][prev_gap] is False:
                if prev_gap == 0:
                    errors += "Start time unknown, delete start of run. "
                errors += f"Unknown timestamps between indexes: {prev_gap}:{gap - 1}. "

            prev_gap = gap

        return ts, errors

    @staticmethod
    def _find_lock_index(ts: pl.DataFrame, gps_start: int) -> int:
        """Find the lock index of the embedded time stamp.

        The 'lock' is the last non-129 status value. If there are two non-129
        status values, the first is the lock.

        Parameters
        ----------
        ts : pl.DataFrame
            Data
        gps_start : int
            Index of time stamp

        Returns
        -------
        int
            Index of time stamp lock
        """
        for i in range(gps_start - 10, gps_start):
            try:
                if ts["Status"][i] != 129:
                    return i
            except KeyError:
                pass

        return 0

    @staticmethod
    def _gap_lengths(ts: pl.DataFrame, gaps: list) -> tuple[list, str]:
        """Determine the lengths of the data gaps.

        Parameters
        ----------
        ts : pl.DataFrame
            Data
        gaps : list
            Indexes of gaps in DataFrame

        Returns
        -------
        Tuple[list, str]
            Lengths of data gaps in data samples
        """
        errors = ""
        gap_lengths = []

        for gap in gaps:
            gap += 1
            if ts["TsValid"][gap - 1] and ts["TsValid"][gap]:
                td = (ts["Timestamp"][gap] - ts["Timestamp"][gap - 1]).total_seconds()
                # Length of gap
                gap_lengths.append(int(td) - 1)
            else:
                gap_lengths.append(ts["Sequence"][gap] - ts["Sequence"][gap - 1] - 1)

        if gap_lengths:
            errors = f"Calculated gap, {gaps}, length(s) of {gap_lengths}"

        return gap_lengths, errors
        # errors = ""
        # gap_lengths = []
        #
        # for gap in gaps:
        #     gap += 1
        #     if (
        #         bool(ts.TsValid.loc[gap - 1]) is True
        #         and bool(ts.TsValid.loc[gap]) is True
        #     ):
        #         td = (ts.Timestamp.loc[gap] -
        #           ts.Timestamp.loc[gap - 1]).total_seconds()
        #         # Length of gap
        #         gap_lengths.append(int(td) - 1)
        #     else:
        #         gap_lengths.append(
        #           ts.Sequence.loc[gap] - ts.Sequence.loc[gap - 1] - 1)
        #
        # if gap_lengths:
        #     errors = f"Calculated gap, {gaps}, length(s) of {gap_lengths}"
        #
        # return gap_lengths, errors

    @staticmethod
    def _unknown_timestamps(ts: pl.DataFrame, gaps: list) -> tuple[pl.DataFrame, str]:
        """Calculate the unknown timestamps in the time series.

        Parameters
        ----------
        ts : pl.DataFrame
            Data
        gaps : list
            Data gap index numbers

        Returns
        -------
        Tuple[pl.DataFrame, str]
            DataFrame of data, errors
        """
        # errors = ""
        # prev_gap = 0
        # prev_seq = 0
        #
        # # get the first valid index where TSValid is True
        # index = ts.where(ts.TsValid).first_valid_index()
        # # index = ts.TsValid[ts.TsValid == True].first_valid_index()
        #
        # if index is None:
        #     errors = "No valid timestamps."
        #     return ts, errors
        #
        # sequence = int(ts.Sequence.loc[index])
        # ref_timestamp = ts.Timestamp.loc[index]
        #
        # for gap in [*gaps, len(ts) - 1]:
        #     seq = int(ts.Sequence.loc[gap])
        #     if bool(ts.TsValid.loc[gap]) is False:
        #         start = ref_timestamp + timedelta(seconds=prev_seq - sequence)
        #         timestamps = pl.date_range(start, periods=1 +
        #         seq - prev_seq, freq="S")
        #
        #         ts.loc[prev_gap:gap, "Timestamp"] = timestamps
        #
        #     gap += 1
        #     if gap != len(ts):
        #         prev_seq = int(ts.Sequence.loc[gap])
        #     prev_gap = gap
        #
        # return ts, errors
        errors = ""
        prev_gap = 0
        prev_seq = 0

        # Get the first valid index where TsValid is True.
        index: int | None = ts.select(pl.col("TsValid").arg_true().first()).item()

        if index is None:
            errors = "No valid timestamps."
            return ts, errors

        # Here we assume that the indexing returns the proper types.
        # Depending on your version of polars, you might prefer using column indexing:
        sequence: int = int(ts[index, "Sequence"])
        ref_timestamp = ts[index, "Timestamp"]

        # Iterate over each gap index, appending the last index ts.height - 1
        for gap in [*gaps, ts.height - 1]:
            seq: int = int(ts[gap, "Sequence"])
            if not ts[gap, "TsValid"]:
                start = ref_timestamp + timedelta(seconds=prev_seq - sequence)
                end = start + timedelta(seconds=1 + seq - sequence)
                # pl.datetime_range returns a Series; we annotate it to help mypy.
                timestamps: pl.Series = pl.datetime_range(
                    start, end, interval="1s", time_unit="ms", eager=True
                )

                # Replace the Timestamp column slice between prev_gap and the number
                # of timestamps. Using len(timestamps) is preferred over
                # timestamps.shape[0]
                ts = ts.with_columns(
                    pl.Series("Timestamp", timestamps).slice(prev_gap, len(timestamps))
                )

            # Update gap values. Here we avoid modifying the loop variable directly.
            new_gap = gap + 1
            if new_gap != ts.height:
                prev_seq = int(ts[new_gap, "Sequence"])
            prev_gap = new_gap

        return ts, errors


def read(path: Path, _project_path: Path | None = None, q_out: Optional[Queue] = None) -> Nims:
    """Read the NIMS file and return the parsed metadata and time series data.

    Args:
        path (Path): Path to the NIMS file.
        project_path (Path): Path to the project folder.
        q_out (Queue): Multiprocessing queue to send status messages. Defaults to None.

    Returns
    -------
        NIMS: Parsed NIMS data.
    """
    start = timer()
    if not isinstance(path, Path):
        path = Path(path)

    if q_out is not None:
        dump(queue=q_out, flag=StatusFlags.STATUS, message="Reading File")

    print(f"{'-' * 80}")
    print(f"{'-' * 80}")
    print(f"-Reading File: {path.name}")
    mtdata = Nims(path)
    mtdata.parse_metadata()
    mtdata.set_emtf_params()
    mtdata.set_gui_time_series_params()
    mtdata.set_gui_spectra_params()
    mtdata.parse_time_series()

    # set the end time
    # seconds = int(mtdata.time_series.shape[1] / mtdata.metadata.sample_rate)
    # mtdata.metadata.end = mtdata.metadata.start + timedelta(seconds=seconds)

    print(mtdata)

    if q_out is not None:
        # Save the Time Series to a temporary file, and clear the time series data
        mtdata.temp_dump_time_series()
        dump(queue=q_out, flag=StatusFlags.FINISHED, message=mtdata)

    end = timer()
    print(f"{'-' * 80}")
    print(f"Parsing files took: {timedelta(seconds=end - start)}")

    return mtdata
