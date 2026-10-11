"""Created by JXP and Claude.

Slide 5 "Humans suck at exponentials" — slide version of Blog 001 Figure 1
(U.S. cumulative COVID-19 cases, log axis, 2.4-day doubling in March 2020),
without the blog's in-figure title and figure number. Data, loader and fit are
imported from blogs/blog001/make_fig1_covid_us_cases.py so the numbers match.

Data: Johns Hopkins CSSE via Our World in Data (cached in blogs/blog001/data/).

Usage:
    conda run -n ocean14 python presentations/py/covid_slide.py
"""
import sys

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from slide_style import ROOT, FULL, apply_style, save, BLUE, ORANGE

sys.path.insert(0, str(ROOT / "blogs" / "blog001"))
import make_fig1_covid_us_cases as covid  # noqa: E402


def main():
    """Created by JXP and Claude. Build s5_covid.png."""
    apply_style()
    df = covid.load_us_cases(covid.DATA_CSV)
    doubling_days, fit_dates, fit_cases = covid.fit_doubling_time(df, covid.FIT_START, covid.FIT_END)
    print(f"doubling every {doubling_days:.1f} days ({covid.FIT_START} to {covid.FIT_END})")

    fig, ax = plt.subplots(figsize=FULL)
    ax.plot(df["date"], df["cases"], color=BLUE, lw=2.4)
    ax.plot(fit_dates, fit_cases, color=ORANGE, lw=2.4, ls="--", zorder=4)
    ax.set_yscale("log")
    ax.yaxis.set_major_formatter(FuncFormatter(
        lambda v, _: {1: "1", 1e2: "100", 1e4: "10,000", 1e6: "1 million", 1e8: "100 million"}.get(v, "")))
    ax.annotate(f"doubling every ~{doubling_days:.1f} days\n(March 2020)",
                (fit_dates.iloc[len(fit_dates) // 2], fit_cases[len(fit_cases) // 2]),
                xytext=(df["date"].iloc[0] + (df["date"].iloc[-1] - df["date"].iloc[0]) * 0.18, 3e2),
                fontsize=15, color=ORANGE, arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1))
    ax.set_ylabel("U.S. COVID-19 cases\n(cumulative, log scale)")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    save(fig, "s5_covid.png", "Data: Johns Hopkins CSSE via Our World in Data (as in Blog 001, Figure 1)", "5")


if __name__ == "__main__":
    main()
