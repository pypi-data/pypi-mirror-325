"""Utility functions for the processing module."""

from dataclasses import dataclass
from multiprocessing import Queue
from multiprocessing.synchronize import Lock
from pathlib import Path

import numpy as np
from scipy import signal


class StatusFlags:
    """Status flags for the processing status."""

    WAITING = 0
    START = 1
    FINISHED = 3
    ERROR = 4


class StatusMessage:
    """Status message class."""

    def __init__(self, file_path: Path | None = None, block_name: str = "SITE-FREQ_DATE_TIME"):
        self.file_path = file_path
        self.block_name = block_name
        self.status = 0

    def __repr__(self) -> str:
        """Return the status message."""
        message = f"{'#' * 40}\n"
        message += "Status Message:\n"
        message += f"  Block Name: {self.block_name}\n"
        message += f"  Status: {self.status}\n"
        message += f"{'#' * 40}\n"

        return message


@dataclass
class TranmtMessage:
    """Tranmt message class."""

    station_path: Path
    block_name: str
    remote_referenced: bool


def send_message(queue: Queue, lock: Lock, message: StatusMessage) -> None:
    """Send a status message to the queue."""
    with lock:
        queue.put(message)


def apply_notch_filter(
    time_series: np.ndarray, f0: float, q: float, sample_rate: float
) -> np.ndarray:
    """Apply a notch filter to the time series data."""
    if f0 >= sample_rate:
        return time_series

    print(f"Applying Notch Filter at frequency: {f0}, and quality factor: {q}")
    b, a = signal.iirnotch(f0, q, sample_rate)
    time_series = signal.filtfilt(b, a, time_series)

    time_series = time_series.astype("i4")

    return time_series
