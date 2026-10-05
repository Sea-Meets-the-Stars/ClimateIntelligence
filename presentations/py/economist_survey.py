"""Created by JXP and Claude.

C10 "Most economists believe technology will save us" — the approved
two-column panel (Q29b, Q41): "Alarmed — and still betting on technology."

Data: Howard & Sylvan 2021, "Gauging Economic Consensus on Climate Change",
Institute for Policy Integrity, NYU School of Law (survey of authors of
climate-economics articles in leading journals; 2,169 invited, 738 responded):
  https://policyintegrity.org/files/publications/Economic_Consensus_on_Climate.pdf
Numbers verified against the report text (extracted 2026-10-04):
  74%  "immediate and drastic action is necessary" (50% in the 2015 survey)
  76%  climate change likely/very likely to reduce global economic GROWTH RATES
  65%  solar/wind-style cost declines likely/very likely to repeat for other
       zero- and negative-emission technologies
  >50% of the global energy mix zero-emission by 2050 (vs ~10% today)

Usage:
    conda run -n ocean14 python presentations/py/economist_survey.py
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from slide_style import FULL, apply_style, save, RED, BLUE, INK, MUTED

ALARMED = [("74%", "say “immediate and\ndrastic action is\nnecessary”"),
           ("76%", "expect climate change\nto cut long-run\neconomic growth")]
BETTING = [("65%", "expect solar-style\ncost collapses to repeat\nfor other clean tech"),
           (">50%", "expect zero-emission\nenergy to be the majority\nby 2050 (~10% today)")]


def column(fig, x0, heading, items, color):
    """Created by JXP and Claude. Draw one column of big-number callouts.
    Inputs: fig, x0 (figure fraction), heading, items [(number, text)], color."""
    fig.patches.append(FancyBboxPatch((x0, 0.16), 0.46, 0.80, boxstyle="round,pad=0.0,rounding_size=0.02",
                                      transform=fig.transFigure, facecolor=color, alpha=0.08,
                                      edgecolor="none"))
    fig.text(x0 + 0.23, 0.88, heading, ha="center", va="center", fontsize=19,
             fontweight="bold", color=color)
    for i, (num, text) in enumerate(items):
        y = 0.63 - i * 0.30
        fig.text(x0 + 0.03, y, num, ha="left", va="center", fontsize=34,
                 fontweight="bold", color=color)
        fig.text(x0 + 0.205, y, text, ha="left", va="center", fontsize=13, color=INK)


def main():
    """Created by JXP and Claude. Build c10_economist_survey.png."""
    apply_style()
    fig = plt.figure(figsize=FULL)
    column(fig, 0.02, "Alarmed…", ALARMED, RED)
    column(fig, 0.52, "…and still betting on technology", BETTING, BLUE)
    save(fig, "c10_economist_survey.png",
         "Data: Howard & Sylvan 2021, Gauging Economic Consensus on Climate Change, Institute for Policy "
         "Integrity (NYU Law); 738 climate economists responded",
         "C10")


if __name__ == "__main__":
    main()
