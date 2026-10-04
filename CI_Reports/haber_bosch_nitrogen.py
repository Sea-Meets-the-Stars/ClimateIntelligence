"""Haber-Bosch nitrogen: how synthetic ammonia underwrites the human population,
and what it costs the climate.

Supports the "Feeding the billions" section of
CI_Reports/CI_2026_07_09_climate_report.md and the nitrogen material in
context/claudes_context.md.

Two things this script does:
  1. Computes the headline numbers used in the report (people fed by synthetic
     nitrogen; the CO2 footprint of ammonia synthesis; reactive N per person),
     from cited inputs, so every figure is reproducible rather than asserted.
  2. Renders Figure 20 (fig20_haber_bosch.png): the lock-step rise of world
     population and synthetic nitrogen-fertilizer use over the 20th century.

Sources for the inputs (see the report's reference list and
context/references.md):
  - Erisman, Sutton, Galloway, Klimont & Winiwarter (2008), "How a century of
    ammonia synthesis changed the world," Nature Geoscience 1, 636-639.
    ~48% of the 2008 population fed via Haber-Bosch N; 42% of 20th-century
    births attributable to it.
  - Smil, V. (2001), "Enriching the Earth" (MIT Press) - origin of the
    "roughly half of humanity is fed by synthetic nitrogen" estimate.
  - Our World in Data, "How many people does synthetic fertilizer feed?"
    (Ritchie 2017; Smil/Erisman synthesis).
  - IEA (2021), "Ammonia Technology Roadmap": ammonia ~2% of global final
    energy (8.6 EJ, 2020); ~180 Mt NH3 produced; direct CO2 ~450 Mt/yr;
    ~70% of feedstock hydrogen from natural gas (rest mostly coal, China).
  - Global Carbon Budget 2025: fossil CO2 ~38.1 GtCO2/yr (context, section 8).
  - IPCC AR6 SRCCL: agriculture = ~81% of anthropogenic N2O (context, 3.8).

Run:
    conda run -n ocean14 python haber_bosch_nitrogen.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).parent / "fig20_haber_bosch.png"

# --- Inputs (cited above) ------------------------------------------------------

WORLD_POP_2025 = 8.2e9          # people (UN WPP 2024, ~2025)
FRAC_FED_LOW = 0.44            # OWID/Smil, year ~2000
FRAC_FED_CENTRAL = 0.48       # Erisman et al. 2008
FRAC_FED_HIGH = 0.50          # "roughly half" (Smil)

NH3_PRODUCTION = 180e6         # t NH3 / yr (IEA 2021, ~180 Mt)
NH3_DIRECT_CO2 = 450e6         # t CO2 / yr, direct emissions (IEA 2021)
FOSSIL_CO2 = 38.1e9            # t CO2 / yr, global fossil (GCB 2025)

# Reactive nitrogen fixed industrially by Haber-Bosch, ~120 Mt N/yr
# (Haber-Bosch fixes roughly as much N as all natural terrestrial fixation).
HB_N_FIXED = 120e6             # t N / yr

# --- Calculations --------------------------------------------------------------

def main():
    people_fed_central = FRAC_FED_CENTRAL * WORLD_POP_2025
    people_fed_low = FRAC_FED_LOW * WORLD_POP_2025
    people_fed_high = FRAC_FED_HIGH * WORLD_POP_2025

    co2_per_nh3 = NH3_DIRECT_CO2 / NH3_PRODUCTION           # t CO2 / t NH3
    co2_share_fossil = NH3_DIRECT_CO2 / FOSSIL_CO2          # fraction
    n_per_person = HB_N_FIXED / WORLD_POP_2025              # t N / person / yr

    print("=" * 68)
    print("Haber-Bosch nitrogen: people and climate")
    print("=" * 68)
    print(f"World population (2025):            {WORLD_POP_2025/1e9:6.2f} billion")
    print("People whose food supply depends on synthetic (Haber-Bosch) N:")
    print(f"   low  (44%, ~2000):              {people_fed_low/1e9:6.2f} billion")
    print(f"   central (48%, Erisman 2008):    {people_fed_central/1e9:6.2f} billion")
    print(f"   high (~50%, 'about half'):      {people_fed_high/1e9:6.2f} billion")
    print("-" * 68)
    print(f"Ammonia production:                 {NH3_PRODUCTION/1e6:6.0f} Mt NH3/yr")
    print(f"Direct CO2 from ammonia synthesis:  {NH3_DIRECT_CO2/1e6:6.0f} Mt CO2/yr")
    print(f"   implied emission factor:         {co2_per_nh3:6.2f} t CO2 / t NH3")
    print(f"   share of global fossil CO2:      {co2_share_fossil*100:6.2f} %")
    print("-" * 68)
    print(f"Industrial N fixed (Haber-Bosch):   {HB_N_FIXED/1e6:6.0f} Mt N/yr")
    print(f"   per person:                      {n_per_person*1e3:6.1f} kg N / person / yr")
    print("=" * 68)

    make_figure()
    print(f"Saved {OUT}")


def make_figure():
    # Milestone values (illustrative, decadal) from OWID/FAO/Smil compilations.
    years = np.array([1900, 1920, 1940, 1960, 1980, 2000, 2020])
    population = np.array([1.65, 1.86, 2.30, 3.03, 4.46, 6.14, 7.84])  # billions
    n_fertilizer = np.array([0.0, 0.4, 2.0, 11.0, 60.0, 82.0, 110.0])  # Mt N/yr

    fig, ax1 = plt.subplots(figsize=(9, 5.2))

    color_pop = "#1f4e79"
    color_n = "#c55a11"

    ax1.plot(years, population, "o-", color=color_pop, lw=2.4, ms=6,
             label="World population")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("World population (billions)", color=color_pop)
    ax1.tick_params(axis="y", labelcolor=color_pop)
    ax1.set_ylim(0, 9)
    ax1.set_xlim(1895, 2025)

    ax2 = ax1.twinx()
    ax2.plot(years, n_fertilizer, "s--", color=color_n, lw=2.4, ms=6,
             label="Synthetic N fertilizer use")
    ax2.set_ylabel("Synthetic nitrogen fertilizer (Mt N / yr)", color=color_n)
    ax2.tick_params(axis="y", labelcolor=color_n)
    ax2.set_ylim(0, 120)

    # Mark the industrial start of Haber-Bosch (Oppau, 1913).
    ax1.axvline(1913, color="gray", ls=":", lw=1.3)
    ax1.annotate("Haber-Bosch\nindustrialized\n(Oppau, 1913)",
                 xy=(1913, 8.4), xytext=(1922, 7.2),
                 fontsize=8.5, color="gray",
                 arrowprops=dict(arrowstyle="->", color="gray", lw=1))

    ax1.annotate(
        "≈48% of today's ~8.2 billion people\n"
        "— about 4 billion — could not be fed\n"
        "without synthetic nitrogen\n"
        "(Smil; Erisman et al. 2008)",
        xy=(2020, 7.84), xytext=(1935, 3.6),
        fontsize=8.5, color=color_pop,
        arrowprops=dict(arrowstyle="->", color=color_pop, lw=1))

    ax1.set_title("Population and synthetic nitrogen rose in lock-step",
                  fontsize=12, fontweight="bold")

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9)

    fig.text(0.01, 0.01,
             "Illustrative decadal milestones (OWID / FAO / Smil compilations); "
             "values approximate.",
             fontsize=7, color="gray")

    fig.tight_layout()
    fig.savefig(OUT, dpi=150, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
