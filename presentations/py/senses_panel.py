"""Created by JXP and Claude.

New slide 4 (B9b) "Our own sensors are exquisite" — four human senses, each
with its sensitivity and (where defined) its dynamic range in orders of
magnitude.

Values (sources):
  Eyes: illuminance from ~1e-6 lux (threshold of vision) to >1e5 lux (bright
    sunlight): ~10 orders of magnitude; dark-adapted rods respond to a single
    photon. (Standard vision-science values; e.g. Reinhard et al., High Dynamic
    Range Imaging, ch. on the human visual system; Hecht, Shlaer & Pirenne 1942.)
  Ears: intensity from 1e-12 W/m^2 (threshold, 0 dB) to 1 W/m^2 (pain, 120 dB):
    12 orders of magnitude; at threshold near 3 kHz the eardrum moves ~1e-11 m,
    about a tenth of a hydrogen atom's diameter (JoVE Science Education, "Sound
    intensity level"; Canadian Acoustics teaching notes).
  Nose: geosmin (the "smell of rain") detected by sensitive people at ~5 ng/L,
    i.e. ~5 parts per trillion (water-utility and USGS summaries; typical
    threshold 5-15 ng/L).
  Skin: fingertips distinguish surface wrinkles only ~10 nm high (Skedung et al.
    2013, Scientific Reports 3, 2617, "Feeling Small").

Usage:
    conda run -n ocean14 python presentations/py/senses_panel.py
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from slide_style import FULL, apply_style, save, BLUE, TEAL, PURPLE, ORANGE, INK, MUTED

SENSES = [  # (sense, big number, line under it, detail, color)
    ("Eyes", "10¹⁰", "range in brightness", "starlight to sunlight;\nrods respond to a\nsingle photon", BLUE),
    ("Ears", "10¹²", "range in loudness", "at threshold the eardrum\nmoves ~1/10 the width\nof an atom", PURPLE),
    ("Nose", "5 ppt", "smell of rain (geosmin)", "5 parts per trillion,\nfor sensitive noses", TEAL),
    ("Skin", "10 nm", "wrinkles you can feel", "fingertips detect bumps\n~10 nanometers high", ORANGE),
]


def main():
    """Created by JXP and Claude. Build s4_senses.png."""
    apply_style()
    fig = plt.figure(figsize=FULL)
    w, gap = 0.235, 0.012
    for k, (sense, num, under, detail, color) in enumerate(SENSES):
        x0 = 0.01 + k * (w + gap)
        fig.patches.append(FancyBboxPatch((x0, 0.03), w, 0.94, boxstyle="round,pad=0,rounding_size=0.02",
                                          transform=fig.transFigure, facecolor=color, alpha=0.09,
                                          edgecolor="none"))
        cx = x0 + w / 2
        fig.text(cx, 0.88, sense, ha="center", fontsize=22, fontweight="bold", color=color)
        fig.text(cx, 0.64, num, ha="center", va="center", fontsize=40, fontweight="bold", color=color)
        fig.text(cx, 0.47, under, ha="center", fontsize=14, color=INK)
        fig.text(cx, 0.22, detail, ha="center", va="center", fontsize=13, color=MUTED, linespacing=1.3)
    save(fig, "s4_senses.png",
         "Vision: standard vision-science values (Hecht et al. 1942); hearing: 0–120 dB (JoVE); "
         "geosmin ~5 ng/L (USGS/water utilities); touch: Skedung et al. 2013, Sci. Rep.", "4")


if __name__ == "__main__":
    main()
