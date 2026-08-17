"""Created by JXP and Claude.

Generate the essential-labor-hours figures (20-22) that accompany
CI_Reports/work_hours_needed_report.md. Every plotted quantity that the model
still contains is IMPORTED from CI_Reports/work_hours_needed.py and recomputed at
plot time, so the figures track the model rather than a frozen transcription of
it. The only hardcoded numbers are Figure 22's four round-1-to-round-2 step
deltas, which are a historical record the current script no longer holds.

Figures:
  20. Category breakdown, CENTRAL scenario: the nine TRADITIONAL lines and the
      seven NON-TRADITIONAL lines in hours/week per working adult, with the
      Tier-1 elder labor contribution shown as a negative (burden-reducing) bar
      and a side panel making the ~3x non-traditional/traditional gap explicit.
  21. LOW / CENTRAL / HIGH range on the headline totals — TRADITIONAL,
      NON-TRADITIONAL and TOTAL hours/week per working adult, with CENTRAL
      marked and labeled inside each span.
  22. Waterfall reconciling the two calculation rounds at CENTRAL: how the
      headline TOTAL moved from the round-1 46.0 hr/wk to the final model
      value, step by named revision.

Data source (all panels):
  - CI_Reports/work_hours_needed.py -- the normative, non-monetary sufficiency
    model (see its module docstring for the life cycle, the LOW/CENTRAL/HIGH
    parameterization, FLAGS 1-6 and full source citations). Figures 20 and 21
    call population_breakdown() / compute_all() / hours_per_working_adult()
    directly; Figure 22 takes its END value from compute_all() too.

Run under the project conda environment:
    conda run -n ocean14 python CI_Reports/make_work_figures.py

Design follows the project coding guidelines: functions (no classes), imports at
top, inline comments, matplotlib, docstrings, "Created by JXP and Claude".
Visual style matches CI_Reports/make_homelessness_figures.py.
"""

# Imports at the top of the file (project coding guideline).
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")  # headless backend; we save PNGs, never display
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# The calculation script lives in this same directory, so a plain module import
# works.  It is guarded by `if __name__ == "__main__": main()`, so importing it
# does NOT trigger its own printout (verified).
from work_hours_needed import (
    ELDER_CONTRIB_LINE,
    SCENARIOS,
    compute_all,
    hours_per_working_adult,
    population_breakdown,
)

HERE = Path(__file__).resolve().parent

plt.rcParams.update({
    "figure.dpi": 130,
    "savefig.dpi": 130,
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# Project accent colors (shared with make_figures.py / make_ai_figures.py /
# make_population_figures.py): blue for traditional/reductions, red for the
# non-traditional headline, teal for the elder contribution, gray for totals.
BLUE, RED, TEAL, GRAY = "#1f5fa6", "#c0392b", "#16a085", "#666666"
DARK = "#333333"

# Two color families, so the bucket a bar belongs to is readable without the
# axis labels: traditional in blues, non-traditional in reds.
TRAD_CMAP = LinearSegmentedColormap.from_list("trad", ["#a8c4e0", BLUE, "#12365f"])
NONTRAD_CMAP = LinearSegmentedColormap.from_list("nontrad", ["#e8a49b", RED, "#7d1f14"])

# ----------------------------------------------------------------------------
# FIGURE 22 HISTORICAL CONSTANTS -- NOT LIVE-COMPUTED.
#
# These are a FIXED HISTORICAL RECORD of how the CENTRAL headline TOTAL moved
# between the first calculation round and the final model.  They cannot be
# pulled from work_hours_needed.py, because that script only ever reflects its
# FINAL state: the round-1 placeholders (ATUS secondary childcare, the ILO
# global-garment-workforce clothing allocation, the ATUS household-task
# benchmark) no longer exist in it, and neither does the round-1 medical-care
# classification.  They are narrative numbers from the revision process, so they
# are hardcoded here and clearly labeled as such.  Only the START and the four
# DELTAS are hardcoded; the END bar uses the live compute_all() value.
# ----------------------------------------------------------------------------
ROUND1_TOTAL_PWA = 46.0   # hr/wk per working adult, CENTRAL, first calculation

# (label, delta hr/wk, one-line reason) in the order the revisions happened.
REVISION_STEPS = (
    ("Childcare\nneeds-based", -12.56,
     "ATUS secondary childcare -> CFOC ratios x waking hours"),
    ("Clothing\nsufficiency wardrobe", -3.14,
     "ILO garment-workforce allocation -> 103-item, 4.1-yr wardrobe"),
    ("Household tasks\nneeds-based", +1.96,
     "ATUS benchmark -> USDA TFP prep time + ISSA cleaning standards"),
    ("Medical care\nreclassified", +0.00,
     "moved non-traditional -> traditional; bucket only, total unchanged"),
)

# Short display labels for the model's category keys.  Keyed on the live dict
# keys so a renamed category shows up as an obvious miss rather than silently
# plotting the wrong bar; unknown keys fall back to their model name.
SHORT_LABELS = {
    # Traditional
    "Shelter (build+materials+maint)": "Shelter",
    "Food (farm+process+distribute)": "Food",
    "Clothing (sufficiency wardrobe, embodied)": "Clothing",
    "Furniture (import-adjusted)": "Furniture",
    "Water / sanitation": "Water / sanitation",
    "Electricity": "Electricity",
    "Freight (essential goods only)": "Freight (essential)",
    "K-12 education (all staff)": "K-12 education",
    "Essential medical care": "Essential medical care",
    # Non-traditional
    "Childcare (non-school, needs-based)": "Childcare (non-school)",
    "Household tasks (needs-based)": "Household tasks",
    "Tier-1 elder light support (60-69)": "Tier-1 eldercare (60-69)",
    "Tier-2 elder support (70-74)": "Tier-2 eldercare (70-74)",
    "Tier-3 institutional care (75-79)": "Tier-3 eldercare (75-79)",
    "Disabled-adult care (25-59)": "Disabled-adult care",
    ELDER_CONTRIB_LINE: "LESS: elder labor contributed",
}


def short_label(key):
    """Created by JXP and Claude.

    Map a model category key to a compact axis label.

    Inputs
    ------
    key : str
        Category name as it appears in a 'trad_detail' / 'nontrad_detail' dict.

    Outputs
    -------
    str
        Short display label, or the key itself if it is not in SHORT_LABELS.
    """
    return SHORT_LABELS.get(key, key)


def category_hours(detail, pops):
    """Created by JXP and Claude.

    Convert one scenario's category detail dict from national weekly hours to
    hours per week per working adult.

    Inputs
    ------
    detail : dict
        Category name -> national hours/week (a 'trad_detail' or
        'nontrad_detail' entry from compute_all()).
    pops : dict
        Output of population_breakdown().

    Outputs
    -------
    list[tuple[str, float]]
        (category name, hours/week per working adult), in the dict's own order.
    """
    return [(cat, hours_per_working_adult(val, pops)) for cat, val in detail.items()]


def fig20_categories():
    """Created by JXP and Claude.

    Figure 20: CENTRAL-scenario category breakdown, traditional vs
    non-traditional, in hours/week per working adult.

    Left panel: every category as a horizontal bar, non-traditional (reds) above
    traditional (blues), separated by a rule, with the Tier-1 elder labor
    contribution drawn as a negative teal bar so it reads as a reduction rather
    than a demand line. Right panel: the two bucket subtotals side by side, which
    is what makes the ~3x gap immediate.

    Inputs
    ------
    (none) imports population_breakdown() / compute_all() /
    hours_per_working_adult() from work_hours_needed.

    Outputs
    -------
    None. Saves fig20_work_hours_categories.png.
    """
    pops = population_breakdown()
    central = compute_all(pops)["CENTRAL"]

    trad = category_hours(central["trad_detail"], pops)
    nontrad = category_hours(central["nontrad_detail"], pops)

    # Sort each bucket by magnitude so the bars read as a ranking.  The elder
    # contribution is negative, so it naturally lands at the bottom of its group.
    trad = sorted(trad, key=lambda kv: kv[1])
    nontrad = sorted(nontrad, key=lambda kv: kv[1])

    trad_total = hours_per_working_adult(central["trad_national"], pops)
    nontrad_total = hours_per_working_adult(central["nontrad_national"], pops)

    # y positions: traditional at the bottom, then a one-slot gap, then
    # non-traditional, so the highest non-traditional bar sits at the top.
    GAP = 1.0
    y_trad = np.arange(len(trad), dtype=float)
    y_nontrad = np.arange(len(nontrad), dtype=float) + len(trad) + GAP

    fig, (ax, ax_b) = plt.subplots(
        1, 2, figsize=(12.4, 7.4), gridspec_kw={"width_ratios": [3.1, 1.0]})

    # --- Left panel: every category ----------------------------------------
    # Shade within each family by rank, darkest for the largest line.
    trad_colors = TRAD_CMAP(np.linspace(0.15, 0.95, len(trad)))
    ax.barh(y_trad, [v for _, v in trad], color=trad_colors, alpha=0.95,
            height=0.72)

    for y, (cat, val) in zip(y_nontrad, nontrad):
        if cat == ELDER_CONTRIB_LINE:
            # The offset: teal, hatched, and drawn to the left of zero so it
            # cannot be mistaken for a demand category.
            ax.barh(y, val, color=TEAL, alpha=0.9, height=0.72,
                    hatch="///", edgecolor="white", lw=0.8)
        else:
            # Rank-shade the positive demand lines only.
            demand = [v for c, v in nontrad if c != ELDER_CONTRIB_LINE]
            frac = 0.15 + 0.80 * (sorted(demand).index(val) / max(len(demand) - 1, 1))
            ax.barh(y, val, color=NONTRAD_CMAP(frac), alpha=0.95, height=0.72)

    # Value labels, pushed to whichever side of the bar has room.
    for y, (_, val) in zip(np.concatenate([y_trad, y_nontrad]), trad + nontrad):
        if val < 0:
            ax.text(val - 0.25, y, f"{val:.2f}", va="center", ha="right",
                    fontsize=8.5, color=TEAL, fontweight="bold")
        else:
            ax.text(val + 0.25, y, f"{val:.2f}", va="center", fontsize=8.5,
                    color="#444")

    ax.set_yticks(np.concatenate([y_trad, y_nontrad]))
    ax.set_yticklabels([short_label(c) for c, _ in trad + nontrad], fontsize=9)
    ax.axvline(0, color=DARK, lw=1.0)

    # Separator between the two buckets, plus a subtotal banner for each.  The
    # banners live in the empty space left of the zero line (only the elder
    # offset bar extends there, and it is several rows away from both).
    y_split = len(trad) - 1 + GAP / 2 + 0.14
    ax.axhline(y_split, color="#999", ls="--", lw=1.0)
    ax.text(-5.8, y_nontrad[-1],
            f"NON-TRADITIONAL\n(care + household)\nsubtotal {nontrad_total:.1f} hr/wk",
            fontsize=9.5, color=RED, fontweight="bold", ha="left", va="center")
    ax.text(-5.8, y_trad[-1],
            f"TRADITIONAL\n(goods, services, medicine)\nsubtotal {trad_total:.1f} hr/wk",
            fontsize=9.5, color=BLUE, fontweight="bold", ha="left", va="center")

    ax.set_xlim(-6.0, 14.0)
    ax.set_xlabel("Hours per week per healthy working-age adult (CENTRAL scenario)")
    ax.set_ylim(-0.8, y_nontrad[-1] + 1.4)
    ax.grid(axis="y", visible=False)
    ax.set_title("Where the essential hours go, category by category")

    # --- Right panel: the two subtotals, for the 3x headline ----------------
    ax_b.bar([0], [trad_total], width=0.62, color=BLUE, alpha=0.95)
    ax_b.bar([1], [nontrad_total], width=0.62, color=RED, alpha=0.95)
    for x, v in ((0, trad_total), (1, nontrad_total)):
        ax_b.text(x, v + 0.6, f"{v:.1f}", ha="center", fontsize=12,
                  fontweight="bold", color=DARK)
    # Annotate the ratio between them, computed rather than quoted.
    ratio = nontrad_total / trad_total
    ax_b.annotate("", xy=(1, nontrad_total), xytext=(1, trad_total),
                  arrowprops=dict(arrowstyle="<->", color=DARK, lw=1.2))
    ax_b.text(1.36, (trad_total + nontrad_total) / 2,
              f"{ratio:.1f}x", fontsize=15, fontweight="bold", color=DARK,
              ha="center", va="center", rotation=90)
    ax_b.set_xticks([0, 1])
    ax_b.set_xticklabels(["Traditional", "Non-\ntraditional"], fontsize=9.5)
    ax_b.set_xlim(-0.6, 1.8)
    ax_b.set_ylim(0, nontrad_total * 1.22)
    ax_b.set_ylabel("Hours per week per working adult")
    ax_b.grid(axis="x", visible=False)
    ax_b.set_title("Care work dominates", fontsize=10.5)

    fig.suptitle(
        "Essential labor: care and household work are the larger burden by ~3x\n"
        "hours/week per healthy working-age US adult, CENTRAL scenario "
        "(net of the Tier-1 elder contribution)",
        fontsize=12.5)
    fig.text(0.99, 0.005,
             "Source: CI_Reports/work_hours_needed.py (normative sufficiency "
             "model; medical care classified traditional per FLAG 1, elder "
             "contribution capped per FLAG 6).",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.025, 1, 0.93))
    fig.savefig(HERE / "fig20_work_hours_categories.png")
    plt.close(fig)


def fig21_range():
    """Created by JXP and Claude.

    Figure 21: the LOW / CENTRAL / HIGH span on the three headline totals
    (TRADITIONAL, NON-TRADITIONAL, TOTAL), hours/week per working adult.

    Each row is a floating range bar from LOW to HIGH with end caps, and a large
    marked point plus a bold label at CENTRAL, so the headline value stays
    prominent while the uncertainty stays honest.

    Inputs
    ------
    (none) imports population_breakdown() / compute_all() from
    work_hours_needed; uses trad_pwa, nontrad_pwa and total_pwa for all three
    scenario columns.

    Outputs
    -------
    None. Saves fig21_work_hours_range.png.
    """
    pops = population_breakdown()
    results = compute_all(pops)

    rows = (
        ("TRADITIONAL", "trad_pwa", BLUE),
        ("NON-TRADITIONAL", "nontrad_pwa", RED),
        ("TOTAL", "total_pwa", DARK),
    )
    # Plot top-down in the listed order, so TOTAL is the bottom (summary) row.
    y = np.arange(len(rows))[::-1].astype(float)

    fig, ax = plt.subplots(figsize=(10.2, 5.4))

    for yi, (label, key, color) in zip(y, rows):
        lo, mid, hi = (results[s][key] for s in SCENARIOS)
        # Floating span, LOW -> HIGH.
        ax.barh(yi, hi - lo, left=lo, height=0.40, color=color, alpha=0.22,
                edgecolor=color, lw=1.0, zorder=2)
        # End caps and their values.
        ax.plot([lo, lo], [yi - 0.20, yi + 0.20], color=color, lw=2.0, zorder=3)
        ax.plot([hi, hi], [yi - 0.20, yi + 0.20], color=color, lw=2.0, zorder=3)
        ax.text(lo - 0.9, yi, f"{lo:.1f}", ha="right", va="center", fontsize=9.5,
                color=color)
        ax.text(hi + 0.9, yi, f"{hi:.1f}", ha="left", va="center", fontsize=9.5,
                color=color)
        # CENTRAL: big marker plus a bold label above it.
        ax.plot(mid, yi, "o", ms=13, color=color, zorder=5,
                markeredgecolor="white", markeredgewidth=1.6)
        ax.text(mid, yi + 0.28, f"{mid:.1f}", ha="center", va="bottom",
                fontsize=13, fontweight="bold", color=color, zorder=6)

    # A 40-hour reference line: the total's CENTRAL sits well below it, but the
    # HIGH column runs past it, which is the point of showing the range.
    ax.axvline(40, color="#999", ls=":", lw=1.2, zorder=1)
    ax.text(40.4, y[0] + 0.52, "40 hr/wk", fontsize=8.5, color="#777",
            va="center")

    ax.set_yticks(y)
    ax.set_yticklabels([r[0] for r in rows], fontsize=11, fontweight="bold")
    ax.set_ylim(-0.75, len(rows) - 0.35)
    ax.set_xlim(0, 57)
    ax.set_xlabel("Hours per week per healthy working-age adult")
    ax.grid(axis="y", visible=False)
    ax.set_title(
        "How much of the week is essential labor? LOW - CENTRAL - HIGH\n"
        "filled span = LOW to HIGH scenario; dot and bold number = CENTRAL")
    ax.text(0.985, 0.06,
            "The columns are OUTCOME scenarios, not parameter columns: the\n"
            "LOW-burden column pairs low demand with the HIGH elder-labor\n"
            "contribution, and vice versa (FLAG 5, author-confirmed).",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=7.5,
            color="#444", bbox=dict(boxstyle="round", fc="#fff7e6",
                                    ec="#e0b050", lw=0.8))
    fig.text(0.99, 0.005,
             "Source: CI_Reports/work_hours_needed.py, compute_all() -- "
             "LOW/CENTRAL/HIGH propagated end-to-end.",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(HERE / "fig21_work_hours_range.png")
    plt.close(fig)


def fig22_revision():
    """Created by JXP and Claude.

    Figure 22: waterfall reconciling the two calculation rounds at CENTRAL --
    from the round-1 headline TOTAL of 46.0 hr/wk to the final model value.

    The START value and the four step deltas are the hardcoded historical
    constants ROUND1_TOTAL_PWA and REVISION_STEPS (the current script retains
    only its final state, so they cannot be recomputed); the END bar uses the
    live compute_all() CENTRAL total, so the endpoint is always exactly right.
    Any residual between the summed rounded deltas and that live endpoint is
    reported on the figure as a rounding note rather than absorbed into a step.

    Inputs
    ------
    (none) imports population_breakdown() / compute_all() from
    work_hours_needed for the END value.

    Outputs
    -------
    None. Saves fig22_work_hours_revision.png.
    """
    pops = population_breakdown()
    end_total = compute_all(pops)["CENTRAL"]["total_pwa"]

    labels = ["Round 1\n(first calculation)"]
    labels += [s[0] for s in REVISION_STEPS]
    labels += ["Final model\n(round 2 + FLAG 6)"]
    x = np.arange(len(labels), dtype=float)

    fig, ax = plt.subplots(figsize=(11.4, 6.2))

    # --- Anchor bars: full-height columns at the two endpoints --------------
    ax.bar(x[0], ROUND1_TOTAL_PWA, width=0.60, color=GRAY, alpha=0.95, zorder=3)
    ax.bar(x[-1], end_total, width=0.60, color=DARK, alpha=0.95, zorder=3)
    for xi, v in ((x[0], ROUND1_TOTAL_PWA), (x[-1], end_total)):
        ax.text(xi, v + 1.0, f"{v:.1f}", ha="center", fontsize=13,
                fontweight="bold", color=DARK, zorder=6)

    # --- Step bars: floating, from the running level to the new level -------
    running = ROUND1_TOTAL_PWA
    for xi, (label, delta, _reason) in zip(x[1:-1], REVISION_STEPS):
        new = running + delta
        if abs(delta) < 1e-9:
            # Zero-height step (the medical reclassification): draw a rule at
            # the running level so the reader sees a step happened, and say why
            # it moves nothing.  A bar of height 0 would be invisible.
            ax.plot([xi - 0.30, xi + 0.30], [running, running], color="#8e44ad",
                    lw=3.0, solid_capstyle="butt", zorder=4)
            ax.text(xi, running + 1.0, "+0.00", ha="center", fontsize=10,
                    fontweight="bold", color="#8e44ad", zorder=6)
            ax.annotate(
                "bucket only: essential medical care moved\n"
                "NON-TRADITIONAL -> TRADITIONAL (FLAG 1).\n"
                "The split changed; the total did not.",
                xy=(xi, running), xytext=(xi - 0.05, running + 12.5),
                fontsize=8, color="#8e44ad", ha="center", va="bottom",
                arrowprops=dict(arrowstyle="->", color="#8e44ad", lw=0.9),
                zorder=6)
        else:
            color = BLUE if delta < 0 else RED
            ax.bar(xi, abs(delta), bottom=min(running, new), width=0.60,
                   color=color, alpha=0.95, zorder=3)
            # Label above for increases, below for decreases, so the sign reads.
            if delta < 0:
                ax.text(xi, min(running, new) - 1.9, f"{delta:+.2f}",
                        ha="center", fontsize=10.5, fontweight="bold",
                        color=color, zorder=6)
            else:
                ax.text(xi, max(running, new) + 1.0, f"{delta:+.2f}",
                        ha="center", fontsize=10.5, fontweight="bold",
                        color=color, zorder=6)
        # Connector from this step's exit level into the next bar.
        ax.plot([xi - 0.30, xi + 0.62], [new, new], color="#aaa", lw=0.9,
                ls="--", zorder=2)
        running = new

    # Connector off the starting anchor.
    ax.plot([x[0] - 0.30, x[0] + 0.62], [ROUND1_TOTAL_PWA, ROUND1_TOTAL_PWA],
            color="#aaa", lw=0.9, ls="--", zorder=2)

    # --- Rounding reconciliation -------------------------------------------
    # Report, never absorb: the deltas are quoted to 2 dp, so their sum need not
    # land exactly on the live model total.
    residual = running - end_total
    recon = (f"Check: {ROUND1_TOTAL_PWA:.1f} "
             + " ".join(f"{d:+.2f}" for _, d, _ in REVISION_STEPS)
             + f" = {running:.2f}, vs the live model's {end_total:.2f} "
               f"({residual:+.3f} hr/wk from rounding the quoted deltas;\n"
               "the final bar uses the live compute_all() value, and no delta "
               "has been adjusted to force the sum).")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylim(0, ROUND1_TOTAL_PWA * 1.42)
    ax.set_ylabel("TOTAL hours per week per working adult (CENTRAL)")
    ax.grid(axis="x", visible=False)
    ax.set_title(
        "Two rounds of research cut the headline by ~30%: 46.0 -> "
        f"{end_total:.1f} hr/wk\n"
        "blue = revision reduced the estimate, red = increased it, "
        "purple = reclassification only")
    ax.text(0.5, 0.015, recon, transform=ax.transAxes, ha="center", va="bottom",
            fontsize=7.5, color="#444",
            bbox=dict(boxstyle="round", fc="#f4f4f4", ec="#bbb", lw=0.8))

    fig.text(0.99, 0.005,
             "Source: CI_Reports/work_hours_needed.py (END value, live). START "
             "and the four step deltas are hardcoded historical "
             "round-1-to-round-2 constants.",
             ha="right", va="bottom", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(HERE / "fig22_work_hours_revision.png")
    plt.close(fig)


def main():
    """Created by JXP and Claude.

    Generate all essential-labor-hours figures.

    Inputs
    ------
    (none)

    Outputs
    -------
    None. Writes fig20-fig22 PNGs beside this script.
    """
    fig20_categories()
    fig21_range()
    fig22_revision()
    print("Wrote fig20_work_hours_categories.png, fig21_work_hours_range.png, "
          "fig22_work_hours_revision.png")


if __name__ == "__main__":
    main()
