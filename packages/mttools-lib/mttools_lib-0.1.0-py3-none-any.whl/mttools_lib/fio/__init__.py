"""File Input/Output (FIO) module for reading and writing data."""

from pathlib import Path
from typing import Callable

from .base import EMDataBase
from .base import MetadataBase as EMMetadata
from .errors import ReaderError
from .instruments import Controller, dart, nims

EMData = EMDataBase

__all__ = [
    "Controller",
    "EMData",
    "EMMetadata",
    "reader",
    "system",
]


systems = {
    ".nim": nims.read,
    ".bin": nims.read,
    # ".z3d": zen,
    ".drt": dart.read,
}


readers = {
    "nims": nims.read,
    # "zen": zen.read,
    "dart": dart.read,
}


# instrument = dart  # | nims | zen


def system(path: Path) -> Callable:
    """Return the system reader based on the file extension.

    Args:
        path (Path): Path to the file

    Returns
    -------
        dart: Reader for the file
    """
    if not isinstance(path, Path):
        try:
            path = Path(path)
        except TypeError as e:
            msg = f"Could not convert path to Path object: {path}"
            raise ReaderError(msg) from e

    # Get the file extension
    file_type = path.suffix.lower()

    if file_type is None or file_type not in systems:
        msg = f"Could not fine associated reader {file_type}"
        msg += f"\nAvailable file types: {list(systems.keys())}"
        raise ReaderError(msg)

    return systems[file_type]


def reader(file_type: str | None = None) -> Callable:
    """Return the reader based on the file type.

    Args:
        file_type (str, optional): File type to read. Defaults to None.

    Returns
    -------
        Callable: Reader for the file
    """
    if not isinstance(file_type, str):
        msg = f"Wrong parameter type for file_type: {file_type}, {type(file_type)}"
        raise TypeError(msg)

    if file_type is None or file_type.lower() not in readers:
        msg = f"Could not fine associated reader {file_type}"
        msg += f"\nAvailable file types: {list(readers.keys())}"
        raise ReaderError(msg)

    return readers[file_type]
