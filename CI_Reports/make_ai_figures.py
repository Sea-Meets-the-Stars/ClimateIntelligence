"""Created by JXP and Claude.

Generate the AI figures (13-14) for the Climate Intelligence report
(CI_2026_07_09_climate_report.md, section 9 on AI's data-center energy and
water surge).

Unlike the population figures, no machine-readable annual series is published
with these reports — the annual curves live only in chart form (LBNL 2024
Figure ES-1; LBNL 2025 Figure 1). To stay honest, these figures therefore plot
ONLY values stated in the report text (each with a page-cited constant below),
drawn as anchor markers joined by straight guide lines, with projections shown
as the ranges the reports actually give. Nothing between anchors is estimated
or smoothed by us, and the provenance footers say so.

Data sources (references [42]-[45] in the report):
  - LBNL 2024: Shehabi et al., "2024 United States Data Center Energy Usage
    Report", LBNL-2001637, Dec 2024 (context/Reports/
    LBNL_2024_US_Data_Center_Energy_Usage_Report.pdf)
  - LBNL 2025: Smith et al., "United States Data Center Energy Usage Report:
    2025 Update", LBNL-2001758, Jun 2026 (context/Reports/
    LBNL_2025_US_Data_Center_Energy_Usage_Update.pdf)
  Page numbers in the constants below are the reports' own pagination.

Run under the project conda environment:
    conda run -n ocean14 python CI_Reports/make_ai_figures.py

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

HERE = Path(__file__).resolve().parent

# Same visual style as make_figures.py, for a consistent report.
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
# Electricity — every value below is stated in the report text.
# ---------------------------------------------------------------------------
# Historical anchors: (year, TWh, share of U.S. electricity or None).
# LBNL 2024 pp. 5-6: "stable between 2014-2016 at about 60 TWh"; "by 2018 data
# centers consumed about 76 TWh, representing 1.9%"; "reaching 176 TWh by
# 2023, representing 4.4%". LBNL 2025 p. 8: 2024 = 192 TWh = 4.7% (revised
# series; prior years revised slightly DOWN vs the 2024 report).
TOTAL_ANCHORS = [
    (2014, 60.0, None),
    (2016, 60.0, None),
    (2018, 76.0, "1.9%"),
    (2023, 176.0, "4.4%"),
    (2024, 192.0, "4.7%"),
]
# Projections. LBNL 2024 p. 6: 325-580 TWh in 2028 (6.7-12.0%).
RANGE_2028_LBNL2024 = (325.0, 580.0)
# LBNL 2025 pp. 8-10: Reference Case 464 TWh (2028) and 649 TWh = 11.8%
# (2030); Compounded Uncertainty Range 521-843 TWh = 9.5-15.3% (2030);
# named scenarios (Table 2): Consolidated Deployment 578, Low Accelerator
# Lifetime 590, High ASIC 664, High Inference Energy 782.
REF_2028, REF_2030 = 464.0, 649.0
RANGE_2030 = (521.0, 843.0)
SCENARIOS_2030 = [578.0, 590.0, 664.0, 782.0]
# AI-server electricity, LBNL 2024 p. 20: "<2 TWh in 2017 to >40 TWh in 2023".
# LBNL 2025 pp. 18-19: AI servers ~55% of ALL data-center electricity by 2030.
AI_ANCHORS = [(2017, 2.0), (2023, 40.0)]
AI_SHARE_2030 = 0.55  # of the Reference Case total (derived point, labeled)

# ---------------------------------------------------------------------------
# Water and efficiency — all from LBNL 2024 (the 2025 Update has no water).
# ---------------------------------------------------------------------------
# p. 55: direct on-site cooling water 21.2 billion L (2014), 66 billion L
# (2023, 84% hyperscale+colocation). p. 57: indirect water evaporated at the
# power plants supplying the electricity ~800 billion L (2023).
DIRECT_2014_BL, DIRECT_2023_BL, INDIRECT_2023_BL = 21.2, 66.0, 800.0
# p. 47: national average PUE 1.6 (2014) -> 1.4 (2023); 1.15-1.35 by 2028.
PUE_ANCHORS = [(2014, 1.6), (2023, 1.4)]
PUE_2028 = (1.15, 1.35)
# pp. 47-48: national average site WUE "just over 0.36 L/kWh through 2023",
# rising to 0.45-0.48 L/kWh by 2028.
WUE_ANCHORS = [(2014, 0.36), (2023, 0.36)]
WUE_2028 = (0.45, 0.48)
# Aggregate 2023 medians by space type, read from LBNL 2024 Figure 4.5 by the
# reader agents (hyperscale WUE 0.32 also stated in text, p. 46): the most
# energy-efficient facilities are among the thirstiest.
SPACE_TYPES = [  # (label, PUE, site WUE L/kWh, color)
    ("AI-specialized", 1.14, 0.61, "#c0392b"),
    ("Hyperscale", 1.25, 0.32, "#1f5fa6"),
]

# Report palette (same fixed assignments as figs 1-12; never cycled).
BLUE, RED, GRAY = "#1f5fa6", "#c0392b", "#666666"


def fig13_datacenter_electricity():
    """Created by JXP and Claude.

    Figure 13: U.S. data-center electricity use, 2014-2030 — the stated
    historical anchors (flat ~60 TWh through 2016, then a sharp rise to
    192 TWh in 2024), the AI-server subseries driving it, and the projection
    ranges from both LBNL reports, drawn as ranges rather than points.

    Inputs
    ------
    (none) uses the page-cited constants above.

    Outputs
    -------
    None. Saves fig13_us_datacenter_electricity.png.
    """
    fig, ax = plt.subplots(figsize=(9, 5.6))

    # Historical total: stated anchors joined by a guide line.
    yr = np.array([a[0] for a in TOTAL_ANCHORS], dtype=float)
    twh = np.array([a[1] for a in TOTAL_ANCHORS])
    ax.plot(yr, twh, "-o", color=BLUE, lw=2, ms=6,
            label="Total (stated values, LBNL 2024/2025)")
    # Percent-of-U.S.-electricity labels at the anchors that state one; the
    # 2023/2024 pair shares one two-line label in the clear zone up-left of
    # the points (everything nearer collides with the AI-server annotations).
    ax.annotate("76 TWh = 1.9%", (2018, 76), xytext=(2014.6, 104),
                fontsize=8.5, color=BLUE)
    ax.annotate("2023: 176 TWh (4.4%)\n2024: 192 TWh (4.7%)", (2024, 192),
                xytext=(2018.9, 215), fontsize=8.5, color=BLUE,
                arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.8,
                                alpha=0.4))
    ax.annotate("flat ~60 TWh since ~2010:\nefficiency offset growth",
                (2015, 60), xytext=(2013.6, 118), fontsize=8.5, color=GRAY,
                arrowprops=dict(arrowstyle="-", color="#999", lw=0.8))

    # LBNL 2025 Reference Case: dashed continuation 2024 -> 2028 -> 2030.
    ax.plot([2024, 2028, 2030], [192, REF_2028, REF_2030], "--", color=BLUE,
            lw=1.8, label="LBNL 2025 Reference Case")
    ax.plot([2028, 2030], [REF_2028, REF_2030], "o", color=BLUE, ms=6,
            mfc="white")
    ax.annotate(f"{REF_2030:.0f} TWh = 11.8%", (2030, REF_2030),
                xytext=(2026.9, REF_2030 + 60), fontsize=8.5, color=BLUE)

    # Projection ranges as vertical bars (the honest way to quote them).
    ax.errorbar(2027.8, np.mean(RANGE_2028_LBNL2024),
                yerr=[[np.mean(RANGE_2028_LBNL2024) - RANGE_2028_LBNL2024[0]],
                      [RANGE_2028_LBNL2024[1] - np.mean(RANGE_2028_LBNL2024)]],
                fmt="none", ecolor="#8aa8cc", elinewidth=5, capsize=4, alpha=0.9)
    ax.annotate("2028 range\n(LBNL 2024):\n325–580 TWh\n= 6.7–12.0%",
                (2027.7, 560), fontsize=8, color="#5f7ea6", ha="right",
                va="center")
    ax.errorbar(2030.25, np.mean(RANGE_2030),
                yerr=[[np.mean(RANGE_2030) - RANGE_2030[0]],
                      [RANGE_2030[1] - np.mean(RANGE_2030)]],
                fmt="none", ecolor=BLUE, elinewidth=5, capsize=4, alpha=0.85)
    ax.annotate("2030 stress-tested\nrange: 521–843 TWh\n= 9.5–15.3%",
                (2030.55, 780), fontsize=8, color=BLUE, ha="left",
                va="center", annotation_clip=False)
    # Named 2030 scenarios as small dots; call out the biggest swing factor.
    ax.plot([2030] * len(SCENARIOS_2030), SCENARIOS_2030, "o", ms=3.5,
            color=GRAY, alpha=0.8, zorder=4)
    ax.annotate("High-Inference scenario (782):\nthe single largest unknown",
                (2030, 782), xytext=(2023.9, 830), fontsize=8, color=GRAY,
                arrowprops=dict(arrowstyle="-", color="#999", lw=0.8))

    # AI-server subseries: the driver. Stated anchors + derived 2030 point.
    ai_yr = [a[0] for a in AI_ANCHORS]
    ai_twh = [a[1] for a in AI_ANCHORS]
    ax.plot(ai_yr, ai_twh, "-s", color=RED, lw=2, ms=6,
            label="AI servers (stated values)")
    ai_2030 = AI_SHARE_2030 * REF_2030  # ~55% of the Reference Case total
    ax.plot([2023, 2030], [40, ai_2030], "--", color=RED, lw=1.6)
    ax.plot(2030, ai_2030, "s", color=RED, ms=6, mfc="white")
    ax.annotate("AI servers <2 TWh (2017)\n→ >40 TWh (2023)", (2023, 40),
                xytext=(2018.7, 55), fontsize=8.5, color=RED,
                arrowprops=dict(arrowstyle="-", color=RED, lw=0.8, alpha=0.5))
    ax.annotate(f"≈55% of all data-center\nelectricity by 2030 (~{ai_2030:.0f} TWh)",
                (2030, ai_2030), xytext=(2030.55, ai_2030 - 40), fontsize=8,
                color=RED, annotation_clip=False)

    ax.set_xlim(2013.5, 2030.5)
    ax.set_ylim(0, 900)
    ax.set_xlabel("Year")
    ax.set_ylabel("Electricity use (TWh per year)")
    ax.set_title("U.S. data-center electricity: the flat decade ended in 2017")
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    fig.text(0.99, 0.01,
             "Values as stated in LBNL 2024 (pp. 5–6, 20) and LBNL 2025 Update (pp. 8–10, Table 2); lines join stated anchors only\n"
             "— annual estimates are in the reports' Fig. ES-1/Fig. 1. 2030 AI-server point derived as 55% × Reference Case.",
             ha="right", va="bottom", fontsize=6.5, color="#555")
    fig.tight_layout(rect=(0, 0.04, 0.97, 1))
    fig.savefig(HERE / "fig13_us_datacenter_electricity.png")
    plt.close(fig)


def fig14_datacenter_water():
    """Created by JXP and Claude.

    Figure 14: the data-center water story, three panels. (a) Where the water
    actually is: direct on-site cooling vs the ~12x larger indirect draw at
    the power plants. (b) Energy efficiency (PUE) improving while (c) water
    intensity (site WUE) worsens — the trade-off LBNL says cannot be
    minimized on both sides at once, with the AI-specialized vs hyperscale
    contrast marked.

    Inputs
    ------
    (none) uses the page-cited constants above.

    Outputs
    -------
    None. Saves fig14_datacenter_water.png.
    """
    fig = plt.figure(figsize=(9.5, 5.6))
    gs = fig.add_gridspec(2, 2, width_ratios=(1.15, 1), hspace=0.42,
                          wspace=0.32)
    ax_a = fig.add_subplot(gs[:, 0])
    ax_b = fig.add_subplot(gs[0, 1])
    ax_c = fig.add_subplot(gs[1, 1])

    # --- (a) Direct vs indirect water, horizontal bars (identity by label,
    # not color alone; sequential blues = same measure, different magnitude).
    bars = [
        ("Direct, on-site\ncooling (2014)", DIRECT_2014_BL, "#a8c4e0"),
        ("Direct, on-site\ncooling (2023)", DIRECT_2023_BL, "#5f8fc0"),
        ("Indirect, at power\nplants (2023)", INDIRECT_2023_BL, "#1f5fa6"),
    ]
    ypos = np.arange(len(bars))[::-1]
    ax_a.barh(ypos, [b[1] for b in bars], color=[b[2] for b in bars],
              height=0.62)
    ax_a.set_yticks(ypos)
    ax_a.set_yticklabels([b[0] for b in bars], fontsize=9)
    for y, (_, val, _) in zip(ypos, bars):
        ax_a.annotate(f"{val:g} B liters", (val + 12, y), va="center",
                      fontsize=9, color="#333")
    ax_a.annotate("≈12× the on-site use —\nevaporated generating\nthe electricity",
                  (INDIRECT_2023_BL * 0.55, ypos[-1] + 0.55), fontsize=8.5,
                  color="#1f5fa6", ha="center")
    ax_a.set_xlim(0, 1000)
    ax_a.set_xlabel("Water consumed (billion liters per year)")
    ax_a.set_title("(a) The water is mostly upstream", fontsize=10.5)
    ax_a.grid(axis="y", visible=False)

    # --- (b) PUE falling (energy efficiency improving)...
    ax_b.plot(*zip(*PUE_ANCHORS), "-o", color="#16a085", lw=2, ms=5)
    ax_b.errorbar(2028, np.mean(PUE_2028),
                  yerr=[[np.mean(PUE_2028) - PUE_2028[0]],
                        [PUE_2028[1] - np.mean(PUE_2028)]],
                  fmt="none", ecolor="#16a085", elinewidth=4, capsize=3,
                  alpha=0.8)
    ax_b.annotate("1.6", (2014, 1.6), xytext=(2014.3, 1.56), fontsize=8.5,
                  color="#16a085")
    ax_b.annotate("1.4", (2023, 1.4), xytext=(2021.2, 1.44), fontsize=8.5,
                  color="#16a085")
    ax_b.annotate("1.15–1.35\nby 2028", (2028, 1.25), xytext=(2024.0, 1.16),
                  fontsize=8, color="#16a085")
    ax_b.set_ylim(1.0, 1.75)
    ax_b.set_xlim(2013, 2029)
    ax_b.set_ylabel("PUE")
    ax_b.set_title("(b) Energy efficiency: improving ↓", fontsize=10.5)

    # --- (c) ...while site WUE rises (water intensity worsening), with the
    # space-type contrast: the greenest buildings are the thirstiest.
    ax_c.plot(*zip(*WUE_ANCHORS), "-o", color=BLUE, lw=2, ms=5)
    ax_c.errorbar(2028, np.mean(WUE_2028),
                  yerr=[[np.mean(WUE_2028) - WUE_2028[0]],
                        [WUE_2028[1] - np.mean(WUE_2028)]],
                  fmt="none", ecolor=BLUE, elinewidth=4, capsize=3, alpha=0.8)
    ax_c.annotate("~0.36 national avg.", (2018.5, 0.36),
                  xytext=(2013.6, 0.27), fontsize=8, color=BLUE)
    ax_c.annotate("0.45–0.48\nby 2028", (2028, 0.465), xytext=(2026.1, 0.55),
                  fontsize=8, color=BLUE, ha="center")
    for label, _, wue, color in SPACE_TYPES:
        ax_c.plot(2023, wue, "D", ms=5, color=color)
        # Hand-placed so neither label hits the average line or 2028 text.
        if label == "AI-specialized":
            ax_c.annotate(f"{label} {wue:.2f}", (2023, wue + 0.05),
                          fontsize=8, color=color, ha="center")
        else:
            ax_c.annotate(f"{label} {wue:.2f}", xy=(2023, wue),
                          xytext=(2022.4, 0.17), fontsize=8, color=color,
                          ha="right",
                          arrowprops=dict(arrowstyle="-", color=color,
                                          lw=0.7, alpha=0.5))
    ax_c.set_ylim(0, 0.75)
    ax_c.set_xlim(2013, 2029)
    ax_c.set_ylabel("Site WUE (L/kWh)")
    ax_c.set_xlabel("Year")
    ax_c.set_title("(c) Water intensity: rising ↑", fontsize=10.5)

    fig.suptitle("Data-center water: upstream volumes and the energy–water trade-off",
                 fontsize=12, y=0.99)
    fig.text(0.99, 0.005,
             "LBNL 2024 (pp. 45–48, 55–57); the 2025 Update contains no water data. Panels (b)/(c): national averages; 2028 = projected range.\n"
             "Space-type medians read from LBNL 2024 Fig. 4.5 (hyperscale WUE also stated on p. 46).",
             ha="right", va="bottom", fontsize=6.5, color="#555")
    fig.subplots_adjust(left=0.155, right=0.985, top=0.86, bottom=0.16)
    fig.savefig(HERE / "fig14_datacenter_water.png")
    plt.close(fig)


def main():
    """Created by JXP and Claude.

    Generate all AI figures for the report.

    Inputs
    ------
    (none)

    Outputs
    -------
    None. Writes fig13-fig14 PNGs next to this script.
    """
    fig13_datacenter_electricity()
    fig14_datacenter_water()
    print("Wrote fig13_us_datacenter_electricity.png, "
          "fig14_datacenter_water.png")


if __name__ == "__main__":
    main()
