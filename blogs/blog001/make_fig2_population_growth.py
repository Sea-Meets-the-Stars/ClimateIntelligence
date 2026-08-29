"""Figure 2 for Blog 001 ("Humans Suck at Exponentials").

Plots world population from 1800 to 2100 on a log y-axis: historical
estimates (solid) through 2023 and the UN medium projection (dashed,
shaded era) through 2100. Fits an exponential to the post-war boom --
the fastest sustained stretch of human population growth -- and
annotates the fitted doubling time on the figure.

Data source (cached locally in CI_Reports/data/, reused here):
    CI_Reports/data/owid_population_long_run_projections.csv
    Our World in Data long-run world population
    (HYDE 3.3 + Gapminder + UN World Population Prospects 2024).
    Estimates run 1800-2023; the UN medium projection runs 2024-2100.

Usage:
    conda run -n ocean14 python blogs/blog001/make_fig2_population_growth.py

Outputs:
    blogs/blog001/fig2_population_growth.png
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
    REPO_DIR, "CI_Reports", "data",
    "owid_population_long_run_projections.csv")
OUT_PNG = os.path.join(SCRIPT_DIR, "fig2_population_growth.png")

# Window for the exponential fit: the post-war population boom. World
# growth rates climbed for a century and a half, peaked near 2.1%/yr in
# the early 1960s, and stayed close to that peak through the late 1980s
# -- the fastest *sustained* doubling cadence in the record. 1950-1990
# brackets that plateau (see the window scan printed by main()).
FIT_START = 1950
FIT_END = 1990


def load_world_population(csv_path):
    """Load the OWID long-run world population series.

    Parameters
    ----------
    csv_path : str
        Path to owid_population_long_run_projections.csv (columns:
        Entity, Code, Year, Population (projections) (Projected),
        Population).

    Returns
    -------
    hist : pandas.DataFrame
        Historical estimates -- columns ``year`` (int) and ``pop``
        (float), sorted by year (1800-2023).
    proj : pandas.DataFrame
        UN medium projection -- same columns (2024-2100), with the last
        historical point prepended so the plotted curves connect.
    """
    df = pd.read_csv(csv_path)
    df = df[df["Code"] == "OWID_WRL"].sort_values("Year")
    hist = (df[["Year", "Population"]]
            .dropna()
            .rename(columns={"Year": "year", "Population": "pop"})
            .reset_index(drop=True))
    proj = (df[["Year", "Population (projections) (Projected)"]]
            .dropna()
            .rename(columns={"Year": "year",
                             "Population (projections) (Projected)": "pop"})
            .reset_index(drop=True))
    # Prepend the last estimate so the dashed projection joins the solid
    # historical curve with no visual gap.
    proj = pd.concat([hist.tail(1), proj], ignore_index=True)
    return hist, proj


def fit_doubling_time(hist, start, end):
    """Fit an exponential to world population over [start, end].

    Fits a straight line to log2(population) vs. year (least squares),
    equivalent to fitting N(t) = N0 * 2**((t - t0) / t_double).

    Parameters
    ----------
    hist : pandas.DataFrame
        Historical series from :func:`load_world_population`.
    start, end : int
        Inclusive year bounds of the fit window.

    Returns
    -------
    doubling_years : float
        Fitted doubling time in years.
    fit_years : numpy.ndarray
        Years within the fit window.
    fit_pop : numpy.ndarray
        Fitted (model) population on those years.
    """
    win = hist[(hist["year"] >= start) & (hist["year"] <= end)]
    years = win["year"].to_numpy(float)
    log2_pop = np.log2(win["pop"].to_numpy(float))
    slope, intercept = np.polyfit(years, log2_pop, 1)
    doubling_years = 1.0 / slope
    fit_pop = 2.0 ** (slope * years + intercept)
    return doubling_years, years, fit_pop


def scan_fit_windows(hist):
    """Print doubling times for candidate 40-year windows (sanity scan).

    Parameters
    ----------
    hist : pandas.DataFrame
        Historical series from :func:`load_world_population`.
    """
    print("Doubling-time scan (40-yr windows):")
    for start in range(1800, 1990, 10):
        end = start + 40
        if end > int(hist["year"].max()):
            break
        t2, _, _ = fit_doubling_time(hist, start, end)
        print(f"  {start}-{end}: {t2:6.1f} yr")


def make_figure(hist, proj, doubling_years, fit_years, fit_pop, out_png):
    """Render and save the log-axis figure with the doubling annotation.

    Parameters
    ----------
    hist, proj : pandas.DataFrame
        Historical and projected series (columns ``year``, ``pop``).
    doubling_years : float
        Fitted doubling time (years) over the boom window.
    fit_years, fit_pop : numpy.ndarray
        Fit window years and model population values.
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

    # Shade the projection era so the estimate/projection boundary reads
    # at a glance, in addition to the solid/dashed line change.
    proj_start = proj["year"].iloc[1]
    ax.axvspan(proj_start, 2100, color="#eef1f5", zorder=0)

    # Historical estimates (solid) and UN medium projection (dashed).
    ax.plot(hist["year"], hist["pop"], color="#2b6cb0", lw=2.0,
            solid_capstyle="round", zorder=3)
    ax.plot(proj["year"], proj["pop"], color="#2b6cb0", lw=2.0,
            ls=(0, (4, 2.5)), zorder=3)

    # Fitted exponential over the boom window, as a dashed overlay.
    ax.plot(fit_years, fit_pop, color="#c05621", lw=2.2, ls="--", zorder=4)

    ax.set_yscale("log")
    ax.set_ylim(8e8, 1.6e10)
    ax.set_xlim(1795, 2105)

    # Recessive grid, no chartjunk.
    ax.grid(True, which="major", axis="y", color="#d7dce1", lw=0.7, zorder=0)
    ax.grid(True, which="major", axis="x", color="#e6eaee", lw=0.6, zorder=0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)

    ax.set_xticks(np.arange(1800, 2101, 25))
    ax.set_yticks([1e9, 2e9, 4e9, 8e9, 1.6e10])
    ax.set_yticklabels(["1 billion", "2 billion", "4 billion", "8 billion",
                        "16 billion"])
    ax.yaxis.set_minor_locator(plt.NullLocator())
    ax.yaxis.set_minor_formatter(plt.NullFormatter())

    ax.set_ylabel("World population (log scale)")
    ax.set_title(
        "World population: humanity's most powerful exponential",
        loc="left", pad=12, fontweight="bold")

    # Annotation: fitted doubling time, pointing at the boom window.
    x_mid = fit_years[len(fit_years) // 2]
    y_mid = fit_pop[len(fit_pop) // 2]
    ax.annotate(
        f"doubling every ~{doubling_years:.0f} years\n"
        f"(exponential fit, {FIT_START}–{FIT_END})",
        xy=(x_mid, y_mid), xycoords="data",
        xytext=(1878, 5.2e9), textcoords="data",
        fontsize=11, color="#8a3f18", ha="center", va="center",
        arrowprops=dict(arrowstyle="-", color="#c05621", lw=1.0,
                        shrinkA=6, shrinkB=8),
    )

    # Direct labels for the two segments of the single series.
    ax.text(1888, 1.28e9, "estimates", color="#2b6cb0", fontsize=11)
    ax.text(2046, 8.0e9, "UN projection\n(medium)", color="#2b6cb0",
            fontsize=11, ha="center", va="top")

    # Footer citing the data source.
    fig.text(0.01, 0.012,
             "Data: Our World in Data (HYDE 3.3 / Gapminder / UN World "
             "Population Prospects 2024) — estimates to 2023, UN medium "
             "projection to 2100",
             fontsize=7.5, color="#6b7280")

    fig.tight_layout(rect=(0, 0.035, 1, 1))
    fig.savefig(out_png)
    plt.close(fig)


def main():
    """Load data, scan windows, fit the boom, and save the figure."""
    hist, proj = load_world_population(DATA_CSV)
    print(f"Historical: {hist['year'].iloc[0]}-{hist['year'].iloc[-1]} "
          f"({hist['pop'].iloc[-1]:,.0f} in {hist['year'].iloc[-1]})")
    print(f"Projection: {proj['year'].iloc[1]}-{proj['year'].iloc[-1]} "
          f"(peak {proj['pop'].max():,.0f} in "
          f"{proj.loc[proj['pop'].idxmax(), 'year']})")
    scan_fit_windows(hist)
    doubling_years, fit_years, fit_pop = fit_doubling_time(
        hist, FIT_START, FIT_END)
    print(f"Fit window: {FIT_START}-{FIT_END}")
    print(f"Fitted doubling time: {doubling_years:.1f} years")
    make_figure(hist, proj, doubling_years, fit_years, fit_pop, OUT_PNG)
    print(f"Wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
