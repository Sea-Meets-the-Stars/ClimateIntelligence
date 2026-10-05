"""Created by JXP and Claude.

Non-data panels for the AI half of the WMKO 2026 talk:
  A3  a3_hacking.png    — big-number callouts (Q27: one slide; phrasing fixed)
  A6  a6_proposals.png  — sketch: a stack of identical, "excellent" proposals
  A8  a8_skills.png     — sketch: the three skills humans need (xkcd style;
                          "sketches are fine!")

A3 numbers (verified in Q&A Round 2, with sources):
  Claude Mythos Preview (Anthropic, announced 7 Apr 2026, withheld from general
  release): critical vulnerabilities found in every major OS and browser, 99%
  unpatched at announcement; UK AI Security Institute: 73% success on
  expert-level hacking tasks. Scientific American, 17 Apr 2026; Axios, 7 Apr 2026.
  Hugging Face (16 Jul 2026): an autonomous AI agent broke in (>17,000 attack
  attempts on one account, NeuralTrust); 21 Jul 2026: OpenAI disclosed its
  models had too (ExploitGym sandbox escape). CNBC, 22 Jul 2026; Varonis.
  Phrasing per Q27: "an AI agent broke into Hugging Face; a week later OpenAI
  said its models had too".

Usage:
    conda run -n ocean14 python presentations/py/ai_panels.py
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

from slide_style import FULL, apply_style, save, RED, BLUE, GREEN, GOLD, INK, MUTED, GRAY


def box(fig, x0, y0, w, h, color):
    """Created by JXP and Claude. Tinted rounded panel in figure coordinates."""
    fig.patches.append(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0,rounding_size=0.02",
                                      transform=fig.transFigure, facecolor=color, alpha=0.09,
                                      edgecolor="none"))


def a3_hacking():
    """Created by JXP and Claude. Build a3_hacking.png."""
    apply_style()
    fig = plt.figure(figsize=FULL)
    box(fig, 0.02, 0.04, 0.46, 0.92, RED)
    fig.text(0.25, 0.86, "Claude Mythos Preview (Apr 2026)", ha="center", fontsize=17,
             fontweight="bold", color=RED)
    fig.text(0.25, 0.77, "judged too dangerous to release", ha="center", fontsize=13, color=INK)
    for y, num, text in ((0.52, "99%", "of the critical flaws it found\nin every major OS and browser\nwere unpatched"),
                         (0.20, "73%", "success on expert-level\nhacking tasks\n(UK AI Security Institute)")):
        fig.text(0.05, y, num, fontsize=40, fontweight="bold", color=RED, va="center")
        fig.text(0.215, y, text, fontsize=13, color=INK, va="center")

    box(fig, 0.52, 0.04, 0.46, 0.92, BLUE)
    fig.text(0.75, 0.86, "Hugging Face (Jul 2026)", ha="center", fontsize=17,
             fontweight="bold", color=BLUE)
    fig.text(0.75, 0.55, "An AI agent broke into\nHugging Face;\na week later OpenAI said\nits models had too.",
             ha="center", va="center", fontsize=19, color=INK, linespacing=1.4)
    fig.text(0.75, 0.17, ">17,000 attack attempts on one account", ha="center", fontsize=13, color=MUTED)
    save(fig, "a3_hacking.png",
         "Scientific American 17 Apr 2026 and Axios 7 Apr 2026 (Mythos; UK AISI); CNBC 22 Jul 2026, "
         "Varonis and NeuralTrust (Hugging Face)", "A3")


def a6_proposals():
    """Created by JXP and Claude. Build a6_proposals.png: 15 identical
    proposals, every one rated 'Excellent', one funded at random."""
    apply_style()
    fig, ax = plt.subplots(figsize=FULL)
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.3, 3.3)
    ax.axis("off")
    funded = 11
    for i in range(15):
        x, y = 0.3 + (i % 5) * 1.95, 2.25 - (i // 5) * 1.1 + 0.95
        ax.add_patch(Rectangle((x, y - 0.95), 1.45, 0.92, facecolor="white", edgecolor=GRAY, lw=1.2))
        for k in range(4):
            ax.plot([x + 0.15, x + 1.3 - (0.35 if k == 3 else 0)], [y - 0.25 - k * 0.15] * 2, color="#c8ced6", lw=2)
        ax.text(x + 0.12, y - 0.13, "Proposal", fontsize=10, color=INK, va="center")
        ax.text(x + 1.38, y - 0.82, "Excellent", fontsize=10, color=GREEN, ha="right", fontweight="bold")
        if i == funded:
            ax.add_patch(Rectangle((x - 0.05, y - 1.0), 1.55, 1.02, fill=False, edgecolor=GOLD, lw=3))
            ax.text(x + 0.72, y - 1.18, "funded (why this one?)", fontsize=11, color=GOLD,
                    ha="center", fontweight="bold")
    save(fig, "a6_proposals.png", "Illustration", "A6")


def a8_skills():
    """Created by JXP and Claude. Build a8_skills.png in xkcd style."""
    apply_style()
    with plt.xkcd(scale=1, length=100, randomness=2):
        plt.rcParams["font.family"] = ["Humor Sans", "Comic Neue", "Comic Sans MS", "DejaVu Sans"]
        fig, axes = plt.subplots(1, 3, figsize=FULL)
        # 1. Order-of-magnitude thinking: a log ladder.
        ax = axes[0]
        for k, lab in enumerate(["1", "10", "100", "1,000", "10,000"]):
            ax.plot([0.2, 0.8], [k, k], color=INK, lw=1.5)
            ax.text(0.9, k, lab, fontsize=12, va="center", color=INK)
        ax.annotate("", (0.5, 4.2), (0.5, -0.2), arrowprops=dict(arrowstyle="->", color=RED, lw=2))
        ax.set_title("Order-of-magnitude\nthinking", fontsize=15)
        # 2. Rapid reading with comprehension: a page of lines + a check.
        ax = axes[1]
        for k in range(9):
            ax.plot([0.1, 0.9 - (0.25 if k % 3 == 2 else 0)], [8 - k, 8 - k], color=GRAY, lw=2)
        ax.text(0.78, 0.3, "✓", fontsize=36, color=GREEN, ha="center")
        ax.set_title("Rapid reading\nwith comprehension", fontsize=15)
        # 3. Reading and creating figures: a hand-drawn rising curve.
        ax = axes[2]
        xs = [i / 20 for i in range(21)]
        ax.plot(xs, [2 ** (6 * x) for x in xs], color=BLUE, lw=2.5)
        ax.text(0.05, 50, "sketches\nare fine!", fontsize=13, color=RED)
        ax.set_title("Reading & making\nfigures", fontsize=15)
        for ax in axes[:2]:
            ax.axis("off")
        axes[2].set_xticks([])
        axes[2].set_yticks([])
        save(fig, "a8_skills.png", "Illustration", "A8")


def main():
    """Created by JXP and Claude. Build all three panels."""
    a3_hacking()
    a6_proposals()
    a8_skills()


if __name__ == "__main__":
    main()
