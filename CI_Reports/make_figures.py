"""Created by JXP and Claude.

Generate the original figures for the initial Climate Intelligence report
(CI_2026_07_09_climate_report.md). Each figure is built from real, publicly
archived data cached under CI_Reports/data/ (fetched 2026-07-09); provenance and
baselines are annotated on the figures themselves.

Data sources (see references in the report):
  - CO2/CH4/N2O: NOAA Global Monitoring Laboratory (gml.noaa.gov)
  - Global surface temperature: NASA GISTEMP v4 (data.giss.nasa.gov)
  - Ocean heat content 0-2000 m: NOAA NCEI (Levitus/WOA)
  - Global mean sea level: CSIRO Church & White reconstruction (1880-2013)

Run under the project conda environment:
    conda run -n ocean14 python CI_Reports/make_figures.py

Design choices follow the project coding guidelines: functions (no classes),
imports at top, inline comments, matplotlib for plotting, docstrings with
inputs/outputs, and "Created by JXP and Claude" on the file and each method.
"""

# Imports at the top of the file (project coding guideline).
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")  # headless backend; we save PNGs, never display
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

# A single consistent visual style across all figures.
plt.rcParams.update({
    "figure.dpi": 130,
    "savefig.dpi": 130,
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def load_co2():
    """Created by JXP and Claude.

    Load NOAA Mauna Loa monthly CO2.

    Inputs
    ------
    (none) reads data/co2_mm_mlo.txt

    Outputs
    -------
    (np.ndarray, np.ndarray, np.ndarray)
        decimal_date, monthly_mean_ppm, deseasonalized_ppm.
    """
    # Columns: year month decimal average deseasonalized ndays sdev unc
    rows = np.genfromtxt(DATA / "co2_mm_mlo.txt", comments="#")
    return rows[:, 2], rows[:, 3], rows[:, 4]


def load_trace_gas(fname):
    """Created by JXP and Claude.

    Load a NOAA global monthly trace-gas file (CH4 or N2O).

    Inputs
    ------
    fname : str
        File name under data/ (e.g. 'ch4_mm_gl.txt').

    Outputs
    -------
    (np.ndarray, np.ndarray)
        decimal_date, globally averaged mole fraction (missing -9.99 removed).
    """
    # Columns: year month decimal average average_unc trend trend_unc
    rows = np.genfromtxt(DATA / fname, comments="#")
    date, val = rows[:, 2], rows[:, 3]
    good = val > 0  # NOAA uses -9.99 for missing months
    return date[good], val[good]


def load_gistemp():
    """Created by JXP and Claude.

    Load NASA GISTEMP v4 annual global-mean anomaly (baseline 1951-1980).

    Inputs
    ------
    (none) reads data/gistemp_glb.csv

    Outputs
    -------
    (np.ndarray, np.ndarray)
        year, annual-mean anomaly in degC (J-D column; missing rows dropped).
    """
    years, anom = [], []
    # First line is a title; second line is the header; data begins line 3.
    for line in (DATA / "gistemp_glb.csv").read_text().splitlines()[2:]:
        parts = line.split(",")
        jd = parts[13]  # 'J-D' annual mean column
        if jd.strip() in ("***", ""):
            continue
        years.append(int(parts[0]))
        # GISTEMP writes values like '-.19'; float() handles the leading dot.
        anom.append(float(jd))
    return np.array(years), np.array(anom)


def load_ohc():
    """Created by JXP and Claude.

    Load NOAA NCEI global ocean heat content anomaly, 0-2000 m.

    Inputs
    ------
    (none) reads data/ohc_2000m.csv

    Outputs
    -------
    (np.ndarray, np.ndarray, np.ndarray)
        year, world-ocean OHC anomaly (10^22 J), 1-sigma error.
    """
    # Columns: YEAR WO WOse NH NHse SH SHse
    rows = np.genfromtxt(DATA / "ohc_2000m.csv", skip_header=1)
    return rows[:, 0], rows[:, 1], rows[:, 2]


def load_sea_level():
    """Created by JXP and Claude.

    Load the CSIRO Church & White global mean sea-level reconstruction.

    Inputs
    ------
    (none) reads data/gmsl_church_white.csv

    Outputs
    -------
    (np.ndarray, np.ndarray, np.ndarray)
        year, GMSL (mm), 1-sigma uncertainty (mm).
    """
    rows = np.genfromtxt(DATA / "gmsl_church_white.csv", delimiter=",", skip_header=1)
    return rows[:, 0], rows[:, 1], rows[:, 2]


def fig_co2(outpath):
    """Created by JXP and Claude.

    Figure 1: the Keeling Curve — Mauna Loa monthly CO2 with the
    seasonally adjusted trend.

    Inputs
    ------
    outpath : Path — PNG destination.

    Outputs
    -------
    None. Writes the figure to disk.
    """
    date, monthly, deseason = load_co2()
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(date, monthly, lw=0.8, color="#4a90d9", label="Monthly mean")
    ax.plot(date, deseason, lw=1.8, color="#c0392b", label="Seasonally adjusted trend")
    ax.axhline(280, ls="--", color="gray", lw=1)
    ax.text(1962, 285, "pre-industrial ~280 ppm", color="gray", fontsize=9)
    ax.set_xlabel("Year")
    ax.set_ylabel("CO$_2$ (ppm)")
    ax.set_title("Atmospheric CO$_2$ at Mauna Loa (the Keeling Curve)")
    ax.legend(loc="upper left")
    ax.text(0.99, 0.02, "Data: NOAA GML. The saw-tooth is the Northern Hemisphere\n"
            "biosphere breathing; the rise is anthropogenic.",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=8, color="#555")
    fig.tight_layout()
    fig.savefig(outpath)
    plt.close(fig)


def fig_temperature(outpath):
    """Created by JXP and Claude.

    Figure 2: global surface temperature anomaly (GISTEMP) with a LOWESS-style
    smoothing and an explicit note on baseline and inter-dataset spread.

    Inputs
    ------
    outpath : Path — PNG destination.

    Outputs
    -------
    None. Writes the figure to disk.
    """
    year, anom = load_gistemp()
    # Simple centered moving average (5-yr) as the smooth trend line.
    win = 5
    kernel = np.ones(win) / win
    smooth = np.convolve(anom, kernel, mode="same")
    smooth[:win] = np.nan
    smooth[-win:] = np.nan

    fig, ax = plt.subplots(figsize=(8, 4.5))
    # Colour bars by sign relative to baseline for quick visual reading.
    colors = ["#c0392b" if a >= 0 else "#4a90d9" for a in anom]
    ax.bar(year, anom, color=colors, width=0.9, alpha=0.6)
    ax.plot(year, smooth, color="black", lw=2, label="5-year mean")
    ax.axhline(0, color="gray", lw=0.8)
    ax.set_xlabel("Year")
    ax.set_ylabel("Anomaly (°C) vs 1951-1980")
    ax.set_title("Global surface temperature anomaly (NASA GISTEMP v4)")
    ax.legend(loc="upper left")
    ax.text(0.99, 0.02,
            "Data: NASA GISTEMP v4 (baseline 1951-1980). Add ~0.3 °C to compare\n"
            "with an 1850-1900 pre-industrial baseline. GISS/NOAA/HadCRUT5/Berkeley\n"
            "agree within ~0.05 °C on recent trends.",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=8, color="#555")
    fig.tight_layout()
    fig.savefig(outpath)
    plt.close(fig)


def fig_sea_level(outpath):
    """Created by JXP and Claude.

    Figure 3: global mean sea level (CSIRO Church & White reconstruction) with
    the 1-sigma uncertainty envelope, illustrating acceleration.

    Inputs
    ------
    outpath : Path — PNG destination.

    Outputs
    -------
    None. Writes the figure to disk.
    """
    year, gmsl, unc = load_sea_level()
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.fill_between(year, gmsl - unc, gmsl + unc, color="#4a90d9", alpha=0.25,
                    label="1$\\sigma$ uncertainty")
    ax.plot(year, gmsl, color="#1f5fa6", lw=1.8, label="GMSL reconstruction")

    # Illustrate acceleration: fit early (1901-1990) vs late (1993-2013) rates.
    def _rate(y0, y1):
        m = (year >= y0) & (year <= y1)
        p = np.polyfit(year[m], gmsl[m], 1)
        return p[0]  # mm/yr
    early = _rate(1901, 1990)
    late = _rate(1993, 2013)
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea level (mm, relative)")
    ax.set_title("Global mean sea level, 1880-2013 (CSIRO reconstruction)")
    ax.legend(loc="upper left")
    ax.text(0.99, 0.02,
            f"Data: Church & White (CSIRO). Mean rate 1901-1990 = {early:.1f} mm/yr;\n"
            f"1993-2013 = {late:.1f} mm/yr — the rise is accelerating.",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=8, color="#555")
    fig.tight_layout()
    fig.savefig(outpath)
    plt.close(fig)


def fig_ocean_heat(outpath):
    """Created by JXP and Claude.

    Figure 4: global ocean heat content anomaly, 0-2000 m, with error bars —
    the least-noisy indicator of planetary energy imbalance.

    Inputs
    ------
    outpath : Path — PNG destination.

    Outputs
    -------
    None. Writes the figure to disk.
    """
    year, ohc, se = load_ohc()
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.errorbar(year, ohc, yerr=se, fmt="o-", color="#b9430f", ecolor="#e0a080",
                capsize=3, lw=1.8, ms=4, label="0-2000 m OHC")
    # Linear trend and its conversion to W/m^2 over Earth's surface.
    p = np.polyfit(year, ohc, 1)
    ax.plot(year, np.polyval(p, year), "--", color="black", lw=1.2,
            label=f"trend {p[0]:.2f}×10$^{{22}}$ J/yr")
    # 1 ZJ/yr = 1e21 J/yr; divide by seconds/yr and Earth area 5.1e14 m^2.
    wm2 = (p[0] * 1e22) / (365.25 * 86400) / 5.1e14
    ax.set_xlabel("Year")
    ax.set_ylabel("OHC anomaly (10$^{22}$ J)")
    ax.set_title("Global ocean heat content, 0-2000 m (NOAA NCEI)")
    ax.legend(loc="upper left")
    ax.text(0.99, 0.02,
            f"Data: NOAA NCEI. Trend ≈ {wm2:.2f} W/m² over Earth's surface.\n"
            "The ocean holds >90% of the excess heat; OHC has the smallest\n"
            "relative uncertainty of the major climate indicators.",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=8, color="#555")
    fig.tight_layout()
    fig.savefig(outpath)
    plt.close(fig)


def fig_ghg_trio(outpath):
    """Created by JXP and Claude.

    Figure 5: the three long-lived greenhouse gases (CO2, CH4, N2O) on a shared
    time axis, each on its own scale, to show synchronous anthropogenic rise.

    Inputs
    ------
    outpath : Path — PNG destination.

    Outputs
    -------
    None. Writes the figure to disk.
    """
    co2_d, co2_v, _ = load_co2()
    ch4_d, ch4_v = load_trace_gas("ch4_mm_gl.txt")
    n2o_d, n2o_v = load_trace_gas("n2o_mm_gl.txt")

    fig, axes = plt.subplots(3, 1, figsize=(8, 7), sharex=True)
    axes[0].plot(co2_d, co2_v, color="#c0392b")
    axes[0].set_ylabel("CO$_2$ (ppm)")
    axes[0].set_title("The three principal long-lived greenhouse gases")
    axes[1].plot(ch4_d, ch4_v, color="#8e44ad")
    axes[1].set_ylabel("CH$_4$ (ppb)")
    axes[2].plot(n2o_d, n2o_v, color="#16a085")
    axes[2].set_ylabel("N$_2$O (ppb)")
    axes[2].set_xlabel("Year")
    axes[2].text(0.99, 0.04,
                 "Data: NOAA GML (CO$_2$ Mauna Loa; CH$_4$/N$_2$O global).",
                 transform=axes[2].transAxes, ha="right", va="bottom",
                 fontsize=8, color="#555")
    fig.tight_layout()
    fig.savefig(outpath)
    plt.close(fig)


def fig_tcre(outpath):
    """Created by JXP and Claude.

    Figure 6: the near-linear relationship between cumulative CO2 emissions and
    warming (TCRE). Constructed from the IPCC AR6 central value
    (0.45 °C per 1000 GtCO2) with its likely range, annotated with the historical
    point and the remaining 1.5/2.0 °C budgets.

    Inputs
    ------
    outpath : Path — PNG destination.

    Outputs
    -------
    None. Writes the figure to disk.
    """
    # Cumulative CO2 axis, 0 to 4000 GtCO2.
    cum = np.linspace(0, 4000, 200)
    tcre_mid, tcre_lo, tcre_hi = 0.45, 0.27, 0.63  # °C per 1000 GtCO2 (AR6)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.fill_between(cum, cum / 1000 * tcre_lo, cum / 1000 * tcre_hi,
                    color="#c0392b", alpha=0.15, label="likely range (AR6)")
    ax.plot(cum, cum / 1000 * tcre_mid, color="#c0392b", lw=2,
            label="0.45 °C / 1000 GtCO$_2$")
    # Historical point: ~2400 GtCO2 emitted 1850-2019 -> ~1.07 degC human-caused.
    ax.plot(2400, 1.07, "ko", ms=7)
    ax.annotate("historical\n(~2400 GtCO$_2$, ~1.07 °C)", (2400, 1.07),
                textcoords="offset points", xytext=(-10, 10), ha="right", fontsize=9)
    for target, label in [(1.5, "1.5 °C"), (2.0, "2.0 °C")]:
        ax.axhline(target, ls=":", color="gray", lw=1)
        ax.text(50, target + 0.03, label, color="gray", fontsize=9)
    ax.set_xlabel("Cumulative CO$_2$ emissions since 1850 (GtCO$_2$)")
    ax.set_ylabel("Human-caused warming (°C)")
    ax.set_title("Warming is near-linear in cumulative CO$_2$ (TCRE)")
    ax.legend(loc="lower right")
    ax.text(0.01, 0.97,
            "Physics: this near-linearity is why 'net-zero CO$_2$' is a\n"
            "requirement, not a slogan — warming roughly halts when\n"
            "cumulative emissions stop growing.",
            transform=ax.transAxes, ha="left", va="top", fontsize=8, color="#555")
    fig.tight_layout()
    fig.savefig(outpath)
    plt.close(fig)


def main():
    """Created by JXP and Claude.

    Build all six figures into CI_Reports/.

    Inputs
    ------
    (none)

    Outputs
    -------
    None. Writes six PNG files and prints their paths.
    """
    jobs = [
        (fig_co2, "fig1_keeling_curve.png"),
        (fig_temperature, "fig2_global_temperature.png"),
        (fig_sea_level, "fig3_sea_level.png"),
        (fig_ocean_heat, "fig4_ocean_heat_content.png"),
        (fig_ghg_trio, "fig5_ghg_trio.png"),
        (fig_tcre, "fig6_tcre.png"),
    ]
    for func, name in jobs:
        out = HERE / name
        func(out)
        print(f"wrote {out.name}")


if __name__ == "__main__":
    main()
