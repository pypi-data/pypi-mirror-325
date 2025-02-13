"""Base classes to hold the metadata and time series of the instruments."""

from datetime import datetime
from pathlib import Path

import numpy as np
import polars as pl
import toml
from dateutil import parser

from mttools_lib.configs import TOML_VERSION
from mttools_lib.utils import LineColors, Units

from .errors import ReaderError


class MetadataBase:
    """Base class to hold the metadata of the data files."""

    __name__ = "Metadata"

    def __init__(self, num_samples: int = 0):
        self.system: str = "UNKNOWN"
        self.station: str = "UNKNOWN"
        self.run_id: str = "UNKNOWN"
        self.station_name: str = "UNKNOWN"
        self.state_province: str = "UNKNOWN"
        self.country: str = "UNKNOWN"

        self.latitude: float = 0
        self.longitude: float = 0
        self.elevation: float = 0

        self.project: str = ""
        self.client: str = ""
        self.contractor: str = ""

        self.start: datetime = datetime(1970, 1, 1)
        self.end: datetime = datetime(1970, 1, 1)

        self.number_of_samples: int = num_samples

        self.run_operator: str = "Nikola Tesla"

        self.duplicate_indexes: list[int] = []
        self.spike_indexes: list[int] = []
        self.extension: str = ".nim"

        self.components_present: list[str] = []
        # self.components: list[str] = []
        self.component_order: dict[str, int] = {
            "Hx": 0,
            "Hy": 1,
            "Hz": 2,
            "Ex": 3,
            "Ey": 4,
            "TB": 5,
            "TH": 6,
        }
        self.ts_order: dict[str, int] = {
            "Hx": 0,
            "Hy": 1,
            "Hz": 2,
            "Ex": 3,
            "Ey": 4,
            "TB": 5,
            "TH": 6,
        }

        self.gain: dict[str, int] = {"Hx": 1, "Hy": 1, "Hz": 1, "Ex": 1, "Ey": 1}

        self.azimuth: dict[str, float] = {}
        self.serial_numbers: dict[str, str] = {}
        self.ground_connection: str = "UNKNOWN"
        self.dipole_length: dict[str, float] = {}
        self.dipole_length_units: dict[str, Units] = {}
        self.declination: float = 0.0
        self.declination_model: str = "IGRF-13"
        self.sample_rate: int = 1
        self.data_logger_serial_number: str = "ZN0001"
        self.data_logger_firmware_version: str = ""
        self.adc_conversion_factor: dict[str, float] = {}

        self.number_of_gaps: int = 0
        self.gap_indexes: list[int] = []
        self.gap_lengths: list[int] = []

        self.comments: str = ""

        self.notch_filters: list[int] = []
        self.processing_errors: dict[str, str] = {}

    def __str__(self) -> str:
        """Return the string representation of the object."""
        lines = [
            f"Station:           {self.station}",
            f"Run ID:            {self.run_id}",
            f"Latitude:          {self.latitude}",
            f"Longitude:         {self.longitude}",
            f"Elevation:         {self.elevation}",
            f"Start:             {self.start}",
            f"End:               {self.end}",
            f"Operator:          {self.run_operator}",
            f"Box SN:            {self.data_logger_serial_number}",
            f"Box FW:            {self.data_logger_firmware_version}",
            f"Sample Rate:       {self.sample_rate} Hz",
            f"Serial Numbers:    {self.serial_numbers}",
            f"Azimuths:          {self.azimuth}",
            f"Dipole Length:     {self.dipole_length}",
            f"Notch Filters:     {self.notch_filters}",
        ]

        return "\n\t".join(["\nStation Summary:", *lines])

    def dump_dict(self) -> dict:
        """Return the metadata attributes a dictionary."""
        meta = self.__dict__.copy()
        meta["start"] = parser.parse(meta["start"].isoformat())
        meta["end"] = parser.parse(meta["end"].isoformat())
        for key in meta["dipole_length_units"]:
            meta["dipole_length_units"][key] = meta["dipole_length_units"][key].name
        return meta

    def load_dict(self, data: dict) -> None:
        """Load the metadata attributes from a dictionary."""
        for key in data["dipole_length_units"]:
            data["dipole_length_units"][key] = Units[data["dipole_length_units"][key]]

        for k, v in data.items():
            setattr(self, k, v)


class TSPlotParamsBase:
    """Base class to hold the GUI time series plotting parameters."""

    __name__ = "TSPlotParams"

    def __init__(self) -> None:
        self.title: str = ""
        self.number_of_plots: int = 0  # Number of plots to display
        self.key_order: list[str] = []  # Order of the plots to display by key
        self.line_colors: dict[str, str] = {}  # Line colors for each plot
        self.labels: dict[str, str] = {}  # Labels for each plot
        self.labels_matplotlib: dict[str, str] = {}  # Labels for each plot, matplotlib tex format
        self.labels_pyqtgraph: dict[str, str] = {}  # Labels for each plot, pyqtgraph format
        self.units: dict[str, str] = {}  # Units for each plot
        self.colors: LineColors = LineColors()

    def __str__(self) -> str:
        """Return the string representation of the object."""
        lines = [
            f"Plot Title:        {self.title}",
            f"Num of Plots:      {self.number_of_plots}",
            f"Plot Order:        {self.key_order}",
            f"Line Colors:       {self.line_colors}",
            f"Labels:            {self.labels}",
            f"Units:             {self.units}",
        ]

        return "\n\t".join(["\nTime Series Plot Parameters:", *lines])

    def validate_params(self) -> None:
        """Validate the parameters of the class."""
        self.title = str(self.title)
        self.number_of_plots = int(self.number_of_plots)
        self.key_order = list(self.key_order)
        self.line_colors = dict(self.line_colors)
        self.labels = dict(self.labels)

    def dump_dict(self) -> dict:
        """Return the metadata attributes as a dictionary."""
        meta = self.__dict__.copy()
        # Remove the LineColors object
        del meta["colors"]
        return meta


class PSPlotParamsBase:
    """Base class to hold the GUI power spectra plotting parameters."""

    __name__ = "PSPlotParams"

    def __init__(self) -> None:
        self.title: str = ""
        self.number_of_components: int = 0  # Number of plots to display
        self.key_order: list[str] = []  # Order of the plots to display by key
        self.line_colors: dict[str, str] = {}  # Line colors for each plot
        self.labels: dict[str, str] = {}  # Labels for each plot
        self.units: dict[str, str] = {}  # Units for each plot
        self.colors: LineColors = LineColors()

    def __str__(self) -> str:
        """Return the string representation of the object."""
        lines = [
            f"Plot Title:        {self.title}",
            f"Num of Components: {self.number_of_components}",
            f"Plot Order:        {self.key_order}",
        ]

        return "\n\t".join(["\nPower Spectra Plot Parameters:", *lines])

    def dump_dict(self) -> dict:
        """Return the metadata attributes as a dictionary."""
        meta = self.__dict__.copy()
        # Remove the LineColors object
        del meta["colors"]
        return meta


class EMTFParamsBase:
    """Base class to hold the EMTF parameters."""

    __name__ = "EMTFParams"

    def __init__(self) -> None:
        self.component_order: list[str] = []  # Order of the components in the time series
        self.number_of_sets: int = -1  # Number of sets of data in a bin file
        self.number_of_components: int = 5  # Number of components to save in the bin file
        self.config_type: str = "lp"  # Options are 'lp' or 'wb'
        self.calibration_files: bool = False  # Files to be copied over
        self.number_of_filters: dict[str, int] = {}  # Number of filters for each component
        self.filter_serial_numbers: dict[str, str] = {}  # Serial numbers of the filters
        self.blocks: dict[int, str] = {}  # {Block Index: Block Name}
        self.missing_sample_value: int = 2**31 - 1  # Missing data value
        self.binary_file_extension: str = ".bin"
        self.number_of_samples_per_block: int = 2**32  # Number of samples per block

    def __str__(self) -> str:
        """Return the string representation of the object."""
        lines = [
            f"Component Order:   {self.component_order}",
            f"Missing DataValue: {self.missing_sample_value}",
        ]

        return "\n\t".join(["\nEMTF Processing Parameters:", *lines])

    # def dump_dict(self) -> dict:
    #     """Return the metadata attributes as a dictionary."""
    #     meta = self.__dict__.copy()
    #     return {
    #         "component_order": self.component_order,
    #         "number_of_sets": self.number_of_sets,
    #         "number_of_components": self.number_of_components,
    #         "config_type": self.config_type,
    #         "calibration_files": self.calibration_files,
    #         "filter_serial_numbers": self.filter_serial_numbers,
    #         "blocks": self.blocks,
    #         "missing_sample_value": self.missing_sample_value,
    #         "extension": self.extension,
    #     }
    # def to_dict(self):
    #     return {
    #         "component_order": self.component_order,
    #     }


ClassType = MetadataBase | TSPlotParamsBase | PSPlotParamsBase | EMTFParamsBase


class EMDataBase:
    """Base class to hold the time series data of the instruments."""

    __name__ = "EMData"

    def __init__(self, _channels: int = 0, length: int = 0):
        self._temp_time_series_path: Path = Path("temp_time_series.parquet")
        self.time_series_path: Path = Path()
        self.time_series: pl.DataFrame | None = pl.DataFrame(
            {
                "Hx": pl.Series(np.zeros(length)),
                "Hy": pl.Series(np.zeros(length)),
                "Hz": pl.Series(np.zeros(length)),
                "Ex": pl.Series(np.zeros(length)),
                "Ey": pl.Series(np.zeros(length)),
            }
        )

        # Create a dummy time stamp is seconds from the epoch time
        # s = pl.Series(x for x in range(length))
        # self.time_stamps: pl.Series = pl.from_epoch(s, time_unit="s")

        self.metadata: MetadataBase = MetadataBase()
        self.ts_plot: TSPlotParamsBase = TSPlotParamsBase()
        self.sp_plot: PSPlotParamsBase = PSPlotParamsBase()
        self.emtf: EMTFParamsBase = EMTFParamsBase()

    def __str__(self) -> str:
        """Return the string representation of the object."""
        return "\n".join(
            [
                self.metadata.__str__(),
                self.ts_plot.__str__(),
                self.sp_plot.__str__(),
                self.emtf.__str__(),
                f"\nTime Series: {self.time_series}",
            ]
        )

    def write_emdata(self, emdata_path: Path) -> None:
        """Write the EMData class to a toml and parquet files."""
        metadata_path = emdata_path.with_suffix(".toml")
        time_series_path = emdata_path.with_suffix(".parquet")
        # tpn_path = emdata_path.with_suffix(".tpn.npy")
        meta = {
            "Version": TOML_VERSION,
            self.metadata.__name__: self.metadata.dump_dict(),
            self.ts_plot.__name__: self.ts_plot.dump_dict(),
            self.sp_plot.__name__: self.sp_plot.dump_dict(),
            self.emtf.__name__: self.emtf.__dict__,
        }
        print(f"Writing {metadata_path}")
        with open(metadata_path, "w") as fle:
            # Write all class attributes to toml file
            toml.dump(meta, fle)

        print(f"Writing {time_series_path}")
        self.write_parquet_file(time_series_path, self.time_series)

    def load_emdata(self, emdata_path: Path) -> None:
        """Load the EMData class from a toml and parquet files."""
        metadata_path = emdata_path.with_suffix(".toml")
        time_series_path = emdata_path.with_suffix(".parquet")

        if not metadata_path.exists():
            raise FileNotFoundError(f"Could not find {metadata_path}")

        print(f"Loading {metadata_path}")
        with open(metadata_path, "r") as fle:
            data = toml.load(fle)
        try:
            self.metadata.load_dict(data[self.metadata.__name__])
            # self._load_class(self.metadata, data[self.metadata.__name__])
            self._load_class(self.ts_plot, data[self.ts_plot.__name__])
            self.ts_plot.validate_params()
            self._load_class(self.sp_plot, data[self.sp_plot.__name__])
            self._load_class(self.emtf, data[self.emtf.__name__])
        except KeyError as e:
            raise ReaderError(f"Could not load class attributes: {data}") from e

        print(f"Loading {time_series_path}")
        time_series = self.load_parquet_file(time_series_path)
        if time_series is None:
            raise FileNotFoundError(f"Could not find {time_series_path}")
        self.time_series = time_series

    def temp_dump_time_series(self) -> None:
        """Write the time series data to a temporary file.

        This is used to save the time series data to a temporary file and clear
        the time series data to reduce the memory usage when passing the EMDataBase
        class through a multiprocessing queue.
        """
        # Create a 'MTTools/temp' directory in the user's home directory
        temp_dir = Path(Path.home(), "MTTools", "temp")
        if not temp_dir.exists():
            temp_dir.mkdir(parents=True)
        temp_path = Path(temp_dir, "temp_time_series.parquet")
        self.write_parquet_file(temp_path, self.time_series)
        self._temp_time_series_path = temp_path
        self.time_series = None

    def temp_load_time_series(self) -> None:
        """Load the time series data from a temporary file.

        This is used to load the time series data from a temporary file that was
        saved using the `temp_dump_time_series` method. The temporary file is then
        removed.
        """
        self.time_series = self.load_parquet_file(self._temp_time_series_path)
        # Remove the temporary file
        self._temp_time_series_path.unlink()

    @staticmethod
    def _load_class(_class: ClassType, data: dict) -> None:
        """Load the class attributes from a dictionary."""
        for k, v in data.items():
            setattr(_class, k, v)

    @staticmethod
    def write_parquet_file(file_path: Path, data: pl.DataFrame | None) -> None:
        """Write a polars data to the file path."""
        if data is None:
            return
        data.write_parquet(str(file_path))

    @staticmethod
    def load_parquet_file(file_path: Path) -> pl.DataFrame | None:
        """Load a polars data from the file path."""
        if not file_path.exists():
            return None
        return pl.read_parquet(str(file_path))

    @staticmethod
    def adc_conversion(data: np.ndarray, conversion_factor: float, gain: float) -> np.ndarray:
        """Convert the ADC values to the real units (mV)."""
        return data * conversion_factor * gain

    @staticmethod
    def electric_field_conversion(ts: np.ndarray, dipole_length: float, units: Units) -> np.ndarray:
        """Convert the time series from mV to V/m.

        Args:
            ts (np.ndarray): Time series data, converted to units of mV
            dipole_length (float): The length of the dipole
            units (Units): Units of the dipole length

        Returns
        -------
            np.ndarray: Time series data converted to V/m
        """
        millivolts_to_volts = 1 / 1_000
        return (ts * millivolts_to_volts) / Units.to_meters(dipole_length, units)
