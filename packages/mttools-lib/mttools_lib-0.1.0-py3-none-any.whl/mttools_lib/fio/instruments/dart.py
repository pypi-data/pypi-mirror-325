"""DART file reader."""

import sys
from datetime import timedelta
from multiprocessing import Queue
from pathlib import Path
from timeit import default_timer as timer
from typing import Literal, Optional

import numpy as np
import polars as pl
import toml

from mttools_lib.utils import Units

from ..base import EMDataBase
from ..utils import StatusFlags, dump


class Dart(EMDataBase):
    """Class to parse DART files."""

    HEADER_BLOCK_SIZE: int = 512
    PACKET_FLAG: bytes = b"~#!"

    def __init__(self, file_path: Path | None = None):
        super().__init__()
        self.metadata.system = "DART"
        self.metadata.extension = ".drt"
        self._file_path: Path | None = file_path

        self._packet_size: int = 32
        self._sample_rate: int = 10

    def _extract_header(self) -> str:
        """Parse the header of the DART file."""
        header_blocks: bytes = b""
        if self._file_path is None:
            raise ValueError("No file path provided.")

        print(f"Extracting header from: {self._file_path}")
        with open(self._file_path, "rb") as file:
            while True:
                block: bytes = file.read(self.HEADER_BLOCK_SIZE)
                header_blocks += block
                if block.endswith(b"\n"):
                    break
                elif block == b"":
                    raise ValueError("End of file reached before header was found.")

        print(f"Done Extracting header from: {self._file_path}")
        return header_blocks.decode("utf-8")

    def parse_metadata(self) -> None:
        """Parse the metadata from the DART file.

        This is a temporary method because the metadata isn't store in the DART file.
        """
        header: dict = toml.loads(self._extract_header())

        self.metadata.station = header["Station"].get("ID", "")
        self.metadata.station_name = header["Station"].get("Name", "")
        self.metadata.state_province = header["Station"].get("State", "")
        self.metadata.country = header["Station"].get("Country", "")
        self.metadata.latitude = header["Station"].get("Latitude", 0.0)
        self.metadata.longitude = header["Station"].get("Longitude", 0.0)
        self.metadata.elevation = header["Station"].get("Elevation", 0.0)

        self.metadata.run_id = header["Run"].get("ID", "")
        self.metadata.sample_rate = int(header["Run"].get("Sample-Rate-Hz", 10))
        self.metadata.start = header["Run"].get("Start", "1970-01-01T00:00:00")
        self._sample_rate = self.metadata.sample_rate
        self.metadata.run_operator = header["Run"].get("Operator", "")
        self.metadata.ground_connection = header["Run"]["Ground-Connection"]
        self.metadata.comments = header["Run"].get("Comments", "")
        self.metadata.ts_order = {}
        self.metadata.component_order = {}
        for channel in header["Run"]["Channels"]:
            component = header["Run"]["Channels"][channel]
            if component == "NA":
                continue
            self.metadata.components_present.append(component)
            self.metadata.ts_order[component] = int(channel)
            self.metadata.component_order[component] = int(channel)

        self.metadata.data_logger_firmware_version = header["System"].get(
            "Firmware-Version", "Unknown"
        )
        self.metadata.data_logger_serial_number = header["System"].get("Serial-Number", "Unknown")

        for component in self.metadata.components_present:
            self.metadata.azimuth[component] = header[component].get("Azimuth", 0.0)
            self.metadata.serial_numbers[component] = header[component].get("Serial-Number", "")
            self.metadata.gain[component] = int(header[component].get("Gain", 1))
            conversion_factor = header[component].get("Digitizer-Conversion-Factor", 1.0)
            if component.startswith("H"):
                conversion_factor /= header[component].get("Sensor-Conversion-Factor", 1.0)
            self.metadata.adc_conversion_factor[component] = conversion_factor
            if component.startswith("E"):
                self.metadata.dipole_length[component] = header[component].get("Dipole-Length", 0.0)
                self.metadata.dipole_length_units[component] = Units.M

        print(self)

    def set_gui_time_series_params(self) -> None:
        """Set time series parameters for gui plotting."""
        self.ts_plot.title = self.metadata.run_id
        self.ts_plot.number_of_plots = 5
        self.ts_plot.key_order = ["Hx", "Hy", "Hz", "Ex", "Ey"]
        # b, g, r, c, m, y, k, w
        self.ts_plot.line_colors = {
            "Hx": self.ts_plot.colors.next(),
            "Hy": self.ts_plot.colors.next(),
            "Hz": self.ts_plot.colors.next(),
            "Ex": self.ts_plot.colors.next(),
            "Ey": self.ts_plot.colors.next(),
        }
        self.ts_plot.labels = {
            "Hx": "$H_{x}$",
            "Hy": "$H_{y}$",
            "Hz": "$H_{z}$",
            "Ex": "$E_{x}$",
            "Ey": "$E_{y}$",
        }
        self.ts_plot.units = {
            "Hx": "nT",
            "Hy": "nT",
            "Hz": "nT",
            "Ex": "mV",
            "Ey": "mV",
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
        self.emtf.component_order = ["Hx", "Hy", "Hz", "Ex", "Ey"]
        self.emtf.filter_serial_numbers = {
            "Hx": self.metadata.serial_numbers["Hx"],
            "Hy": self.metadata.serial_numbers["Hy"],
            "Hz": self.metadata.serial_numbers["Hz"],
        }
        self.emtf.number_of_components = 5
        self.emtf.number_of_sets = self.metadata.number_of_samples

    def _extract_time_series(self) -> bytes:
        """Extract the time series bytes from the DART file."""
        if self._file_path is None:
            raise ValueError("No file path provided.")

        with open(self._file_path, "rb") as file:
            data: bytes = file.read()

        # Find the start of the time series data
        start = data.find(self.PACKET_FLAG)
        print(f"Start of data: {start}")
        if start == -1:
            raise ValueError("Packet flag not found in the file.")
        data = data[start:]

        return data

    def parse_time_series(self) -> None:
        """Parse the time series data from the DART file."""
        units: dict[int, tuple[str, Literal["ms", "us", "ns"]]] = {
            5: ("200ms", "ms"),
            10: ("100ms", "ms"),
            20: ("50ms", "ms"),
            50: ("20ms", "ms"),
            100: ("10ms", "ms"),
            400: ("2ms500us", "ms"),
        }
        if self._file_path is None:
            raise ValueError("No file path provided.")

        data: bytes = self._extract_time_series()

        count, bitmap, hx, hy, hz, ex, ey = self._parse_dart_bytes(data)

        # TODO: This needs to handle the variable sample rate in the future
        delta: timedelta = timedelta(seconds=len(count) * 1 / self._sample_rate)
        interval, time_unit = units[self._sample_rate]
        s = pl.datetime_range(
            start=self.metadata.start,
            end=self.metadata.start + delta,
            interval=interval,
            time_unit=time_unit,
            eager=True,
        )
        s = s[:-1]

        self.time_series = pl.DataFrame(
            {
                "Timestamp": s,
                "TsValid": bitmap,
                "Sequence": count,
                "Ex": ex,
                "Ey": ey,
                "Hx": hx,
                "Hy": hy,
                "Hz": hz,
            }
        )

    @staticmethod
    def _parse_dart_bytes(data: bytes) -> tuple[np.ndarray, ...]:
        """Parse the DART data from the bytes.

        Args:
            data (bytes): DART data bytes.

        Returns
        -------
            tuple(np.ndarray, ...): Parsed DART data.
        """
        # Use numpy to parse the data as a structured array
        dtype = np.dtype(
            [
                (
                    "header",
                    "S3",
                ),  # Combine the three header bytes into one 3-byte field
                ("reserved", "u1"),  # Reserved field (not used, 1 byte)
                ("count", "u4"),  # Unsigned 4-byte integer for count
                ("bitmap", "u1"),  # Unsigned 1-byte integer for bitmap
                ("hx", "i4"),  # Signed 4-byte integer for Hx
                ("hy", "i4"),  # Signed 4-byte integer for Hy
                ("hz", "i4"),  # Signed 4-byte integer for Hz
                ("ex", "i4"),  # Signed 4-byte integer for Ex
                ("ey", "i4"),  # Signed 4-byte integer for Ey
                ("star", "u1"),  # Star "*" field (not used, 1 byte)
                ("checksum", "u2"),  # Checksum field (not used, 2 bytes)
            ]
        )

        # Read the data as structured array using bulk processing
        parsed_data = np.frombuffer(data, dtype=dtype)

        # Extract individual fields
        count = parsed_data["count"]
        bitmap = parsed_data["bitmap"]
        hx = parsed_data["hx"]
        hy = parsed_data["hy"]
        hz = parsed_data["hz"]
        ex = parsed_data["ex"]
        ey = parsed_data["ey"]

        # The data is in big-endian byte order, so we need to convert it to native
        # byte order if the native byte order is little-endian, otherwise polars
        # will through an error when trying to convert the data to a DataFrame
        if sys.byteorder == "little":
            count = count.byteswap()
            hx = hx.byteswap()
            hy = hy.byteswap()
            hz = hz.byteswap()
            ex = ex.byteswap()
            ey = ey.byteswap()

        return count, bitmap, hx, hy, hz, ex, ey


def read(path: Path, _project_path: Path | None = None, q_out: Optional[Queue] = None) -> Dart:
    """Read the DART file and return the parsed metadata and time series data.

    Args:
        path (Path): Path to the DART file.
        project_path (Path): Path to the project folder.
        q_out (Queue): Multiprocessing queue to send status messages. Defaults to None.

    Returns
    -------
        Dart: Parsed DART data.
    """
    start = timer()
    if not isinstance(path, Path):
        path = Path(path)

    if q_out is not None:
        dump(queue=q_out, flag=StatusFlags.STATUS, message="Reading File")

    print(f"{'-' * 80}")
    print(f"{'-' * 80}")
    print(f"-Reading File: {path.name}")
    mtdata = Dart(path)
    mtdata.parse_metadata()
    mtdata.set_emtf_params()
    mtdata.set_gui_time_series_params()
    mtdata.set_gui_spectra_params()
    mtdata.parse_time_series()

    # set the number_of_samples and the end time
    if mtdata.time_series is not None:
        mtdata.metadata.number_of_samples = mtdata.time_series.height
        seconds = int(mtdata.metadata.number_of_samples / mtdata.metadata.sample_rate)
        mtdata.metadata.end = mtdata.metadata.start + timedelta(seconds=seconds)

    print(mtdata)

    if q_out is not None:
        # Save the Time Series to a temporary file, and clear the time series data
        mtdata.temp_dump_time_series()
        dump(queue=q_out, flag=StatusFlags.FINISHED, message=mtdata)

    end = timer()
    print(f"\n{'-' * 80}")
    print(f"Parsing files took: {timedelta(seconds=end - start)}")

    return mtdata
