"""Utilities for rolling project performance monitoring.

Author: Brian Cookson
Date: 2026-11

Load synthetic project request data and calculate rolling
response-time and overdue-rate monitoring signals.
"""

from pathlib import Path

import polars as pl


def load_project_data(data_file: Path) -> pl.DataFrame:
    """Load project request data sorted chronologically."""
    return pl.read_csv(data_file, try_parse_dates=True).sort("timestamp")


def compute_project_rolling_metrics(
    df: pl.DataFrame,
    window_size: int = 5,
    threshold_days: int = 7,
) -> pl.DataFrame:
    """Calculate rolling project performance signals.

    Rolling windows include the current and previous observations.
    Only complete windows produce rolling statistics.
    """
    if window_size < 1:
        raise ValueError("window_size must be at least 1")

    if threshold_days < 0:
        raise ValueError("threshold_days cannot be negative")

    return df.with_columns(
        (pl.col("response_days") > threshold_days).cast(pl.Int8).alias("overdue_flag")
    ).with_columns(
        pl.col("response_days")
        .rolling_mean(window_size=window_size)
        .alias("rolling_avg_response_days"),
        (pl.col("overdue_flag").rolling_mean(window_size=window_size) * 100)
        .round(2)
        .alias("rolling_overdue_rate_pct"),
    )
