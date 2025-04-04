"""General utils for processing data and performing common operations."""

from enum import Enum

from . import nmea
from .decimate import decimate
from .rotate import mt_2d_clockwise_rotation

__all__ = [
    "LineColors",
    "Units",
    "decimate",
    "mt_2d_clockwise_rotation",
    "nmea",
]


class LineColors:
    """Class to handle color codes for plotting."""

    # Define the colors as a class attribute (excluding AUX)
    _colors = (
        "#1f77b4",  # Blue
        "#ff7f0e",  # Orange
        "#2ca02c",  # Green
        "#d62728",  # Red
        "#9467bd",  # Purple
        "#8c564b",  # Brown
        "#e377c2",  # Pink
        "#7f7f7f",  # Gray
        "#bcbd22",  # Yellow-Green
        "#17becf",  # Teal
    )

    AUX = "#ffffff"  # AUX color (accessible directly)

    def __init__(self) -> None:
        """Initialize the LineColors with a counter for circular behavior."""
        self.name = "LineColors"
        self._index = 0  # Internal index to track the current color

    def next(self) -> str:
        """Return the next color in the list, wrapping around when at the end."""
        color = self._colors[self._index]
        # Increment the index and wrap around using modulo
        self._index = (self._index + 1) % len(self._colors)
        return color

    def reset(self) -> None:
        """Reset the circular color index to the beginning."""
        self._index = 0

    def current(self) -> str:
        """Return the current color without moving to the next."""
        return self._colors[self._index]


class Units(Enum):
    """Measurement units for the data."""

    M = 0
    KM = 1
    FT = 2
    ML = 3
    NA = 4

    @staticmethod
    def to_meters(value: float, units: "Units") -> float:
        """Convert the value to meters."""
        if not isinstance(units, Units):
            raise AttributeError("Invalid unit type {units}")

        if units == Units.M:
            return value

        if units == Units.KM:
            return value * 1_000
        if units == Units.FT:
            return value * 0.3048
        if units == Units.ML:
            return value * 1_609.34 * 1_000

        return 0.0
