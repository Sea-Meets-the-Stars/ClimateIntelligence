"""Figure 2 for Blog 001 ("Humans Suck at Exponentials").

Plots world population from 10,000 BCE to 2100 on a log y-axis:
historical estimates (solid) through 2023 and the UN medium projection
(dashed, shaded era) through 2100. The time axis is logarithmic in
"years before 2125" (a Kremer-style deep-history axis), so the ~12,000
years of slow agricultural-era growth stay visible while the last two
centuries -- where all the action is -- get most of the plot width.

Fits exponentials to four distinct growth eras and annotates each with
its fitted doubling time:
    1. Agricultural era        (10,000 BCE - 1700 CE)
    2. Early industrial era    (1700 - 1900)
    3. Early 20th century      (1900 - 1950)
    4. Post-war boom           (1950 - 1990)

Data source (cached locally in blogs/blog001/data/):
    owid_population_long_run_full.csv
    https://ourworldindata.org/grapher/population-long-run-with-projections.csv?v=1&csvType=full&useColumnShortNames=true
    Our World in Data long-run world population
    (HYDE 3.3 + Gapminder + UN World Population Prospects 2024).
    Estimates run 10,000 BCE - 2023; UN medium projection 2024-2100.

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
DATA_CSV = os.path.join(SCRIPT_DIR, "data",
                        "owid_population_long_run_full.csv")
OUT_PNG = os.path.join(SCRIPT_DIR, "fig2_population_growth.png")

# Reference year for the log time axis: x = REF_YEAR - year ("years
# before 2125"). Chosen slightly beyond the 2100 projection endpoint so
# every plotted year maps to a positive, loggable value.
REF_YEAR = 2125

# Exponential-fit windows (inclusive calendar-year bounds). Boundaries
# picked where the doubling cadence visibly shifts regime: growth was
# glacially slow through the agricultural millennia, stepped up with the
# industrial revolution, accelerated again in the early 20th century,
# and peaked in the post-war boom (rates near 2.1%/yr, 1950s-1980s).
FIT_PERIODS = [
    {"name": "Agricultural era", "start": -10000, "end": 1700},
    {"name": "Early industrial", "start": 1700, "end": 1900},
    {"name": "Early 20th century", "start": 1900, "end": 1950},
    {"name": "Post-war boom", "start": 1950, "end": 1990},
]


def to_before(year):
    """Convert calendar year(s) to 'years before REF_YEAR' (loggable)."""
    return REF_YEAR - np.asarray(year, dtype=float)


def load_world_population(csv_path):
    """Load the OWID long-run world population series.

    Parameters
    ----------
    csv_path : str
        Path to owid_population_long_run_full.csv (columns: entity,
        code, year, population_projection__projected,
        population_historical).

    Returns
    -------
    hist : pandas.DataFrame
        Historical estimates -- columns ``year`` (int) and ``pop``
        (float), sorted by year (-10000 to 2023).
    proj : pandas.DataFrame
        UN medium projection -- same columns (2024-2100), with the last
        historical point prepended so the plotted curves connect.
    """
    df = pd.read_csv(csv_path)
    df = df[df["code"] == "OWID_WRL"].sort_values("year")
    hist = (df[["year", "population_historical"]]
            .dropna()
            .rename(columns={"population_historical": "pop"})
            .reset_index(drop=True))
    proj = (df[["year", "population_projection__projected"]]
            .dropna()
            .rename(columns={"population_projection__projected": "pop"})
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
    slope, intercept : float
        Fit coefficients of log2(pop) = slope * year + intercept.
    """
    win = hist[(hist["year"] >= start) & (hist["year"] <= end)]
    years = win["year"].to_numpy(float)
    log2_pop = np.log2(win["pop"].to_numpy(float))
    slope, intercept = np.polyfit(years, log2_pop, 1)
    return 1.0 / slope, slope, intercept


def fit_curve(slope, intercept, start, end, n=200):
    """Evaluate the fitted exponential on a grid dense in log-x space.

    Parameters
    ----------
    slope, intercept : float
        Coefficients from :func:`fit_doubling_time`.
    start, end : int
        Calendar-year bounds of the fit window.
    n : int
        Number of grid points.

    Returns
    -------
    years : numpy.ndarray
        Calendar years, geometrically spaced in years-before-REF_YEAR
        so the curve renders smoothly on the log time axis.
    pop : numpy.ndarray
        Model population on those years.
    """
    x = np.geomspace(to_before(end), to_before(start), n)
    years = REF_YEAR - x
    pop = 2.0 ** (slope * years + intercept)
    return years, pop


def fmt_doubling(t2):
    """Format a doubling time for annotation (rounded, with commas)."""
    if t2 >= 200:
        return f"{round(t2, -2):,.0f}"
    return f"{t2:.0f}"


def fmt_year(y):
    """Format a calendar year for annotation (BCE/CE aware)."""
    if y < 0:
        return f"{-y:,d} BCE"
    if y == 0:
        return "1 CE"
    return f"{y:d}"


def make_figure(hist, proj, fits, out_png):
    """Render and save the deep-history figure with era annotations.

    Parameters
    ----------
    hist, proj : pandas.DataFrame
        Historical and projected series (columns ``year``, ``pop``).
    fits : list of dict
        One entry per era: keys ``name``, ``start``, ``end``,
        ``doubling``, ``slope``, ``intercept``.
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

    fig, ax = plt.subplots(figsize=(10, 6))

    # Shade the projection era so the estimate/projection boundary reads
    # at a glance, in addition to the solid/dashed line change.
    proj_start = proj["year"].iloc[1]
    ax.axvspan(to_before(proj_start), to_before(2100), color="#eef1f5",
               zorder=0)

    # Historical estimates (solid) and UN medium projection (dashed).
    ax.plot(to_before(hist["year"]), hist["pop"], color="#2b6cb0", lw=2.0,
            solid_capstyle="round", zorder=3)
    ax.plot(to_before(proj["year"]), proj["pop"], color="#2b6cb0", lw=2.0,
            ls=(0, (4, 2.5)), zorder=3)

    # Fitted exponentials over each era, as dashed overlays.
    for f in fits:
        yrs, pop = fit_curve(f["slope"], f["intercept"], f["start"],
                             f["end"])
        ax.plot(to_before(yrs), pop, color="#c05621", lw=2.2, ls="--",
                zorder=4)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(to_before(-11500), to_before(2108))
    ax.set_ylim(3e6, 2.2e10)

    # Recessive grid, no chartjunk.
    ax.grid(True, which="major", axis="y", color="#d7dce1", lw=0.7,
            zorder=0)
    ax.grid(True, which="major", axis="x", color="#e6eaee", lw=0.6,
            zorder=0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)

    # Calendar-year ticks on the log years-before axis.
    tick_years = [-10000, -5000, -2000, 0, 1000, 1500, 1800,
                  1950, 2000, 2050, 2100]
    tick_labels = ["10,000\nBCE", "5000\nBCE", "2000\nBCE", "1 CE",
                   "1000", "1500", "1800", "1950", "2000",
                   "2050", "2100"]
    ax.set_xticks(to_before(tick_years))
    ax.set_xticklabels(tick_labels, fontsize=9.5)
    ax.xaxis.set_minor_locator(plt.NullLocator())
    ax.xaxis.set_minor_formatter(plt.NullFormatter())

    ax.set_yticks([1e7, 1e8, 1e9, 1e10])
    ax.set_yticklabels(["10 million", "100 million", "1 billion",
                        "10 billion"])
    ax.yaxis.set_minor_locator(plt.NullLocator())
    ax.yaxis.set_minor_formatter(plt.NullFormatter())

    ax.set_xlabel("Year  (log timescale: recent centuries expanded)")
    ax.set_ylabel("World population (log scale)")
    ax.set_title(
        "World population: humanity's most powerful exponential",
        loc="left", pad=12, fontweight="bold")

    # Era annotations: a diagonal cascade in the empty space below the
    # rising curve, each pointing at the midpoint of its fit segment.
    label_spots = [  # (x_text in years-before, y_text) per era, in order
        (2500, 1.6e7),
        (420, 6.5e7),
        (165, 3.2e8),
        (63, 1.3e9),
    ]
    for f, (xt, yt) in zip(fits, label_spots):
        # Midpoint of the fit segment, in log-x space.
        xa = np.sqrt(to_before(f["start"]) * to_before(f["end"]))
        year_mid = REF_YEAR - xa
        ya = 2.0 ** (f["slope"] * year_mid + f["intercept"])
        ax.annotate(
            f"{f['name']}\ndoubling every ~{fmt_doubling(f['doubling'])} "
            f"yr\n({fmt_year(f['start'])}–{fmt_year(f['end'])})",
            xy=(xa, ya), xycoords="data",
            xytext=(xt, yt), textcoords="data",
            fontsize=9.5, color="#8a3f18", ha="center", va="center",
            arrowprops=dict(arrowstyle="-", color="#c05621", lw=1.0,
                            shrinkA=8, shrinkB=6),
        )

    # Direct labels for the two segments of the single series.
    ax.text(to_before(-3500), 3.2e8, "historical estimates",
            color="#2b6cb0", fontsize=10.5, ha="center")
    ax.text(to_before(2058), 1.35e10, "UN projection\n(medium)",
            color="#2b6cb0", fontsize=10, ha="center", va="bottom")

    # Figure number for the blog post's sequence (bottom-right corner,
    # mirroring the data-source footer at bottom-left) -- matches the
    # placement convention used by figures 1, 3, 4, and 5.
    fig.text(0.99, 0.012, "Figure 2", ha="right", fontsize=9.5,
             fontweight="bold", color="#6b7280")

    # Footer citing the data source.
    fig.text(0.01, 0.012,
             "Data: Our World in Data (HYDE 3.3 / Gapminder / UN World "
             "Population Prospects 2024) — estimates 10,000 BCE to 2023, "
             "UN medium projection to 2100",
             fontsize=7.5, color="#6b7280")

    fig.tight_layout(rect=(0, 0.035, 1, 1))
    fig.savefig(out_png)
    plt.close(fig)


def main():
    """Load data, fit each era's exponential, and save the figure."""
    hist, proj = load_world_population(DATA_CSV)
    print(f"Historical: {hist['year'].iloc[0]}-{hist['year'].iloc[-1]} "
          f"({hist['pop'].iloc[-1]:,.0f} in {hist['year'].iloc[-1]})")
    print(f"Projection: {proj['year'].iloc[1]}-{proj['year'].iloc[-1]} "
          f"(peak {proj['pop'].max():,.0f} in "
          f"{proj.loc[proj['pop'].idxmax(), 'year']})")
    fits = []
    for period in FIT_PERIODS:
        t2, slope, intercept = fit_doubling_time(
            hist, period["start"], period["end"])
        fits.append({**period, "doubling": t2, "slope": slope,
                     "intercept": intercept})
        print(f"  {period['name']:<20s} {period['start']:>6d} to "
              f"{period['end']:>4d}: doubling every {t2:8.1f} yr")
    make_figure(hist, proj, fits, OUT_PNG)
    print(f"Wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
