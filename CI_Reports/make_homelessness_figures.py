"""Created by JXP and Claude.

Generate the homelessness figures (10-12) for the Climate Intelligence report
(CI_2026_07_09_climate_report.md, Section 7). All three use real, archived data
cached under CI_Reports/data/ (fetched 2026-07-12); provenance is annotated on
each figure.

Figures:
  10. U.S. homeless population by year (HUD point-in-time count), 2007-2025,
      showing the 2016 low, the record 2024 spike, and the 2021 data gap.
  11. Homelessness rate per 10,000 by U.S. state, 2024 (highest ~12 and lowest
      ~5, with the national average marked).
  12. Reported homelessness rate per 10,000 by country (national definitions) —
      with a prominent comparability caveat.

Data sources (see report references):
  - HUD AHAR Part 1 point-in-time counts -> data/us_homeless_by_year.csv
  - HUD 2024 PIT state rates per 10,000 -> data/state_homeless_rate_2024.csv
  - OWID "reported share of people experiencing homelessness" (national
    definitions; converted to per-10,000) -> data/country_homeless_rate.csv

Run under the project conda environment:
    conda run -n ocean14 python CI_Reports/make_homelessness_figures.py

Design follows the project coding guidelines: functions (no classes), imports at
top, inline comments, matplotlib, docstrings, "Created by JXP and Claude".
Visual style matches CI_Reports/make_figures.py.
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

plt.rcParams.update({
    "figure.dpi": 130,
    "savefig.dpi": 130,
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def load_year_series():
    """Created by JXP and Claude.

    Load the U.S. point-in-time homeless count by year.

    Inputs
    ------
    (none) reads data/us_homeless_by_year.csv (blank total = data gap).

    Outputs
    -------
    (np.ndarray, np.ndarray)
        year, total  (total is NaN where the count is missing, e.g. 2021).
    """
    years, totals = [], []
    with open(DATA / "us_homeless_by_year.csv") as f:
        for r in csv.DictReader(f):
            years.append(int(r["year"]))
            totals.append(float(r["total"]) if r["total"] else np.nan)
    return np.array(years), np.array(totals)


def load_rate_csv(fname, key):
    """Created by JXP and Claude.

    Load a name/rate CSV into parallel lists (file order preserved).

    Inputs
    ------
    fname : str
        CSV file under data/.
    key : str
        Column holding the label (e.g. 'state' or 'country').

    Outputs
    -------
    list[dict]
        Raw rows as dicts.
    """
    with open(DATA / fname) as f:
        return list(csv.DictReader(f))


def fig10_by_year():
    """Created by JXP and Claude.

    Figure 10: U.S. homeless population by year (HUD PIT), 2007-2025.

    Inputs
    ------
    (none) reads the cached year series.

    Outputs
    -------
    None. Saves fig10_us_homeless_by_year.png.
    """
    year, total = load_year_series()
    good = ~np.isnan(total)

    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    # Plot the connected series across the 2021 gap by masking NaNs; matplotlib
    # breaks the line at NaN automatically, which correctly shows the data gap.
    ax.plot(year, total / 1e3, color="#c0392b", lw=2, marker="o", ms=4,
            zorder=3)
    # Mark the 2016 minimum and 2024 maximum among observed years.
    yr_obs, tot_obs = year[good], total[good]
    imin = int(np.argmin(tot_obs))
    imax = int(np.argmax(tot_obs))
    ax.annotate(f"2016 low\n{tot_obs[imin]/1e3:.0f}k",
                (yr_obs[imin], tot_obs[imin] / 1e3),
                xytext=(yr_obs[imin] - 0.5, tot_obs[imin] / 1e3 - 60),
                fontsize=9, color="#333", ha="center",
                arrowprops=dict(arrowstyle="->", color="#999", lw=0.8))
    ax.annotate(f"2024 record\n{tot_obs[imax]/1e3:.0f}k",
                (yr_obs[imax], tot_obs[imax] / 1e3),
                xytext=(yr_obs[imax] - 1.6, tot_obs[imax] / 1e3 + 5),
                fontsize=9, color="#c0392b", ha="center", fontweight="bold")
    # Flag the 2021 gap.
    ax.axvspan(2020.5, 2021.5, color="gray", alpha=0.12)
    ax.text(2021, 500, "2021:\nno full\ncount\n(COVID)", fontsize=7.5,
            color="#777", ha="center", va="center")

    ax.set_xlim(2006.5, 2025.5)
    ax.set_ylim(480, 820)
    ax.set_xlabel("Year")
    ax.set_ylabel("People experiencing homelessness (thousands)")
    ax.set_title("U.S. homelessness by year: a decade of decline, then a record surge\n"
                 "HUD point-in-time count, one January night, 2007–2025")
    fig.text(0.99, 0.01,
             "Data: HUD AHAR Part 1 (point-in-time counts). 2021 unsheltered "
             "count largely waived for COVID. Fetched 2026-07-12.",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(HERE / "fig10_us_homeless_by_year.png")
    plt.close(fig)


def fig11_by_state():
    """Created by JXP and Claude.

    Figure 11: homelessness rate per 10,000 by U.S. state, 2024 — highest ~12
    and lowest ~5, with the national average marked.

    Inputs
    ------
    (none) reads the cached state rates.

    Outputs
    -------
    None. Saves fig11_us_homeless_by_state.png.
    """
    rows = load_rate_csv("state_homeless_rate_2024.csv", "state")
    NATIONAL = 22.7  # HUD 2024 national rate per 10,000
    # Sort within the file (already high->low then low group); build a single
    # descending list, coloring by group.
    states = [r["state"] for r in rows]
    rates = [float(r["rate_per_10k"]) for r in rows]
    groups = [r["group"] for r in rows]
    order = np.argsort(rates)  # ascending so highest ends at top of barh
    y = np.arange(len(rows))
    colors = ["#c0392b" if groups[i] == "high" else "#4a90d9" for i in order]

    fig, ax = plt.subplots(figsize=(9, 6.6))
    ax.barh(y, [rates[i] for i in order], color=colors, alpha=0.9)
    for yi, i in zip(y, order):
        ax.text(rates[i] + 0.7, yi, f"{rates[i]:.1f}", va="center", fontsize=8)
    ax.set_yticks(y)
    ax.set_yticklabels([states[i] for i in order], fontsize=9)
    ax.axvline(NATIONAL, color="#333", ls="--", lw=1.2)
    ax.text(NATIONAL + 0.6, 0.3, f"national avg {NATIONAL}", rotation=90,
            fontsize=8, color="#333", va="bottom")
    ax.set_xlim(0, 90)
    ax.set_xlabel("People experiencing homelessness per 10,000 residents (2024)")
    ax.set_title("Homelessness is intensely geographic: rate per 10,000 by state, 2024\n"
                 "highest 12 (red) and lowest 5 (blue) — a 23× spread")
    ax.grid(axis="y", visible=False)
    fig.text(0.99, 0.005,
             "Data: HUD 2024 PIT state rates. Fetched 2026-07-12.",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(HERE / "fig11_us_homeless_by_state.png")
    plt.close(fig)


def fig12_by_country():
    """Created by JXP and Claude.

    Figure 12: reported homelessness rate per 10,000 by country (national
    definitions), with a prominent comparability caveat. Finland highlighted.

    Inputs
    ------
    (none) reads the cached country rates.

    Outputs
    -------
    None. Saves fig12_homeless_by_country.png.
    """
    rows = load_rate_csv("country_homeless_rate.csv", "country")
    countries = [r["country"] for r in rows]
    rates = [float(r["rate_per_10k"]) for r in rows]
    years = [r["year"] for r in rows]
    order = np.argsort(rates)  # ascending -> highest on top in barh
    y = np.arange(len(rows))

    # Highlight Finland (the policy standout) and the US (our reference).
    def color_for(name):
        if name == "Finland":
            return "#1a9850"
        if name == "United States":
            return "#c0392b"
        return "#7f8c9b"

    colors = [color_for(countries[i]) for i in order]

    fig, ax = plt.subplots(figsize=(9, 5.6))
    ax.barh(y, [rates[i] for i in order], color=colors, alpha=0.9)
    for yi, i in zip(y, order):
        ax.text(rates[i] + 0.5, yi, f"{rates[i]:.1f}  ({years[i]})",
                va="center", fontsize=8)
    ax.set_yticks(y)
    ax.set_yticklabels([countries[i] for i in order], fontsize=9)
    ax.set_xlim(0, 55)
    ax.set_xlabel("Reported people experiencing homelessness per 10,000 "
                  "(national definition, latest year)")
    ax.set_title("Homelessness rate by country — read with care\n"
                 "Finland (green) lowest of its peers; U.S. (red) for reference")
    ax.grid(axis="y", visible=False)
    # Prominent comparability caveat (Principle 1).
    ax.text(0.98, 0.04,
            "CAVEAT: definitions are NOT harmonized across countries — some count\n"
            "only rough sleepers, others include shelters, institutions, or people\n"
            "staying with others. Broad-definition counts (e.g. Germany ~1.03M incl.\n"
            "refugees/institutional; France) are omitted to avoid false comparison.",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=7.5,
            color="#444", bbox=dict(boxstyle="round", fc="#fff7e6",
                                    ec="#e0b050", lw=0.8))
    fig.text(0.99, 0.005,
             "Data: OWID 'reported share of population experiencing homelessness' "
             "(national defs), ×100 to per-10,000. Fetched 2026-07-12.",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(HERE / "fig12_homeless_by_country.png")
    plt.close(fig)


def main():
    """Created by JXP and Claude.

    Generate all homelessness figures.

    Inputs
    ------
    (none)

    Outputs
    -------
    None. Writes fig10-fig12 PNGs beside this script.
    """
    fig10_by_year()
    fig11_by_state()
    fig12_by_country()
    print("Wrote fig10_us_homeless_by_year.png, fig11_us_homeless_by_state.png, "
          "fig12_homeless_by_country.png")


if __name__ == "__main__":
    main()
