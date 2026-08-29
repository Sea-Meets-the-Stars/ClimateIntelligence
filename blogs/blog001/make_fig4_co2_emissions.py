"""Figure 4 for Blog 001 ("Humans Suck at Exponentials").

Plots global annual fossil CO2 emissions (fossil fuels + industry) from
1750 to the present on a log y-axis. Fits an exponential to the long
industrial ramp-up (1850-1970), annotates the fitted doubling time, and
extrapolates the fit past 1970 so the reader can see the exponential
"break": annual emissions growth slowed sharply after ~1970 and has been
nearly flat since ~2010, falling far below the fit's extrapolation.

Data source (cached locally, reused here -- do not re-fetch):
    climate_intelligence/data/raw/owid-co2-data.csv
    Global Carbon Project fossil + industry CO2 emissions,
    redistributed by Our World in Data (column ``co2``, in Mt CO2/yr,
    filtered to country == "World").

Usage:
    conda run -n ocean14 python blogs/blog001/make_fig4_co2_emissions.py

Outputs:
    blogs/blog001/fig4_co2_emissions.png
"""

import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Paths anchored to this script's directory so it runs from anywhere.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
DATA_CSV = os.path.join(
    REPO_DIR, "climate_intelligence", "data", "raw", "owid-co2-data.csv")
OUT_PNG = os.path.join(SCRIPT_DIR, "fig4_co2_emissions.png")

# Window for the exponential fit: the industrial ramp-up. The OWID/GCP
# series technically starts in 1750, but before ~1850 it is tiny
# (< 200 Mt/yr, essentially British coal) and quasi-interpolated. From
# 1850 to 1970 emissions climbed ~75-fold along a remarkably steady
# exponential (wars and the Depression are visible wiggles, not trend
# breaks). After 1970 growth slows sharply, so the fit stops there and
# the later data are left to diverge from the extrapolation.
FIT_START = 1850
FIT_END = 1970


def load_world_emissions(csv_path):
    """Load the OWID/GCP global fossil CO2 emissions series.

    Parameters
    ----------
    csv_path : str
        Path to owid-co2-data.csv (columns include ``country``,
        ``year``, and ``co2`` -- annual fossil + industry CO2 in Mt).

    Returns
    -------
    world : pandas.DataFrame
        Columns ``year`` (int) and ``co2`` (float, Mt CO2/yr), filtered
        to country == "World", positive values only, sorted by year.
    """
    df = pd.read_csv(csv_path, usecols=["country", "year", "co2"])
    world = (df[df["country"] == "World"]
             .dropna(subset=["co2"])
             .sort_values("year")
             .reset_index(drop=True))
    world = world[world["co2"] > 0]
    return world


def fit_doubling_time(world, start, end):
    """Fit an exponential to emissions over [start, end].

    Fits a straight line to log2(emissions) vs. year (least squares),
    equivalent to E(t) = E0 * 2**((t - t0) / t_double).

    Parameters
    ----------
    world : pandas.DataFrame
        Series from :func:`load_world_emissions`.
    start, end : int
        Inclusive year bounds of the fit window.

    Returns
    -------
    doubling_years : float
        Fitted doubling time in years.
    slope, intercept : float
        Coefficients of the log2-linear fit (base-2 log of Mt vs year).
    """
    win = world[(world["year"] >= start) & (world["year"] <= end)]
    years = win["year"].to_numpy(float)
    log2_co2 = np.log2(win["co2"].to_numpy(float))
    slope, intercept = np.polyfit(years, log2_co2, 1)
    doubling_years = 1.0 / slope
    return doubling_years, slope, intercept


def scan_fit_windows(world):
    """Print doubling times for candidate windows (sanity scan).

    Shows how the doubling cadence lengthens over time -- steady through
    ~1970, then slowing -- to justify the chosen fit window.

    Parameters
    ----------
    world : pandas.DataFrame
        Series from :func:`load_world_emissions`.
    """
    print("Doubling-time scan (40-yr windows):")
    for start in range(1850, 2000, 10):
        end = min(start + 40, int(world["year"].max()))
        t2, _, _ = fit_doubling_time(world, start, end)
        print(f"  {start}-{end}: {t2:6.1f} yr")
    print("Longer windows:")
    for start, end in [(1850, 1970), (1850, 1950), (1970, 2024),
                       (2010, 2024)]:
        t2, _, _ = fit_doubling_time(world, start, end)
        print(f"  {start}-{end}: {t2:6.1f} yr")


def make_figure(world, doubling_years, slope, intercept, out_png):
    """Render and save the log-axis figure with the doubling annotation.

    Parameters
    ----------
    world : pandas.DataFrame
        Series from :func:`load_world_emissions` (``year``, ``co2`` Mt).
    doubling_years : float
        Fitted doubling time (years) over the FIT_START-FIT_END window.
    slope, intercept : float
        Log2-linear fit coefficients from :func:`fit_doubling_time`.
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

    last_year = int(world["year"].max())

    # Emissions history (solid blue).
    ax.plot(world["year"], world["co2"], color="#2b6cb0", lw=2.0,
            solid_capstyle="round", zorder=3)

    # Fitted exponential over the ramp-up window (dashed orange), then
    # extrapolated past FIT_END (dotted, lighter) so the divergence of
    # the real curve from "the exponential" is unmissable.
    fit_years = np.arange(FIT_START, FIT_END + 1)
    ax.plot(fit_years, 2.0 ** (slope * fit_years + intercept),
            color="#c05621", lw=2.2, ls="--", zorder=4)
    ext_years = np.arange(FIT_END, last_year + 1)
    ax.plot(ext_years, 2.0 ** (slope * ext_years + intercept),
            color="#c05621", lw=1.6, ls=(0, (1.5, 2.5)), alpha=0.75,
            zorder=4)

    ax.set_yscale("log")
    ax.set_ylim(5, 6e5)
    ax.set_xlim(1745, last_year + 8)

    # Recessive grid, no chartjunk.
    ax.grid(True, which="major", axis="y", color="#d7dce1", lw=0.7, zorder=0)
    ax.grid(True, which="major", axis="x", color="#e6eaee", lw=0.6, zorder=0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)

    ax.set_xticks(np.arange(1750, 2026, 25))
    ax.set_yticks([10, 100, 1000, 10000, 100000])
    ax.set_yticklabels(["10 Mt", "100 Mt", "1 Gt", "10 Gt", "100 Gt"])
    ax.yaxis.set_minor_locator(plt.NullLocator())
    ax.yaxis.set_minor_formatter(plt.NullFormatter())

    ax.set_ylabel("Global fossil CO$_2$ emissions per year (log scale)")
    ax.set_title(
        "Fossil CO$_2$ emissions: an exponential that broke",
        loc="left", pad=12, fontweight="bold")

    # Figure number for the blog post's sequence (bottom-right corner,
    # mirroring the data-source footer at bottom-left).
    fig.text(0.99, 0.012, "Figure 4", ha="right", fontsize=9.5,
             fontweight="bold", color="#6b7280")

    # Annotation: fitted doubling time, pointing at the fit line.
    x_pt = 1930.0
    y_pt = 2.0 ** (slope * x_pt + intercept)
    ax.annotate(
        f"doubling every ~{doubling_years:.0f} years\n"
        f"(exponential fit, {FIT_START}–{FIT_END})",
        xy=(x_pt, y_pt), xycoords="data",
        xytext=(1885, 3.5e4), textcoords="data",
        fontsize=11, color="#8a3f18", ha="center", va="center",
        arrowprops=dict(arrowstyle="-", color="#c05621", lw=1.0,
                        shrinkA=6, shrinkB=8),
    )

    # Annotation: where the real curve leaves the exponential behind.
    ax.annotate(
        "growth slows after ~1970,\nnearly flat since ~2010",
        xy=(2012, 3.4e4), xycoords="data",
        xytext=(1990, 1.5e3), textcoords="data",
        fontsize=11, color="#1d4e89", ha="center", va="center",
        arrowprops=dict(arrowstyle="-", color="#2b6cb0", lw=1.0,
                        shrinkA=6, shrinkB=8),
    )

    # Direct label for the extrapolation.
    ax.text(2005, 2.6e5, "if the doubling\nhad continued",
            color="#c05621", alpha=0.85, fontsize=10, ha="center",
            va="center")

    # Footer citing the data source.
    fig.text(0.01, 0.012,
             "Data: Global Carbon Budget — fossil fuel and industry CO$_2$ "
             f"emissions, 1750–{last_year}, via Our World in Data",
             fontsize=7.5, color="#6b7280")

    fig.tight_layout(rect=(0, 0.035, 1, 1))
    fig.savefig(out_png)
    plt.close(fig)


def main():
    """Load data, scan fit windows, fit the ramp-up, save the figure."""
    world = load_world_emissions(DATA_CSV)
    print(f"Series: {world['year'].iloc[0]}-{world['year'].iloc[-1]} "
          f"({world['co2'].iloc[0]:.1f} Mt -> "
          f"{world['co2'].iloc[-1]:,.0f} Mt)")
    scan_fit_windows(world)
    doubling_years, slope, intercept = fit_doubling_time(
        world, FIT_START, FIT_END)
    print(f"Fit window: {FIT_START}-{FIT_END}")
    print(f"Fitted doubling time: {doubling_years:.1f} years")
    make_figure(world, doubling_years, slope, intercept, OUT_PNG)
    print(f"Wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
