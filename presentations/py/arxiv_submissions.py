"""Created by JXP and Claude.

A5 "AI will force the collapse of peer review" — arXiv monthly new
submissions, 1991-2026, log axis, with the author-chosen callouts and the
1 Oct 2026 rate-limit policy.

Data: arXiv, monthly submission statistics, fetched 2026-10-05:
  https://arxiv.org/stats/get_monthly_submissions
cached at presentations/data/arxiv_monthly_submissions.csv.
Callout values (match arXiv blog, 1 Oct 2026, "Updated rate limit policy",
https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/):
  Sep 2016 9,869; Sep 2024 20,569; Sep 2026 40,363 ("doubled in two years").
  Policy: at most 2 submissions per author per calendar month, 3 active.

Usage:
    conda run -n ocean14 python presentations/py/arxiv_submissions.py
"""
import csv

import numpy as np
import matplotlib.pyplot as plt

from slide_style import FULL, DATA, apply_style, save, BLUE, RED, INK, GRAY

CALLOUTS = ["2016-09", "2024-09", "2026-09"]
LAST_COMPLETE_MONTH = "2026-09"  # data fetched 2026-10-05


def load():
    """Created by JXP and Claude. Outputs: list of 'YYYY-MM', decimal year,
    submissions per month."""
    months, t, n = [], [], []
    with open(DATA / "arxiv_monthly_submissions.csv") as f:
        for r in csv.DictReader(f):
            if r["month"] > LAST_COMPLETE_MONTH:
                continue  # drop the partial current month
            y, m = map(int, r["month"].split("-"))
            months.append(r["month"]); t.append(y + (m - 0.5) / 12); n.append(int(r["submissions"]))
    return months, np.array(t), np.array(n)


def main():
    """Created by JXP and Claude. Build a5_arxiv.png."""
    apply_style()
    months, t, n = load()
    vals = {m: v for m, v in zip(months, n)}
    print("callouts:", {m: vals[m] for m in CALLOUTS}, f"; 2024-09 -> 2026-09 x{vals['2026-09'] / vals['2024-09']:.2f}")

    fig, ax = plt.subplots(figsize=FULL)
    ax.plot(t, n, color=BLUE, lw=1.6)
    text_at = {"2016-09": (2003.5, 1.8e4), "2024-09": (2008.5, 5.0e4), "2026-09": (2011.5, 1.4e5)}
    for m in CALLOUTS:
        x = int(m[:4]) + (int(m[5:]) - 0.5) / 12
        tx, ty = text_at[m]
        ax.plot(x, vals[m], "o", ms=7, color=RED if m == "2026-09" else BLUE, zorder=3)
        ax.annotate(f"{m[:4]}: {vals[m]:,}/month", (x, vals[m]), xytext=(tx, ty),
                    fontsize=12, color=RED if m == "2026-09" else INK,
                    fontweight="bold" if m == "2026-09" else "normal",
                    arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.8))
    ax.axvline(2026.75, color=RED, lw=1.2, ls="--")
    ax.text(2026.3, 30, "1 Oct 2026:\narXiv caps authors\nat 2 papers/month", ha="right",
            fontsize=12, color=RED)
    ax.set_yscale("log")
    ax.set_xlim(1991.5, 2027.5)
    ax.set_ylim(10, 3e5)
    ax.set_ylabel("New arXiv submissions\nper month")
    save(fig, "a5_arxiv.png",
         "Data: arXiv monthly submission statistics (arxiv.org/stats); arXiv blog, 1 Oct 2026, "
         "“Updated rate limit policy”",
         "A5")


if __name__ == "__main__":
    main()
