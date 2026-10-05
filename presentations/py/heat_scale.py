"""Created by JXP and Claude.

C3a sub-line (B8b): what does ~1 W/m^2 of extra heat mean for a human?

Inputs (with sources):
  Earth's energy imbalance: 0.7 W/m^2 (IPCC AR6 WGI Fig. 7.2; 0.79 for 2006-2018).
  Resting human heat output: 1 met = 58.2 W per m^2 of body surface
    (ASHRAE Standard 55 definition of the metabolic unit for a seated, resting adult).
  Earth's surface area 5.10e14 m^2 and world primary energy use 620 EJ in 2023
    (Energy Institute Statistical Review 2024), imported from
    CI_Reports/planetary_boundaries_energy.py.
  Hiroshima bomb: ~15 kt TNT = 15 x 4.184e12 J = 6.3e13 J.

Outputs (printed; the slide text uses the rounded values):
  - 1 W/m^2 as a fraction of a resting body's heat output per m^2 of skin;
  - the planet-wide imbalance in TW, as a multiple of all human energy use,
    and in Hiroshima bombs per second.

Usage:
    conda run -n ocean14 python presentations/py/heat_scale.py
"""
import sys

from slide_style import ROOT

sys.path.insert(0, str(ROOT / "CI_Reports"))
from planetary_boundaries_energy import (EARTH_SURFACE_M2, PRIMARY_ENERGY_2023_EJ,  # noqa: E402
                                         primary_power_tw)

IMBALANCE_W_M2 = 0.7
MET_W_M2 = 58.2
HIROSHIMA_J = 15 * 4.184e12


def main():
    """Created by JXP and Claude. Print the human-scale comparisons."""
    frac_body = 1.0 / MET_W_M2
    total_tw = IMBALANCE_W_M2 * EARTH_SURFACE_M2 / 1e12
    human_tw = primary_power_tw(PRIMARY_ENERGY_2023_EJ)
    bombs_per_s = total_tw * 1e12 / HIROSHIMA_J
    print(f"1 W/m^2 = {frac_body:.1%} of a resting body's heat per m^2 of skin ({MET_W_M2} W/m^2)")
    print(f"Earth imbalance {IMBALANCE_W_M2} W/m^2 x {EARTH_SURFACE_M2:.3g} m^2 = {total_tw:.0f} TW")
    print(f"human primary energy use {human_tw:.1f} TW -> imbalance = {total_tw / human_tw:.0f}x")
    print(f"= {bombs_per_s:.1f} Hiroshima bombs per second ({bombs_per_s * 86400:,.0f} per day)")


if __name__ == "__main__":
    main()
