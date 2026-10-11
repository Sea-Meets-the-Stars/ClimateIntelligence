"""Created by JXP and Claude.

C3a "Heat in vs. heat out": Earth's top-of-atmosphere energy budget as
arrows (left) and the satellite-measured growth of the imbalance (right).

Values (W/m^2, global annual mean, early 21st century):
  IPCC AR6 WGI Ch. 7, Figure 7.2 (all-sky; 5-95% ranges in parentheses):
    incoming solar 340 (340, 341); reflected solar 100 (97, 100);
    outgoing thermal 239 (237, 242); imbalance 0.7 (0.5, 0.9).
  AR6 WGI Ch. 7 Sec. 7.2.2: energy imbalance 0.79 [0.52 to 1.06] W/m^2 for 2006-2018
    (91% of the heat goes into the ocean).
  Loeb et al. 2021, GRL 48, e2021GL093047 ("Satellite and Ocean Data Reveal
    Marked Increase in Earth's Heating Rate"): linear trend in CERES data
    implies 0.42 +/- 0.48 W/m^2 in mid-2005 and 1.12 +/- 0.48 W/m^2 in
    mid-2019 — an approximate doubling, confirmed independently by Argo.
  Note: the rounded arrows (340 - 100 - 239 = 1) do not close exactly; the
  imbalance is measured from the change in heat stored (mostly ocean), not
  by differencing the arrows (CERES absolute calibration is ~1-3 W/m^2).

Usage:
    conda run -n ocean14 python presentations/py/energy_budget_arrows.py
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrow, Rectangle

from slide_style import MAIN, apply_style, save, GOLD, RED, BLUE, MUTED, INK

# AR6 WGI Fig. 7.2 (W/m^2)
INCOMING, REFLECTED, OUTGOING, IMBALANCE = 340, 100, 239, 0.7
IMBALANCE_RANGE = (0.5, 0.9)
# Loeb et al. 2021 (W/m^2): (label, central, 1-sigma-ish uncertainty quoted)
LOEB = [("mid-2005", 0.42, 0.48), ("mid-2019", 1.12, 0.48)]


def arrow(ax, x, y, dx, dy, width, color):
    """Created by JXP and Claude. Thick arrow whose width scales with the flux."""
    ax.add_patch(FancyArrow(x, y, dx, dy, width=width, head_width=width * 1.8,
                            head_length=0.45, length_includes_head=True,
                            color=color, ec="none"))


def main():
    """Created by JXP and Claude. Build c3a_energy_budget.png."""
    apply_style()
    fig = plt.figure(figsize=MAIN)  # sized to sit beside the CERES photo on the slide
    ax = fig.add_axes([0.0, 0.10, 0.60, 0.90])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    # Earth (a big arc at the bottom) and a thin atmosphere band.
    ax.add_patch(Circle((5, -9.2), 10.6, color="#9cc3e6", zorder=0))
    ax.add_patch(Circle((5, -9.2), 10.0, color="#2e6fa8", zorder=1))
    ax.add_patch(Rectangle((0, 5.2), 10, 0.02, color=MUTED))
    ax.text(5.75, 5.32, "top of atmosphere", ha="center", fontsize=11, color=MUTED)

    # Arrow widths proportional to flux (0.0032 data-units per W/m^2).
    k = 0.0032
    arrow(ax, 2.6, 6.0, 1.0, -4.5, INCOMING * k, GOLD)
    ax.text(0.1, 3.2, f"Sunlight in\n{INCOMING}", fontsize=13, color="#a07000",
            fontweight="bold")
    arrow(ax, 4.0, 1.6, 0.8, 4.2, REFLECTED * k, "#e8cf7a")
    ax.text(4.95, 2.9, f"Reflected\n{REFLECTED}", fontsize=13, color="#a07000")
    arrow(ax, 7.4, 1.4, 0.5, 4.4, OUTGOING * k, RED)
    ax.text(8.15, 3.3, f"Heat out\n(infrared)\n{OUTGOING}", fontsize=13,
            color=RED, fontweight="bold")
    ax.text(5.0, 0.4, f"Kept: ≈ +{IMBALANCE} W/m²", ha="center", fontsize=15,
            color="white", fontweight="bold", zorder=3)
    ax.text(9.9, 0.95, "W/m², global average", ha="right", fontsize=11, color=MUTED)

    # Right panel: the imbalance is growing (CERES; Loeb et al. 2021).
    bx = fig.add_axes([0.74, 0.30, 0.25, 0.58])
    labels = [f"{r[0]}\n{r[1]:.2f}" for r in LOEB]
    vals = [r[1] for r in LOEB]
    errs = [r[2] for r in LOEB]
    bx.bar(labels, vals, yerr=errs, color=["#e6a39a", RED], capsize=5, width=0.6,
           error_kw=dict(elinewidth=1.2, ecolor="#555555"))
    bx.set_ylabel("Imbalance (W/m²)")
    bx.set_ylim(0, 1.8)
    bx.grid(axis="x", visible=False)
    bx.set_title("it has doubled", fontsize=13, color=INK)

    save(fig, "c3a_energy_budget.png",
         "Arrows: IPCC AR6 WGI Fig. 7.2 (CERES-era budget; imbalance 0.7 [0.5–0.9] W/m²). "
         "Bars: CERES satellite trend, Loeb et al. 2021 (GRL), confirmed by Argo ocean heat uptake",
         "C3a")


if __name__ == "__main__":
    main()
