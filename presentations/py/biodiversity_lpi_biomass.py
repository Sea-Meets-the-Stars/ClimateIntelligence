"""Created by JXP and Claude.

C7a "Biodiversity is declining fast" — two of the three independent metrics
(Q11: "declining fast", not "exponentially"):
  left:  the Living Planet Index, 1970-2020 (average change in monitored
         vertebrate population sizes; -73%);
  right: the mass of mammals on Earth today (Bar-On et al. 2018).
The third metric (extinction rate vs background) is C7b, extinction_rate.py.

Data:
  LPI: WWF / ZSL Living Planet Report 2024, via Our World in Data, fetched
    2026-10-05: https://ourworldindata.org/grapher/global-living-planet-index.csv
    cached at presentations/data/owid_living_planet_index.csv (World rows;
    central estimate with 95% interval).
    Caveat (small print): the LPI is a geometric mean of ~35,000 population
    trends; -73% is the average relative change in population size, NOT the
    fraction of animals or species lost.
  Biomass (Gt C): Bar-On, Phillips & Milo 2018, PNAS 115, 6506, "The biomass
    distribution on Earth": humans 0.06; livestock 0.1; wild mammals 0.007
    (terrestrial ~0.003 + marine ~0.004).

Usage:
    conda run -n ocean14 python presentations/py/biodiversity_lpi_biomass.py
"""
import csv

import numpy as np
import matplotlib.pyplot as plt

from slide_style import DATA, FULL, apply_style, save, GREEN, RED, GRAY, ORANGE, BLUE, INK

MAMMAL_BIOMASS_GTC = [("Livestock", 0.10, GRAY), ("Humans", 0.06, ORANGE),
                      ("Wild mammals", 0.007, GREEN)]


def load_lpi():
    """Created by JXP and Claude. Outputs: year, central, upper, lower
    (World, index 1970 = 100)."""
    rows = []
    with open(DATA / "owid_living_planet_index.csv") as f:
        for r in csv.DictReader(f):
            if r["Entity"] == "World":
                rows.append((int(r["Year"]), float(r["Central estimate"]),
                             float(r["Upper estimate"]), float(r["Lower estimate"])))
    a = np.array(sorted(rows))
    return a[:, 0], a[:, 1], a[:, 2], a[:, 3]


def main():
    """Created by JXP and Claude. Build c7a_lpi_biomass.png."""
    apply_style()
    yr, c, hi, lo = load_lpi()
    drop = 100 - c[-1]
    total = sum(v for _, v, _ in MAMMAL_BIOMASS_GTC)
    print(f"LPI {int(yr[0])}-{int(yr[-1])}: {c[-1]:.1f} (-{drop:.0f}%, 95% {lo[-1]:.0f}-{hi[-1]:.0f}); "
          f"mammal biomass shares: " + ", ".join(f"{n} {v / total:.0%}" for n, v, _ in MAMMAL_BIOMASS_GTC))

    fig, (ax, bx) = plt.subplots(1, 2, figsize=FULL, gridspec_kw=dict(width_ratios=(1.5, 1)))
    ax.fill_between(yr, lo, hi, color=GREEN, alpha=0.2, lw=0)
    ax.plot(yr, c, color=GREEN, lw=2.8)
    ax.text(yr[-1], c[-1] + 12, f"−{drop:.0f}%", ha="right", fontsize=20,
            color=RED, fontweight="bold")
    ax.set_xlim(1970, 2021)
    ax.set_ylim(0, 110)
    ax.set_ylabel("Living Planet Index\n(1970 = 100)")
    ax.text(1971, 8, "Average change in ~35,000 monitored vertebrate\npopulations "
            "(not the fraction of animals lost)", fontsize=10, color=INK)

    names = [n for n, _, _ in MAMMAL_BIOMASS_GTC]
    vals = [v / total * 100 for _, v, _ in MAMMAL_BIOMASS_GTC]
    bx.barh(names[::-1], vals[::-1], color=[col for _, _, col in MAMMAL_BIOMASS_GTC][::-1], height=0.65)
    for y, v in enumerate(vals[::-1]):
        bx.text(v + 1.5, y, f"{v:.0f}%", va="center", fontsize=15, fontweight="bold")
    bx.set_xlim(0, 75)
    bx.set_xlabel("% of all mammal mass")
    bx.grid(axis="y", visible=False)

    save(fig, "c7a_lpi_biomass.png",
         "Left: WWF/ZSL Living Planet Index 2024 via Our World in Data (95% interval shaded). "
         "Right: Bar-On, Phillips & Milo 2018, PNAS (by carbon mass)",
         "C7a")


if __name__ == "__main__":
    main()
