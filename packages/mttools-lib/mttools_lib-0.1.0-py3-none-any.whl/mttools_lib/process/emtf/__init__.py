"""EMTF interface and processing module."""

from pathlib import Path

from loguru import logger as log

from mttools_lib.fio import EMData

from .dnff import DNFF


class EMTFProcessingError(Exception):
    """EMTF specific errors."""

    pass


class EMTF:
    """Fortran EMTF initialization and control class."""

    def __init__(self, workspace: Path, run_id: str):
        """Initialize the EMTF class."""
        self._dnff = DNFF(workspace, run_id)

    def create_processing_directory(self, station_path: Path) -> None:
        """Initialize the processing directory folder structure.

        Args:
            station_path (Path): Station processing directory
        """
        log.info(f"Creating processing directory structure: {station_path}")
        self._mkdir(station_path)
        self._mkdir(Path(station_path, "CF"))
        self._mkdir(Path(station_path, "data"))
        self._mkdir(Path(station_path, "data", "BR"))
        self._mkdir(Path(station_path, "original"))
        self._mkdir(Path(station_path, "FC"))
        self._mkdir(Path(station_path, "MT"))
        self._mkdir(Path(station_path, "plot"))
        self._mkdir(Path(station_path, "SP"))
        self._mkdir(Path(station_path, "logs"))
        self._mkdir(Path(station_path, "sensors"))

    def calculate_binary_block_indexes(
        self, mtdata: EMData, number_of_sample_per_block: int = -1
    ) -> None:
        """Section the data into blocks for individual DNFF processing."""
        self._dnff.calculate_binary_block_indexes(mtdata, number_of_sample_per_block)

    def write_binary_file(self, mtdata: EMData, station_path: Path, block_index_key: int) -> None:
        """Write the binary file for the EMTF software."""
        try:
            self._dnff.write_binary_file(mtdata, station_path, block_index_key)
        except AttributeError:
            raise EMTFProcessingError("No EMData object provided.") from None

    @staticmethod
    def _mkdir(path: Path) -> None:
        """Create a directory if it does not exist."""
        path.mkdir(exist_ok=True, parents=True)
