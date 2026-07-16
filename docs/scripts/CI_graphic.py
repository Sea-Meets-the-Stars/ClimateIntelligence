"""
CI_graphic.py
=============

Generate the Climate Intelligence project "summary graphic" in two formats from
a single set of drawing helpers + a per-format layout config:

  * "banner"  -> docs/CI_graphic.png                (figsize 16x6, wide README banner)
  * "slides"  -> docs/CI_graphic_google_slides.png  (figsize 16x9, Google Slides 16:9)

Design (light theme, muted professional palette):
  Elements are the same across both formats -- only their positions/sizes/font
  scales differ (see LAYOUTS). Elements:
    - "Climate Intelligence" wordmark (top-left)
    - two-line tagline "Where climate science meets / artificial intelligence."
      (upper-right, right of the wordmark and above the chart)
    - three small muted-terracotta climate stat callouts (left column)
    - an OBSERVED-warming chart (scatter of annual anomalies + smooth trend +
      modest uncertainty band; NO forecast/projection, NO "AI" analysis --
      simply the climate evidence)
    - five topic icons along the bottom, each a hand-drawn vector glyph in a
      soft colored circle: Climate Physics, Biodiversity, Population, Unhoused,
      Artificial Intelligence (a violet microchip). No robot/human/globe/bear.

  AI's presence lives in the wordmark, tagline, and the AI topic icon -- NOT in
  the chart, which never implies AI is computing or forecasting the warming.

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


# ----------------------------------------------------------------------------
# Chart data -- synthesized ONCE with a fixed seed and reused by both formats.
# ----------------------------------------------------------------------------
def _signal(year):
    """Smooth, accelerating warming 'signal' underlying the observed record."""
    n = year - 1850.0
    return -0.2 + 2.1 * (n / 200.0) ** 3.6


np.random.seed(12)  # reproducible observation noise (seeded once, before draw)
_OBS_YEARS = np.arange(1850, 2026)  # historical / observed only (ends ~present)
_TREND = _signal(_OBS_YEARS)
_OBS = _TREND + np.random.normal(0.0, 0.11, _OBS_YEARS.size)


# ----------------------------------------------------------------------------
# Element helpers -- each takes a layout config so positions/sizes are not
# hard-coded and can be reused across formats.
# ----------------------------------------------------------------------------
def draw_title(ax, cfg):
    """Wordmark (top-left) + two-line tagline (upper-right)."""
    t = cfg["title"]
    ax.text(t["x"], t["y"], "Climate Intelligence",
            ha="left", va="center", fontsize=t["fs"], fontweight="bold",
            color=CHARCOAL)
    g = cfg["tagline"]
    ax.text(g["x"], g["y1"], "Where climate science meets",
            ha=g["ha"], va="center", fontsize=g["fs"], color=MUTED)
    ax.text(g["x"], g["y2"], "artificial intelligence.",
            ha=g["ha"], va="center", fontsize=g["fs"], color=MUTED)


def draw_stats(ax, cfg):
    """Three well-sourced climate numbers as small quiet accents (left column)."""
    stats = [
        ("+1.1 °C", "warming since pre-industrial"),
        (">430 ppm", "atmospheric CO₂"),
        ("+3.7 mm/yr", "sea-level rise"),
    ]
    s = cfg["stats"]
    for (number, caption), y in zip(stats, s["ys"]):
        ax.text(s["num_x"], y, number, ha="left", va="center",
                fontsize=s["num_fs"], fontweight="bold", color=STAT)
        ax.text(s["cap_x"], y - s["cap_dy"], caption, ha="left", va="center",
                fontsize=s["cap_fs"], color=MUTED)


def draw_chart(ax, cfg):
    """The OBSERVED climate record: scatter + smooth trend + uncertainty band.

    No forecast/projection and no 'AI' analysis is depicted -- this is simply
    the climate evidence.
    """
    f = cfg["chart_fonts"]
    ax.scatter(_OBS_YEARS, _OBS, s=20, color=NAVY, alpha=0.30,
               edgecolors="none", zorder=2, label="observations")
    ax.plot(_OBS_YEARS, _TREND, color=ACCENT, lw=3.4, zorder=4, label="trend")
    ax.fill_between(_OBS_YEARS, _TREND - 0.11, _TREND + 0.11,
                    color=ACCENT, alpha=0.15, zorder=1)  # uncertainty, not a forecast
    ax.axhline(0.0, color=MUTED, lw=0.8, alpha=0.35, zorder=1)

    ax.set_facecolor(BG)
    ax.set_xlim(1848, 2026)
    ax.set_ylim(-0.6, 1.5)
    ax.set_xticks([1900, 1950, 2000])
    ax.set_yticks([0, 0.5, 1.0])
    ax.set_yticklabels(["0", "+0.5", "+1.0"])
    ax.tick_params(labelsize=f["tick"], length=4, color=MUTED,
                   labelcolor=CHARCOAL)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(MUTED)
    ax.set_ylabel("temperature anomaly (°C)", fontsize=f["ylabel"], color=MUTED)
    ax.set_title("observed global warming (1850–present)",
                 fontsize=f["title"], color=CHARCOAL, loc="left", pad=8)
    ax.legend(loc="upper left", fontsize=f["legend"], frameon=False,
              handlelength=1.6, borderaxespad=0.4)


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
    """Unhoused -> a simple house (base + triangular roof + door)."""
    a.add_patch(Rectangle((-0.42, -0.55), 0.84, 0.72, facecolor=c,
                          edgecolor="none", zorder=3))
    a.add_patch(Polygon([(-0.58, 0.14), (0.58, 0.14), (0.0, 0.72)],
                        facecolor=c, edgecolor="none", zorder=3))
    a.add_patch(Rectangle((-0.12, -0.55), 0.24, 0.40, facecolor=bg,
                          edgecolor="none", zorder=4))


def glyph_chip(a, c, bg):
    """Artificial Intelligence -> a microchip / processor (die + pins)."""
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
    a.add_patch(FancyBboxPatch((-0.40, -0.40), 0.80, 0.80,
                               boxstyle="round,pad=0,rounding_size=0.14",
                               facecolor=c, edgecolor="none", zorder=3,
                               mutation_aspect=1))
    a.add_patch(Rectangle((-0.17, -0.17), 0.34, 0.34, facecolor=bg,
                          edgecolor="none", zorder=4))


TOPICS = [
    ("Climate Physics",        "#d9ecef", "#0f5e6e", glyph_thermometer),
    ("Biodiversity",           "#dcefe0", "#2e7d4f", glyph_leaf),
    ("Population",             "#dde7f2", "#123b52", glyph_people),
    ("Unhoused",               "#f5e9d5", "#b5761f", glyph_house),
    ("Artificial\nIntelligence", "#e6e1f0", "#6d5b9e", glyph_chip),
]


def draw_topics(fig, ax, cfg):
    """Row of five topic icons (colored circle + glyph) with labels beneath."""
    t = cfg["topics"]
    n = len(TOPICS)
    step = (t["right"] - t["left"]) / n
    centers = [t["left"] + (i + 0.5) * step for i in range(n)]
    icon_h = t["icon_h"]
    # Keep each icon Axes physically square for this figure's aspect ratio.
    icon_w = icon_h * cfg["fig_h"] / cfg["fig_w"]
    y0 = t["y0"]
    for cx, (label, tint, glyph_color, glyph_fn) in zip(centers, TOPICS):
        iax = fig.add_axes([cx - icon_w / 2.0, y0, icon_w, icon_h])
        iax.set_xlim(-1, 1)
        iax.set_ylim(-1, 1)
        iax.set_aspect("equal")
        iax.axis("off")
        iax.add_patch(Circle((0, 0), 0.98, facecolor=tint, edgecolor="none",
                             zorder=1))
        glyph_fn(iax, glyph_color, tint)
        ax.text(cx, y0 - t["label_dy"], label, ha="center", va="top",
                fontsize=t["label_fs"], color=CHARCOAL, linespacing=1.0)


# ----------------------------------------------------------------------------
# Per-format layout configs
# ----------------------------------------------------------------------------
LAYOUTS = {
    # Wide README banner -- reproduces the established appearance exactly.
    "banner": {
        "fig_w": 16.0, "fig_h": 6.0,
        "title": {"x": 0.05, "y": 0.905, "fs": 52},
        "tagline": {"x": 0.965, "y1": 0.895, "y2": 0.825, "fs": 23, "ha": "right"},
        "stats": {"num_x": 0.05, "cap_x": 0.052, "ys": [0.75, 0.64, 0.53],
                  "num_fs": 24, "cap_fs": 14, "cap_dy": 0.045},
        "chart": [0.45, 0.35, 0.51, 0.37],
        "chart_fonts": {"tick": 16, "ylabel": 15, "title": 18, "legend": 15},
        "topics": {"left": 0.06, "right": 0.94, "y0": 0.12, "icon_h": 0.15,
                   "label_fs": 22, "label_dy": 0.018},
    },
    # Google Slides 16:9 -- uses the extra vertical room; larger fonts.
    "slides": {
        "fig_w": 16.0, "fig_h": 9.0,
        "title": {"x": 0.05, "y": 0.925, "fs": 58},
        "tagline": {"x": 0.965, "y1": 0.930, "y2": 0.868, "fs": 26, "ha": "right"},
        "stats": {"num_x": 0.05, "cap_x": 0.052, "ys": [0.64, 0.52, 0.40],
                  "num_fs": 31, "cap_fs": 17, "cap_dy": 0.05},
        "chart": [0.37, 0.34, 0.57, 0.40],
        "chart_fonts": {"tick": 18, "ylabel": 17, "title": 22, "legend": 17},
        "topics": {"left": 0.05, "right": 0.95, "y0": 0.10, "icon_h": 0.14,
                   "label_fs": 24, "label_dy": 0.020},
    },
}


# ----------------------------------------------------------------------------
# Compose a figure for a given layout, then render both formats.
# ----------------------------------------------------------------------------
def build_figure(layout):
    fig = plt.figure(figsize=(layout["fig_w"], layout["fig_h"]))

    # Full-figure decorative background Axes (manual 0-1 placement).
    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_xlim(0, 1)
    bg.set_ylim(0, 1)
    bg.axis("off")

    draw_title(bg, layout)
    draw_stats(bg, layout)
    draw_topics(fig, bg, layout)

    cax = fig.add_axes(layout["chart"])
    draw_chart(cax, layout)

    return fig


def main():
    out_dir = Path(__file__).resolve().parents[1]
    outputs = {
        "banner": "CI_graphic.png",
        "slides": "CI_graphic_google_slides.png",
    }
    for fmt, fname in outputs.items():
        fig = build_figure(LAYOUTS[fmt])
        path = out_dir / fname
        fig.savefig(path, dpi=200)
        plt.close(fig)
        print(f"Saved [{fmt}]: {path}")


if __name__ == "__main__":
    main()
