"""Figure 1 for Blog 001 ("Humans Suck at Exponentials").

Plots cumulative confirmed COVID-19 cases in the United States on a log
y-axis over the full JHU-era record (2020-01-22 through 2023-03-09), and
fits an exponential to the original spring-2020 wave to measure its
doubling time, which is annotated on the figure.

Data source (cached locally in data/owid_jhu_total_cases.csv):
    https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/total_cases.csv
    (Our World in Data mirror of the Johns Hopkins CSSE dataset; the JHU
    series ended in March 2023.)

Usage:
    conda run -n ocean14 python blogs/blog001/make_fig1_covid_us_cases.py

Outputs:
    blogs/blog001/fig1_covid_us_cases.png
"""

import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Paths anchored to this script's directory so it runs from anywhere.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_CSV = os.path.join(SCRIPT_DIR, "data", "owid_jhu_total_cases.csv")
OUT_PNG = os.path.join(SCRIPT_DIR, "fig1_covid_us_cases.png")

DATA_URL = (
    "https://raw.githubusercontent.com/owid/covid-19-data/"
    "master/public/data/jhu/total_cases.csv"
)

# Window for the exponential fit: the steep growth phase of the original
# 2020 wave. Jan-Feb 2020 is nearly flat (a handful of travel-linked
# cases and almost no testing), so the fit starts when community spread
# takes off at the beginning of March.
FIT_START = "2020-03-01"
FIT_END = "2020-04-01"


def load_us_cases(csv_path):
    """Load cumulative U.S. confirmed cases from the OWID/JHU wide CSV.

    Parameters
    ----------
    csv_path : str
        Path to the OWID total_cases.csv (columns: date, one per country).

    Returns
    -------
    pandas.DataFrame
        Columns ``date`` (datetime64) and ``cases`` (float), rows with
        missing U.S. values dropped, sorted by date.
    """
    df = pd.read_csv(csv_path, usecols=["date", "United States"])
    df = df.rename(columns={"United States": "cases"}).dropna(subset=["cases"])
    df["date"] = pd.to_datetime(df["date"])
    return df.sort_values("date").reset_index(drop=True)


def fit_doubling_time(df, start, end):
    """Fit an exponential to cumulative cases over [start, end].

    Fits a straight line to log2(cases) vs. time (least squares), which
    is equivalent to fitting N(t) = N0 * 2**(t / t_double).

    Parameters
    ----------
    df : pandas.DataFrame
        Output of :func:`load_us_cases` (columns ``date``, ``cases``).
    start, end : str
        Inclusive date bounds (ISO format) of the fit window.

    Returns
    -------
    doubling_days : float
        Fitted doubling time in days.
    fit_dates : pandas.Series
        Dates within the fit window.
    fit_cases : numpy.ndarray
        Fitted (model) case counts on those dates.
    """
    win = df[(df["date"] >= start) & (df["date"] < end)]
    t_days = (win["date"] - win["date"].iloc[0]).dt.days.to_numpy(float)
    log2_cases = np.log2(win["cases"].to_numpy(float))
    slope, intercept = np.polyfit(t_days, log2_cases, 1)
    doubling_days = 1.0 / slope
    fit_cases = 2.0 ** (slope * t_days + intercept)
    return doubling_days, win["date"], fit_cases


def make_figure(df, doubling_days, fit_dates, fit_cases, out_png):
    """Render and save the log-axis figure with the 2020-wave annotation.

    Parameters
    ----------
    df : pandas.DataFrame
        Full U.S. series (columns ``date``, ``cases``).
    doubling_days : float
        Fitted doubling time (days) for the 2020 wave.
    fit_dates : pandas.Series
        Dates of the fit window.
    fit_cases : numpy.ndarray
        Model case counts over the fit window.
    out_png : str
        Output PNG path.
    """
    plt.rcParams.update({
        "figure.dpi": 130,
        "savefig.dpi": 130,
        "font.family": "sans-serif",
        "font.size": 11,
        "axes.titlesize": 14,
        "axes.labelsize": 11.5,
        "axes.edgecolor": "#9aa4af",
        "axes.linewidth": 0.8,
        "xtick.color": "#3d434a",
        "ytick.color": "#3d434a",
        "text.color": "#21262b",
        "axes.labelcolor": "#21262b",
    })

    fig, ax = plt.subplots(figsize=(9, 5.5))

    # Full-arc data series.
    ax.plot(df["date"], df["cases"], color="#2b6cb0", lw=2.0,
            solid_capstyle="round", zorder=3)

    # Fitted exponential over the spring-2020 wave, extended slightly for
    # visibility as a dashed overlay.
    ax.plot(fit_dates, fit_cases, color="#c05621", lw=2.0, ls="--", zorder=4)

    ax.set_yscale("log")
    ax.set_ylim(0.8, 3e8)
    ax.set_xlim(df["date"].iloc[0] - pd.Timedelta(days=15),
                df["date"].iloc[-1] + pd.Timedelta(days=30))

    # Recessive grid, no chartjunk.
    ax.grid(True, which="major", axis="y", color="#d7dce1", lw=0.7, zorder=0)
    ax.grid(True, which="major", axis="x", color="#e6eaee", lw=0.6, zorder=0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)

    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=(4, 7, 10)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.set_yticks([1, 1e2, 1e4, 1e6, 1e8])
    ax.set_yticklabels(["1", "100", "10,000", "1 million", "100 million"])

    ax.set_ylabel("Cumulative confirmed cases (log scale)")
    ax.set_title("COVID-19 in the United States: the exponential spring of 2020",
                 loc="left", pad=12, fontweight="bold")

    # Figure number for the blog post's sequence (bottom-right corner,
    # mirroring the data-source footer at bottom-left).
    fig.text(0.99, 0.012, "Figure 1", ha="right", fontsize=9.5,
             fontweight="bold", color="#6b7280")

    # Annotation: fitted doubling time, pointing at the 2020 wave.
    x_mid = fit_dates.iloc[len(fit_dates) // 2]
    y_mid = fit_cases[len(fit_cases) // 2]
    ax.annotate(
        f"doubling every ~{doubling_days:.1f} days\n(exponential fit, Mar 2020)",
        xy=(x_mid, y_mid), xycoords="data",
        xytext=(pd.Timestamp("2020-08-15"), 300), textcoords="data",
        fontsize=11, color="#8a3f18", ha="left", va="center",
        arrowprops=dict(arrowstyle="-", color="#c05621", lw=1.0,
                        shrinkA=4, shrinkB=6),
    )

    # Direct label for the single data series (no legend box needed).
    ax.text(pd.Timestamp("2021-09-01"), 8e6, "cumulative confirmed cases",
            color="#2b6cb0", fontsize=11)

    # Footer citing the data source.
    fig.text(0.01, 0.012,
             f"Data: Johns Hopkins CSSE via Our World in Data — {DATA_URL}",
             fontsize=7.5, color="#6b7280")

    fig.tight_layout(rect=(0, 0.035, 1, 1))
    fig.savefig(out_png)
    plt.close(fig)


def main():
    """Load data, fit the 2020 wave, print the fit, and save the figure."""
    df = load_us_cases(DATA_CSV)
    doubling_days, fit_dates, fit_cases = fit_doubling_time(
        df, FIT_START, FIT_END)
    print(f"Data range: {df['date'].iloc[0].date()} to "
          f"{df['date'].iloc[-1].date()} ({len(df)} days)")
    print(f"Final cumulative cases: {df['cases'].iloc[-1]:,.0f}")
    print(f"Fit window: {FIT_START} to {FIT_END}")
    print(f"Fitted doubling time: {doubling_days:.2f} days")
    make_figure(df, doubling_days, fit_dates, fit_cases, OUT_PNG)
    print(f"Wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
