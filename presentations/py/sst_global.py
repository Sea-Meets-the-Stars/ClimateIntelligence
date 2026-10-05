"""Created by JXP and Claude.

C4a "The ocean is warming: surface" — global ocean surface temperature
anomaly, annual means 1850-2025 (+ 2026 to date).

Data: NOAA NCEI Climate at a Glance, global ocean monthly temperature
departures (NOAAGlobalTemp; ocean component from ERSSTv5), base 1901-2000,
fetched 2026-10-05:
  https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/ocean/tavg/1/0/1850-2026/data.csv
cached at presentations/data/noaa_cag_global_ocean.csv.
Instruments: ship buckets and engine intakes -> moored and drifting buoys
-> Argo floats (near-surface).

Usage:
    conda run -n ocean14 python presentations/py/sst_global.py
"""
import numpy as np
import matplotlib.pyplot as plt

from slide_style import FULL, DATA, apply_style, save, RED, BLUE, GRAY, INK


def load_monthly():
    """Created by JXP and Claude. Outputs: year (int array), month (int
    array), anomaly (C, base 1901-2000)."""
    rows = np.genfromtxt(DATA / "noaa_cag_global_ocean.csv", delimiter=",",
                         comments="#", skip_header=1, dtype=float)
    # Header lines start with '#'; first non-comment line is 'Date,...'.
    rows = rows[~np.isnan(rows[:, 0])]
    date = rows[:, 0].astype(int)
    return date // 100, date % 100, rows[:, 1]


def annual_means(year, month, anom):
    """Created by JXP and Claude. Calendar-year means of complete years.
    Outputs: years, means, (partial_year, partial_mean, n_months)."""
    years, means = [], []
    for y in np.unique(year):
        m = year == y
        if m.sum() == 12:
            years.append(y); means.append(anom[m].mean())
    last = year.max()
    m = year == last
    partial = (last, anom[m].mean(), int(m.sum())) if m.sum() < 12 else None
    return np.array(years), np.array(means), partial


def main():
    """Created by JXP and Claude. Build c4a_sst_global.png."""
    apply_style()
    year, month, anom = load_monthly()
    yrs, means, partial = annual_means(year, month, anom)
    print(f"annual means {yrs[0]}-{yrs[-1]}; warmest {yrs[np.argmax(means)]} = {means.max():.2f} C; "
          f"partial {partial}")

    fig, ax = plt.subplots(figsize=FULL)
    ax.bar(yrs, means, width=0.9, color=np.where(means >= 0, RED, BLUE))
    if partial:
        ax.bar(partial[0], partial[1], width=0.9, color="none", edgecolor=RED, lw=1.2)
        mon = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][partial[2]]
        ax.text(2027, 1.17, f"outlined: {partial[0]}, Jan–{mon}", ha="right", fontsize=11, color=INK)
    iw = np.argmax(means)
    ax.annotate(f"{yrs[iw]}: +{means[iw]:.2f} °C", (yrs[iw], means[iw]),
                xytext=(1945, 0.85), fontsize=13, color=RED,
                arrowprops=dict(arrowstyle="-", color=RED, lw=0.8))
    ax.axhline(0, color=GRAY, lw=0.8)
    ax.set_xlim(1848, 2029)
    ax.set_ylim(-0.75, 1.25)
    ax.set_ylabel("Ocean surface temperature\nvs 1901–2000 average (°C)")
    ax.grid(axis="x", visible=False)
    save(fig, "c4a_sst_global.png",
         f"Data: NOAA NCEI Climate at a Glance, global ocean surface (NOAAGlobalTemp / ERSSTv5), annual means "
         f"{yrs[0]}–{yrs[-1]}; ships → buoys → Argo",
         "C4a")


if __name__ == "__main__":
    main()
