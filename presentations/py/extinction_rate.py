"""Created by JXP and Claude.

C7b "Biodiversity is declining fast: extinctions" — vertebrate extinctions
since 1900, observed vs. what the natural background rate would produce.

Data: Ceballos et al. 2015, Science Advances 1, e1400253, "Accelerated modern
human-induced species losses: Entering the sixth mass extinction"
(full text via Europe PMC, PMC4640606), Table 1 (IUCN Red List 2014.3):
  since 1900, "highly conservative" (EX only):        198 vertebrates
  since 1900, "conservative" (EX + EW + PE):          477 vertebrates
    (mammals 69, birds 80, reptiles 24, amphibians 146, fishes 158)
  background 2 E/MSY (2 extinctions per 10,000 species per 100 years) applied
  to the 39,223 vertebrate species evaluated -> "9 vertebrate extinctions
  would have been expected since 1900" (paper text; recomputed below).
  Paper: losses since 1900 "would have taken ... between 800 and 10,000 years"
  at the background rate; rates "up to 100 times higher than the background".

Usage:
    conda run -n ocean14 python presentations/py/extinction_rate.py
"""
import matplotlib.pyplot as plt

from slide_style import MAIN, apply_style, save, GRAY, RED, ORANGE, INK

BACKGROUND_E_MSY = 2.0
N_EVALUATED = 39_223
YEARS = 114           # 1900 to 2014 (IUCN 2014.3)
EX_SINCE_1900 = 198
CONSERVATIVE_SINCE_1900 = 477
BY_CLASS = {"amphibians": 146, "fishes": 158, "birds": 80, "mammals": 69, "reptiles": 24}


def expected_background(e_msy, n_species, years):
    """Created by JXP and Claude. Extinctions expected at e_msy
    (per million species-years) for n_species over `years`."""
    return e_msy * n_species * years / 1e6


def main():
    """Created by JXP and Claude. Build c7b_extinctions.png."""
    apply_style()
    exp = expected_background(BACKGROUND_E_MSY, N_EVALUATED, YEARS)
    print(f"expected at 2 E/MSY since 1900: {exp:.1f} (paper: 9); observed {EX_SINCE_1900}-{CONSERVATIVE_SINCE_1900} "
          f"= {EX_SINCE_1900 / exp:.0f}-{CONSERVATIVE_SINCE_1900 / exp:.0f}x")

    labels = ["Expected from the\nnatural background rate",
              "Observed: confirmed\nextinct",
              "Observed: incl. extinct in the\nwild & possibly extinct"]
    vals = [exp, EX_SINCE_1900, CONSERVATIVE_SINCE_1900]
    fig, ax = plt.subplots(figsize=MAIN)
    ax.barh(labels[::-1], vals[::-1], color=[RED, ORANGE, GRAY], height=0.62)
    for y, v in enumerate(vals[::-1]):
        ax.text(v + 6, y, f"{v:.0f}", va="center", fontsize=16, fontweight="bold")
    ax.set_xlim(0, 560)
    ax.set_xlabel("Vertebrate species extinct since 1900")
    ax.grid(axis="y", visible=False)
    parts = [f"{k} {v}" for k, v in BY_CLASS.items()]
    ax.text(545, 2, f"of the {CONSERVATIVE_SINCE_1900}: " + ", ".join(parts[:2]) + ",\n" + ", ".join(parts[2:]),
            ha="right", va="center", fontsize=11, color=INK)
    save(fig, "c7b_extinctions.png",
         "Data: Ceballos et al. 2015, Science Advances (IUCN Red List 2014.3; background = 2 extinctions "
         "per 10,000 species per century, itself 2× older estimates)",
         "C7b")


if __name__ == "__main__":
    main()
