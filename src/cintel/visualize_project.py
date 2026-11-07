"""Visualize rolling project response performance.

Author: Brian Cookson
Date: 2026-11

Create a chart showing changes in project response times
and overdue rates using five-observation rolling windows.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import polars as pl

ROOT_DIR = Path.cwd()
INPUT_FILE = ROOT_DIR / "artifacts" / "project_rolling_metrics.csv"
OUTPUT_DIR = ROOT_DIR / "docs" / "images"
OUTPUT_FILE = OUTPUT_DIR / "project_rolling_chart.png"


def main() -> None:
    """Create and save the rolling project monitoring chart."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pl.read_csv(INPUT_FILE, try_parse_dates=True)

    dates = df["timestamp"].to_list()
    response_days = df["response_days"].to_list()
    rolling_average = df["rolling_avg_response_days"].to_list()
    overdue_rate = df["rolling_overdue_rate_pct"].to_list()

    fig, axes = plt.subplots(
        2,
        1,
        figsize=(12, 8),
        sharex=True,
    )

    axes[0].plot(
        dates,
        response_days,
        marker="o",
        linestyle=":",
        color="lightgray",
        label="Individual response time",
    )
    axes[0].plot(
        dates,
        rolling_average,
        linewidth=2.5,
        color="blue",
        label="Five-request rolling average",
    )
    axes[0].axhline(
        y=7,
        color="red",
        linestyle="--",
        label="Seven-day threshold",
    )
    axes[0].set_title("Project Request Response Times")
    axes[0].set_ylabel("Response time (days)")
    axes[0].legend()
    axes[0].grid(alpha=0.3)

    axes[1].plot(
        dates,
        overdue_rate,
        marker="o",
        linewidth=2.5,
        color="darkorange",
        label="Rolling overdue rate",
    )
    axes[1].set_title("Rolling Percentage of Overdue Requests")
    axes[1].set_ylabel("Overdue requests (%)")
    axes[1].set_xlabel("Observation date")
    axes[1].set_ylim(0, 105)
    axes[1].legend()
    axes[1].grid(alpha=0.3)

    fig.suptitle(
        "Rolling Project Performance Monitoring",
        fontsize=16,
        fontweight="bold",
    )
    fig.autofmt_xdate(rotation=45)
    fig.tight_layout()

    fig.savefig(OUTPUT_FILE, dpi=150, bbox_inches="tight")
    plt.close(fig)

    print(f"Chart saved successfully: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
