"""Module for processing data through Egbert's Fortran DNFF software."""

import datetime as dt
import struct
from pathlib import Path

import numpy as np
import polars as pl

from mttools_lib.fio import EMData


class DNFF:
    """Helper class for Egbert's Fortran DNFF software."""

    def __init__(self, workspace: Path, run_id: str, binary_file_directory_name: str = "data"):
        """Initialize the DNFF class."""
        self._binary_file_directory_name = binary_file_directory_name
        self._workspace = workspace
        self._run_id = run_id
        self._missing_sample_value = -9999
        # def write_bin(mtdata: EMData, station_path: Path, block_index_key: int):

    @staticmethod
    def calculate_binary_block_indexes(
        mtdata: EMData, number_of_sample_per_block: int = -1
    ) -> None:
        """Section the data into blocks for individual DNFF processing."""
        block_start = 0
        start = mtdata.metadata.start
        run_id = mtdata.metadata.run_id
        sample_rate = mtdata.metadata.sample_rate
        number_of_samples = mtdata.metadata.number_of_samples

        if number_of_sample_per_block == -1:
            number_of_sample_per_block = mtdata.emtf.number_of_samples_per_block

        for i in range(block_start, number_of_samples, number_of_sample_per_block):
            time = start + dt.timedelta(seconds=i / sample_rate)
            mtdata.emtf.blocks[i] = (
                f"{run_id}_{int(sample_rate)}Hz_{time.strftime('%y%m%d-%H%M%S')}"
            )

    def write_binary_file(self, mtdata: EMData, station_path: Path, block_index_key: int) -> None:
        """Write a fortran dnff compatible binary file."""
        if mtdata.time_series is None:
            raise ValueError("No time series data to write to binary file.")

        # Determine if there are any gaps in this data set
        # gap_indexes = [
        #     i for i in mtdata.metadata.gap_indexes if start_index
        #     <= i < start_index + number_of_sets
        # ]
        gap_indexes = mtdata.metadata.gap_indexes
        gap_indexes.append(mtdata.time_series.shape[1] - 1)
        gap_lengths = mtdata.metadata.gap_lengths
        gap_lengths.append(0)

        data: np.ndarray = self._extract_time_series(mtdata)
        # data = signal.decimate(data, 10, axis=0).astype(np.int32)
        # Truncate the data to the number of components
        # Reconstruct the data to fill out the gaps with the missing data value
        # TODO: Handle file blocking, currently assumes all data is the block
        # start_old: int = 0
        # start_new: int = 0
        # for ind, length in zip(gap_indexes, gap_lengths, strict=False):
        #     end_new = start_new + ind + 1 - start_old
        #     data[:, start_new:end_new] = mtdata.time_series[
        #         :number_of_components, start_old : ind + 1
        #     ]
        #     start_old = ind + 1
        #     start_new = end_new + length

        # Flatten data to C format, convert to bytes, and write to file
        self._write_binary_file(
            self._generate_binary_file_name(mtdata, station_path, block_index_key),
            self._generate_binary_header(mtdata, block_index_key),
            data.flatten("C").tobytes(),
        )

    @staticmethod
    def _extract_time_series(mtdata: EMData) -> np.ndarray:
        """Extract the time series data from the EMData object."""
        if not isinstance(mtdata.time_series, pl.DataFrame):
            raise ValueError("No time series data to write to binary file.")
        return mtdata.time_series[mtdata.emtf.component_order].to_numpy()

    @staticmethod
    def _generate_binary_header(mtdata: EMData, block_index_key: int) -> bytes:
        """Write a fortran dnff compatible binary file.

        Header Format:
        0  headerLength    int32     5,108
        1  latitude        float32
        2  longitude       float32
        3  declination     float32
        4  sampleDelta     float32
        5  elevation       float32
        6  startYear       int32
        7  startMonth      int32
        8  startDay        int32
        9  startHour       int32
        10 startMinute     int32
        11 startSecond     int32
        12 clkZeoYear      int32
        13 clkZeoMonth     int32     1
        14 clkZeoDay       int32     1
        15 clkZeoHour      int32     0
        16 clkZeoMinute    int32     0
        17 clkZeoSecond    int32     0
        18 numSets         int32
        19 gapType(#chan)  int32
        20 missDataFlag    int32
        21 numberGaps      int32     0
        n  gapStruct*      int32, int32, int32
        .  zerosPadding**  int32
        -1 headerLength    int32     5,108

        Data Format:
        0  numDataBytes    int32
        .  data('F')       int32
        -1 numDataBytes    int32

        *gapsStruct Format:
        I don't know if DNFF actually reads this information, but the gapStruct is
        broken down as follows:
        -Start at the end of the file gap information and work to the front
            -The first int32 is the size of the gap in number of samples
            -The second int32 is the index of the first sample in the gap, 1 based
             index value...Fortran style
            -The third int32 is the index of the last sample in the gap, 1 based index
             value...Fortran style
        Repeat this pattern until all the gap information is written.

        **zerosPadding:
        Zeros are added to the header to make the header length 5,108 bytes.  This
        will speed up DNFF reading by allowing to read the file in blocks. If the
        header is longer than 5,108 bytes, DNFF will read the file one byte at a time.

        If there are more than 1674 data gaps, the header will be longer than 5,108
        bytes.

        Args:
            mtdata (EMData): EMData object
            block_index_key (int): Start of block index

        Returns
        -------
            bytes: Header bytes
        """
        start_index: int = block_index_key
        number_of_sets: int = mtdata.emtf.number_of_sets
        number_of_components: int = mtdata.emtf.number_of_components

        gap_lengths: list[int] = mtdata.metadata.gap_lengths
        gap_lengths.append(0)

        start_time = mtdata.metadata.start + dt.timedelta(
            seconds=start_index / mtdata.metadata.sample_rate
        )

        header: np.ndarray = np.zeros(1_279, dtype=np.int32)
        bytes_header: bytes

        header[0] = 5108  # Header length
        header[1] = 0  # Latitude
        header[2] = 0  # Longitude
        header[3] = 0  # Declination
        header[4] = 0  # Sampling Rate Delta
        header[5] = 0  # Elevation
        header[6] = start_time.year
        header[7] = start_time.month
        header[8] = start_time.day
        header[9] = start_time.hour
        header[10] = start_time.minute
        header[11] = start_time.second
        header[12] = start_time.year
        header[13] = 1
        header[14] = 1
        header[15] = 0
        header[16] = 0
        header[17] = 0
        header[18] = number_of_sets
        header[19] = number_of_components
        header[20] = mtdata.emtf.missing_sample_value
        header[21] = len(mtdata.metadata.gap_indexes)
        # TODO: Add gap information
        header[-1] = 5108

        number_of_sets += sum(gap_lengths)
        # Finish header and convert to bytes
        header[18] = number_of_sets

        # Convert the header to bytes and add in the float values
        bytes_header = bytearray(header.tobytes())

        # Insert float values into byte array
        bytes_header[4:8] = struct.pack("f", mtdata.metadata.latitude)
        bytes_header[8:12] = struct.pack("f", mtdata.metadata.longitude)
        bytes_header[12:16] = struct.pack("f", mtdata.metadata.declination)
        bytes_header[16:20] = struct.pack("f", 1 / mtdata.metadata.sample_rate)
        # bytes_header[16:20] = struct.pack("f", 1)
        bytes_header[20:24] = struct.pack("f", mtdata.metadata.elevation)

        return bytes_header

    def _generate_binary_file_name(
        self, mtdata: EMData, station_path: Path, block_index_key: int
    ) -> Path:
        file_name: str = f"{mtdata.emtf.blocks[block_index_key]}{mtdata.emtf.binary_file_extension}"
        return Path(station_path, self._binary_file_directory_name, file_name)

    @staticmethod
    def _write_binary_file(destination_path: Path, header: bytes, flattened_data: bytes) -> None:
        binary_format: str = "i"  # Integer format for the binary file
        with open(destination_path, "wb") as fle:
            fle.write(header)
            # Write the number of bytes in the data len(data) * 4 bytes each sample
            fle.write(struct.pack(binary_format, len(flattened_data)))
            fle.write(flattened_data)
            fle.write(struct.pack(binary_format, len(flattened_data)))
