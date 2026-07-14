"""
CI_graphic.py
=============

Generate the Climate Intelligence project banner: a wide, light-background
"summary graphic" for the GitHub README (and reuse in talks / slides).

Design concept (v2, revised after author review in claude_prompts/website.md):
  A clean, professional, light-theme banner. The hero visual fuses the two
  themes the author wants front-and-center -- **Artificial Intelligence** and
  the **climate crisis** -- in one *intuitive* picture: a chart of noisy annual
  temperature OBSERVATIONS that an AI fits into a clear RISING TREND, then
  extends as a dashed PROJECTION. It reads instantly as "the climate is warming"
  and as "AI extracts the signal and predicts from noisy data" -- a fresher AI
  cue than a generic neural-network mesh (dropped in v2), and more intuitive
  than the abstract warming-stripes ribbon (also dropped in v2).

  Left side: the "Climate Intelligence" wordmark plus three well-sourced climate
  numbers. Bottom: the four topic areas, each a small hand-drawn vector icon in
  a soft colored circle. No robot, human figure, burning globe, or polar bear.

Output:
  docs/CI_graphic.png  (dpi=200, figsize 16x6 => wide ~2.7:1 banner)

Run:
  conda run -n ocean14 python docs/scripts/CI_graphic.py
"""

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")  # headless / reproducible
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Circle, Ellipse, FancyBboxPatch, Polygon, Rectangle, Wedge,
)

# ----------------------------------------------------------------------------
# Palette & global style (restrained, professional, light theme)
# ----------------------------------------------------------------------------
BG = "#fbfcfe"          # very-light page background
CHARCOAL = "#16222e"    # primary text
NAVY = "#123b52"        # observation dots
ACCENT = "#c24a3f"      # warm accent for the observed-trend line
STAT = "#b05a52"        # muted brick/terracotta for the quiet stat numbers
MUTED = "#6b7885"       # small captions / secondary text / axis furniture

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "text.color": CHARCOAL,
        "figure.facecolor": BG,
        "savefig.facecolor": BG,
    }
)

np.random.seed(12)  # reproducible observation noise

FIG_W, FIG_H = 16.0, 6.0  # inches; used to size physically-square icon axes


# ----------------------------------------------------------------------------
# Hero chart: noisy observations -> AI-fit trend -> dashed projection
# ----------------------------------------------------------------------------
def _signal(year):
    """Smooth, accelerating warming 'signal' (the truth the AI recovers).

    -0.2 degC ~1850  ->  ~0 ~1950  ->  ~+1.1 ~2025  ->  ~+1.9 ~2050.
    """
    n = year - 1850.0
    return -0.2 + 2.1 * (n / 200.0) ** 3.6


def draw_chart(ax):
    """A real data Axes showing only the OBSERVED climate record: a scatter of
    annual anomalies with a smooth trend line + modest uncertainty band.

    No forecast/projection and no 'AI' analysis is depicted -- this is simply
    the climate evidence. AI's role in the project lives in the title, tagline,
    and the Artificial Intelligence topic icon, not in computing the warming.
    """
    obs_years = np.arange(1850, 2026)  # historical / observed only
    obs = _signal(obs_years) + np.random.normal(0.0, 0.11, obs_years.size)

    # Observations: light, semi-transparent dots (the raw record).
    ax.scatter(obs_years, obs, s=20, color=NAVY, alpha=0.30,
               edgecolors="none", zorder=2, label="observations")

    # Smooth trend through the historical data, with a modest (constant)
    # uncertainty band -- uncertainty, NOT a prediction.
    trend = _signal(obs_years)
    ax.plot(obs_years, trend, color=ACCENT, lw=3.4, zorder=4, label="trend")
    ax.fill_between(obs_years, trend - 0.11, trend + 0.11,
                    color=ACCENT, alpha=0.15, zorder=1)

    # Zero baseline only -- no 'present' divider, no future region.
    ax.axhline(0.0, color=MUTED, lw=0.8, alpha=0.35, zorder=1)

    # Clean, minimal axes; x ends at the present.
    ax.set_facecolor(BG)
    ax.set_xlim(1848, 2026)
    ax.set_ylim(-0.6, 1.5)
    ax.set_xticks([1900, 1950, 2000])
    ax.set_yticks([0, 0.5, 1.0])
    ax.set_yticklabels(["0", "+0.5", "+1.0"])
    ax.tick_params(labelsize=16, length=4, color=MUTED, labelcolor=CHARCOAL)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(MUTED)
    ax.set_ylabel("temperature anomaly (°C)", fontsize=15, color=MUTED)
    ax.set_title("observed global warming (1850–present)",
                 fontsize=18, color=CHARCOAL, loc="left", pad=8)
    ax.legend(loc="upper left", fontsize=15, frameon=False,
              handlelength=1.6, borderaxespad=0.4)


# ----------------------------------------------------------------------------
# Title + climate stat callouts (left column)
# ----------------------------------------------------------------------------
def draw_title(ax):
    ax.text(0.05, 0.905, "Climate Intelligence",
            ha="left", va="center", fontsize=52, fontweight="bold",
            color=CHARCOAL)
    # Tagline: round-4 option 3 (see Q&A in claude_prompts/website.md), "for now".
    ax.text(0.052, 0.805, "Where climate science meets artificial intelligence.",
            ha="left", va="center", fontsize=24, color=MUTED)


def draw_stats(ax):
    """Three well-sourced climate numbers stacked under the title (left)."""
    stats = [
        ("+1.1 °C", "warming since pre-industrial"),
        (">430 ppm", "atmospheric CO₂"),
        ("+3.7 mm/yr", "sea-level rise"),
    ]
    # Quiet supporting accents: smaller + muted so they don't dominate.
    ys = [0.62, 0.48, 0.34]
    for (number, caption), y in zip(stats, ys):
        ax.text(0.05, y, number, ha="left", va="center",
                fontsize=30, fontweight="bold", color=STAT)
        ax.text(0.052, y - 0.055, caption, ha="left", va="center",
                fontsize=16, color=MUTED)


# ----------------------------------------------------------------------------
# Topic icons: simple drawn vector glyphs in soft colored circles
# ----------------------------------------------------------------------------
def glyph_thermometer(a, c, bg):
    """Climate Physics -> thermometer (rounded stem + bulb)."""
    a.add_patch(Rectangle((-0.13, -0.45), 0.26, 1.05, facecolor=c,
                          edgecolor="none", zorder=3))
    a.add_patch(Circle((0, 0.60), 0.13, facecolor=c, edgecolor="none", zorder=3))
    a.add_patch(Circle((0, -0.45), 0.30, facecolor=c, edgecolor="none",
                       zorder=3))
    # light "mercury" channel inside the stem, with a filled bulb
    a.add_patch(Rectangle((-0.05, -0.45), 0.10, 0.85, facecolor=bg,
                          edgecolor="none", zorder=4))
    a.add_patch(Circle((0, -0.45), 0.15, facecolor=c, edgecolor="none",
                       zorder=5))


def glyph_leaf(a, c, bg):
    """Biodiversity -> leaf (rotated ellipse + midrib vein)."""
    a.add_patch(Ellipse((0, 0), width=1.35, height=0.68, angle=42,
                        facecolor=c, edgecolor="none", zorder=3))
    ang = np.deg2rad(42)
    dx, dy = np.cos(ang), np.sin(ang)
    a.plot([-0.62 * dx, 0.62 * dx], [-0.62 * dy, 0.62 * dy],
           color=bg, lw=2.2, zorder=4, solid_capstyle="round")


def glyph_people(a, c, bg):
    """Population -> a small cluster of people (head + shoulders)."""
    def person(cx, cy, s, col):
        a.add_patch(Wedge((cx, cy - 0.30 * s), 0.34 * s, 0, 180,
                          facecolor=col, edgecolor="none", zorder=3))
        a.add_patch(Circle((cx, cy + 0.18 * s), 0.19 * s, facecolor=col,
                           edgecolor="none", zorder=3))
    back = "#4a6f86"  # slightly lighter navy for the two rear figures
    person(-0.42, -0.02, 0.85, back)
    person(0.42, -0.02, 0.85, back)
    person(0.0, 0.08, 1.0, c)


def glyph_house(a, c, bg):
    """Homelessness -> a simple house (base + triangular roof + door)."""
    a.add_patch(Rectangle((-0.42, -0.55), 0.84, 0.72, facecolor=c,
                          edgecolor="none", zorder=3))
    a.add_patch(Polygon([(-0.58, 0.14), (0.58, 0.14), (0.0, 0.72)],
                        facecolor=c, edgecolor="none", zorder=3))
    a.add_patch(Rectangle((-0.12, -0.55), 0.24, 0.40, facecolor=bg,
                          edgecolor="none", zorder=4))


def glyph_chip(a, c, bg):
    """Artificial Intelligence -> a microchip / processor (die + pins).

    A fresher AI cue than a robot: a rounded-square chip body with a small inner
    'die' square and short pins along all four sides.
    """
    pin_len, pin_w = 0.16, 0.09
    for off in (-0.24, 0.0, 0.24):  # three pins per side, behind the body
        a.add_patch(Rectangle((off - pin_w / 2, 0.42), pin_w, pin_len,
                              facecolor=c, edgecolor="none", zorder=2))   # top
        a.add_patch(Rectangle((off - pin_w / 2, -0.42 - pin_len), pin_w,
                              pin_len, facecolor=c, edgecolor="none",
                              zorder=2))                                  # bottom
        a.add_patch(Rectangle((-0.42 - pin_len, off - pin_w / 2), pin_len,
                              pin_w, facecolor=c, edgecolor="none",
                              zorder=2))                                  # left
        a.add_patch(Rectangle((0.42, off - pin_w / 2), pin_len, pin_w,
                              facecolor=c, edgecolor="none", zorder=2))   # right
    # rounded-square chip body
    a.add_patch(FancyBboxPatch((-0.40, -0.40), 0.80, 0.80,
                               boxstyle="round,pad=0,rounding_size=0.14",
                               facecolor=c, edgecolor="none", zorder=3,
                               mutation_aspect=1))
    # inner die (tint cut-out)
    a.add_patch(Rectangle((-0.17, -0.17), 0.34, 0.34, facecolor=bg,
                          edgecolor="none", zorder=4))


TOPICS = [
    ("Climate Physics",        "#d9ecef", "#0f5e6e", glyph_thermometer),
    ("Biodiversity",           "#dcefe0", "#2e7d4f", glyph_leaf),
    ("Population",             "#dde7f2", "#123b52", glyph_people),
    ("Homelessness",           "#f5e9d5", "#b5761f", glyph_house),
    ("Artificial\nIntelligence", "#e6e1f0", "#6d5b9e", glyph_chip),
]


def draw_topics(fig, ax):
    """Row of four topic icons (colored circle + glyph) with labels beneath."""
    # Five topic icons, evenly spaced as bin-centers across the width.
    n = len(TOPICS)
    left, right = 0.06, 0.94
    step = (right - left) / n
    centers = [left + (i + 0.5) * step for i in range(n)]
    icon_h = 0.15
    icon_w = icon_h * FIG_H / FIG_W  # keep the icon Axes physically square
    y0 = 0.12
    for cx, (label, tint, glyph_color, glyph_fn) in zip(centers, TOPICS):
        iax = fig.add_axes([cx - icon_w / 2.0, y0, icon_w, icon_h])
        iax.set_xlim(-1, 1)
        iax.set_ylim(-1, 1)
        iax.set_aspect("equal")
        iax.axis("off")
        iax.add_patch(Circle((0, 0), 0.98, facecolor=tint, edgecolor="none",
                             zorder=1))
        glyph_fn(iax, glyph_color, tint)
        ax.text(cx, y0 - 0.018, label, ha="center", va="top",
                fontsize=22, color=CHARCOAL, linespacing=1.0)


# ----------------------------------------------------------------------------
# Compose the banner
# ----------------------------------------------------------------------------
def build_figure():
    fig = plt.figure(figsize=(FIG_W, FIG_H))

    # Full-figure decorative background Axes (manual 0-1 placement).
    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_xlim(0, 1)
    bg.set_ylim(0, 1)
    bg.axis("off")

    draw_title(bg)
    draw_stats(bg)
    draw_topics(fig, bg)

    # Hero data chart on the right, sitting on top of the background Axes.
    # Kept low enough that its title clears the wordmark + tagline on the left.
    cax = fig.add_axes([0.45, 0.35, 0.51, 0.37])
    draw_chart(cax)

    return fig


def main():
    out_path = Path(__file__).resolve().parents[1] / "CI_graphic.png"
    fig = build_figure()
    fig.savefig(out_path, dpi=200)
    plt.close(fig)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
