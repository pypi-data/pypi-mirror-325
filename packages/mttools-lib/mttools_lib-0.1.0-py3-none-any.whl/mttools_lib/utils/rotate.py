"""Matrix rotation functions and utilities."""

import numpy as np


def cartesian_2d_clockwise_rotation(
    x: np.ndarray, y: np.ndarray, angle: float
) -> tuple[np.ndarray, np.ndarray]:
    """Rotate 2D vectors clockwise by a given angle in cartesian format.

    Parameters
    ----------
    x : np.ndarray
        Cartesian x-coordinates of the vectors.
    y : np.ndarray
        Cartesian y-coordinates of the vectors.
    angle : float
        Angle in degrees to rotate the vectors.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Rotated x and y coordinates.
    """
    angle = np.deg2rad(angle)
    x_type = x.dtype
    y_type = y.dtype
    x_rot = x * np.cos(angle) + y * np.sin(angle)
    y_rot = x * -np.sin(angle) + y * np.cos(angle)

    return x_rot.astype(x_type), y_rot.astype(y_type)


def mt_2d_clockwise_rotation(
    n: np.ndarray, e: np.ndarray, angle: float
) -> tuple[np.ndarray, np.ndarray]:
    """Rotate 2D vectors clockwise by a given angle in mt format.

    Parameters
    ----------
    n : np.ndarray
        North component of the vectors.
    e : np.ndarray
        East component of the vectors.
    angle :  float
        Angle in degrees to rotate the vectors.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Rotated north and east vectors.
    """
    return cartesian_2d_clockwise_rotation(x=e, y=n, angle=angle)
