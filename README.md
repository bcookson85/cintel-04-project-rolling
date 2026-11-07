
# cintel-04-project-rolling

[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](pyproject.toml)
[![CI](https://github.com/bcookson85/cintel-04-project-rolling/actions/workflows/ci-python-zensical.yml/badge.svg)](https://github.com/bcookson85/cintel-04-project-rolling/actions/workflows/ci-python-zensical.yml)
[![Documentation](https://img.shields.io/badge/docs-site-blue?logo=github)](https://bcookson85.github.io/cintel-04-project-rolling/)

[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

> Exploring time series analysis and rolling window monitoring to identify trends and changes in project performance over time.

## Project Overview

**Author:** Brian Cookson

**Date:** November 2026

This project explores time series analysis and rolling window monitoring using Python and Polars as part of the Continuous Intelligence course at Northwest Missouri State University.

The initial objective is to understand and execute Dr. Denise Case's original rolling monitoring example, which analyzes time-ordered system measurements and uses rolling statistics to identify changes in system behavior.

### Proposed Customization: Project Performance Monitoring

My proposed customization will apply rolling window techniques to project request response times, building upon the project performance monitoring applications developed in previous modules.

Using synthetic, timestamped project request data, the application will explore indicators such as:

- **Rolling Average Response Time:** Monitor changes in average project request response times over successive observations.
- **Rolling Overdue Rate:** Track the percentage of requests exceeding a predefined response-time threshold.
- **Response-Time Trends:** Identify periods where project response times are increasing or decreasing.
- **Project Performance Monitoring:** Explore how rolling statistics can reveal developing operational bottlenecks.

The goal is to demonstrate how time-based analysis can provide additional insight into project performance and support more informed operational decisions.

The project is configured in [pyproject.toml](pyproject.toml).

### Custom Application: Project Response-Time Monitoring

The proposed customization has been implemented using a synthetic
dataset of 30 project requests recorded from October 1 through
October 30, 2026.

The application monitors two indicators:

- **Rolling Average Response Time:** The average response time
  across the five most recent project requests.
- **Rolling Overdue Rate:** The percentage of the five most recent
  requests that took more than seven days to receive a response.

The data includes request identifiers, timestamps, project phases,
and response times. It was created for educational purposes and
does not represent actual employer or organizational data.

#### Run the Custom Application

From the project root directory, install the project dependencies:

```powershell
uv sync
```

Run the custom rolling monitoring pipeline:

```powershell
uv run python -m cintel.project_rolling
```

This processes `data/project_responses_timeseries.csv` and generates:

`artifacts/project_rolling_metrics.csv`

Generate the visualization:

```powershell
uv run python -m cintel.visualize_project
```

The visualization is saved to:

`docs/images/project_rolling_chart.png`

#### Custom Results

The five-request rolling average increased to 9.6 days on
October 18, while the rolling overdue rate reached 80%.

By October 30, the rolling average had decreased to 3.6 days,
and the rolling overdue rate had returned to 0%.

These findings demonstrate how rolling monitoring can reveal
a period of increasing project response delays followed by
improvement.

The dataset is synthetic, so the findings demonstrate the
analytical approach rather than actual project performance.

#### Custom Project Files

- [Custom Dataset](data/project_responses_timeseries.csv)
- [Monitoring Application](src/cintel/project_rolling.py)
- [Project Utility Functions](src/cintel/utils_project.py)
- [Visualization Code](src/cintel/visualize_project.py)
- [Generated Results](artifacts/project_rolling_metrics.csv)
- [Project Report](docs/index.md)
- [Visualization](docs/images/project_rolling_chart.png)

### Technical Experiment: Rolling Window Size

**Author:** Brian Cookson  
**Date:** November 2026

#### Objective

Evaluate how increasing the rolling window size affects the calculation and interpretation of time-series monitoring signals.

#### Modification

In `src/cintel/rolling_monitor.py`, I changed the rolling window size from 3 to 5 observations.

#### Prediction

I predicted that increasing the window size would produce smoother rolling averages that respond more slowly to sudden changes in the underlying data. I also expected the first four observations to have incomplete rolling averages instead of the first two.

#### Results

The modified pipeline executed successfully and processed all 60 time-series records.

The results confirmed that:

- The original three-observation window produced its first rolling average on the third observation.
- The modified five-observation window produced its first rolling average on the fifth observation.
- The first calculated rolling request average changed from 135 to 150.
- The first four observations contained blank rolling-average values because the window was not yet complete.
- The resulting dataset was saved to `artifacts/rolling_metrics.csv`.

#### Interpretation

Increasing the rolling window size incorporates more historical observations into each calculation. This generally reduces the influence of individual fluctuations and produces a more stable monitoring signal.

However, a larger window can also delay the detection of sudden changes because newer observations have less influence on the calculated average.

#### Conclusion

This experiment demonstrated that rolling window size is an important design decision in time-series analysis. Analysts must balance the need for stable signals against the ability to identify meaningful changes quickly.

## Data

The example uses time-series system metrics from `data/`.

Each observation includes:

- `timestamp` - time of observation.
- `requests` - number of requests handled.
- `errors` - number of failed requests.
- `total_latency_ms` - total response time in milliseconds.

## Approach

The pipeline uses Polars to:

1. Read and order observations by timestamp.
2. Calculate rolling averages over a defined window.
3. Save the monitoring results for interpretation.

Explore these project components:

- [pyproject.toml](pyproject.toml) - project configuration and dependencies.
- [src/cintel/rolling_monitor.py](src/cintel/rolling_monitor.py) - rolling monitoring pipeline.
- [data/](data/) - time-series data.
- [artifacts/](artifacts/) - generated monitoring results.
- [tests/](tests/) - automated tests.
- [.github/workflows/](.github/workflows/) - automated checks and documentation deployment.
- [docs/](docs/) - project documentation.

## Run the Project

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
to set up your machine and project environment.

From a VS Code terminal in the project root:

```shell
uv run python -m cintel.rolling_monitor
```

## Run the Reactive App

From a VS Code terminal in the project root
(hit CTRL + c to quit):

```shell
uv run marimo run  src/cintel/app.py
```

## Results

The pipeline calculates rolling averages and writes
`artifacts/rolling_metrics.csv`.
Review the rolling measurements to understand
how smoothing can reveal trends and reduce short-term variation.

Successful execution produces a terminal message:

```shell
========================
Pipeline executed successfully!
========================
```

A `project.log` file is created in the project root.

This confirms that the Python pipeline executes
and the logging system works.

## Verification

Run the automated tests:

```shell
uv run pytest
```

## Project Documentation

The [hosted documentation site](https://bcookson85.github.io/cintel-04-project-rolling/)
is published using Zensical and GitHub Pages.

The documentation site is used to present the project report,
covering such sections as data, methods, results, visualizations,
interpretation, and conclusions.

## CI/CD and GitHub Actions

This project includes continuous integration and continuous deployment (CI/CD)
to check project files and publish the docs.
GitHub Actions include:

- [CI: Python and Documentation Checks](https://github.com/bcookson85/cintel-04-project-rolling/actions/workflows/ci-python-zensical.yml)
- [CD: Documentation Deployment](https://github.com/bcookson85/cintel-04-project-rolling/actions/workflows/deploy-zensical.yml)

## Developer Reference

Follow the
[Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
for **detailed instructions and troubleshooting**.

### Initialize and Update the Python Environment

With the project open in VS Code, open a VS Code terminal.
Paste each command and hit Enter or Return after to run it.

```shell
uvx pup-clean --delete
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync
uv audit
```

### Set Up and Run Git Hooks

Set up and run the git hooks to perform
basic checks automatically before
any changes get pushed to GitHub.

In the VS Code terminal,
paste each command and hit Enter or Return after to run it.

```shell
uvx prek install --force
uvx prek update --freeze --cooldown-days 7

git add -A
uvx prek run --all-files
# repeat if changes were made
uvx prek run --all-files
```

### Run Common Chores

Run linters, formatters, type checks, tests, and
build the documentation.

```shell
uv run ruff check . --fix
uv run ruff format .

uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Git add-commit-push to GitHub

After making useful changes, save your work to GitHub.

```shell
git add -A
git commit -m "describe your changes in quotes"
git push -u origin main
```

## Developer Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Developer Tools

This project uses professional Python tools to support development,
testing, documentation, and code quality.

- [uv](https://docs.astral.sh/uv/) - Python environments and dependencies.
- [Ruff](https://docs.astral.sh/ruff/) - Python linting and formatting, configured in [.ruff.toml](.ruff.toml).
- [ty](https://docs.astral.sh/ty/) - Python type checking.
- [pytest](https://docs.pytest.org/) - automated Python testing, configured in [.pytest.toml](.pytest.toml).
- [prek](https://prek.j178.dev/) - Git hooks and automated checks, configured in [prek.toml](prek.toml).
- [Zensical](https://zensical.org/) - project documentation, configured in [zensical.toml](zensical.toml).

## Links

- [Hosted Documentation](https://bcookson85.github.io/cintel-04-project-rolling/)
- [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
- [Citation](CITATION.cff)
- [License](LICENSE)
