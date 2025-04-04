"""Decimation utilities."""

from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Any

import numpy as np
import polars as pl
import scipy

if TYPE_CHECKING:
    from mttools_lib.fio import EMData  # noqa: TC004


def decimate(mtdata: EMData, decimation_factor: int = 10) -> None:
    """Decimate the time series data."""
    # mtdata.time_series = scipy.signal.decimate(
    #     mtdata.time_series, decimation_factor, axis=0
    # ).astype(np.int32)
    # mtdata.metadata.sample_rate = mtdata.metadata.sample_rate / decimation_factor

    time_series = extract_time_series(mtdata)
    time_series = scipy.signal.decimate(time_series, decimation_factor, axis=0).astype(np.int32)

    new_sample_rate = mtdata.metadata.sample_rate / decimation_factor
    timestamps = time_stamps(mtdata.metadata.start, time_series.shape[0], new_sample_rate)

    mtdata.metadata.number_of_samples = time_series.shape[0]
    mtdata.metadata.end = mtdata.metadata.start + timedelta(
        seconds=int(mtdata.metadata.number_of_samples / new_sample_rate) - 1
    )
    mtdata.metadata.sample_rate = int(new_sample_rate)
    df = pl.from_numpy(time_series, schema=mtdata.emtf.component_order, orient="row")
    # tsvalid = mtdata.time_series.select(pl.col("TsValid")
    # .gather_every(decimation_factor))
    print(timestamps)
    df.insert_column(0, pl.Series("Timestamp", timestamps))
    print(df)
    mtdata.time_series = df


def extract_time_series(mtdata: EMData) -> Any:
    """Extract the time series data from the EMData object."""
    if not isinstance(mtdata.time_series, pl.DataFrame):
        raise ValueError("No time series data to write to binary file.")
    return mtdata.time_series[mtdata.emtf.component_order].to_numpy()


def time_stamps(start: datetime, length: int, sample_rate: float) -> pl.Series:
    """Generate a series of time stamps."""
    # TODO: This needs to handle the variable sample rate in the future
    delta: timedelta = timedelta(seconds=length * 1 / sample_rate)
    s = pl.datetime_range(
        start=start,
        end=start + delta,
        interval="1000ms",
        time_unit="ms",
        eager=True,
    )
    s = s[:-1]
    return s
