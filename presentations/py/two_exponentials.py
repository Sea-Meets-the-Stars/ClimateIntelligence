"""Created by JXP and Claude.

Slide 4 "The two exponentials" — side by side on log axes:
  left:  world fossil + industry CO2 emissions, 1850-2024, with the
         1850-1970 exponential fit (and how it broke after ~1970);
  right: training compute of notable AI models, 2010-2026, with its fit.

Data and fits are reused from Blog 001 so the numbers match the blog:
  blogs/blog001/make_fig4_co2_emissions.py   (OWID / Global Carbon Project,
      climate_intelligence/data/raw/owid-co2-data.csv; fit 1850-1970)
  blogs/blog001/make_fig3_ai_compute_growth.py (Epoch AI "Notable AI Models",
      blogs/blog001/data/epoch_notable_ai_models.csv; fit from 2010)

Usage:
    conda run -n ocean14 python presentations/py/two_exponentials.py
"""
import sys

import numpy as np
import matplotlib.pyplot as plt

from slide_style import ROOT, FULL, apply_style, save, RED, BLUE, GRAY, INK

sys.path.insert(0, str(ROOT / "blogs" / "blog001"))
import make_fig3_ai_compute_growth as ai    # noqa: E402
import make_fig4_co2_emissions as co2       # noqa: E402


def main():
    """Created by JXP and Claude. Build s4_two_exponentials.png."""
    apply_style()
    world = co2.load_world_emissions(co2.DATA_CSV)
    t2_co2, slope, intercept = co2.fit_doubling_time(world, co2.FIT_START, co2.FIT_END)
    models = ai.load_models(ai.DATA_CSV)
    t2_ai, growth, trend_years, trend_flop, n_fit = ai.fit_doubling_time(models, ai.ERA_START_YEAR)
    print(f"CO2 doubling {t2_co2:.1f} yr (1850-1970); AI compute doubling {t2_ai:.1f} months "
          f"(x{growth:.1f}/yr, n={n_fit})")

    fig, (ax, bx) = plt.subplots(1, 2, figsize=FULL)

    yrs = world["year"].to_numpy()
    mt = world["co2"].to_numpy()
    ax.plot(yrs, mt / 1e3, color=RED, lw=2.4)
    fit_y = np.arange(1850, 2025)
    ax.plot(fit_y, 2 ** (slope * fit_y + intercept) / 1e3, "--", color=GRAY, lw=1.4)
    ax.set_yscale("log")
    ax.set_xlim(1850, 2026)
    ax.set_ylim(0.1, 300)
    ax.set_ylabel("Fossil CO₂ (Gt per year)")
    ax.text(1856, 60, f"CO₂ emissions\ndoubled every {t2_co2:.0f} years\n(1850–1970)",
            fontsize=13, color=RED)
    ax.text(1975, 120, "…then the\nexponential broke", fontsize=12, color=GRAY)

    bx.scatter(models["year"], models["flop"], s=10, color=BLUE, alpha=0.45, lw=0)
    bx.plot(trend_years, trend_flop, "--", color=INK, lw=1.4)
    # Landmark models, as in Blog 001 Figure 3 (same dataset names and offsets).
    for name, (label, dx, dy) in ai.CALLOUTS.items():
        row = models[models["model"] == name]
        if row.empty:
            continue
        x, y = row["year"].iloc[0], row["flop"].iloc[0]
        bx.plot(x, y, "o", ms=6, color=BLUE, mec="white", zorder=3)
        bx.annotate(label, (x, y), xytext=(x + dx, y * 10.0 ** dy), fontsize=11, color=INK,
                    arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.7))
    bx.set_yscale("log")
    bx.set_xlim(2010, 2027)
    bx.set_ylim(1e12, 1e28)
    bx.set_ylabel("AI training compute (FLOP)")
    bx.text(2010.5, 1e25, f"AI compute\ndoubles every\n~{t2_ai:.0f} months", fontsize=13, color=BLUE)

    save(fig, "s4_two_exponentials.png",
         "Left: Global Carbon Project via Our World in Data. Right: Epoch AI, Notable AI Models "
         "(training compute). Fits as in Blog 001",
         "4")


if __name__ == "__main__":
    main()
