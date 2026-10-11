"""Created by JXP and Claude.

A2 "AI can already help create a deadly pandemic" — the arc of measured
"uplift" (how much better people do at bio-weapon-relevant tasks with an AI
model than with the internet alone), 2024 -> 2026. On the slide, Bill
Gates's words carry the claim (Q26a); this figure is the supporting data.

Points (uplift = success with AI / success of internet-only controls):
  2024-01  RAND red-team exercise (Mouton, Lucas & Guest 2024, RAND RR-A2977-2):
           no statistically significant difference between LLM and internet-only
           teams' attack plans -> plotted at 1x.
  2024-01  OpenAI (Patwardhan et al. 2024, "Building an early warning system
           for LLM-aided biological threat creation"): mild uplift, not
           statistically significant -> plotted at 1x.
  2025-05  Anthropic, System Card: Claude Opus 4 & Claude Sonnet 4 (May 2025),
           bioweapons-acquisition uplift trial: 63% +/- 13% with Opus 4 vs
           25% +/- 13% controls = 2.53x (ASL-3 threshold 2.8x; ASL-3 activated).
  2026-02  Zhang et al. 2026, arXiv:2602.23329, "LLM Novice Uplift on Dual-Use,
           In Silico Biology Tasks": novices with LLMs 4.16x more accurate than
           internet-only controls (95% CI 2.63-6.87); beat experts on 3 of 4
           benchmarks with expert baselines.
  Annotated separately (different metric): Virology Capabilities Test
           (Gotting et al. 2025, arXiv:2504.16137): OpenAI o3 scored 43.8% vs
           expert virologists' 22.1% in their own sub-areas (beats 94% of them).
Caveat: these studies measure knowledge / planning / in-silico tasks, not
wet-lab success; designs differ, so the arc is indicative, not one series.

Usage:
    conda run -n ocean14 python presentations/py/bio_uplift_arc.py
"""
import matplotlib.pyplot as plt

from slide_style import FULL, apply_style, save, RED, GRAY, INK, MUTED

POINTS = [  # (decimal year, uplift, lo, hi, label, text offset (dx, dy))
    (2024.04, 1.0, None, None, "RAND & OpenAI 2024:\nno significant uplift", (-0.15, 0.8)),
    (2024.08, 1.0, None, None, "", (0, 0)),
    (2025.38, 2.53, None, None, "Anthropic, Claude Opus 4\nsystem card: 2.53×", (-0.95, 0.55)),
    (2026.12, 4.16, 2.63, 6.87, "Zhang et al. 2026:\nnovices + AI 4.16×", (-1.05, 1.1)),
]


def main():
    """Created by JXP and Claude. Build a2_bio_uplift.png."""
    apply_style()
    fig, ax = plt.subplots(figsize=FULL)
    xs = [p[0] for p in POINTS]
    ys = [p[1] for p in POINTS]
    ax.plot(xs, ys, color=RED, lw=1.5, alpha=0.5, zorder=1)
    for x, y, lo, hi, label, (dx, dy) in POINTS:
        if lo is not None:
            ax.errorbar(x, y, yerr=[[y - lo], [hi - y]], fmt="none", ecolor=RED, capsize=4, lw=1.4)
        ax.plot(x, y, "o", ms=11, color=RED if y > 1 else GRAY, zorder=3)
        ax.text(x + dx, y + dy, label, fontsize=12, color=INK, va="center")
    ax.axhline(1, color=GRAY, lw=1, ls="--")
    ax.text(2026.45, 0.7, "no help", ha="right", fontsize=11, color=MUTED)
    ax.set_xlim(2023.8, 2026.5)
    ax.set_ylim(0, 7.5)
    ax.set_xticks([2024, 2025, 2026])
    ax.set_ylabel("Uplift: success with AI ÷\nsuccess with internet alone")
    ax.text(2023.85, 6.9, "Also: OpenAI o3 beat 94% of expert virologists on\n"
            "protocol troubleshooting (VCT, 2025)", fontsize=11, color=MUTED, va="top")
    save(fig, "a2_bio_uplift.png",
         "Mouton et al. 2024 (RAND); Patwardhan et al. 2024 (OpenAI); Anthropic Claude Opus 4 system card 2025; "
         "Zhang et al. 2026 (arXiv:2602.23329); Götting et al. 2025 (arXiv:2504.16137). "
         "Knowledge/in-silico tasks, not wet-lab; study designs differ",
         "A2")


if __name__ == "__main__":
    main()
