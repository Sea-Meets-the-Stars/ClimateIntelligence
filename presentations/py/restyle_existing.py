"""Created by JXP and Claude.

B2: slide versions of existing Climate Intelligence report figures for the
WMKO 2026 talk. Originals in CI_Reports/ are untouched; numbers come from
the same sources (refreshed where the source has updated).

  C1  c1_keeling.png           <- CI_Reports fig1  (NOAA GML, refreshed 2026-10-05)
  C2  c2_us_cumulative.png     <- CI_Reports fig24 right panel (GCB 2025 via OWID)
  C4b c4b_ohc_0_2000m.png      <- CI_Reports fig4  (NOAA NCEI, refreshed 2026-10-05)
  C8  c8_planetary_bounds.png  <- CI_Reports fig15 (constants in planetary_boundaries_energy.py)
  C9a c9a_population.png       <- CI_Reports fig7  (OWID / UN WPP 2024, refreshed 2026-10-05)
  C9b c9b_fertility.png        <- CI_Reports fig9 / blog001 fig5 (OWID / UN WPP 2024, refreshed)
  A4  a4_dc_electricity.png    <- CI_Reports fig13 (LBNL 2024/2025 stated values)
  A4  a4_dc_water_inset.png    <- CI_Reports fig14 panel (a) (LBNL 2024)

Refreshed data live in presentations/data/:
  co2_mm_mlo.txt  https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt
  ohc_2000m.dat   https://www.ncei.noaa.gov/data/oceans/woa/DATA_ANALYSIS/3M_HEAT_CONTENT/DATA/basin/yearly/h22-w0-2000m.dat
  owid_population_long_run_projections.csv  https://ourworldindata.org/grapher/population-long-run-with-projections.csv
  owid_fertility_with_projections.csv       https://ourworldindata.org/grapher/fertility-rate-with-projections.csv

Usage:
    conda run -n ocean14 python presentations/py/restyle_existing.py
"""
import csv
import json
import sys

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

from slide_style import (ROOT, DATA, MAIN, INSET, apply_style, save,
                         BLUE, LBLUE, RED, ORANGE, TEAL, PURPLE, GREEN, GRAY, MUTED)

# Page-cited constants live with the original report scripts; import, don't copy.
sys.path.insert(0, str(ROOT / "CI_Reports"))
import make_ai_figures as aif                     # noqa: E402
import make_population_figures as popf            # noqa: E402
from planetary_boundaries_energy import BOUNDARIES  # noqa: E402

apply_style()  # after the imports above, which set their own rcParams


def load_co2():
    """Created by JXP and Claude. NOAA Mauna Loa monthly CO2.
    Outputs: decimal_date, monthly_mean_ppm, deseasonalized_ppm."""
    rows = np.genfromtxt(DATA / "co2_mm_mlo.txt", comments="#")
    return rows[:, 2], rows[:, 3], rows[:, 4]


def load_ohc():
    """Created by JXP and Claude. NOAA NCEI world-ocean heat content 0-2000 m.
    Outputs: year, OHC anomaly (10^22 J), 1-sigma error."""
    rows = np.genfromtxt(DATA / "ohc_2000m.dat", skip_header=1)
    return rows[:, 0], rows[:, 1], rows[:, 2]


def load_world_population():
    """Created by JXP and Claude. OWID world population, estimates + UN medium
    projection. Outputs: est_year, est_pop, proj_year, proj_pop (billions)."""
    est, proj = [], []
    with open(DATA / "owid_population_long_run_projections.csv") as f:
        for row in csv.DictReader(f):
            if row["Entity"] != "World":
                continue
            year = int(row["Year"])
            if row["Population"]:
                est.append((year, float(row["Population"]) / 1e9))
            if row["Population (projections) (Projected)"]:
                proj.append((year, float(row["Population (projections) (Projected)"]) / 1e9))
    est.sort(); proj.sort()
    return (np.array([r[0] for r in est]), np.array([r[1] for r in est]),
            np.array([r[0] for r in proj]), np.array([r[1] for r in proj]))


def load_fertility(entities):
    """Created by JXP and Claude. OWID total fertility rate (UN WPP 2024
    estimates + medium projection). Inputs: entities (iterable of names).
    Outputs: dict entity -> (year, tfr, n_estimates)."""
    rows = {e: [] for e in entities}
    with open(DATA / "owid_fertility_with_projections.csv") as f:
        for row in csv.DictReader(f):
            if row["Entity"] not in rows:
                continue
            est = row["Fertility rate (estimates)"]
            val = est or row["Fertility rate (projections) (Projected)"]
            if val:
                rows[row["Entity"]].append((int(row["Year"]), float(val), bool(est)))
    out = {}
    for e, r in rows.items():
        r.sort()
        out[e] = (np.array([x[0] for x in r]), np.array([x[1] for x in r]),
                  sum(x[2] for x in r))
    return out


def c1_keeling():
    """Created by JXP and Claude. C1: the Keeling Curve, monthly + trend."""
    date, monthly, deseason = load_co2()
    fig, ax = plt.subplots(figsize=MAIN)
    ax.plot(date, monthly, lw=0.9, color=LBLUE)
    ax.plot(date, deseason, lw=2.2, color=RED)
    ax.axhline(280, ls="--", color=GRAY, lw=1.2)
    ax.text(1960, 287, "pre-industrial ≈ 280 ppm", color=GRAY, fontsize=12)
    ax.annotate(f"{deseason[0]:.0f} ppm\n{int(date[0])}", (date[0], deseason[0]),
                xytext=(1962, 335), fontsize=12, color=RED,
                arrowprops=dict(arrowstyle="-", color=RED, lw=0.8))
    last = f"{deseason[-1]:.0f} ppm\n{int(date[-1])}"
    ax.annotate(last, (date[-1], deseason[-1]), xytext=(2003, 428), fontsize=12,
                color=RED, ha="right", va="center",
                arrowprops=dict(arrowstyle="-", color=RED, lw=0.8))
    ax.set_xlim(1955, 2029)
    ax.set_ylim(270, 440)
    ax.set_ylabel("CO$_2$ (ppm)")
    save(fig, "c1_keeling.png",
         f"Data: NOAA GML / Scripps, Mauna Loa monthly mean (blue) and seasonally adjusted (red), through {int(date[-1])}-{round((date[-1] % 1) * 12 + 0.5):02d}",
         "C1")


def c2_us_cumulative():
    """Created by JXP and Claude. C2: top-10 cumulative CO2 share since 1750,
    U.S. highlighted."""
    with open(ROOT / "climate_intelligence" / "data" / "CO2" / "co2_by_country.json") as f:
        d = json.load(f)
    countries = [r for r in d["data"] if r["category"] != "World"]
    top = sorted(countries, key=lambda r: r["cumulative_share_of_global_pct"], reverse=True)[:10][::-1]
    names = [r["category"] for r in top]
    vals = [r["cumulative_share_of_global_pct"] for r in top]
    colors = [RED if n == "United States" else "#9aa7b4" for n in names]
    fig, ax = plt.subplots(figsize=MAIN)
    ax.barh(names, vals, color=colors, height=0.7)
    for y, v in enumerate(vals):
        ax.text(v + 0.3, y, f"{v:.1f}%", va="center", fontsize=12,
                fontweight="bold" if names[y] == "United States" else "normal")
    ax.set_xlabel("Share of all fossil CO$_2$ emitted since 1750 (%)")
    ax.set_xlim(0, max(vals) * 1.15)
    ax.grid(axis="y", visible=False)
    save(fig, "c2_us_cumulative.png",
         "Data: Global Carbon Project, Global Carbon Budget 2025, via Our World in Data (territorial emissions, 1750–2024)",
         "C2")


def c4b_ohc():
    """Created by JXP and Claude. C4b: ocean heat content 0-2000 m with trend
    expressed in W/m^2 over Earth's surface."""
    year, ohc, se = load_ohc()
    fig, ax = plt.subplots(figsize=MAIN)
    ax.errorbar(year, ohc, yerr=se, fmt="o-", color=ORANGE, ecolor="#e0a080",
                capsize=3, lw=2, ms=5)
    p = np.polyfit(year, ohc, 1)
    ax.plot(year, np.polyval(p, year), "--", color="black", lw=1.2)
    # 10^22 J/yr -> W, spread over Earth's surface (5.1e14 m^2).
    wm2 = (p[0] * 1e22) / (365.25 * 86400) / 5.1e14
    ax.text(0.03, 0.92, f"+{p[0]:.1f}×10$^{{22}}$ J per year\n≈ {wm2:.2f} W/m² over the whole Earth",
            transform=ax.transAxes, va="top", fontsize=13)
    ax.set_xticks(range(2005, 2026, 5))
    ax.set_ylabel("Ocean heat content\n0–2000 m (10$^{22}$ J)")
    save(fig, "c4b_ohc_0_2000m.png",
         f"Data: NOAA NCEI ocean heat content anomaly, 0–2000 m, yearly, {int(year[0])}–{int(year[-1])} (Argo era)",
         "C4b")


def c8_planetary_boundaries():
    """Created by JXP and Claude. C8: transgression ratio of the nine
    planetary boundaries (biosphere capped at 10 for display)."""
    items = sorted(BOUNDARIES, key=lambda b: b[1])
    fig, ax = plt.subplots(figsize=MAIN)
    y = np.arange(len(items))
    ax.barh(y, [b[1] for b in items], color=[RED if b[2] else GREEN for b in items],
            alpha=0.88, height=0.7)
    ax.axvline(1.0, color="black", lw=1.6, ls="--")
    ax.text(1.12, -0.9, "safe limit", fontsize=12, va="bottom")
    ax.set_yticks(y)
    ax.set_yticklabels([b[0] for b in items])
    ax.set_xlim(0, 11.2)
    ax.set_ylim(-1, len(items) - 0.4)
    ax.text(10.05, y[-1], ">10×", va="center", fontsize=12)
    ax.set_xlabel("Pressure ÷ boundary  (>1 = beyond the safe zone)")
    ax.legend(handles=[Patch(facecolor=RED, label="Transgressed (7)"),
                       Patch(facecolor=GREEN, label="Within safe zone (2)")],
              loc="lower right", frameon=False)
    ax.grid(axis="y", visible=False)
    save(fig, "c8_planetary_bounds.png",
         "Data: Richardson et al. 2023 (Sci. Adv.); Planetary Health Check 2025 (ocean acidification crossed)",
         "C8")


def c9a_population():
    """Created by JXP and Claude. C9a: world population 1900-2100 with the
    UN peak and end-of-century projection spread."""
    ey, ep, py, pp = load_world_population()
    keep = ey >= 1900
    ey, ep = ey[keep], ep[keep]
    fig, ax = plt.subplots(figsize=MAIN)
    ax.plot(ey, ep, color=BLUE, lw=2.6)
    ax.plot(py, pp, color=BLUE, lw=2.6, ls="--")
    ipk = np.argmax(pp)
    ax.plot(py[ipk], pp[ipk], "o", color=RED, ms=8, zorder=5)
    ax.text(1990, 11.6, f"peak ≈ {pp[ipk]:.1f} billion in {py[ipk]}",
            fontsize=13, color=RED)
    ax.text(1990, 3.2, "UN projection →", fontsize=12, color=BLUE)
    ax.axvline(ey[-1], color=GRAY, lw=0.8, ls=":")
    for x, (mid, lo, hi), name, color in ((2104, popf.UN_2100, "UN", BLUE),
                                          (2111, popf.IHME_2100, "IHME", ORANGE)):
        ax.errorbar(x, mid, yerr=[[mid - lo], [hi - mid]], fmt="o", ms=5, color=color,
                    capsize=3, lw=1.6, clip_on=False)
        ax.text(x, lo - 0.75, name, fontsize=11, ha="center", color=color)
    ax.set_xlim(1900, 2114)
    ax.set_xticks([1900, 1950, 2000, 2050, 2100])
    ax.set_ylim(0, 12.6)
    ax.set_ylabel("World population (billions)")
    save(fig, "c9a_population.png",
         "Data: OWID (HYDE / Gapminder / UN WPP 2024); 2100 bars = 95% ranges (UN WPP 2024; IHME, Vollset et al. 2020)",
         "C9a")


def c9b_fertility():
    """Created by JXP and Claude. C9b: total fertility rate by region vs the
    2.1 replacement level, 1950-2100."""
    regions = [("Africa (UN)", RED), ("Asia (UN)", PURPLE),
               ("Latin America and the Caribbean (UN)", TEAL),
               ("Northern America (UN)", ORANGE), ("Europe (UN)", BLUE)]
    series = load_fertility([r[0] for r in regions] + ["World"])
    fig, ax = plt.subplots(figsize=MAIN)
    labels = []
    for name, color in regions:
        yr, tfr, _ = series[name]
        ax.plot(yr, tfr, color=color, lw=1.8, alpha=0.9)
        short = name.replace(" (UN)", "").replace("Latin America and the Caribbean", "Latin Am.").replace("Northern America", "N. America")
        labels.append([tfr[-1], short, color, False])
    yr, tfr, n_est = series["World"]
    ax.plot(yr, tfr, color="black", lw=3.2)
    labels.append([tfr[-1], "World", "black", True])
    labels.sort(key=lambda r: r[0])
    ypos = [r[0] for r in labels]
    for i in range(1, len(ypos)):
        ypos[i] = max(ypos[i], ypos[i - 1] + 0.45)
    for (val, lab, color, bold), y in zip(labels, ypos):
        ax.annotate(lab, (2102, y), fontsize=12, color=color, va="center",
                    annotation_clip=False, fontweight="bold" if bold else "normal")
    ax.axhline(2.1, ls="--", color=GRAY, lw=1.2)
    ax.annotate("replacement ≈ 2.1", (2000, 2.1), xytext=(1985, 0.55),
                color=GRAY, fontsize=12,
                arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.8))
    last_est = yr[n_est - 1]
    ax.axvline(last_est, color=GRAY, lw=0.8, ls=":")
    ax.text(last_est + 2, 6.5, "projection →", fontsize=12, color=GRAY)
    ax.set_xlim(1950, 2100)
    ax.set_ylim(0, 7.2)
    ax.set_ylabel("Births per woman")
    save(fig, "c9b_fertility.png",
         f"Data: UN World Population Prospects 2024 via OWID (estimates to {last_est}; medium projection after)",
         "C9b", right=0.85)


def a4_dc_electricity():
    """Created by JXP and Claude. A4: U.S. data-center electricity, stated
    LBNL anchors, Reference Case and the 2030 range."""
    fig, ax = plt.subplots(figsize=MAIN)
    yr = [a[0] for a in aif.TOTAL_ANCHORS]
    twh = [a[1] for a in aif.TOTAL_ANCHORS]
    ax.plot(yr, twh, "-o", color=BLUE, lw=2.4, ms=7, label="All data centers")
    ax.plot([2024, 2028, 2030], [192, aif.REF_2028, aif.REF_2030], "--", color=BLUE, lw=2)
    lo, hi = aif.RANGE_2030
    ax.errorbar(2030.3, (lo + hi) / 2, yerr=(hi - lo) / 2, fmt="none", ecolor=BLUE,
                elinewidth=7, capsize=5, alpha=0.75)
    ax.annotate("2024: 192 TWh\n= 4.7% of U.S. electricity", (2024, 192),
                xytext=(2015.0, 330), fontsize=12, color=BLUE,
                arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.8))
    ax.annotate("2030: 9.5–15%", (2030.3, hi), xytext=(2025.6, 800), fontsize=13,
                color=BLUE, fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.8))
    ax.plot([a[0] for a in aif.AI_ANCHORS], [a[1] for a in aif.AI_ANCHORS], "-s",
            color=RED, lw=2.2, ms=7, label="AI servers")
    ax.annotate("AI servers: <2 → >40 TWh\n(2017 → 2023)", (2023, 40),
                xytext=(2015.0, 110), fontsize=12, color=RED,
                arrowprops=dict(arrowstyle="-", color=RED, lw=0.8))
    ax.set_xlim(2013.5, 2031.2)
    ax.set_ylim(0, 900)
    ax.set_ylabel("Electricity (TWh per year)")
    ax.legend(loc="upper left", frameon=False)
    save(fig, "a4_dc_electricity.png",
         "Data: LBNL 2024 U.S. Data Center Energy Usage Report; LBNL 2025 Update (Reference Case and 2030 range)",
         "A4")


def a4_dc_water_inset():
    """Created by JXP and Claude. A4 inset: direct vs indirect data-center
    water use (LBNL 2024)."""
    bars = [("On-site\n2014", aif.DIRECT_2014_BL, "#a8c4e0"),
            ("On-site\n2023", aif.DIRECT_2023_BL, "#5f8fc0"),
            ("Power plants\n2023", aif.INDIRECT_2023_BL, BLUE)]
    fig, ax = plt.subplots(figsize=INSET)
    ypos = np.arange(len(bars))[::-1]
    ax.barh(ypos, [b[1] for b in bars], color=[b[2] for b in bars], height=0.65)
    ax.set_yticks(ypos)
    ax.set_yticklabels([b[0] for b in bars], fontsize=11)
    for y, (_, v, _) in zip(ypos, bars):
        ax.text(v + 15, y, f"{v:g}", va="center", fontsize=11)
    ax.set_xlim(0, 1050)
    ax.set_xlabel("Water (billion liters/yr)", fontsize=11)
    ax.tick_params(axis="x", labelsize=10)
    ax.grid(axis="y", visible=False)
    save(fig, "a4_dc_water_inset.png", "Data: LBNL 2024", "A4")


def main():
    """Created by JXP and Claude. Build all B2 slide figures."""
    c1_keeling()
    c2_us_cumulative()
    c4b_ohc()
    c8_planetary_boundaries()
    c9a_population()
    c9b_fertility()
    a4_dc_electricity()
    a4_dc_water_inset()


if __name__ == "__main__":
    main()
