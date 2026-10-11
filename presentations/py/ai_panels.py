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
import numpy as np
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
    ax.set_ylim(-0.5, 3.3)
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
            ax.text(x + 0.72, y - 1.35, "funded (why this one?)", fontsize=17, color=GOLD,
                    ha="center", fontweight="bold")
    save(fig, "a6_proposals.png", "Illustration", "A6")


def a8_skills():
    """Created by JXP and Claude. Build a8_skills.png in xkcd style (B9b):
      1. order-of-magnitude thinking — an estimate in the right decade beats a
         precise-looking wrong answer;
      2. rapid reading — AI emits pages per second; a person reads ~240 words
         per minute (Brysbaert 2019, J. Mem. Lang.: 238 wpm, adult silent
         reading of non-fiction);
      3. reading & making figures — a richer hand-drawn plot (data with error
         bars, a model with an uncertainty band, a legend, an annotation)."""
    apply_style()
    rng = np.random.default_rng(7)
    with plt.xkcd(scale=1, length=100, randomness=2):
        plt.rcParams["font.family"] = ["Humor Sans", "Comic Neue", "Comic Sans MS", "DejaVu Sans"]
        fig, axes = plt.subplots(1, 3, figsize=FULL, gridspec_kw=dict(width_ratios=(1, 1, 1.15)))

        # 1. Order of magnitude: a log number line, truth, a good estimate, a bad precise answer.
        ax = axes[0]
        ax.set_xlim(-0.3, 8.6)
        ax.set_ylim(-1.6, 4.2)
        ax.plot([0, 8], [0, 0], color=INK, lw=1.5)
        for k in range(0, 9, 2):
            ax.plot([k, k], [-0.15, 0.15], color=INK, lw=1.5)
            ax.text(k, -0.55, f"10$^{{{k}}}$", ha="center", fontsize=12)
        ax.axvspan(3.5, 4.5, ymin=0.3, ymax=0.62, color=GREEN, alpha=0.25)
        ax.plot(4.2, 0, "o", ms=10, color=INK)
        ax.text(4.2, -1.25, "truth", ha="center", fontsize=12)
        ax.plot(3.8, 0.55, "v", ms=12, color=GREEN)
        ax.text(2.3, 1.2, "your guess:\n~10$^4$ — close!", ha="center", fontsize=11, color=GREEN)
        ax.plot(6.5, 0.55, "v", ms=12, color=RED)
        ax.text(7.0, 1.2, "3,141,592.65\n(precise, wrong)", ha="center", fontsize=11, color=RED)
        ax.text(4.1, 2.6, "roughly right beats\nprecisely wrong", ha="center", fontsize=13, color=INK)
        ax.set_title("Order-of-magnitude\nthinking", fontsize=15)
        ax.axis("off")

        # 2. Rapid reading: a flood of pages from AI vs one human reader.
        ax = axes[1]
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.add_patch(Rectangle((0.3, 6.6), 2.6, 2.4, facecolor=BLUE, alpha=0.85))
        ax.text(1.6, 7.8, "AI", ha="center", va="center", fontsize=22, color="white")
        for k in range(26):
            x, y = 3.2 + rng.uniform(0, 6.2), 2.2 + rng.uniform(0, 7.2)
            ax.add_patch(Rectangle((x, y), 0.9, 1.15, angle=rng.uniform(-35, 35), facecolor="white",
                                   edgecolor=GRAY, lw=1))
        ax.text(1.6, 5.7, "pages per\nsecond", ha="center", va="top", fontsize=13, color=BLUE)
        ax.text(2.0, 1.0, "you: ~240 words\nper minute", ha="center", fontsize=12, color=RED)
        ax.plot([2.0], [3.2], "o", ms=14, color=RED)  # a head
        ax.plot([2.0, 2.0], [3.0, 1.9], color=RED, lw=2)
        ax.set_title("Rapid reading\nwith comprehension", fontsize=15)
        ax.axis("off")

        # 3. Figures: data + error bars, a model with an uncertainty band, legend, annotation.
        ax = axes[2]
        x = np.linspace(0, 10, 12)
        model = 1 + 0.08 * x ** 2
        ax.fill_between(x, model - 1.2, model + 1.2, color=BLUE, alpha=0.18, lw=0)
        ax.plot(x, model, color=BLUE, lw=2, label="model")
        y = model + rng.normal(0, 0.8, x.size)
        y[9] += 3.5
        ax.errorbar(x, y, yerr=0.9, fmt="o", color=INK, ms=5, capsize=3, label="data")
        ax.annotate("anomaly!", (x[9], y[9]), xytext=(4.3, y[9] + 0.3), fontsize=12, color=RED,
                    arrowprops=dict(arrowstyle="->", color=RED, lw=1.5))
        ax.legend(loc="lower right", fontsize=11, frameon=False)
        ax.set_xlabel("time")
        ax.set_ylabel("thing we measured")
        ax.set_xticks([])
        ax.set_yticks([])
        ax.text(0.2, 11.0, "sketches\nare fine!", ha="left", va="top", fontsize=12, color=RED)
        ax.set_title("Reading & making\nfigures", fontsize=15)
        save(fig, "a8_skills.png", "Illustration; reading speed: Brysbaert 2019 (J. Mem. Lang.)", "A8")


def main():
    """Created by JXP and Claude. Build all three panels."""
    a3_hacking()
    a6_proposals()
    a8_skills()


if __name__ == "__main__":
    main()
