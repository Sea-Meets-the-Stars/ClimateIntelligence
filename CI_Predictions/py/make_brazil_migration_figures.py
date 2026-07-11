"""Created by JXP and Claude.

Generate the figures for the Brazil climate-migration prediction document
(CI_Predictions/CI_2026_predictions_migration.md). Figures are written to
CI_Predictions/ (one level up from this script).

IMPORTANT — two kinds of figure live here, and they must not be confused:
  * Figures 1 and part of 4 use REAL, archived data (IBGE 2022 census regional
    populations; OWID/UN national population trajectory), cached under
    CI_Predictions/data/.
  * Figures 2 and 3 visualize the document's OWN PREDICTIONS — the migration
    corridors and the falsifiable ledger. These are STRUCTURED JUDGMENTS by the
    authors (JXP + Claude), conditional on the stated 2050 assumptions, NOT
    measurements. Every such figure is watermarked "Author projection" so a
    future reader never mistakes a prediction for an observation. The ledger
    numbers are read from data/brazil_migration_ledger.csv so the figure and the
    document's ledger table cannot drift apart.

Data sources:
  - IBGE 2022 Census, population by region -> data/brazil_regions_2022.csv
  - OWID "population-long-run-with-projections" (HYDE/Gapminder/UN WPP 2024),
    Brazil -> data/owid_brazil_population.csv
  - Ledger central/low/high estimates -> data/brazil_migration_ledger.csv
    (the authors' conditional projections; see the document for derivation)

Run under the project conda environment, from anywhere:
    conda run -n ocean14 python CI_Predictions/py/make_brazil_migration_figures.py

Design follows the project coding guidelines: functions (no classes), imports
at top, inline comments, matplotlib, docstrings with inputs/outputs, and
"Created by JXP and Claude" on the file and each method. Visual style matches
CI_Reports/make_figures.py.
"""

# Imports at the top of the file (project coding guideline).
import csv
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")  # headless backend; we save PNGs, never display
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"       # CI_Predictions/data
OUT = HERE.parent                 # CI_Predictions/ (figures live beside the .md)

# Shared visual style, consistent with the climate report's figures.
plt.rcParams.update({
    "figure.dpi": 130,
    "savefig.dpi": 130,
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# Consistent region -> color map (fixed order, never cycled).
REGION_COLORS = {
    "North": "#1a9850",           # Amazon green
    "Northeast": "#d73027",       # semi-arid red (heat/drought)
    "Center-West": "#fdae61",     # Cerrado frontier amber
    "Southeast": "#4575b4",       # industrial blue
    "South": "#7b3294",           # southern purple
}


def _projection_watermark(ax):
    """Created by JXP and Claude.

    Stamp a figure axis as an author projection (not measured data).

    Inputs
    ------
    ax : matplotlib Axes

    Outputs
    -------
    None. Draws a light diagonal watermark in the axis background.
    """
    ax.text(0.5, 0.5, "AUTHOR PROJECTION", transform=ax.transAxes,
            fontsize=26, color="#bbbbbb", alpha=0.22, ha="center",
            va="center", rotation=25, zorder=0, fontweight="bold")


def load_regions():
    """Created by JXP and Claude.

    Load IBGE 2022 regional populations.

    Inputs
    ------
    (none) reads data/brazil_regions_2022.csv

    Outputs
    -------
    list[tuple[str, float, float]]
        (region, population_millions, share_percent), file order.
    """
    rows = []
    with open(DATA / "brazil_regions_2022.csv") as f:
        for r in csv.DictReader(f):
            rows.append((r["region"], float(r["population_millions"]),
                         float(r["share_percent"])))
    return rows


def load_national_trajectory():
    """Created by JXP and Claude.

    Load Brazil's national population series (OWID: estimates + UN projection).

    Inputs
    ------
    (none) reads data/owid_brazil_population.csv
    Columns: Entity, Code, Year, Population (projections) (Projected), Population

    Outputs
    -------
    (np.ndarray, np.ndarray, np.ndarray, np.ndarray)
        est_year, est_pop, proj_year, proj_pop  (millions).
    """
    est, proj = [], []
    with open(DATA / "owid_brazil_population.csv") as f:
        for row in csv.DictReader(f):
            year = int(row["Year"])
            if row["Population"]:
                est.append((year, float(row["Population"]) / 1e6))
            if row["Population (projections) (Projected)"]:
                proj.append((year, float(row["Population (projections) (Projected)"]) / 1e6))
    est.sort(); proj.sort()
    return (np.array([r[0] for r in est]), np.array([r[1] for r in est]),
            np.array([r[0] for r in proj]), np.array([r[1] for r in proj]))


def load_ledger():
    """Created by JXP and Claude.

    Load the prediction ledger (the authors' conditional 2050 estimates).

    Inputs
    ------
    (none) reads data/brazil_migration_ledger.csv

    Outputs
    -------
    list[dict]
        One dict per ledger row with parsed numeric fields.
    """
    rows = []
    with open(DATA / "brazil_migration_ledger.csv") as f:
        for r in csv.DictReader(f):
            for k in ("central", "low", "high", "probability"):
                r[k] = float(r[k])
            rows.append(r)
    return rows


def fig1_regions_and_trajectory():
    """Created by JXP and Claude.

    Figure 1 (REAL DATA): Brazil's population by region (2022 census, left) and
    the national trajectory with the UN medium projection to 2100 (right),
    marking the ~2040 national peak.

    Inputs
    ------
    (none) reads the cached IBGE + OWID data.

    Outputs
    -------
    None. Saves fig1_brazil_population.png.
    """
    regions = load_regions()
    ey, ep, py, pp = load_national_trajectory()

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.8),
                                   gridspec_kw={"width_ratios": [1, 1.25]})

    # Left: regional bars (real census data).
    names = [r[0] for r in regions]
    pops = [r[1] for r in regions]
    colors = [REGION_COLORS[n] for n in names]
    y = np.arange(len(names))[::-1]
    axL.barh(y, pops, color=colors, alpha=0.9)
    for yi, (n, p, s) in zip(y, regions):
        axL.text(p + 1, yi, f"{p:.1f} M ({s:.0f}%)", va="center", fontsize=9)
    axL.set_yticks(y)
    axL.set_yticklabels(names)
    axL.set_xlim(0, 100)
    axL.set_xlabel("Population (millions)")
    axL.set_title("Population by region, 2022 census")
    axL.grid(axis="y", visible=False)

    # Right: national trajectory (real estimates + UN projection).
    axR.plot(ey, ep, color="#4575b4", lw=2, label="Estimates")
    axR.plot(py, pp, color="#4575b4", lw=2, ls="--",
             label="UN WPP 2024 medium projection")
    ipk = int(np.argmax(pp))
    axR.plot(py[ipk], pp[ipk], "o", color="#d73027", ms=7, zorder=5)
    axR.annotate(f"peak ~{pp[ipk]:.0f} M ({py[ipk]})",
                 (py[ipk], pp[ipk]), xytext=(py[ipk] - 62, pp[ipk] - 22),
                 fontsize=9, color="#d73027",
                 arrowprops=dict(arrowstyle="->", color="#d73027", lw=0.8))
    axR.axvline(2050, color="gray", lw=0.8, ls=":")
    axR.text(2052, 60, "2050\nhorizon", fontsize=8, color="gray")
    axR.set_xlim(1950, 2100)
    axR.set_ylim(0, 240)
    axR.set_xlabel("Year")
    axR.set_ylabel("Population (millions)")
    axR.set_title("National population, 1950–2100")
    axR.legend(loc="lower center", frameon=False, fontsize=8)

    fig.suptitle("Brazil: where the people are, and the demographic backdrop",
                 fontsize=13)
    fig.text(0.99, 0.01,
             "Data: IBGE 2022 Census (regions); OWID / UN WPP 2024 (national). "
             "Fetched 2026-07-11. Real data.",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 0.96))
    fig.savefig(OUT / "fig1_brazil_population.png")
    plt.close(fig)


def fig2_corridors():
    """Created by JXP and Claude.

    Figure 2 (AUTHOR PROJECTION): a stylized map of Brazil's five regions with
    the internal climate-migration corridors the document predicts. Region
    boxes are schematic (approximate relative positions), NOT a geographic
    projection; arrow widths encode relative predicted flow magnitude.

    Inputs
    ------
    (none)

    Outputs
    -------
    None. Saves fig2_migration_corridors.png.
    """
    # Schematic region centers on a unit canvas (approx. Brazilian geography).
    # Spread out and sized so boxes do not overlap (schematic, not geographic).
    pos = {
        "North": (2.5, 7.0),        # Amazon basin, NW
        "Northeast": (7.4, 7.0),    # NE bulge
        "Center-West": (2.6, 4.2),  # Cerrado, central-W
        "Southeast": (7.0, 3.6),    # SE
        "South": (5.0, 1.2),        # S
    }
    size = {  # schematic box half-widths (roughly by area/population salience)
        "North": (1.5, 0.95), "Northeast": (1.4, 0.95), "Center-West": (1.25, 0.85),
        "Southeast": (1.3, 0.8), "South": (1.15, 0.7),
    }

    fig, ax = plt.subplots(figsize=(8.2, 8.4))
    _projection_watermark(ax)

    # Draw region boxes.
    for name, (x, y) in pos.items():
        hw, hh = size[name]
        ax.add_patch(Rectangle((x - hw, y - hh), 2 * hw, 2 * hh,
                               facecolor=REGION_COLORS[name], alpha=0.30,
                               edgecolor=REGION_COLORS[name], lw=1.8, zorder=2))
        ax.text(x, y, name, ha="center", va="center", fontsize=10,
                fontweight="bold", color="#222", zorder=3)

    # Predicted corridors: (from, to, relative weight, label).
    corridors = [
        ("Northeast", "Southeast", 5.0, "semi-arid drought\n(largest flow)"),
        ("Northeast", "South", 2.0, ""),
        ("North", "Center-West", 2.2, "Amazon degradation"),
        ("North", "Southeast", 1.6, ""),
        ("Center-West", "Southeast", 1.4, "frontier ↔ metros"),
    ]
    for src, dst, w, label in corridors:
        x0, y0 = pos[src]
        x1, y1 = pos[dst]
        arrow = FancyArrowPatch((x0, y0), (x1, y1),
                                arrowstyle="-|>", mutation_scale=18,
                                lw=w, color="#333", alpha=0.65,
                                connectionstyle="arc3,rad=0.12", zorder=4)
        ax.add_patch(arrow)
        if label:
            ax.text(0.5 * (x0 + x1) + 0.5, 0.5 * (y0 + y1) + 0.15, label,
                    fontsize=8, color="#333", style="italic", zorder=5,
                    ha="center")

    # Intra-urban flood displacement marker: star at the lower-left corner of
    # the South box (Porto Alegre 2024), caption below, clear of the label.
    sx, sy = pos["South"]
    ax.plot(sx - size["South"][0] + 0.15, sy, marker="*", ms=17,
            color="#d73027", zorder=6)
    ax.text(sx, sy - size["South"][1] - 0.35,
            "flood displacement (e.g. Porto Alegre 2024)", fontsize=8,
            color="#d73027", ha="center", va="top", zorder=6)

    # Legend for arrow width.
    ax.plot([0.7, 1.6], [8.5, 8.5], lw=5, color="#333", alpha=0.65)
    ax.text(1.75, 8.5, "thicker = larger predicted flow", fontsize=8,
            va="center", color="#333")

    ax.set_xlim(0.5, 9.4)
    ax.set_ylim(0.0, 8.9)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Predicted internal climate-migration corridors to 2050\n"
                 "(conditional on +2.0 °C and a materially degraded Amazon)",
                 fontsize=12)
    fig.text(0.99, 0.01,
             "Schematic (not a geographic projection). Corridors are author "
             "projections, not observed flows. 2026-07-11.",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout()
    fig.savefig(OUT / "fig2_migration_corridors.png")
    plt.close(fig)


def fig3_ledger():
    """Created by JXP and Claude.

    Figure 3 (AUTHOR PROJECTION): the prediction ledger's quantified estimates
    as central points with low-high ranges, read straight from the ledger CSV
    so the figure and the document's table stay in sync. Each row is annotated
    with its assigned probability. Note: rows use different units, so the x
    axis is drawn per-row (broken) rather than shared — values are labeled.

    Inputs
    ------
    (none) reads data/brazil_migration_ledger.csv

    Outputs
    -------
    None. Saves fig3_prediction_ledger.png.
    """
    rows = load_ledger()
    n = len(rows)
    fig, ax = plt.subplots(figsize=(9.5, 0.95 * n + 1.6))
    _projection_watermark(ax)

    y = np.arange(n)[::-1] * 1.6   # extra vertical room per row
    # The range bar occupies a fixed panel on the RIGHT (x in [0.30, 0.92]);
    # the descriptive label sits ABOVE the bar so nothing overlaps. Each row is
    # normalized to its own [low, high] span (units differ); real numbers are
    # annotated.
    bx0, bx1 = 0.30, 0.92
    for yi, r in zip(y, rows):
        lo, mid, hi = r["low"], r["central"], r["high"]
        span = hi - lo if hi > lo else 1.0
        x_mid = bx0 + (bx1 - bx0) * (mid - lo) / span
        ax.plot([bx0, bx1], [yi, yi], color="#4575b4", lw=3, alpha=0.5,
                solid_capstyle="round", zorder=2)
        ax.plot(x_mid, yi, "o", color="#d73027", ms=11, zorder=3)
        ax.text(bx0 - 0.015, yi, f"{lo:g}", ha="right", va="center",
                fontsize=8, color="#555")
        ax.text(bx1 + 0.015, yi, f"{hi:g}", ha="left", va="center",
                fontsize=8, color="#555")
        ax.text(x_mid, yi + 0.22, f"{mid:g}", ha="center", va="bottom",
                fontsize=10, color="#d73027", fontweight="bold")
        # Label block, left-aligned, above the bar (no collision with numbers).
        ax.text(0.0, yi + 0.42, f"{r['id']}  {r['label']}", ha="left",
                va="center", fontsize=9.5)
        ax.text(0.0, yi + 0.10, f"{r['unit']}  ·  P≈{r['probability']:g}"
                f"  ·  {r['confidence']} confidence",
                ha="left", va="center", fontsize=7.5, color="#666")

    ax.set_xlim(-0.02, 1.0)
    ax.set_ylim(min(y) - 0.9, max(y) + 0.9)
    ax.axis("off")
    ax.set_title("Brazil climate-migration prediction ledger (2050)\n"
                 "central estimate ● with low–high range; conditional on +2.0 °C "
                 "and a degraded Amazon",
                 fontsize=12)
    fig.text(0.99, 0.01,
             "Author projections (structured judgments), NOT measurements. "
             "Bars scaled per-row to their own range; numbers are the real "
             "estimates. Source: brazil_migration_ledger.csv.",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(OUT / "fig3_prediction_ledger.png")
    plt.close(fig)


def fig4_drivers():
    """Created by JXP and Claude.

    Figure 4 (SCHEMATIC): the causal chain the document argues — physical
    climate drivers -> intermediate stressors -> migration response -> feedbacks
    — as a simple left-to-right flow. Communicates mechanism, not magnitude.

    Inputs
    ------
    (none)

    Outputs
    -------
    None. Saves fig4_driver_chain.png.
    """
    fig, ax = plt.subplots(figsize=(11, 5.2))

    cols = {
        "Physical drivers\n(+2.0 °C, 2050)": (
            ["NE/N heat &\nheat-stress days", "Amazon degradation\n& drought",
             "Extreme rainfall\n& floods"], "#d73027", 1.2),
        "Intermediate\nstressors": (
            ["Crop-yield loss\n(soy/maize, safrinha)", "Water stress\n(rural & urban)",
             "Housing destroyed\n(favela/floodplain)"], "#fdae61", 4.4),
        "Migration\nresponse": (
            ["Semi-arid → SE/S\ncities (largest)", "Amazon/N → regional\nhubs",
             "Intra-urban\ndisplacement"], "#4575b4", 7.6),
        "Feedbacks &\nrisks": (
            ["Urban capacity strain\n(compounding hazard)",
             "Land/water conflict", "Trapped populations\n(cannot move)"],
            "#7b3294", 10.6),
    }

    for header, (items, color, x) in cols.items():
        ax.text(x, 5.3, header, ha="center", va="center", fontsize=10.5,
                fontweight="bold", color=color)
        for i, it in enumerate(items):
            yy = 4.1 - i * 1.35
            ax.add_patch(Rectangle((x - 1.15, yy - 0.5), 2.3, 1.0,
                                   facecolor=color, alpha=0.18,
                                   edgecolor=color, lw=1.4))
            ax.text(x, yy, it, ha="center", va="center", fontsize=8.2)

    # Arrows between column bands.
    for x in (2.55, 5.75, 8.95):
        ax.add_patch(FancyArrowPatch((x, 2.7), (x + 0.7, 2.7),
                                     arrowstyle="-|>", mutation_scale=20,
                                     lw=2, color="#888"))

    ax.set_xlim(-0.4, 12.0)
    ax.set_ylim(0.5, 5.8)
    ax.axis("off")
    ax.set_title("How +2 °C becomes migration in Brazil: the causal chain",
                 fontsize=13)
    fig.text(0.99, 0.01,
             "Schematic of the document's argued mechanism (Principle 6: make "
             "the logic explicit). 2026-07-11.",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(OUT / "fig4_driver_chain.png")
    plt.close(fig)


def main():
    """Created by JXP and Claude.

    Generate all Brazil migration figures.

    Inputs
    ------
    (none)

    Outputs
    -------
    None. Writes fig1–fig4 PNGs into CI_Predictions/.
    """
    fig1_regions_and_trajectory()
    fig2_corridors()
    fig3_ledger()
    fig4_drivers()
    print("Wrote fig1_brazil_population.png, fig2_migration_corridors.png, "
          "fig3_prediction_ledger.png, fig4_driver_chain.png")


if __name__ == "__main__":
    main()
