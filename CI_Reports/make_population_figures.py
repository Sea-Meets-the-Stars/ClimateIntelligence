"""Created by JXP and Claude.

Generate the population figures (7-9) for the Climate Intelligence report
(CI_2026_07_09_climate_report.md, section on global population). Each figure is
built from real, publicly archived data cached under CI_Reports/data/ (fetched
2026-07-11); provenance and baselines are annotated on the figures themselves.

Data sources (see references in the report):
  - World population, 1800-2023 estimates + UN medium projection to 2100:
    Our World in Data grapher "population-long-run-with-projections"
    (HYDE 3.3 + Gapminder + UN World Population Prospects 2024), cached as
    data/owid_population_long_run_projections.csv
  - Total fertility rate, 1950-2023 estimates + UN medium projection to 2100,
    world + UN regions: Our World in Data grapher
    "fertility-rate-with-projections" (UN WPP 2024), cached as
    data/owid_fertility_with_projections.csv
  - 95% prediction intervals and comparison projections (IHME 2020,
    Wittgenstein Centre 2023) are single anchor values quoted from
    UN WPP 2024 "Summary of Results" and Lancet/IHME (2020); they are
    annotated as points/bars, not fabricated fans.

Run under the project conda environment:
    conda run -n ocean14 python CI_Reports/make_population_figures.py

Design choices follow the project coding guidelines: functions (no classes),
imports at top, inline comments, matplotlib for plotting, docstrings with
inputs/outputs, and "Created by JXP and Claude" on the file and each method.
"""

# Imports at the top of the file (project coding guideline).
import csv
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")  # headless backend; we save PNGs, never display
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

# Same visual style as make_figures.py, for a consistent report.
plt.rcParams.update({
    "figure.dpi": 130,
    "savefig.dpi": 130,
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# Anchor values quoted from the primary sources (not derivable from the cached
# series). UN 95% prediction intervals: WPP 2024 Summary of Results, ch. IV
# ("10.2 billion, ranging from 9.0 to 11.4 billion, with a probability of 95
# per cent"). IHME: Vollset et al. 2020, Lancet (8.8 [6.8-11.8] billion in
# 2100). WIC: Wittgenstein Centre 2023 (9.9 billion in 2100), as quoted in the
# same WPP 2024 box.
UN_2100 = (10.18, 9.0, 11.4)     # median, lo95, hi95 (billions)
IHME_2100 = (8.8, 6.8, 11.8)
WIC_2100 = 9.9


def load_world_population():
    """Created by JXP and Claude.

    Load the OWID long-run world population series (estimates + UN medium
    projection).

    Inputs
    ------
    (none) reads data/owid_population_long_run_projections.csv
    Columns: Entity, Code, Year, Population (projections) (Projected), Population

    Outputs
    -------
    (np.ndarray, np.ndarray, np.ndarray, np.ndarray)
        est_year, est_pop, proj_year, proj_pop  (population in billions).
    """
    est, proj = [], []
    with open(DATA / "owid_population_long_run_projections.csv") as f:
        for row in csv.DictReader(f):
            year = int(row["Year"])
            if row["Population"]:
                est.append((year, float(row["Population"]) / 1e9))
            if row["Population (projections) (Projected)"]:
                proj.append((year, float(row["Population (projections) (Projected)"]) / 1e9))
    est.sort(); proj.sort()
    ey, ep = np.array([r[0] for r in est]), np.array([r[1] for r in est])
    py, pp = np.array([r[0] for r in proj]), np.array([r[1] for r in proj])
    return ey, ep, py, pp


def load_fertility():
    """Created by JXP and Claude.

    Load the OWID fertility series (UN WPP 2024 estimates + medium projection)
    for the world and UN regions.

    Inputs
    ------
    (none) reads data/owid_fertility_with_projections.csv
    Columns: Entity, Code, Year, Fertility rate (estimates),
             Fertility rate (projections) (Projected)

    Outputs
    -------
    dict
        entity -> (year np.ndarray, tfr np.ndarray) with estimates and
        projections concatenated into one continuous series.
    """
    series = {}
    with open(DATA / "owid_fertility_with_projections.csv") as f:
        for row in csv.DictReader(f):
            val = row["Fertility rate (estimates)"] or \
                row["Fertility rate (projections) (Projected)"]
            if not val:
                continue
            series.setdefault(row["Entity"], []).append((int(row["Year"]), float(val)))
    out = {}
    for entity, rows in series.items():
        rows.sort()
        out[entity] = (np.array([r[0] for r in rows]), np.array([r[1] for r in rows]))
    return out


def first_crossing(year, pop, threshold):
    """Created by JXP and Claude.

    Return the first year the population series reaches a threshold.

    Inputs
    ------
    year, pop : np.ndarray
        Year and population (billions), sorted by year.
    threshold : float
        Population level in billions.

    Outputs
    -------
    int
        First year with pop >= threshold.
    """
    return int(year[np.argmax(pop >= threshold)])


def fig7_world_population():
    """Created by JXP and Claude.

    Figure 7: world population 1900-2100 — estimates, UN medium projection,
    milestone crossings, and the spread of end-of-century projections
    (UN / Wittgenstein / IHME) as annotated uncertainty bars.

    Inputs
    ------
    (none) reads the cached OWID series.

    Outputs
    -------
    None. Saves fig7_world_population.png.
    """
    ey, ep, py, pp = load_world_population()
    keep = ey >= 1900
    ey, ep = ey[keep], ep[keep]

    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.plot(ey, ep, color="#1f5fa6", lw=2, label="Estimates (HYDE/Gapminder/UN)")
    ax.plot(py, pp, color="#1f5fa6", lw=2, ls="--",
            label="UN WPP 2024 medium projection")

    # Peak of the medium projection.
    ipk = np.argmax(pp)
    ax.plot(py[ipk], pp[ipk], "o", color="#c0392b", ms=7, zorder=5)
    ax.annotate(f"peak {pp[ipk]:.1f} B in {py[ipk]}",
                (py[ipk], pp[ipk]), xytext=(py[ipk] - 46, pp[ipk] + 0.25),
                fontsize=9, color="#c0392b")

    # Billion-crossing milestones computed from the series itself.
    for level in (2, 4, 8):
        yr = first_crossing(np.r_[ey, py], np.r_[ep, pp], level)
        ax.plot(yr, level, "o", color="#1f5fa6", ms=5)
        ax.annotate(f"{level} B — {yr}", (yr, level),
                    xytext=(yr + 3, level - 0.55), fontsize=9, color="#333")

    # End-of-century spread across independent projections: vertical 95% bars.
    for x, (mid, lo, hi), name, color, ytext in (
            (2101.5, UN_2100, "UN", "#1f5fa6", 11.55),
            (2105.5, IHME_2100, "IHME", "#b9430f", 11.95)):
        ax.errorbar(x, mid, yerr=[[mid - lo], [hi - mid]], fmt="o", ms=5,
                    color=color, capsize=3, lw=1.4, clip_on=False)
        ax.annotate(name, (x, ytext), fontsize=8, ha="center",
                    color=color, annotation_clip=False)
    ax.plot(2103.5, WIC_2100, "s", ms=5, color="#16a085", clip_on=False)
    ax.annotate("WIC", (2103.5, 9.35), fontsize=8, ha="center",
                color="#16a085", annotation_clip=False)

    ax.set_xlim(1900, 2100)
    ax.set_ylim(0, 12.2)
    ax.set_xlabel("Year")
    ax.set_ylabel("World population (billions)")
    ax.set_title("World population, 1900–2100: a century of growth approaching its peak")
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    fig.text(0.99, 0.01,
             "Data: OWID (HYDE 3.3/Gapminder/UN WPP 2024), fetched 2026-07-11. "
             "2100 bars: 95% prediction intervals (UN WPP 2024; IHME/Lancet 2020); WIC 2023 median.",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(HERE / "fig7_world_population.png")
    plt.close(fig)


def fig8_growth_rate():
    """Created by JXP and Claude.

    Figure 8: the rise and fall of growth — annual growth rate (%/yr, top) and
    absolute annual increment (millions/yr, bottom), 1900-2100, computed
    directly from the population series (two panels, one axis each).

    Inputs
    ------
    (none) reads the cached OWID series.

    Outputs
    -------
    None. Saves fig8_growth_rate.png.
    """
    ey, ep, py, pp = load_world_population()
    # One continuous series so the rate is defined across the 2023/24 seam.
    year = np.r_[ey, py]
    pop = np.r_[ep, pp]
    keep = year >= 1899
    year, pop = year[keep], pop[keep]
    # Centered growth measures from year-over-year differences.
    rate = 100 * np.diff(np.log(pop))          # %/yr
    incr = 1000 * np.diff(pop)                 # millions/yr
    ymid = 0.5 * (year[1:] + year[:-1])
    # 5-year smoothing to suppress single-year census/revision steps; 'valid'
    # mode avoids zero-padding bias at the 1900 and 2100 edges.
    kern = np.ones(5) / 5
    rate_s = np.convolve(rate, kern, mode="valid")
    incr_s = np.convolve(incr, kern, mode="valid")
    ymid = ymid[2:-2]

    fig, axes = plt.subplots(2, 1, figsize=(9, 6.6), sharex=True)

    axes[0].plot(ymid, rate_s, color="#c0392b", lw=2)
    axes[0].axhline(0, color="gray", lw=0.8)
    axes[0].set_ylabel("Growth rate (% per year)")
    ipk = np.argmax(rate_s)
    axes[0].plot(ymid[ipk], rate_s[ipk], "o", color="#c0392b", ms=6)
    axes[0].annotate(f"peak ≈ {rate_s[ipk]:.1f}%/yr ({ymid[ipk]:.0f})",
                     (ymid[ipk], rate_s[ipk]),
                     xytext=(ymid[ipk] + 8, rate_s[ipk] + 0.05), fontsize=9,
                     color="#c0392b")
    inow = np.argmin(np.abs(ymid - 2025))
    axes[0].annotate(f"2025 ≈ {rate_s[inow]:.1f}%/yr", (2025, rate_s[inow]),
                     xytext=(1990, rate_s[inow] + 0.45), fontsize=9, color="#333",
                     arrowprops=dict(arrowstyle="-", color="#999", lw=0.8))
    axes[0].axvline(2024, color="gray", lw=0.8, ls=":")
    axes[0].text(2026, 1.95, "projection →", fontsize=8, color="gray")

    axes[1].plot(ymid, incr_s, color="#1f5fa6", lw=2)
    axes[1].axhline(0, color="gray", lw=0.8)
    axes[1].set_ylabel("Net addition (millions per year)")
    axes[1].set_xlabel("Year")
    jpk = np.argmax(incr_s)
    axes[1].plot(ymid[jpk], incr_s[jpk], "o", color="#1f5fa6", ms=6)
    axes[1].annotate(f"peak ≈ {incr_s[jpk]:.0f} M/yr ({ymid[jpk]:.0f})",
                     (ymid[jpk], incr_s[jpk]),
                     xytext=(ymid[jpk] + 8, incr_s[jpk] - 4), fontsize=9,
                     color="#1f5fa6")
    axes[1].axvline(2024, color="gray", lw=0.8, ls=":")

    axes[0].set_title("The great acceleration, ending: growth rate and net additions")
    axes[0].set_xlim(1900, 2100)
    fig.text(0.99, 0.01,
             "Computed from OWID population series (5-yr smoothed); "
             "projection = UN WPP 2024 medium. Fetched 2026-07-11.",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(HERE / "fig8_growth_rate.png")
    plt.close(fig)


def fig9_fertility():
    """Created by JXP and Claude.

    Figure 9: total fertility rate, 1950-2100, world + UN regions, with the
    replacement level marked. Fixed categorical color order; direct labels.

    Inputs
    ------
    (none) reads the cached OWID fertility series.

    Outputs
    -------
    None. Saves fig9_fertility.png.
    """
    series = load_fertility()
    # Fixed entity -> color assignment (never cycled), consistent with the
    # report's palette; World gets the neutral, heaviest line.
    entities = [
        ("Africa (UN)", "#c0392b"),
        ("Asia (UN)", "#8e44ad"),
        ("Latin America and the Caribbean (UN)", "#16a085"),
        ("Northern America (UN)", "#b9430f"),
        ("Europe (UN)", "#1f5fa6"),
    ]

    fig, ax = plt.subplots(figsize=(9, 5.2))
    # Collect (end value, label, color) so the direct labels can be spread
    # vertically without overlapping — the 2100 values cluster near 1.6-2.0.
    labels = []
    for name, color in entities:
        yr, tfr = series[name]
        ax.plot(yr, tfr, color=color, lw=1.6, alpha=0.9)
        label = name.replace(" (UN)", "").replace(
            "Latin America and the Caribbean", "Latin America & Carib.")
        labels.append([tfr[-1], label, color, False])
    yr, tfr = series["World"]
    ax.plot(yr, tfr, color="black", lw=2.6)
    labels.append([tfr[-1], "World", "black", True])
    # De-overlap: sort by end value, then push labels apart to >=0.22 spacing.
    labels.sort(key=lambda r: r[0])
    ypos = [r[0] for r in labels]
    for i in range(1, len(ypos)):
        ypos[i] = max(ypos[i], ypos[i - 1] + 0.22)
    for (val, label, color, bold), y in zip(labels, ypos):
        ax.annotate(label, (2101.5, y), fontsize=9, color=color,
                    va="center", annotation_clip=False,
                    fontweight="bold" if bold else "normal")

    ax.axhline(2.1, ls="--", color="gray", lw=1)
    ax.text(1952, 2.16, "replacement level ≈ 2.1", color="gray", fontsize=9)
    ax.axvline(2024, color="gray", lw=0.8, ls=":")
    ax.text(2026, 6.4, "projection →", fontsize=8, color="gray")

    ax.set_xlim(1950, 2100)
    ax.set_ylim(0, 7)
    ax.set_xlabel("Year")
    ax.set_ylabel("Total fertility rate (births per woman)")
    ax.set_title("The demographic transition: fertility by region, 1950–2100")
    fig.text(0.99, 0.01,
             "Data: UN WPP 2024 via OWID (estimates to 2023; medium projection "
             "2024–2100), fetched 2026-07-11.",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(HERE / "fig9_fertility.png")
    plt.close(fig)


def main():
    """Created by JXP and Claude.

    Generate all population figures for the report.

    Inputs
    ------
    (none)

    Outputs
    -------
    None. Writes fig7-fig9 PNGs next to this script.
    """
    fig7_world_population()
    fig8_growth_rate()
    fig9_fertility()
    print("Wrote fig7_world_population.png, fig8_growth_rate.png, "
          "fig9_fertility.png")


if __name__ == "__main__":
    main()
