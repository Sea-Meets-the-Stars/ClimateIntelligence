"""Created by JXP and Claude.

A9 "The AI bubble will pop (with a few major winners)" — capital spending by
the four largest AI hyperscalers, 2019-2025 actual and 2026 guidance.

Actuals (US$ billions): cash purchases of property & equipment from each
company's 10-K, via SEC EDGAR XBRL company facts (fetched 2026-10-05,
https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json; cached at
presentations/data/sec_facts_{MSFT,GOOGL,AMZN,META}.json):
  Microsoft  PaymentsToAcquirePropertyPlantAndEquipment  (fiscal years ending June)
  Alphabet   PaymentsToAcquirePropertyPlantAndEquipment
  Amazon     PaymentsToAcquireProductiveAssets
  Meta       PaymentsToAcquirePropertyPlantAndEquipment
  (Excludes finance leases, so understates total build-out for MSFT/META.)
2026 guidance (calendar 2026, as of Q2-2026 earnings calls, July 2026;
compiled in Platformonomics, "Follow the CAPEX: Q2 2026 Scoreboard",
https://platformonomics.com/2026/07/follow-the-capex-q2-2026-scoreboard/):
  Amazon ~$220B; Alphabet $195-205B (mid 200); Meta $130-145B incl. finance
  lease principal (mid 137.5); Microsoft ~$175B (calendar year, after a
  finance->operating lease reclassification).

Usage:
    conda run -n ocean14 python presentations/py/ai_capex.py
"""
import json
from datetime import date

import numpy as np
import matplotlib.pyplot as plt

from slide_style import DATA, MAIN, apply_style, save, BLUE, RED, ORANGE, TEAL, GRAY, INK

COMPANIES = [  # (ticker, label, XBRL concept, color)
    ("MSFT", "Microsoft", "PaymentsToAcquirePropertyPlantAndEquipment", BLUE),
    ("GOOGL", "Alphabet", "PaymentsToAcquirePropertyPlantAndEquipment", RED),
    ("AMZN", "Amazon", "PaymentsToAcquireProductiveAssets", ORANGE),
    ("META", "Meta", "PaymentsToAcquirePropertyPlantAndEquipment", TEAL),
]
YEARS = list(range(2019, 2026))
GUIDANCE_2026 = {"MSFT": 175.0, "GOOGL": 200.0, "AMZN": 220.0, "META": 137.5}


def annual_capex(ticker, concept):
    """Created by JXP and Claude. Full-year 10-K values from SEC company
    facts. Output: dict fiscal-period-end-year -> US$ billions."""
    d = json.load(open(DATA / f"sec_facts_{ticker}.json"))
    out = {}
    for u in d["facts"]["us-gaap"][concept]["units"]["USD"]:
        if u.get("form") != "10-K" or "start" not in u:
            continue
        s, e = date.fromisoformat(u["start"]), date.fromisoformat(u["end"])
        if (e - s).days > 350:
            out[e.year] = u["val"] / 1e9  # later filings overwrite restated values
    return out


def main():
    """Created by JXP and Claude. Build a9_ai_capex.png."""
    apply_style()
    data = {t: annual_capex(t, c) for t, _, c, _ in COMPANIES}
    totals = [sum(data[t][y] for t, *_ in COMPANIES) for y in YEARS]
    g_total = sum(GUIDANCE_2026.values())
    for y, tot in zip(YEARS, totals):
        print(y, " ".join(f"{t} {data[t][y]:.1f}" for t, *_ in COMPANIES), f"total {tot:.1f}")
    print(f"2026 guidance total {g_total:.1f}")

    fig, ax = plt.subplots(figsize=MAIN)
    x = np.arange(len(YEARS) + 1)
    bottom = np.zeros(len(x))
    for t, label, _, color in COMPANIES:
        vals = np.array([data[t][y] for y in YEARS] + [GUIDANCE_2026[t]])
        bars = ax.bar(x, vals, bottom=bottom, color=color, width=0.7, label=label)
        bars[-1].set_alpha(0.45)
        bars[-1].set_hatch("//")
        bottom += vals
    for xi, tot in zip(x, totals + [g_total]):
        ax.text(xi, tot + 12, f"${tot:.0f}B", ha="center", fontsize=12, color=INK,
                fontweight="bold" if xi == x[-1] else "normal")
    ax.set_xticks(x)
    ax.set_xticklabels([str(y) for y in YEARS] + ["2026\nguidance"])
    ax.set_ylim(0, 820)
    ax.set_ylabel("Capital spending\n(US$ billions per year)")
    ax.legend(loc="upper left", frameon=False, ncol=2)
    ax.grid(axis="x", visible=False)
    save(fig, "a9_ai_capex.png",
         "Data: company 10-K filings via SEC EDGAR (cash purchases of property & equipment; Microsoft fiscal "
         "years end June). 2026: guidance from July 2026 earnings calls (Platformonomics compilation)",
         "A9")


if __name__ == "__main__":
    main()
