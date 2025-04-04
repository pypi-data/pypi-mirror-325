"""Helper functions to parse NMEA sentences."""

from datetime import datetime

import numpy as np
from pyIGRF import igrf_value

TIME_INDEX = 1
STATUS = 2
LATITUDE_INDEX = 3
LATITUDE_DIRECTION_INDEX = 4
LONGITUDE_INDEX = 5
LONGITUDE_DIRECTION_INDEX = 6
DATE_INDEX = 9

ELEVATION = 9


def valid_nmea(sentence: str) -> bool:
    """Compute the NMEA checksum to see if the sentence is valid.

    Args:
        sentence (str): NMEA sentence to check

    Returns
    -------
        bool: Valid checksum or not
    """
    c = 0

    # Remove the leading $ and split
    sentence, *checksum = sentence[1:].split("*")

    # XOR the characters
    for x in sentence:
        c ^= ord(x)

    try:
        return c == int(checksum[0], 16)
    except (ValueError, IndexError):
        return False


def parse_time(sentences: list[str]) -> list[datetime]:
    """Parse the date and time from the sentence and return datetime.

    Args:
        sentences (list): NMEA sentence with date and time

    Returns
    -------
        list: UTC date times for each sentence
    """
    time = []

    for s in sentences:
        parts = s.split(",")
        time.append(
            datetime.strptime(
                f"{parts[DATE_INDEX]} {parts[TIME_INDEX].split('.')[0]}", "%d%m%y %H%M%S"
            )
        )

    return time


def dm2dd(degrees: int, minutes: float, direction: str) -> float:
    """Convert a given DM to DD.

    Args:
        degrees (int): DMS degrees
        minutes (float): DMS minutes
        direction (str): 'N', 'S', 'E', 'W' directions

    Returns
    -------
        float: Decimal degree format of lat or long
    """
    multiplier = {"N": 1, "S": -1, "E": 1, "W": -1}
    dd = degrees + minutes / 60
    dd *= multiplier[direction]

    return dd


def median_latitude(sentences: list) -> float:
    """Extract median latitude from the NMEA sentences.

    The latitude (ddmm.mmm*) dm and direction from nmea sentence.
    Convert to dd then take the median value.

    Args:
        sentences (list): NMEA sentences

    Returns
    -------
        float: Median latitude in DD
    """
    latitudes = []

    for s in sentences:
        try:
            fields = s.split(",")
            degrees = int(fields[LATITUDE_INDEX][:2])
            minutes = float(fields[LATITUDE_INDEX][2:])
            latitudes.append(dm2dd(degrees, minutes, fields[LATITUDE_DIRECTION_INDEX]))
        except (ValueError, IndexError):
            continue

    if not latitudes:
        return np.nan
    return float(round(np.median(latitudes), 6))


def median_longitude(sentences: list[str]) -> float:
    """Extract longitude from the NMEA sentences.

    The longitude (dddmm.mmm*) dm and direction from nmea
    Convert to dd then take the median value.

    Args:
        sentences (list): List of NMEA sentences

    Returns
    -------
        float: Median longitude in DD
    """
    longitudes = []

    for s in sentences:
        try:
            fields = s.split(",")
            degrees = int(fields[LONGITUDE_INDEX][:3])
            minutes = float(fields[LONGITUDE_INDEX][3:])
            longitudes.append(dm2dd(degrees, minutes, fields[LONGITUDE_DIRECTION_INDEX]))
        except (ValueError, IndexError):
            continue

    if not longitudes:
        return np.nan
    return float(round(np.median(longitudes), 6))


def median_elevation(sentences: list) -> float:
    """Extract the elevation and take the median value.

    Args:
        sentences (list): List of NMEA sentences

    Returns
    -------
        float: Median elevation in meters
    """
    elevations = []

    for s in sentences:
        fields = s.split(",")
        # Need because of no validation checking due to partial sentences
        try:
            elevations.append(float(fields[ELEVATION]))
        except (ValueError, IndexError):
            continue

    if not elevations:
        return np.nan
    return float(round(np.median(elevations), 1))


def compute_declination(time: int, lat: float, lon: float, elev: float) -> tuple[float, str]:
    """Compute the declination.

    Based off of the pyIGRF library. Currently, using IGRF-13 model.
    Should be good until ~2025.

    Args:
        time (int): Description
        lat (float): Median Latitude
        lon (float): Median Longitude
        elev (float): Median Elevation
        time (DataTime) Year of run

    Returns
    -------
        Tuple[float, str]: Declination, in degrees, and the model used
    """
    model = "IGRF-13"
    decl = igrf_value(lat, lon, elev, time)[0]

    return round(decl, 4), model
