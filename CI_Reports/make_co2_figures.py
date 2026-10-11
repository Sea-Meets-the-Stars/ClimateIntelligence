"""Created by JXP and Claude.

Generate figures 23-31 for the CO2 emissions report (CI_Reports/co2_report.md).
Every figure is built from the seven machine-readable CO2 datasets in
climate_intelligence/data/CO2/*.json (each with its own provenance/caveats
fields) plus the long-run historical time series cached in
climate_intelligence/data/raw/owid-co2-data.csv (Global Carbon Project fossil
CO2 data, redistributed by Our World in Data). No numbers are invented here:
every plotted value is read directly from one of those files.

Data sources (see the JSON files themselves for full provenance):
  - co2_by_country.json    : Global Carbon Project - Global Carbon Budget 2025
  - co2_by_sector.json     : Climate Watch (CO2-only, 2023) + IPCC AR6 WGIII
                             (all-GHG CO2e, 2019, shown separately/labelled)
  - co2_by_fuel_type.json  : Global Carbon Project via OWID, 2019-2023
  - co2_by_transport_type.json : IEA / Climate Watch / IATA / ICCT (mixed
                             vintages, some values derived -- flagged in the
                             file's own caveats)
  - co2_by_industry.json   : IEA sector/tracking pages, mixed years 2021-2023
  - co2_by_energy_type.json: IEA / Ember (power sector), 2023-2024
  - co2_fate_atmosphere_ocean_land.json : Global Carbon Project - Global
                             Carbon Budget 2024 (Friedlingstein et al. 2025)
                             decade-average sink partition, plus IPCC AR6 and
                             Bennett et al. 2024 historical comparison points
  - owid-co2-data.csv      : Global Carbon Project fossil+industry CO2,
                             World row, 1750-2024 (used here from 1850)

Run under the project conda environment:
    conda run -n ocean14 python CI_Reports/make_co2_figures.py

Design choices follow the project coding guidelines (Logs/logging.md):
functions (no classes), imports at top, inline comments, matplotlib for
plotting, docstrings with inputs/outputs, and "Created by JXP and Claude" on
the file and each method. Figure numbering continues from the existing
CI_Reports house style (highest prior figure was fig22), so this file writes
fig23-fig31.
"""

# Imports at the top of the file (project coding guideline).
import json
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # headless backend; we save PNGs, never display
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA_CO2 = ROOT / "climate_intelligence" / "data" / "CO2"
DATA_RAW = ROOT / "climate_intelligence" / "data" / "raw"

# Same visual style as make_figures.py / make_population_figures.py, for a
# consistent report look across the whole blog.
plt.rcParams.update({
    "figure.dpi": 130,
    "savefig.dpi": 130,
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# A fixed categorical palette reused across figures for visual consistency,
# in the same hex-color idiom as the rest of CI_Reports/make_*.py.
BLUE = "#1f5fa6"
LBLUE = "#4a90d9"
RED = "#c0392b"
ORANGE = "#b9430f"
PURPLE = "#8e44ad"
TEAL = "#16a085"
GREEN = "#27ae60"
GRAY = "#7f8c8d"
GOLD = "#e1a100"
CAT_PALETTE = [BLUE, RED, TEAL, PURPLE, ORANGE, GOLD, GREEN, GRAY, LBLUE, "#2c3e50"]


def load_json(name):
    """Created by JXP and Claude.

    Load one of the CO2 dataset JSON files.

    Inputs
    ------
    name : str
        File name under climate_intelligence/data/CO2/ (e.g.
        'co2_by_country.json').

    Outputs
    -------
    dict
        Parsed JSON with keys 'title', 'description', 'unit', 'data',
        'provenance', 'caveats'.
    """
    with open(DATA_CO2 / name) as f:
        return json.load(f)


def load_world_co2_series(min_year=1850):
    """Created by JXP and Claude.

    Load the long-run World fossil+industry CO2 emissions series from the
    cached OWID/Global Carbon Project raw CSV.

    Inputs
    ------
    min_year : int
        Earliest year to keep (data technically runs back to 1750; we use
        1850 by default per the report's "since 1850" long-run framing).

    Outputs
    -------
    (np.ndarray, np.ndarray)
        year, co2 (MtCO2), sorted by year, NaNs dropped.
    """
    df = pd.read_csv(DATA_RAW / "owid-co2-data.csv", usecols=["country", "year", "co2"])
    w = df[(df["country"] == "World") & df["co2"].notna()].sort_values("year")
    w = w[w["year"] >= min_year]
    return w["year"].to_numpy(), w["co2"].to_numpy()


def cagr(start_value, end_value, start_year, end_year):
    """Created by JXP and Claude.

    Compound annual growth rate between two points on a time series.

    Inputs
    ------
    start_value, end_value : float
        Series values at the start and end years.
    start_year, end_year : int
        Calendar years of those values.

    Outputs
    -------
    float
        CAGR as a fraction per year (multiply by 100 for %).
    """
    n = end_year - start_year
    return (end_value / start_value) ** (1.0 / n) - 1.0


def fig23_global_growth():
    """Created by JXP and Claude.

    Figure 23: the long-run global CO2 emissions time series (1850-2024) on
    both linear and log y-axes, with four eras shaded and their compound
    annual growth rates (CAGR) computed and annotated, plus a small bar panel
    comparing the four era CAGRs directly. This is the figure that answers
    "is growth exponential, and is it accelerating or decelerating?".

    Inputs
    ------
    (none) reads climate_intelligence/data/raw/owid-co2-data.csv

    Outputs
    -------
    None. Saves fig23_global_co2_growth.png.
    """
    year, co2 = load_world_co2_series(min_year=1850)

    # Eras chosen per the task brief; all four boundary years exist exactly
    # in the OWID series, so CAGR is computed directly from data (no
    # interpolation).
    eras = [
        (1950, 1973, "1950-1973\npostwar boom"),
        (1973, 2000, "1973-2000\noil shocks / efficiency"),
        (2000, 2010, "2000-2010\nChina buildout"),
        (2010, 2024, "2010-2024\nrecent decade+"),
    ]
    era_colors = [LBLUE, TEAL, ORANGE, RED]

    def value_at(y):
        return float(co2[year == y][0])

    era_cagrs = []
    for y0, y1, _ in eras:
        era_cagrs.append(100 * cagr(value_at(y0), value_at(y1), y0, y1))

    fig = plt.figure(figsize=(10, 9.5))
    gs = GridSpec(3, 1, height_ratios=[1.1, 1.1, 0.9], hspace=0.55)
    ax_lin = fig.add_subplot(gs[0])
    ax_log = fig.add_subplot(gs[1], sharex=ax_lin)
    ax_bar = fig.add_subplot(gs[2])

    for ax, use_log in ((ax_lin, False), (ax_log, True)):
        ax.plot(year, co2, color="black", lw=1.8)
        for (y0, y1, label), c in zip(eras, era_colors):
            ax.axvspan(y0, y1, color=c, alpha=0.12)
        if use_log:
            ax.set_yscale("log")
            ax.set_ylabel("CO$_2$ (MtCO$_2$/yr, log scale)")
        else:
            ax.set_ylabel("CO$_2$ (MtCO$_2$/yr)")
    ax_lin.set_title("World fossil + industry CO$_2$ emissions, 1850-2024: linear vs. log scale")
    ax_log.set_xlabel("Year")
    # Annotate CAGR once, on the linear panel. The four eras crowd together
    # after 1950, so labels are staggered across two heights (alternating by
    # index) and kept to a single short line to avoid overlapping text.
    ax_lin.set_ylim(top=ax_lin.get_ylim()[1] * 1.12)  # headroom for labels
    ytop = ax_lin.get_ylim()[1]
    # Since the curve rises monotonically, place each era's label just above
    # the highest point the curve reaches WITHIN that era (not a fixed
    # height), so later (higher-value) eras get pushed higher and never
    # collide with the curve or with each other.
    for y0, y1, label in eras:
        c = era_colors[eras.index((y0, y1, label))]
        g = era_cagrs[eras.index((y0, y1, label))]
        local_max = co2[(year >= y0) & (year <= y1)].max()
        y_ann = min(local_max + 0.10 * ytop, 0.97 * ytop)
        xm = y0 + 0.5 * (y1 - y0)
        ax_lin.annotate(f"{y0}-{y1}: {g:+.1f}%/yr", (xm, y_ann),
                         ha="center", fontsize=7.5, color=c, fontweight="bold")
    ax_lin.text(0.01, 0.99,
                "A straight line on the LOG panel means constant %-growth\n"
                "(true exponential growth); bending flatter means decelerating.",
                transform=ax_lin.transAxes, ha="left", va="top", fontsize=8, color="#555")

    # Era-CAGR bar panel: makes the deceleration/re-acceleration pattern
    # impossible to miss even without reading the log-panel curvature.
    xpos = np.arange(len(eras))
    ax_bar.bar(xpos, era_cagrs, color=era_colors, width=0.6)
    for x, g in zip(xpos, era_cagrs):
        ax_bar.text(x, g + (0.08 if g >= 0 else -0.12), f"{g:.1f}%",
                    ha="center", va="bottom" if g >= 0 else "top", fontsize=9)
    ax_bar.set_xticks(xpos)
    ax_bar.set_xticklabels([f"{y0}-{y1}" for y0, y1, _ in eras], fontsize=9)
    ax_bar.axhline(0, color="gray", lw=0.8)
    ax_bar.set_ylabel("CAGR (%/yr)")
    ax_bar.set_title("Era-by-era compound annual growth rate: growth has not been steadily exponential")

    fig.text(0.99, 0.005,
             "Data: Global Carbon Project fossil+industry CO2 (World), via Our World in Data "
             "(climate_intelligence/data/raw/owid-co2-data.csv). CAGR computed at exact endpoint years.",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(HERE / "fig23_global_co2_growth.png")
    plt.close(fig)
    return dict(zip([e[2].split("\n")[0] for e in eras], era_cagrs))


def fig24_country_breakdown():
    """Created by JXP and Claude.

    Figure 24: emissions by country, three panels telling the "who emits
    now vs. who is historically responsible" story --
      (a) top 15 absolute emitters, 2024 (MtCO2);
      (b) per-capita emissions (tCO2/person) for those same 15 countries;
      (c) top 10 countries by cumulative share of global CO2 since 1750.

    Inputs
    ------
    (none) reads climate_intelligence/data/CO2/co2_by_country.json

    Outputs
    -------
    None. Saves fig24_country_breakdown.png.
    """
    d = load_json("co2_by_country.json")
    countries = [r for r in d["data"] if r["category"] != "World"]

    top15_abs = sorted(countries, key=lambda r: r["value"], reverse=True)[:15]
    top10_cum = sorted(countries, key=lambda r: r["cumulative_share_of_global_pct"], reverse=True)[:10]

    fig, axes = plt.subplots(1, 3, figsize=(15, 6.5))

    # (a) absolute top 15, largest at top.
    names_a = [r["category"] for r in top15_abs][::-1]
    vals_a = [r["value"] for r in top15_abs][::-1]
    axes[0].barh(names_a, vals_a, color=BLUE)
    axes[0].set_xlabel("CO$_2$, 2024 (MtCO$_2$)")
    axes[0].set_title("Top 15 emitters (absolute, 2024)")
    for y, v in enumerate(vals_a):
        axes[0].text(v, y, f" {v:,.0f}", va="center", fontsize=7.5)

    # (b) per-capita for the same 15 countries, sorted by per-capita value.
    top15_by_pc = sorted(top15_abs, key=lambda r: r["per_capita_tCO2"])
    names_b = [r["category"] for r in top15_by_pc]
    vals_b = [r["per_capita_tCO2"] for r in top15_by_pc]
    axes[1].barh(names_b, vals_b, color=RED)
    axes[1].set_xlabel("tCO$_2$ per person, 2024")
    axes[1].set_title("Per-capita emissions\n(same 15 countries)")
    for y, v in enumerate(vals_b):
        axes[1].text(v, y, f" {v:.1f}", va="center", fontsize=7.5)

    # (c) cumulative historical share since 1750, top 10.
    names_c = [r["category"] for r in top10_cum][::-1]
    vals_c = [r["cumulative_share_of_global_pct"] for r in top10_cum][::-1]
    axes[2].barh(names_c, vals_c, color=TEAL)
    axes[2].set_xlabel("% of cumulative global CO$_2$ since 1750")
    axes[2].set_title("Top 10 by cumulative\nhistorical share")
    for y, v in enumerate(vals_c):
        axes[2].text(v, y, f" {v:.1f}%", va="center", fontsize=7.5)

    fig.suptitle("CO$_2$ emissions by country: current emitters vs. historical responsibility", y=1.02, fontsize=13)
    fig.text(0.01, -0.02,
             "Data: Global Carbon Project - Global Carbon Budget 2025, via Our World in Data "
             "(climate_intelligence/data/co2_by_country.json). Territorial (production-based) "
             "accounting; not adjusted for trade.",
             ha="left", va="bottom", fontsize=8, color="#555")
    fig.tight_layout()
    fig.savefig(HERE / "fig24_country_breakdown.png", bbox_inches="tight")
    plt.close(fig)


def fig25_sector_breakdown():
    """Created by JXP and Claude.

    Figure 25: emissions by sector, two panels shown side by side but
    explicitly NOT pooled into one total --
      (a) Climate Watch CO2-only sector breakdown, 2023;
      (b) IPCC AR6 WGIII all-GHG (CO2-equivalent) sectoral shares, 2019.
    The two use different gases, scopes, and years; the figure labels this
    clearly rather than implying they are the same measurement.

    Inputs
    ------
    (none) reads climate_intelligence/data/CO2/co2_by_sector.json

    Outputs
    -------
    None. Saves fig25_sector_breakdown.png.
    """
    d = load_json("co2_by_sector.json")
    cw = [r for r in d["data"] if r["source"].startswith("Climate Watch") and not r["category"].startswith("Total")]
    cw = sorted(cw, key=lambda r: r["value"], reverse=True)
    ipcc = [r for r in d["data"] if "IPCC AR6 WGIII" in r["category"]]
    ipcc = sorted(ipcc, key=lambda r: r["value"], reverse=True)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    names_a = [r["category"] for r in cw][::-1]
    vals_a = [r["value"] for r in cw][::-1]
    axes[0].barh(names_a, vals_a, color=CAT_PALETTE[0])
    axes[0].set_xlabel("CO$_2$, 2023 (MtCO$_2$)")
    axes[0].set_title("(a) Climate Watch: CO$_2$-only, 2023")
    for y, v in enumerate(vals_a):
        axes[0].text(v, y, f" {v:,.0f}", va="center", fontsize=8)

    names_b = [r["category"].split(" (IPCC")[0] for r in ipcc][::-1]
    vals_b = [r["value"] for r in ipcc][::-1]
    axes[1].barh(names_b, vals_b, color=CAT_PALETTE[1])
    axes[1].set_xlabel("All GHG, CO$_2$eq, 2019 (MtCO$_2$eq)")
    axes[1].set_title("(b) IPCC AR6 WGIII: all-GHG CO$_2$eq, 2019")
    for y, v in enumerate(vals_b):
        axes[1].text(v, y, f" {v:,.0f}", va="center", fontsize=8)

    fig.suptitle("CO$_2$ emissions by sector -- two different, non-additive framings", y=1.03, fontsize=13)
    fig.text(0.01, -0.03,
             "(a) Climate Watch CO2-only sectoral data, 2023 (co2_by_sector.json). (b) IPCC AR6 WGIII Fig. SPM.2, "
             "ALL greenhouse gases as CO2-equivalent, 2019 -- do not sum panel (a) and panel (b): different gases, "
             "scope, and year. See the file's 'caveats' field.",
             ha="left", va="bottom", fontsize=8, color="#555")
    fig.tight_layout()
    fig.savefig(HERE / "fig25_sector_breakdown.png", bbox_inches="tight")
    plt.close(fig)


def fig26_fuel_type_trend():
    """Created by JXP and Claude.

    Figure 26: world CO2 emissions by fuel/source type, 2019-2023, as a
    stacked bar chart (coal, oil, gas, cement, flaring, other industry) with
    the total_fossil_co2 series overlaid as a line.

    Inputs
    ------
    (none) reads climate_intelligence/data/CO2/co2_by_fuel_type.json

    Outputs
    -------
    None. Saves fig26_fuel_type_trend.png.
    """
    d = load_json("co2_by_fuel_type.json")
    cats = ["coal", "oil", "gas", "cement", "flaring", "other_industry"]
    colors = {"coal": "#3b3b3b", "oil": ORANGE, "gas": LBLUE, "cement": GRAY,
              "flaring": GOLD, "other_industry": PURPLE}
    years = sorted({r["year"] for r in d["data"] if r["category"] in cats})
    by_cat = {c: [next(r["value"] for r in d["data"] if r["category"] == c and r["year"] == y)
                  for y in years] for c in cats}
    totals = [next(r["value"] for r in d["data"] if r["category"] == "total_fossil_co2" and r["year"] == y)
              for y in years]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    bottom = np.zeros(len(years))
    for c in cats:
        vals = np.array(by_cat[c])
        ax.bar(years, vals, bottom=bottom, color=colors[c], label=c.replace("_", " "), width=0.6)
        bottom += vals
    ax.plot(years, totals, "o--", color="black", lw=1.2, ms=4, label="total (check sum)")
    ax.set_xticks(years)
    ax.set_ylabel("CO$_2$ (MtCO$_2$/yr)")
    ax.set_xlabel("Year")
    ax.set_title("World CO$_2$ emissions by fuel/source type, 2019-2023")
    ax.legend(loc="lower right", fontsize=8, ncol=2)
    ax.text(0.01, 0.97,
            "Coal remains the single largest source, ~41% of the projected 2025 total per\n"
            "Global Carbon Budget 2025 (not plotted here -- only verified 2019-2023 absolutes shown).",
            transform=ax.transAxes, ha="left", va="top", fontsize=8, color="#555")
    fig.text(0.99, 0.01,
             "Data: Global Carbon Project - Global Carbon Budget, via Our World in Data "
             "(climate_intelligence/data/co2_by_fuel_type.json).",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(HERE / "fig26_fuel_type_trend.png")
    plt.close(fig)


def fig27_transport_breakdown():
    """Created by JXP and Claude.

    Figure 27: emissions by transport mode, two panels --
      (a) IEA's 2018 percentage-share breakdown by mode (road passenger,
          road freight, aviation, shipping, rail, other);
      (b) the OWID/Climate Watch total-transport CO2 time series, 2015-2023,
          with the pandemic dip visible, plus separately sourced recent
          mode-specific points (road 2024, aviation 2019/2023/2024,
          shipping 2023) annotated as non-comparable cross-checks.

    Inputs
    ------
    (none) reads climate_intelligence/data/CO2/co2_by_transport_type.json

    Outputs
    -------
    None. Saves fig27_transport_breakdown.png.
    """
    d = load_json("co2_by_transport_type.json")
    shares = [r for r in d["data"] if r["unit"] == "% of transport-sector CO2"]
    shares = sorted(shares, key=lambda r: r["value"], reverse=True)
    totals = sorted([r for r in d["data"] if r["category"] == "total_transport"], key=lambda r: r["year"])

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    labels = [r["category"].replace("_", " ") for r in shares]
    vals = [r["value"] for r in shares]
    # Small slices (rail, other) crowd/overlap if labelled directly on the
    # wedge, so labels+percentages go in a legend; the two tiny slices
    # (<3%) skip the on-wedge percent text entirely to avoid overlap.
    autopct = lambda pct: f"{pct:.0f}%" if pct >= 3 else ""
    wedges, _, _ = axes[0].pie(vals, autopct=autopct, colors=CAT_PALETTE,
                                startangle=90, pctdistance=0.75,
                                textprops={"fontsize": 9})
    legend_labels = [f"{lab} ({v:.0f}%)" for lab, v in zip(labels, vals)]
    axes[0].legend(wedges, legend_labels, loc="upper center", bbox_to_anchor=(0.5, 0.02),
                    fontsize=8, frameon=False, ncol=3)
    axes[0].set_title("(a) Share of transport CO$_2$ by mode, 2018 (IEA)")

    ty = [r["year"] for r in totals]
    tv = [r["value"] for r in totals]
    axes[1].plot(ty, tv, "o-", color=BLUE, lw=2, label="Total transport CO$_2$\n(Climate Watch/CAIT)")
    # Separately-sourced recent mode points -- annotated, not spliced into the line.
    extras = [
        ("road (2024, IEA)", 2024, 6000.0, RED, "s"),
        ("aviation (2019, lit.)", 2019, 1000.0, TEAL, "^"),
        ("aviation (2023, IATA)", 2023, 882.0, TEAL, "v"),
        ("aviation (2024, IATA)", 2024, 942.0, TEAL, "D"),
        ("shipping (2023, ICCT, CO2e)", 2023, 911.0, PURPLE, "P"),
    ]
    for label, y, v, c, m in extras:
        axes[1].scatter([y], [v], color=c, marker=m, s=55, zorder=5, label=label)
    axes[1].set_xlabel("Year")
    axes[1].set_ylabel("CO$_2$ (MtCO$_2$/yr)")
    axes[1].set_title("(b) Total transport CO$_2$, 2015-2023,\nwith non-comparable mode cross-checks")
    axes[1].legend(loc="upper left", fontsize=7)

    fig.suptitle("CO$_2$ emissions by transport type", y=1.02, fontsize=13)
    fig.text(0.01, -0.04,
             "(a) IEA 2018 mode shares applied to a single year (via OWID). (b) Climate Watch/CAIT total transport "
             "CO2 (all modes); scatter points are separately sourced (IEA, IATA, ICCT) and use different scopes/"
             "gases/years -- ICCT shipping figure is CO2e (incl. CH4/N2O), not pure CO2. See caveats in "
             "co2_by_transport_type.json.",
             ha="left", va="bottom", fontsize=7.5, color="#555")
    fig.tight_layout()
    fig.savefig(HERE / "fig27_transport_breakdown.png", bbox_inches="tight")
    plt.close(fig)


def fig28_industry_breakdown():
    """Created by JXP and Claude.

    Figure 28: direct CO2 emissions by heavy-industry subsector (iron &
    steel, cement, chemicals, aluminium, pulp & paper, other/residual),
    each labelled with its data-vintage year, plus the IEA total-industry
    figure shown as a reference line.

    Inputs
    ------
    (none) reads climate_intelligence/data/CO2/co2_by_industry.json

    Outputs
    -------
    None. Saves fig28_industry_breakdown.png.
    """
    d = load_json("co2_by_industry.json")
    rows = [r for r in d["data"] if not r["category"].startswith("Total")]
    rows = sorted(rows, key=lambda r: r["value"], reverse=True)
    total = next(r for r in d["data"] if r["category"].startswith("Total"))

    fig, ax = plt.subplots(figsize=(10, 5.5))
    names = [f"{r['category']} ({r['year']})" for r in rows][::-1]
    vals = [r["value"] for r in rows][::-1]
    colors = [RED if "residual" in r["category"].lower() or "other" in r["category"].lower()
              else BLUE for r in rows][::-1]
    ax.barh(names, vals, color=colors)
    for y, v in enumerate(vals):
        ax.text(v, y, f" {v:,.0f}", va="center", fontsize=9)
    ax.set_xlim(0, total["value"] * 1.28)  # headroom so the total label/line fit
    ax.axvline(total["value"], color="black", ls="--", lw=1.2)
    ax.annotate(f"Total industry:\n{total['value']:,.0f} Mt ({total['year']})",
                (total["value"], len(names) - 0.6), fontsize=8, color="#333",
                ha="left", va="top")
    ax.set_xlabel(f"Direct CO$_2$ ({d['unit']}, mixed years -- see labels)")
    ax.set_title("World CO$_2$ emissions by industry subsector")
    ax.text(0.99, 0.02,
            "Iron & steel and cement alone are ~55% of direct industrial CO$_2$.\n"
            "'Other' is a residual computed by the author, mixing vintages (see caveats).",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=8, color="#555")
    fig.text(0.01, 0.005,
             "Data: IEA sector/tracking pages, mixed years 2021-2023 (climate_intelligence/data/co2_by_industry.json).",
             ha="left", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(HERE / "fig28_industry_breakdown.png", bbox_inches="tight")
    plt.close(fig)


def fig29_energy_type_breakdown():
    """Created by JXP and Claude.

    Figure 29: the power (electricity & heat) generation sector, two panels
      (a) power-sector CO2 composition (coal vs. gas+oil) and the IEA-vs-Ember
          methodology disagreement over the 2024 total, shown side by side
          rather than reconciled;
      (b) the 2024 global electricity generation mix by source (coal, gas,
          oil, renewables+nuclear), which sets up why coal contributes so
          disproportionately to power-sector CO2.

    Inputs
    ------
    (none) reads climate_intelligence/data/CO2/co2_by_energy_type.json

    Outputs
    -------
    None. Saves fig29_energy_type_breakdown.png.
    """
    d = load_json("co2_by_energy_type.json")

    def val(cat, year):
        return next(r["value"] for r in d["data"] if r["category"] == cat and r["year"] == year)

    coal_2023 = val("Coal-fired electricity generation", 2023)
    gasoil_2023 = val("Natural gas- and oil-fired electricity generation (combined)", 2023)
    total_2023 = val("Total power-sector CO2 (all fuels)", 2023)
    total_2024_ember = val("Total power-sector CO2 (all fuels)", 2024)
    # IEA's own, lower 2024 estimate (~13,800 Mt) is recorded in this dataset's
    # own 'notes' field for the Ember 2024 entry, not fabricated here.
    total_2024_iea = 13800.0

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))

    axes[0].bar(["2023\n(Ember)"], [coal_2023], color="#3b3b3b")
    axes[0].bar(["2023\n(Ember)"], [gasoil_2023], bottom=[coal_2023], color=LBLUE)
    axes[0].bar(["2024\n(Ember)"], [total_2024_ember], color=GRAY, alpha=0.5)
    axes[0].bar(["2024\n(IEA)"], [total_2024_iea], color=GRAY, alpha=0.8)
    # Label the 2023 stacked segments directly (avoids a legend box that
    # would otherwise cover the top-of-bar total labels).
    axes[0].text("2023\n(Ember)", coal_2023 / 2, "coal", ha="center", va="center",
                 color="white", fontsize=9)
    axes[0].text("2023\n(Ember)", coal_2023 + gasoil_2023 / 2, "gas + oil", ha="center",
                 va="center", color="white", fontsize=9)
    for x, v in zip(["2023\n(Ember)", "2024\n(Ember)", "2024\n(IEA)"],
                     [total_2023, total_2024_ember, total_2024_iea]):
        axes[0].text(x, v + 250, f"{v:,.0f}", ha="center", fontsize=9)
    axes[0].set_ylim(0, total_2024_ember * 1.15)
    axes[0].set_ylabel("Power-sector CO$_2$ (MtCO$_2$/yr)")
    axes[0].set_title("(a) Power-sector CO$_2$: composition (2023)\nand IEA-vs-Ember 2024 disagreement")

    gen_mix = {
        "Coal": val("Coal share of global electricity generation", 2024),
        "Natural gas": val("Natural gas share of global electricity generation", 2024),
        "Oil": val("Oil share of global electricity generation", 2024),
        "Renewables + nuclear\n(near-zero direct CO2)": val(
            "Renewables + nuclear electricity generation (near-zero direct CO2)", 2024),
    }
    axes[1].pie(gen_mix.values(), labels=gen_mix.keys(), autopct="%.0f%%",
                colors=["#3b3b3b", LBLUE, ORANGE, GREEN], startangle=90,
                textprops={"fontsize": 9})
    axes[1].set_title("(b) Global electricity generation mix, 2024\n(IEA)")

    fig.suptitle("CO$_2$ by energy type: the power sector", y=1.03, fontsize=13)
    fig.text(0.01, -0.04,
             "(a) Ember Global Electricity Review 2024/2025; IEA's 2024 total from Electricity 2025 (methodology "
             "differs -- both shown, not reconciled). Gas+oil 2023 bar is a derived residual (total minus coal). "
             "(b) IEA Global Energy Review 2025. Coal supplied only ~35% of 2024 generation but ~65% of power-"
             "sector CO2, reflecting its higher carbon intensity per kWh. Carbon intensity of generation fell from "
             "480 gCO2/kWh (2023, Ember) to 445 gCO2/kWh (2024, IEA).",
             ha="left", va="bottom", fontsize=7.5, color="#555")
    fig.tight_layout()
    fig.savefig(HERE / "fig29_energy_type_breakdown.png", bbox_inches="tight")
    plt.close(fig)


def fig30_fate_partition():
    """Created by JXP and Claude.

    Figure 30: where 2014-2023's annually emitted CO2 (fossil+industry+
    land-use-change combined) actually went -- a stacked bar (a) showing the
    atmosphere/ocean-sink/land-sink partition in MtCO2/yr with the small
    budget-imbalance residual annotated, and a matching pie (b) of the same
    three headline percentages (48% / 26% / 30%), which is this report's most
    direct answer to "where has the world's CO2 gone?".

    Inputs
    ------
    (none) reads
    climate_intelligence/data/CO2/co2_fate_atmosphere_ocean_land.json

    Outputs
    -------
    None. Saves fig30_co2_fate_partition.png.
    """
    d = load_json("co2_fate_atmosphere_ocean_land.json")
    decade = [r for r in d["data"] if r.get("period") == "2014-2023"]

    def val(cat):
        return next(r["value"] for r in decade if r["category"] == cat)

    def pct(cat):
        return next(r["pct_of_total_emissions"] for r in decade if r["category"] == cat)

    cats = ["atmosphere", "ocean_sink", "land_sink"]
    labels = ["Atmosphere", "Ocean sink", "Land sink"]
    colors = [RED, BLUE, GREEN]
    vals = [val(c) for c in cats]
    pcts = [pct(c) for c in cats]
    imbalance = val("budget_imbalance")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))

    # (a) stacked single bar, MtCO2/yr, with the imbalance called out.
    bottom = 0.0
    for lab, v, c in zip(labels, vals, colors):
        axes[0].bar(["2014-2023\naverage"], [v], bottom=[bottom], color=c, label=lab, width=0.5)
        axes[0].text(0, bottom + v / 2, f"{lab}\n{v:,.0f} MtCO$_2$/yr", ha="center",
                     va="center", color="white", fontsize=9)
        bottom += v
    axes[0].set_ylabel("CO$_2$ (MtCO$_2$/yr)")
    axes[0].set_title("(a) Decade-average partition\n(stacked, with imbalance noted)")
    axes[0].text(0, bottom * 1.03,
                 f"Sum of the three shares = {sum(pcts):.0f}% (not exactly 100%);\n"
                 f"implied budget imbalance $\\approx$ {imbalance:,.0f} MtCO$_2$/yr "
                 "(author-derived residual, see caveats).",
                 ha="center", va="bottom", fontsize=7.5, color="#555")
    axes[0].set_ylim(0, bottom * 1.25)

    # (b) pie of the three headline percentages -- the number readers will
    # actually remember and quote.
    axes[1].pie(pcts, labels=[f"{lab}\n{p:.0f}%" for lab, p in zip(labels, pcts)],
                colors=colors, startangle=90, textprops={"fontsize": 10})
    axes[1].set_title("(b) Share of total emitted CO$_2$,\n2014-2023 average")

    fig.suptitle("Where does emitted CO$_2$ go? Atmosphere vs. ocean vs. land, 2014-2023",
                  y=0.99, fontsize=13)
    # Footer wrapped into short lines (each well under the figure width) so
    # bbox_inches="tight" does not stretch the saved canvas to fit one very
    # long unwrapped line.
    fig.text(0.01, 0.01,
             "Data: Global Carbon Project - Global Carbon Budget 2024 (Friedlingstein et al. 2025, ESSD),\n"
             "decade average 2014-2023 (co2_fate_atmosphere_ocean_land.json). 'Total emissions' here = fossil +\n"
             "industry + land-use-change CO2 combined -- a broader scope than the fossil-only totals used in\n"
             "section 1/4 of this report. The ocean's ~26% CARBON uptake shown here is NOT the same statistic as\n"
             "the ocean's >90% HEAT uptake (a different physical quantity, IPCC SROCC) -- see the report text.",
             ha="left", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.14, 1, 0.92))
    fig.savefig(HERE / "fig30_co2_fate_partition.png")
    plt.close(fig)


def fig31_airborne_fraction_history():
    """Created by JXP and Claude.

    Figure 31: how stable has the "airborne fraction" (atmosphere's share of
    total emitted CO2) been over time? Three sourced comparison points --
    the six-decade (1959-2023) long-term average, the 2010-2019 decade
    (IPCC AR6), and the 2014-2023 decade (Global Carbon Budget 2024) -- shown
    as a small bar chart, annotated with the open question of whether the
    fraction is now creeping upward.

    Inputs
    ------
    (none) reads
    climate_intelligence/data/CO2/co2_fate_atmosphere_ocean_land.json

    Outputs
    -------
    None. Saves fig31_airborne_fraction_history.png.
    """
    d = load_json("co2_fate_atmosphere_ocean_land.json")
    atmo_rows = [r for r in d["data"] if r["category"] == "atmosphere"]

    def pct_value(r):
        # The 2014-2023 "atmosphere" record's 'value' field is the absolute
        # MtCO2/yr figure (unit "MtCO2/yr"); its percentage lives in
        # 'pct_of_total_emissions'. The other two records store the
        # percentage directly in 'value' (unit is a "%..." string). Handle
        # both so this figure always plots a percentage, never MtCO2/yr.
        return r["pct_of_total_emissions"] if "pct_of_total_emissions" in r else r["value"]

    # Order chronologically by period label for a left-to-right "over time" read.
    order = ["1959-2023 (long-term average)", "2010-2019", "2014-2023"]
    rows = sorted(atmo_rows, key=lambda r: order.index(r["period"]))
    period_labels = ["1959-2023\n(long-term avg.)", "2010-2019\n(IPCC AR6)", "2014-2023\n(GCB 2024)"]
    values = [pct_value(r) for r in rows]

    fig, ax = plt.subplots(figsize=(8.5, 6))
    bars = ax.bar(period_labels, values, color=[GRAY, ORANGE, RED], width=0.55)
    for b, v in zip(bars, values):
        ax.text(b.get_x() + b.get_width() / 2, v + 1.5, f"{v:.0f}%", ha="center", fontsize=11)
    # Headroom above the tallest bar's label so the dashed reference line and
    # its own label (placed on the RIGHT, away from the "44%" bar-top label
    # on the left, so the two texts never overlap) both fit cleanly.
    ax.set_ylim(0, max(values) * 1.35)
    ax.axhline(44.0, color=GRAY, ls="--", lw=1, alpha=0.6)
    # Widen the x-axis so there is empty space to the right of the last bar,
    # and put the reference-line label there -- the first bar's own value
    # (44%) equals this reference line exactly, so any label placed near the
    # bars would collide with that bar's "44%" top-of-bar text; parking it
    # off to the side avoids that entirely.
    ax.set_xlim(-0.6, len(period_labels) - 0.15)
    ax.text(len(period_labels) - 0.65, 44.0, "six-decade avg. (44%)",
            ha="left", va="center", fontsize=8, color="#555",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.75, pad=1.5))
    ax.set_ylabel("Airborne fraction (% of total CO$_2$ emissions\nremaining in the atmosphere)")
    ax.set_title("Is the airborne fraction stable? Three sourced comparison points")
    # Explanatory note placed in the otherwise-empty upper-left of the plot
    # area (above the short 1959-2023 bar), not overlapping any bar or label.
    ax.text(0.02, 0.97,
            "Long-standing finding: ~44% for six decades even as\n"
            "absolute emissions grew several-fold. Recent decades\n"
            "run a few points higher; whether this is a genuine\n"
            "upward trend (sinks struggling to keep pace) or\n"
            "decadal noise is actively debated -- not yet settled.",
            transform=ax.transAxes, ha="left", va="top", fontsize=7.5, color="#555")

    # Footer wrapped into short lines (each well under the figure width) so
    # bbox_inches="tight" does not stretch the saved canvas to fit one very
    # long unwrapped line, as happened in an earlier version of this figure.
    fig.text(0.01, 0.01,
             "Data: co2_fate_atmosphere_ocean_land.json. Sources: Bennett et al. 2024 (JGR Biogeosciences,\n"
             "long-term average); IPCC AR6 WGI Ch.5 (2010-2019, author-derived residual from ocean+land shares);\n"
             "Global Carbon Project - Global Carbon Budget 2024 (2014-2023). See file caveats for the 2010-2019\n"
             "derivation and the open debate over a possible recent upward trend.",
             ha="left", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.13, 1, 1))
    fig.savefig(HERE / "fig31_airborne_fraction_history.png")
    plt.close(fig)


def main():
    """Created by JXP and Claude.

    Generate all CO2 figures (23-31) for the report.

    Inputs
    ------
    (none)

    Outputs
    -------
    None. Writes fig23-fig31 PNGs into CI_Reports/ and prints the computed
    era CAGRs (also used verbatim in co2_report.md).
    """
    era_cagrs = fig23_global_growth()
    fig24_country_breakdown()
    fig25_sector_breakdown()
    fig26_fuel_type_trend()
    fig27_transport_breakdown()
    fig28_industry_breakdown()
    fig29_energy_type_breakdown()
    fig30_fate_partition()
    fig31_airborne_fraction_history()
    print("Wrote fig23_global_co2_growth.png through fig31_airborne_fraction_history.png")
    print("Era CAGRs (%/yr):", {k: round(v, 2) for k, v in era_cagrs.items()})


if __name__ == "__main__":
    main()
