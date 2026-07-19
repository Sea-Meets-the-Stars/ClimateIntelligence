"""Created by JXP and Claude.

Generate the planetary-boundaries + energy-balance figures (15-18) and the
supporting calculations for the Climate Intelligence report
(CI_2026_07_09_climate_report.md, section "Planetary boundaries and the energy
balance of a low-carbon future").

The section follows Tom Murphy's *Energy and Human Ambitions on a Finite Planet*
(2021) but updates the headline inputs to the most recent public data where
possible (per the author's instruction, planetary_boundaries.md prompt 2, Q3).
Every number the report quotes is computed here from stated inputs, so it is
reviewable and reproducible.

Figures produced (saved next to this file, matching the report's fig<N>_*.png
naming):
  - fig15_planetary_boundaries.png : the nine boundaries as a transgression
      ratio (current pressure / boundary), 7 of 9 beyond the safe line (2025).
  - fig16_eroi.png                 : energy return on investment by source
      (Murphy 2021 table) with recent lifecycle ranges for the two most
      contested (solar PV, nuclear) overlaid.
  - fig17_solar_land_storage.png   : (a) land area to run the world on solar,
      as % of ice-free land, for two 2100 demand cases x three power densities;
      (b) battery storage to buffer N days of global demand, in TWh and in
      "years of 2024 global battery-manufacturing capacity".
  - fig18_waste_heat.png           : the waste-heat ceiling (frame B, the
      bounding sidebar) - anthropogenic heat as a surface forcing over time for
      several growth rates, against today's GHG forcing and the boiling limit.

Data / source inputs (see report references):
  - Global primary energy 2023 = 620 EJ (Energy Institute, Statistical Review of
    World Energy 2024). 620 EJ/yr -> 19.66 TW.
  - Battery manufacturing capacity 2024 ~ 3 TWh/yr; annual demand > 1 TWh (IEA,
    Global EV Outlook / battery market 2025).
  - Solar power density: ~30 W/m^2 of *panel* (Murphy 2021, ~20% efficiency x
    ~150 W/m^2 mean insolation); ~10 W/m^2 of *land* once inter-row spacing is
    included; ~5 W/m^2 conservative (Smil; Our World in Data land-use figures).
  - EROI: Murphy (2021) Table; recent ranges - solar PV 8-34 and energy payback
    ~1 yr (Fraunhofer ISE); nuclear 20-81 (WNA); wind ~20 (Wikipedia/EROI
    literature). Point-of-use vs primary-energy-equivalent boundary choices
    explain much of the spread.
  - Planetary boundaries control values: Steffen et al. 2015; Richardson et al.
    2023; 2025 Planetary Health Check (see claudes_context.md sec 16).
  - Earth surface area 5.10e14 m^2; ice-free land area 1.30e14 m^2 (land 1.49e14
    m^2, ~13% ice/barren removed for the "usable land" comparison).

Run under the project conda environment:
    conda run -n ocean14 python CI_Reports/planetary_boundaries_energy.py

Design choices follow the project coding guidelines: functions (no classes),
imports at top, inline comments, matplotlib for plotting, docstrings with
inputs/outputs, and "Created by JXP and Claude" on the file and each method.
"""

# Imports at the top of the file (project coding guideline).
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")  # headless backend; we save PNGs, never display
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

HERE = Path(__file__).resolve().parent

# Same visual style as the other report figure scripts, for consistency.
plt.rcParams.update({
    "figure.dpi": 130,
    "savefig.dpi": 130,
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# ---------------------------------------------------------------------------
# Physical constants and headline inputs (all sourced in the module docstring).
# ---------------------------------------------------------------------------
SECONDS_PER_YEAR = 3.1536e7          # 365 d
EARTH_SURFACE_M2 = 5.10e14           # total surface area
LAND_AREA_M2 = 1.49e14               # total land area
ICE_FREE_LAND_M2 = 1.30e14           # ice-free / usable land (~87% of land)
SIGMA = 5.670374e-8                  # Stefan-Boltzmann, W/m^2/K^4

PRIMARY_ENERGY_2023_EJ = 620.0       # Energy Institute Statistical Review 2024
FOSSIL_ENERGY_2023_EJ = 505.0        # 81.5% of the above
GHG_FORCING_2024 = 3.0               # W/m^2, total anthropogenic ERF (~AR6 2019 + since)

BATTERY_MFG_2024_TWH = 3.0           # global Li-ion manufacturing capacity, TWh/yr (IEA)


def primary_power_tw(energy_ej):
    """Created by JXP and Claude.

    Convert an annual primary-energy figure (EJ/yr) to continuous power (TW).
    Input: energy_ej (float, EJ/yr). Output: power in TW (float).
    """
    watts = energy_ej * 1e18 / SECONDS_PER_YEAR
    return watts / 1e12


def demand_scenarios_2100(p0_tw, base_year=2025, target_year=2100):
    """Created by JXP and Claude.

    Build the 2100 demand cases used throughout the section. Inputs: current
    power p0_tw (TW), base/target years. Output: dict of scenario -> TW.

    - flat: today's primary power held constant to 2100.
    - growth_1pct: 1%/yr compound growth (Murphy's caution about exponentials;
      well below the historical ~2.3%/yr, chosen as a *modest* case).
    - electrified_flat: electrifying end-uses removes most fossil thermal-
      conversion loss, so a fully electric world needs less *primary-equivalent*
      power for the same services; ~0.55 is a mid estimate (LLNL/IEA electrify-
      everything analyses put the reduction near 40-50%).
    """
    years = target_year - base_year
    return {
        "Flat (20 TW)": p0_tw,
        "Growth 1%/yr": p0_tw * (1.01 ** years),
        "Electrified, flat": p0_tw * 0.55,
    }


def solar_land_fraction(demand_tw, density_w_m2):
    """Created by JXP and Claude.

    Land area (as a fraction of ice-free land) to meet demand_tw from solar at a
    given land power density (W/m^2). Inputs: demand (TW), density (W/m^2).
    Output: (area_km2, fraction_of_ice_free_land).
    """
    area_m2 = demand_tw * 1e12 / density_w_m2
    return area_m2 / 1e6, area_m2 / ICE_FREE_LAND_M2


def storage_twh(days, p0_tw):
    """Created by JXP and Claude.

    Energy (TWh) to store `days` of continuous global demand at p0_tw.
    Inputs: days (float), p0_tw (TW). Output: TWh (float).
    """
    joules = p0_tw * 1e12 * days * 86400.0
    return joules / 3.6e15  # J -> TWh


def waste_heat_forcing(p_tw):
    """Created by JXP and Claude.

    Anthropogenic waste-heat expressed as a global-mean surface forcing (W/m^2):
    all primary energy ultimately degrades to heat. Input: power (TW). Output:
    forcing (W/m^2).
    """
    return p_tw * 1e12 / EARTH_SURFACE_M2


def years_to_forcing(p0_tw, growth_rate, target_forcing):
    """Created by JXP and Claude.

    Years for waste-heat forcing to reach target_forcing (W/m^2) under compound
    growth. Inputs: p0_tw (TW), growth_rate (fraction/yr), target_forcing
    (W/m^2). Output: years (float) or inf if growth_rate <= 0.
    """
    if growth_rate <= 0:
        return float("inf")
    p_target_tw = target_forcing * EARTH_SURFACE_M2 / 1e12
    return np.log(p_target_tw / p0_tw) / np.log(1.0 + growth_rate)


# ---------------------------------------------------------------------------
# Planetary-boundaries data (claudes_context.md sec 16). "ratio" = current
# pressure / boundary, oriented so >1 means transgressed. Values with mixed
# direction (land, ozone) are converted to a loss/depletion ratio in the
# comments. Biosphere integrity is capped for display (true value >>10).
# ---------------------------------------------------------------------------
BOUNDARIES = [
    # (label, ratio, transgressed, note)
    ("Biosphere integrity", 10.0, True, ">10x (ext. rate >100 vs <10 E/MSY)"),
    ("Biogeochemical (N)", 190.0 / 62.0, True, "N fixation 190 vs 62 Tg/yr"),
    ("Freshwater (green)", 22.0 / 12.0, True, "soil-moisture deviation"),
    ("Land-system change", 40.0 / 25.0, True, "forest loss 40% vs 25% allowed"),
    ("Climate change", 420.0 / 350.0, True, "CO2 420 vs 350 ppm"),
    ("Novel entities", 1.5, True, "no metric; judged over (unquantified)"),
    ("Ocean acidification", (3.44 - 2.84) / (3.44 - 2.86), True, "newly crossed 2025"),
    ("Aerosol loading", 0.076 / 0.10, False, "AOD diff 0.076 vs 0.10"),
    ("Stratospheric ozone", 5.0 / 14.0, False, "recovering (Montreal Protocol)"),
]

# EROI table: Murphy (2021). recent = (low, high) lifecycle range where the
# figure is strongly contested; None if we keep Murphy's single value.
EROI_MURPHY = [
    ("Hydro", 40, None),
    ("Wind", 20, (18, 22)),
    ("Coal", 18, None),
    ("Oil", 16, None),
    ("Nuclear", 5, (20, 81)),
    ("Natural gas", 7, None),
    ("Solar PV", 6, (8, 34)),
    ("Tar sands", 4, None),
    ("Corn ethanol", 1.4, None),
]


def make_fig15_boundaries(path):
    """Created by JXP and Claude. Horizontal transgression-ratio chart of the
    nine planetary boundaries. Output: writes PNG to `path`."""
    items = sorted(BOUNDARIES, key=lambda b: b[1])
    labels = [b[0] for b in items]
    ratios = [b[1] for b in items]
    colors = ["#c0392b" if b[2] else "#27ae60" for b in items]

    fig, ax = plt.subplots(figsize=(8.2, 5.0))
    y = np.arange(len(labels))
    ax.barh(y, ratios, color=colors, alpha=0.85)
    ax.axvline(1.0, color="black", lw=1.5, ls="--")
    ax.text(1.02, len(labels) - 0.4, "boundary", rotation=90,
            va="top", ha="left", fontsize=9)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlabel("Transgression ratio  (current pressure / boundary; >1 = beyond safe zone)")
    ax.set_xlim(0, 10.6)
    # annotate the capped biosphere bar
    for yi, b in enumerate(items):
        if b[0] == "Biosphere integrity":
            ax.text(10.0, yi, "  >10x", va="center", ha="left", fontsize=9)
    ax.set_title("Figure 15. Planetary boundaries: 7 of 9 transgressed (2025)")
    legend = [Patch(facecolor="#c0392b", label="Transgressed (7)"),
              Patch(facecolor="#27ae60", label="Within safe zone (2)")]
    ax.legend(handles=legend, loc="lower right", frameon=False)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def make_fig16_eroi(path):
    """Created by JXP and Claude. EROI by source (Murphy 2021) with recent
    ranges for solar PV and nuclear overlaid. Output: writes PNG to `path`."""
    items = sorted(EROI_MURPHY, key=lambda e: e[1])
    labels = [e[0] for e in items]
    vals = [e[1] for e in items]

    fig, ax = plt.subplots(figsize=(8.2, 5.0))
    y = np.arange(len(labels))
    ax.barh(y, vals, color="#34495e", alpha=0.85)
    # overlay recent lifecycle ranges where contested
    for yi, e in enumerate(items):
        if e[2] is not None:
            lo, hi = e[2]
            ax.plot([lo, hi], [yi, yi], color="#e67e22", lw=3, solid_capstyle="round")
            ax.plot([lo, hi], [yi, yi], "|", color="#e67e22", ms=10)
    ax.axvline(7, color="#7f8c8d", ls=":", lw=1.3)
    ax.text(7.2, 0.1, "~7:1 societal\nbreak-even", fontsize=8.5, color="#7f8c8d")
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlabel("Energy return on investment (EROI, output:input)")
    ax.set_title("Figure 16. EROI by source — Murphy (2021), with recent ranges (orange)")
    ax.legend(handles=[plt.Line2D([0], [0], color="#e67e22", lw=3,
              label="recent lifecycle range (PV, nuclear)")],
              loc="lower right", frameon=False)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def make_fig17_land_storage(path, demands, p0_tw):
    """Created by JXP and Claude. Two-panel: (a) solar land as % of ice-free
    land; (b) battery storage for N days. Inputs: demands dict, p0_tw.
    Output: writes PNG to `path`."""
    fig, (axa, axb) = plt.subplots(1, 2, figsize=(11.5, 5.0))

    # (a) land area: two demand cases x three densities
    densities = [(30, "panel only\n(Murphy)"), (10, "with spacing"), (5, "conservative")]
    cases = ["Flat (20 TW)", "Growth 1%/yr"]
    width = 0.25
    xbase = np.arange(len(cases))
    for i, (dens, dlabel) in enumerate(densities):
        fracs = [100.0 * solar_land_fraction(demands[c], dens)[1] for c in cases]
        axa.bar(xbase + (i - 1) * width, fracs, width, label=f"{dens} W/m² ({dlabel})")
    axa.set_xticks(xbase)
    axa.set_xticklabels(cases)
    axa.set_ylabel("Solar footprint (% of ice-free land)")
    axa.set_title("(a) Land to run the world on solar")
    axa.axhline(11, color="#7f8c8d", ls=":", lw=1.2)
    axa.text(-0.35, 11.3, "cropland today ≈ 11% of land", fontsize=8, color="#7f8c8d")
    axa.legend(fontsize=8, frameon=False)

    # (b) storage for N days, TWh, with years-of-mfg annotation
    days = [1, 7, 30]
    twh = [storage_twh(d, p0_tw) for d in days]
    x = np.arange(len(days))
    bars = axb.bar(x, twh, color="#8e44ad", alpha=0.85)
    axb.set_xticks(x)
    axb.set_xticklabels([f"{d} day\nbuffer" for d in days])
    axb.set_ylabel("Battery storage required (TWh)")
    axb.set_title("(b) Seasonal storage is the hard wall")
    for xi, (d, val) in enumerate(zip(days, twh)):
        yrs = val / BATTERY_MFG_2024_TWH
        axb.text(xi, val, f"{val:,.0f} TWh\n= {yrs:,.0f}× 2024\nglobal battery\noutput",
                 ha="center", va="bottom", fontsize=8)
    axb.set_ylim(0, max(twh) * 1.35)

    fig.suptitle("Figure 17. Solar land footprint and storage for a ~20 TW world",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(path)
    plt.close(fig)


def make_fig18_waste_heat(path, p0_tw):
    """Created by JXP and Claude. Waste-heat forcing vs year for several growth
    rates (frame B sidebar). Input: p0_tw. Output: writes PNG to `path`."""
    years = np.arange(2025, 2525)
    t = years - 2025
    rates = [(0.0, "0% (flat)"), (0.01, "1%/yr"), (0.023, "2.3%/yr (historical)"),
             (0.03, "3%/yr")]

    fig, ax = plt.subplots(figsize=(8.6, 5.2))
    for r, lbl in rates:
        p = p0_tw * (1.0 + r) ** t
        ax.plot(years, waste_heat_forcing(p), lw=2, label=lbl)
    ax.set_yscale("log")
    ax.axhline(GHG_FORCING_2024, color="#c0392b", ls="--", lw=1.3)
    ax.text(2033, GHG_FORCING_2024 * 0.62, "today's total GHG forcing ≈ 3 W/m²",
            color="#c0392b", fontsize=9)
    ax.axhline(4.0, color="#e67e22", ls=":", lw=1.2)
    ax.text(2300, 5.2, "≈ CO₂-doubling forcing (~4 W/m²)", color="#e67e22", fontsize=8.5)
    ax.set_xlabel("Year")
    ax.set_ylabel("Anthropogenic waste-heat forcing (W/m², log scale)")
    ax.set_title("Figure 18. The waste-heat ceiling on growth (any energy source)")
    ax.legend(loc="upper left", frameon=False, title="primary-power growth")
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def print_calculations(p0_tw, demands):
    """Created by JXP and Claude. Print every number the report quotes, so the
    section is reviewable. Output: stdout only."""
    print("=" * 70)
    print("PLANETARY BOUNDARIES + ENERGY BALANCE — computed values")
    print("=" * 70)
    print(f"\nCurrent primary power (620 EJ/yr, 2023): {p0_tw:.2f} TW")
    print(f"Fossil share: {FOSSIL_ENERGY_2023_EJ/PRIMARY_ENERGY_2023_EJ*100:.1f}%")

    print("\n2100 demand scenarios:")
    for k, v in demands.items():
        print(f"  {k:22s}: {v:6.1f} TW")

    print("\nSolar land footprint (% of ice-free land):")
    for c in ["Flat (20 TW)", "Growth 1%/yr"]:
        for dens in (30, 10, 5):
            km2, frac = solar_land_fraction(demands[c], dens)
            print(f"  {c:14s} @ {dens:2d} W/m^2: {km2:10,.0f} km^2  = {frac*100:5.2f}% of ice-free land")

    print("\nStorage to buffer N days of global demand:")
    for d in (1, 7, 30):
        twh = storage_twh(d, p0_tw)
        print(f"  {d:2d} day(s): {twh:9,.0f} TWh  = {twh/BATTERY_MFG_2024_TWH:7,.0f}x 2024 global battery mfg (3 TWh/yr)")

    print("\nWaste-heat ceiling:")
    f_now = waste_heat_forcing(p0_tw)
    print(f"  Waste-heat forcing today: {f_now:.4f} W/m^2 ({f_now/GHG_FORCING_2024*100:.1f}% of GHG forcing)")
    flux_now = SIGMA * 288.0 ** 4
    flux_boil = SIGMA * 373.0 ** 4
    p_boil_tw = (flux_boil - flux_now) * EARTH_SURFACE_M2 / 1e12
    print(f"  Power to boil the surface (288K->373K): {p_boil_tw:,.0f} TW")
    for r in (0.01, 0.023, 0.03):
        yb = years_to_forcing(p0_tw, r, flux_boil - flux_now)
        yg = years_to_forcing(p0_tw, r, GHG_FORCING_2024)
        print(f"  @ {r*100:4.1f}%/yr: {yg:6.0f} yr to rival today's GHG forcing; {yb:6.0f} yr to boiling")
    print("=" * 70)


def main():
    """Created by JXP and Claude. Compute all values and write figures 15-18."""
    p0_tw = primary_power_tw(PRIMARY_ENERGY_2023_EJ)
    demands = demand_scenarios_2100(p0_tw)

    print_calculations(p0_tw, demands)

    make_fig15_boundaries(HERE / "fig15_planetary_boundaries.png")
    make_fig16_eroi(HERE / "fig16_eroi.png")
    make_fig17_land_storage(HERE / "fig17_solar_land_storage.png", demands, p0_tw)
    make_fig18_waste_heat(HERE / "fig18_waste_heat.png", p0_tw)
    print("\nWrote fig15_planetary_boundaries.png, fig16_eroi.png, "
          "fig17_solar_land_storage.png, fig18_waste_heat.png")


if __name__ == "__main__":
    main()
