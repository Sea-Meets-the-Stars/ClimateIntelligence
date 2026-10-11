"""Created by JXP and Claude.

Slide 3 (B9b) "Climate Intelligence" — concept schematic:
  - hub: the blog (written by the author) and the podcast (with a Gen-Z
    interviewer), "and more";
  - spokes: YouTube, TikTok, Instagram (one spoke each);
  - inputs from the outside world: new data on climate and on AI.
Platform names are plain text labels (no logos).

Usage:
    conda run -n ocean14 python presentations/py/ci_schematic.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

from slide_style import FULL, apply_style, save, BLUE, RED, TEAL, PURPLE, ORANGE, GREEN, INK, MUTED

HUB = (5.4, 2.0)
R = 1.75
SPOKES = [("YouTube", RED, 35), ("TikTok", INK, 0), ("Instagram", PURPLE, -35)]
INPUTS = [("New climate data", "CO₂, ocean heat, sea level,\nbiodiversity…", TEAL, 3.3),
          ("New AI developments", "models, compute, papers,\npolicy…", ORANGE, 0.7)]


def arrow(ax, a, b, color, lw=3):
    """Created by JXP and Claude. Thick arrow from point a to point b."""
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=22, lw=lw, color=color,
                                 shrinkA=0, shrinkB=0))


def main():
    """Created by JXP and Claude. Build s3_ci_concept.png."""
    apply_style()
    fig, ax = plt.subplots(figsize=FULL)
    ax.set_xlim(0, 10.4)
    ax.set_ylim(-0.2, 4.2)
    ax.set_aspect("equal")
    ax.axis("off")

    # Hub: Climate Intelligence = blog + podcast (and more).
    ax.add_patch(Circle(HUB, R, facecolor=BLUE, alpha=0.12, edgecolor=BLUE, lw=2.5))
    ax.text(HUB[0], HUB[1] + 1.2, "Climate\nIntelligence", ha="center", va="center", fontsize=15,
            fontweight="bold", color=BLUE, linespacing=1.0)
    for dy, head, sub in ((0.3, "Blog", "written by Xavier"),
                          (-0.6, "Podcast", "with a Gen-Z interviewer")):
        ax.add_patch(FancyBboxPatch((HUB[0] - 1.25, HUB[1] + dy - 0.38), 2.5, 0.76,
                                    boxstyle="round,pad=0.02,rounding_size=0.12", facecolor="white",
                                    edgecolor=BLUE, lw=1.5))
        ax.text(HUB[0], HUB[1] + dy + 0.12, head, ha="center", va="center", fontsize=15, fontweight="bold", color=INK)
        ax.text(HUB[0], HUB[1] + dy - 0.19, sub, ha="center", va="center", fontsize=11, color=MUTED)
    ax.text(HUB[0], HUB[1] - 1.38, "…and more", ha="center", fontsize=12, color=MUTED, style="italic")

    # Spokes out to the platforms.
    for name, color, ang in SPOKES:
        a = np.radians(ang)
        start = (HUB[0] + (R + 0.05) * np.cos(a), HUB[1] + (R + 0.05) * np.sin(a))
        end = (HUB[0] + 2.75 * np.cos(a), HUB[1] + 2.75 * np.sin(a))
        arrow(ax, start, end, color)
        ax.add_patch(FancyBboxPatch((end[0] + 0.05, end[1] - 0.3), 2.0, 0.6,
                                    boxstyle="round,pad=0.02,rounding_size=0.15", facecolor=color,
                                    alpha=0.9, edgecolor="none"))
        ax.text(end[0] + 1.05, end[1], name, ha="center", va="center", fontsize=16,
                fontweight="bold", color="white")

    # Inputs from the outside world.
    for head, sub, color, y in INPUTS:
        ax.add_patch(FancyBboxPatch((0.05, y - 0.45), 2.75, 0.9, boxstyle="round,pad=0.02,rounding_size=0.12",
                                    facecolor=color, alpha=0.12, edgecolor=color, lw=1.5))
        ax.text(1.42, y + 0.18, head, ha="center", va="center", fontsize=14, fontweight="bold", color=color)
        ax.text(1.42, y - 0.2, sub, ha="center", va="center", fontsize=10.5, color=INK)
        a = np.radians(150 if y > HUB[1] else 210)
        arrow(ax, (2.85, y), (HUB[0] + (R + 0.05) * np.cos(a), HUB[1] + (R + 0.05) * np.sin(a)), color, lw=2.5)
    save(fig, "s3_ci_concept.png", "Concept schematic", "3")


if __name__ == "__main__":
    main()
