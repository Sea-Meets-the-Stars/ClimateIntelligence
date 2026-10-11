"""Created by JXP and Claude.

C6b "Sea level is rising: Honolulu" — NOAA tide gauge 1612340 (Honolulu
Harbor), monthly mean sea level with the seasonal cycle removed, 1905-2026,
with a least-squares trend.

Data: NOAA CO-OPS Sea Level Trends, fetched 2026-10-05:
  https://tidesandcurrents.noaa.gov/sltrends/data/1612340_meantrend.txt
cached at presentations/data/honolulu_1612340_meantrend.txt.
Columns: Year, Month, Monthly_MSL (m, relative to the station MSL datum),
Linear_Trend, High_Conf., Low_Conf. (NOAA's own fit, given only through the
end of their trend period). This is RELATIVE sea level (includes any
vertical land motion at the gauge).

Usage:
    conda run -n ocean14 python presentations/py/honolulu_tide_gauge.py
"""
import numpy as np
import matplotlib.pyplot as plt

from slide_style import DATA, MAIN, apply_style, save, BLUE, LBLUE, RED, INK


def load():
    """Created by JXP and Claude. Outputs: decimal year, monthly MSL (mm),
    NOAA trend line (mm, NaN where absent)."""
    rows = []
    for line in (DATA / "honolulu_1612340_meantrend.txt").read_text().splitlines():
        parts = line.split()
        if len(parts) >= 3 and parts[0].isdigit():
            trend = float(parts[3]) if len(parts) > 3 else np.nan
            rows.append((int(parts[0]) + (int(parts[1]) - 0.5) / 12, float(parts[2]) * 1000, trend * 1000))
    a = np.array(rows)
    return a[:, 0], a[:, 1], a[:, 2]


def main():
    """Created by JXP and Claude. Build c6b_honolulu.png."""
    apply_style()
    t, msl, noaa_trend = load()
    p = np.polyfit(t, msl, 1)
    has = ~np.isnan(noaa_trend)
    noaa_rate = np.polyfit(t[has], noaa_trend[has], 1)[0]
    rise_cm = p[0] * (t[-1] - t[0]) / 10
    print(f"Honolulu {t[0]:.1f}-{t[-1]:.1f}: fit {p[0]:.2f} mm/yr (NOAA trend line slope {noaa_rate:.2f}); "
          f"~{rise_cm:.0f} cm over the record")

    # Annual means for a readable line on top of the monthly scatter.
    years = np.floor(t).astype(int)
    uy = np.array([y for y in np.unique(years) if (years == y).sum() >= 10])
    am = np.array([msl[years == y].mean() for y in uy])
    zero = am[:10].mean()  # first decade = 0

    fig, ax = plt.subplots(figsize=MAIN)
    ax.plot(t, msl - zero, ".", ms=2.5, color=LBLUE, alpha=0.6)
    ax.plot(uy + 0.5, am - zero, color=BLUE, lw=2)
    ax.plot(t, np.polyval(p, t) - zero, "--", color=RED, lw=2)
    ax.text(1908, 370, f"+{p[0]:.1f} mm per year\n≈ {rise_cm:.0f} cm since {int(t[0])}",
            fontsize=15, color=RED, va="top", fontweight="bold")
    ax.set_xlim(1903, 2028)
    ax.set_ylim(-150, 380)
    ax.set_ylabel("Honolulu sea level\nvs 1905–1914 (mm)")
    save(fig, "c6b_honolulu.png",
         f"Data: NOAA CO-OPS tide gauge 1612340, Honolulu Harbor, monthly means (seasonal cycle removed), "
         f"{int(t[0])}–{int(t[-1])}; relative sea level",
         "C6b")


if __name__ == "__main__":
    main()
