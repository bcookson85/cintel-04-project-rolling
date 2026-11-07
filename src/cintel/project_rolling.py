"""Custom rolling project performance monitoring application.

Author: Brian Cookson
Date: 2026-11

Analyze synthetic project request response times using
rolling averages and overdue-rate monitoring signals.
"""

import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path
import polars as pl

from cintel.utils_project import (
    compute_project_rolling_metrics,
    load_project_data,
)

LOG: logging.Logger = get_logger("P4", level="DEBUG")

ROOT_DIR: Final[Path] = Path.cwd()
DATA_FILE: Final[Path] = ROOT_DIR / "data" / "project_responses_timeseries.csv"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts"
OUTPUT_FILE: Final[Path] = ARTIFACTS_DIR / "project_rolling_metrics.csv"

WINDOW_SIZE: Final[int] = 5
THRESHOLD_DAYS: Final[int] = 7


def main() -> None:
    """Run the custom rolling project performance pipeline."""
    log_header(LOG, "PROJECT ROLLING MONITORING")

    log_path(LOG, "DATA_FILE", DATA_FILE)
    log_path(LOG, "OUTPUT_FILE", OUTPUT_FILE)

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    df: pl.DataFrame = load_project_data(DATA_FILE)

    LOG.info(f"Loaded {df.height} project request records")
    LOG.info(f"Rolling window size: {WINDOW_SIZE}")
    LOG.info(f"Overdue threshold: {THRESHOLD_DAYS} days")

    signals_df: pl.DataFrame = compute_project_rolling_metrics(
        df,
        window_size=WINDOW_SIZE,
        threshold_days=THRESHOLD_DAYS,
    )

    signals_df.write_csv(OUTPUT_FILE)

    LOG.info(f"Created {signals_df.height} rolling monitoring records")
    LOG.info(f"Saved rolling monitoring results: {OUTPUT_FILE}")
    LOG.info("Pipeline executed successfully!")


if __name__ == "__main__":
    main()
