"""Created by JXP and Claude.

C5 "The ocean isn't done warming" — both framings on one slide (Q38c):
  left:  warming realized so far vs. the equilibrium warming implied by
         today's forcing (with Murphy's ~1.7 C CO2-only marker);
  right: the sea-level commitment over the next 2000 years.
Caveat in small print: the equilibrium bars hold today's forcing constant;
AR6 finds that if CO2 emissions stop, surface warming roughly stops too.

Inputs (all typed with citations):
  Realized: GSAT 2011-2020 vs 1850-1900 = 1.09 [0.95 to 1.20] C
            (IPCC AR6 WGI SPM A.1.2).
  Forcing:  total anthropogenic ERF 2019 vs 1750 = 2.72 [1.96 to 3.48] W/m^2
            (AR6 WGI Ch. 7; context/claudes_context.md sec 3.2).
  ECS:      3 C best estimate, likely 2.5-4 C (AR6 WGI Ch. 7).
  F_2x:     ERF of doubled CO2 = 3.93 W/m^2 (AR6 WGI Ch. 7, Table 7.4 value).
  Murphy:   CO2-only committed warming ~1.7 C at today's CO2, using
            RF = 5.35 ln(CO2/280) and 0.8 C per W/m^2 (Murphy 2021, Energy and
            Human Ambitions on a Finite Planet; context sec 3.1).
  ZEC:      zero-emissions commitment close to zero (AR6 WGI Ch. 4, 4.7.1).
  Sea level over the next 2000 years: ~2-3 m if warming limited to 1.5 C,
            2-6 m if limited to 2 C, 19-22 m with 5 C (AR6 WGI SPM B.5.4).

Calculation (equilibrium at constant 2019 forcing):
  dT_eq = ERF * ECS / F_2x = 2.72 * 3 / 3.93 ~= 2.1 C   (ECS 2.5-4 -> 1.7-2.8 C)

Usage:
    conda run -n ocean14 python presentations/py/committed_warming.py
"""
import numpy as np
import matplotlib.pyplot as plt

from slide_style import FULL, apply_style, save, RED, BLUE, ORANGE, GRAY, MUTED, INK

REALIZED, REALIZED_RANGE = 1.09, (0.95, 1.20)
ERF_2019 = 2.72
ECS, ECS_LIKELY = 3.0, (2.5, 4.0)
F2X = 3.93
MURPHY_CO2_ONLY = 1.7
SEA_LEVEL_2000YR = [("1.5 °C", 2.0, 3.0), ("2 °C", 2.0, 6.0)]
SEA_LEVEL_5C = (19.0, 22.0)


def equilibrium_warming(erf, ecs, f2x=F2X):
    """Created by JXP and Claude. Equilibrium GSAT change (C) for a constant
    forcing erf (W/m^2), given climate sensitivity ecs (C per doubling)."""
    return erf * ecs / f2x


def main():
    """Created by JXP and Claude. Build c5_committed_warming.png."""
    apply_style()
    eq = equilibrium_warming(ERF_2019, ECS)
    eq_lo, eq_hi = (equilibrium_warming(ERF_2019, e) for e in ECS_LIKELY)
    print(f"equilibrium warming at 2019 forcing: {eq:.2f} C (ECS likely range {eq_lo:.2f}-{eq_hi:.2f})")

    fig, (ax, sx) = plt.subplots(1, 2, figsize=FULL, gridspec_kw=dict(width_ratios=(1.35, 1)))

    # Left: realized vs equilibrium.
    names = ["Warming so far\n(2011–2020)", "Where today's forcing\nis heading"]
    ax.bar(names, [REALIZED, eq], color=[ORANGE, RED], width=0.55,
           yerr=[[REALIZED - REALIZED_RANGE[0], eq - eq_lo],
                 [REALIZED_RANGE[1] - REALIZED, eq_hi - eq]],
           capsize=6, ecolor="#555555")
    ax.text(0, REALIZED / 2, f"{REALIZED:.1f} °C", ha="center", color="white",
            fontsize=16, fontweight="bold")
    ax.text(1, eq / 2, f"≈{eq:.1f} °C", ha="center", color="white",
            fontsize=16, fontweight="bold")
    ax.hlines(MURPHY_CO2_ONLY, 0.68, 1.32, color=BLUE, lw=2.5, ls="--")
    ax.text(1.34, MURPHY_CO2_ONLY, "CO₂ alone\n(Murphy) 1.7 °C", va="center",
            fontsize=11, color=BLUE)
    ax.set_ylabel("Warming vs 1850–1900 (°C)")
    ax.set_ylim(0, 3.1)
    ax.set_xlim(-0.5, 1.9)
    ax.grid(axis="x", visible=False)

    # Right: sea level keeps rising for centuries.
    for i, (lab, lo, hi) in enumerate(SEA_LEVEL_2000YR):
        sx.bar(i, hi - lo, bottom=lo, color=BLUE, alpha=0.75, width=0.5)
        sx.text(i, hi + 0.2, f"{lo:g}–{hi:g} m", ha="center", fontsize=14, color=INK)
    sx.set_xticks([0, 1])
    sx.set_xticklabels([f"if held to\n{s[0]}" for s in SEA_LEVEL_2000YR])
    sx.set_ylim(0, 7.5)
    sx.set_xlim(-0.6, 1.6)
    sx.set_ylabel("Sea-level rise over the\nnext 2000 years (m)")
    sx.text(0.5, 6.95, f"(5 °C: {SEA_LEVEL_5C[0]:g}–{SEA_LEVEL_5C[1]:g} m)", ha="center",
            fontsize=12, color=MUTED)
    sx.grid(axis="x", visible=False)

    # Q38c: the caveat stays on the figure, in small print.
    fig.text(0.01, 0.01, "Caveat: the red bar holds today's forcing constant. If CO₂ emissions stopped, surface "
             "warming would roughly stop too (AR6 zero-emissions commitment ≈ 0) — but sea level keeps rising "
             "for centuries.", fontsize=10, color=MUTED, wrap=True)
    save(fig, "c5_committed_warming.png",
         "Left: AR6 WGI (1.09 [0.95–1.20] °C; forcing 2.72 W/m² × ECS 3 [2.5–4] °C ÷ 3.93 W/m²); Murphy 2021. "
         "Caveat: the right-hand bar holds today's forcing constant — if CO₂ emissions stopped, surface warming "
         "would roughly stop too (AR6 zero-emissions commitment ≈ 0). "
         "Right: AR6 WGI SPM B.5.4 — sea level keeps rising for centuries either way",
         "C5", bottom=0.12)


if __name__ == "__main__":
    main()
