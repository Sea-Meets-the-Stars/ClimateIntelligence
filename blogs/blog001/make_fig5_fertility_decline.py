"""Figure 5: Global total fertility rate vs. the 2.1 replacement threshold.

Plots the world's total fertility rate (TFR) from UN estimates (1950-present)
and UN medium-variant projections (to 2100), against the replacement-level
line of 2.1 children per woman. Unlike Figures 1-4 of this post, the y-axis
is deliberately LINEAR: this is a threshold-crossing story, not a doubling
story. The year the global curve crosses below 2.1 is annotated.

Data: Our World in Data, "Fertility rate, with UN projections" (UN World
Population Prospects), cached at
CI_Reports/data/owid_fertility_with_projections.csv.

Usage:
    conda run -n ocean14 python blogs/blog001/make_fig5_fertility_decline.py
"""

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA_PATH = "CI_Reports/data/owid_fertility_with_projections.csv"
OUT_PATH = "blogs/blog001/fig5_fertility_decline.png"

REPLACEMENT = 2.1

# Colors (single-series chart: one hue; dash style separates estimates
# from projections; the threshold line gets a reserved warm accent).
COLOR_TFR = "#2f6fb3"       # blue for the world TFR curve
COLOR_THRESHOLD = "#c25454"  # muted red for the 2.1 replacement line
COLOR_INK = "#333333"        # primary text
COLOR_MUTED = "#777777"      # secondary text / footer


def load_world_tfr(path):
    """Load the OWID fertility CSV and return the World rows.

    Parameters
    ----------
    path : str
        Path to the cached OWID CSV.

    Returns
    -------
    est : pandas.DataFrame
        Columns ``Year`` and ``tfr`` for the historical UN estimates.
    proj : pandas.DataFrame
        Columns ``Year`` and ``tfr`` for the UN medium-variant projections.
    """
    df = pd.read_csv(path)
    world = df[df["Entity"] == "World"]

    est = world[["Year", "Fertility rate (estimates)"]].dropna()
    est = est.rename(columns={"Fertility rate (estimates)": "tfr"})

    proj = world[["Year", "Fertility rate (projections) (Projected)"]].dropna()
    proj = proj.rename(
        columns={"Fertility rate (projections) (Projected)": "tfr"})

    return est.sort_values("Year"), proj.sort_values("Year")


def find_crossing(est, proj, threshold=REPLACEMENT):
    """Find the year the world TFR first drops below the threshold.

    Concatenates estimates and projections into one series and linearly
    interpolates between the last year at/above the threshold and the
    first year below it.

    Parameters
    ----------
    est, proj : pandas.DataFrame
        Estimate and projection frames from :func:`load_world_tfr`.
    threshold : float
        The replacement-level TFR.

    Returns
    -------
    year_cross : float
        Interpolated crossing year.
    in_projection : bool
        True if the crossing occurs in the projected portion of the data.
    """
    full = pd.concat([est, proj], ignore_index=True).sort_values("Year")
    years = full["Year"].to_numpy(dtype=float)
    tfr = full["tfr"].to_numpy(dtype=float)

    below = np.where(tfr < threshold)[0]
    if len(below) == 0:
        raise ValueError("TFR never drops below the threshold in this data.")
    i = below[0]  # first year below threshold
    # Linear interpolation between (i-1) and i for the exact crossing.
    y0, y1 = years[i - 1], years[i]
    t0, t1 = tfr[i - 1], tfr[i]
    year_cross = y0 + (threshold - t0) * (y1 - y0) / (t1 - t0)

    last_est_year = est["Year"].max()
    in_projection = years[i] > last_est_year
    return year_cross, in_projection


def make_figure(est, proj, year_cross, out_path=OUT_PATH):
    """Render and save the fertility-decline figure.

    Parameters
    ----------
    est, proj : pandas.DataFrame
        Estimate and projection frames from :func:`load_world_tfr`.
    year_cross : float
        Interpolated year the TFR crosses below replacement.
    out_path : str
        Destination PNG path.
    """
    fig, ax = plt.subplots(figsize=(9, 5.5))

    # Bridge the visual gap between the two segments.
    bridge = pd.concat([est.tail(1), proj.head(1)])

    ax.plot(est["Year"], est["tfr"], color=COLOR_TFR, lw=2.2,
            solid_capstyle="round", label="UN estimates", zorder=3)
    ax.plot(bridge["Year"], bridge["tfr"], color=COLOR_TFR, lw=2.2,
            ls="--", zorder=3)
    ax.plot(proj["Year"], proj["tfr"], color=COLOR_TFR, lw=2.2, ls="--",
            label="UN projection (medium variant)", zorder=3)

    # Replacement-level reference line.
    ax.axhline(REPLACEMENT, color=COLOR_THRESHOLD, lw=1.8, zorder=2)
    ax.text(1951, REPLACEMENT + 0.09,
            "Replacement level: 2.1 children per woman",
            color=COLOR_THRESHOLD, fontsize=10.5, va="bottom")

    # Mark the crossing.
    ax.plot([year_cross], [REPLACEMENT], marker="o", ms=9,
            mfc="white", mec=COLOR_THRESHOLD, mew=2, zorder=4)
    ax.axvline(year_cross, color=COLOR_THRESHOLD, lw=1.0, ls=":",
               alpha=0.7, zorder=1)
    ax.annotate(
        f"World falls below replacement\n~{year_cross:.0f} (UN projection)",
        xy=(year_cross, REPLACEMENT), xytext=(year_cross - 2, 3.15),
        ha="right", fontsize=10.5, color=COLOR_INK,
        arrowprops=dict(arrowstyle="->", color=COLOR_MUTED, lw=1.2,
                        connectionstyle="arc3,rad=0.25"))

    # Context: where we are now (last estimate).
    last = est.iloc[-1]
    ax.annotate(
        f"{last['tfr']:.2f} in {int(last['Year'])}",
        xy=(last["Year"], last["tfr"]),
        xytext=(last["Year"] - 6, last["tfr"] - 0.55),
        ha="right", fontsize=10, color=COLOR_MUTED,
        arrowprops=dict(arrowstyle="->", color=COLOR_MUTED, lw=1.0,
                        connectionstyle="arc3,rad=-0.25"))

    # Axes / styling: linear y-axis, recessive grid.
    ax.set_xlim(1948, 2102)
    ax.set_ylim(0, 5.6)
    ax.set_ylabel("Children per woman (total fertility rate)", fontsize=11)
    ax.set_title("The world is running out of babies (that's the good news)",
                 fontsize=14, color=COLOR_INK, pad=12, loc="left")

    # Figure number for the blog post's sequence (bottom-right corner,
    # mirroring the data-source footer at bottom-left).
    fig.text(0.99, 0.012, "Figure 5", ha="right", fontsize=9.5,
             fontweight="bold", color="#6b7280")
    ax.grid(axis="y", color="#dddddd", lw=0.7, zorder=0)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color("#aaaaaa")
    ax.tick_params(colors="#555555", labelsize=10)

    ax.legend(loc="upper right", frameon=False, fontsize=10.5)

    fig.text(0.01, 0.01,
             "Data: UN World Population Prospects, via Our World in Data",
             fontsize=8.5, color=COLOR_MUTED, ha="left")

    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(out_path, dpi=130)
    plt.close(fig)


def main():
    """Load the data, find the crossing year, and render the figure."""
    est, proj = load_world_tfr(DATA_PATH)
    year_cross, in_projection = find_crossing(est, proj)
    where = "UN projection" if in_projection else "historical estimates"
    print(f"Last estimate: {est['Year'].max():.0f} "
          f"(TFR = {est['tfr'].iloc[-1]:.3f})")
    print(f"World TFR crosses below {REPLACEMENT} in ~{year_cross:.1f} "
          f"({where}).")
    make_figure(est, proj, year_cross)
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
