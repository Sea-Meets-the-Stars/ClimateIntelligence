"""Created by JXP and Claude.

Shared matplotlib style for the WMKO 2026 slide figures.

Kraw-style slides are 10" x 5.625" with a title across the top (~0.85") and
an optional sub-line near the bottom. Figures are drawn at the physical size
they will occupy on the slide, so font sizes below are the sizes the
audience sees (points on the slide):
  - FULL  : 9.2" x 3.95" — figure spans the slide (any slide without a photo)
  - MAIN  : 6.4" x 3.95" — figure plus an instrument photo beside it
  - INSET : 3.0" x 2.6"  — small companion panel
No in-figure titles (the slide title does that). The full source string is
recorded in presentations/2026_WMKO/figs/sources.json; on the slides the
source appears as ~16pt slide text (assemble_deck.py), so by default it is
NOT drawn inside the PNG (set SOURCE_IN_FIGURE = True for standalone use).
"""
import json
import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # headless backend; we save PNGs, never display
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
PRES = ROOT / "presentations"
DATA = PRES / "data"
FIGS = PRES / "2026_WMKO" / "figs"
SOURCES_JSON = FIGS / "sources.json"

FULL = (9.2, 3.95)
MAIN = (6.4, 3.95)
INSET = (3.0, 2.6)
DPI = 220

# Palette carried over from CI_Reports (fixed assignments, never cycled).
BLUE, LBLUE, RED, ORANGE = "#1f5fa6", "#4a90d9", "#c0392b", "#b9430f"
TEAL, PURPLE, GREEN, GRAY, GOLD = "#16a085", "#8e44ad", "#27ae60", "#7f8c8d", "#e1a100"
INK, MUTED = "#222222", "#666666"

SOURCE_FONTSIZE = 10
SOURCE_IN_FIGURE = False  # sources go on the slide as 16pt text (Q10)


def apply_style():
    """Created by JXP and Claude. Set rcParams for slide-sized figures.
    Inputs: none. Outputs: none (mutates matplotlib.rcParams)."""
    plt.rcParams.update({
        "font.family": ["Helvetica Neue", "Arial", "DejaVu Sans"],
        "font.size": 14,
        "axes.labelsize": 15,
        "xtick.labelsize": 13,
        "ytick.labelsize": 13,
        "legend.fontsize": 12,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.edgecolor": "#444444",
        "text.color": INK,
        "axes.labelcolor": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "savefig.dpi": DPI,
        "savefig.transparent": False,
        "savefig.facecolor": "white",
    })


def save(fig, name, source, slide, right=1.0, bottom=0.0):
    """Created by JXP and Claude.

    Lay out the figure, add the (wrapped) source line, save the PNG to FIGS,
    and record it in sources.json. Callers should not call tight_layout.

    Inputs
    ------
    fig : matplotlib Figure
    name : str — output file name (e.g. 'c1_keeling.png')
    source : str — data source, shown small at the bottom
    slide : str — slide id from the skeleton (e.g. 'C1')
    right : float — right edge of the axes area (room for direct labels)
    bottom : float — minimum bottom margin (figure fraction) for in-figure notes

    Outputs
    -------
    Path of the written PNG.
    """
    FIGS.mkdir(parents=True, exist_ok=True)
    width_in, height_in = fig.get_size_inches()
    # ~0.5 em per character at SOURCE_FONTSIZE; wrap so nothing is clipped.
    chars = int(width_in * 72 / (SOURCE_FONTSIZE * 0.52))
    lines = textwrap.wrap(source, chars) if SOURCE_IN_FIGURE else []
    bottom = max(bottom, (len(lines) * SOURCE_FONTSIZE * 1.25 / 72 + 0.06) / height_in)
    fig.tight_layout(rect=(0, bottom, right, 1))
    if lines:
        fig.text(0.01, 0.01, "\n".join(lines), ha="left", va="bottom",
                 fontsize=SOURCE_FONTSIZE, color=MUTED)
    out = FIGS / name
    fig.savefig(out)
    plt.close(fig)

    manifest = json.loads(SOURCES_JSON.read_text()) if SOURCES_JSON.exists() else {}
    manifest[name] = {"slide": slide, "source": source}
    SOURCES_JSON.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {out.relative_to(ROOT)}")
    return out
