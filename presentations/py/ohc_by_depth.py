"""Created by JXP and Claude.

C4b "The ocean is warming: depth" — global ocean heat content anomaly split
into 0-700 m and 700-2000 m layers, 1957-2023.

Data: NOAA NCEI World Ocean Database heat content, pentadal (5-year running)
means, world ocean (column WO), 10^22 J, fetched 2026-10-05:
  .../3M_HEAT_CONTENT/DATA/basin/pentad/pent_h22-w0-700m.dat
  .../3M_HEAT_CONTENT/DATA/basin/pentad/pent_h22-w0-2000m.dat
  (base https://www.ncei.noaa.gov/data/oceans/woa/DATA_ANALYSIS)
cached at presentations/data/ohc_0_700m_pentad.dat, ohc_0_2000m_pentad.dat.
700-2000 m layer = (0-2000 m) - (0-700 m); uncertainties not propagated.
Instruments: XBTs and ship CTDs (before ~2005), the Argo float array since
(~4000 floats profiling to 2000 m every 10 days).

Usage:
    conda run -n ocean14 python presentations/py/ohc_by_depth.py
"""
import numpy as np
import matplotlib.pyplot as plt

from slide_style import DATA, MAIN, apply_style, save, ORANGE, BLUE, GRAY, INK


def load_pentad(fname):
    """Created by JXP and Claude. Outputs: year (mid-pentad), world-ocean
    OHC anomaly (10^22 J)."""
    rows = np.genfromtxt(DATA / fname, skip_header=1)
    return rows[:, 0], rows[:, 1]


def main():
    """Created by JXP and Claude. Build c4b_ohc_by_depth.png."""
    apply_style()
    y7, upper = load_pentad("ohc_0_700m_pentad.dat")
    y2, total = load_pentad("ohc_0_2000m_pentad.dat")
    assert np.allclose(y7, y2), "pentad years differ between depth files"
    deep = total - upper
    # Express both layers as change since the first pentad so the stack starts at 0.
    upper_c, deep_c = upper - upper[0], deep - deep[0]
    print(f"{y7[0]}-{y7[-1]}: 0-700 m +{upper_c[-1]:.1f}, 700-2000 m +{deep_c[-1]:.1f} "
          f"(x10^22 J); deep share {deep_c[-1] / (upper_c[-1] + deep_c[-1]):.0%}")

    fig, ax = plt.subplots(figsize=MAIN)
    ax.fill_between(y7, 0, upper_c, color=ORANGE, alpha=0.85, lw=0)
    ax.fill_between(y7, upper_c, upper_c + deep_c, color=BLUE, alpha=0.8, lw=0)
    xl = 2013.0  # label the upper layer inside, the deep layer just above the stack
    u, d = np.interp(xl, y7, upper_c), np.interp(xl, y7, deep_c)
    ax.text(xl, u * 0.5, "0–700 m", ha="center", va="center", fontsize=14,
            color="white", fontweight="bold")
    ax.text(xl - 4, u + d + 3, "700–2000 m", ha="center", va="bottom",
            fontsize=14, color=BLUE, fontweight="bold")
    share = deep_c[-1] / (upper_c[-1] + deep_c[-1])
    ax.text(1960, 30, f"Since the late 1950s the ocean has gained\n≈{upper_c[-1] + deep_c[-1]:.0f}×10$^{{22}}$ J; "
            f"{share:.0%} of it below 700 m", fontsize=13, color=INK, va="top")
    ax.set_xlim(y7[0], y7[-1] + 0.5)
    ax.set_ylim(0, (upper_c[-1] + deep_c[-1]) * 1.1)
    ax.set_ylabel("Heat gained since 1955–59\n(10$^{22}$ J)")
    save(fig, "c4b_ohc_by_depth.png",
         f"Data: NOAA NCEI ocean heat content, world ocean, 5-year means {int(y7[0] - 2)}–{int(y7[-1] + 2)}; "
         "XBT/CTD then Argo floats",
         "C4b")


if __name__ == "__main__":
    main()
