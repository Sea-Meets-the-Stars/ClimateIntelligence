"""What does "emissions" mean in Blog 001 Figure 4?  A definitions check.

Created by JXP and Claude.

Written to answer a reader's (Richard N.) question about Figure 4: which
"emissions" are plotted, and would "retained atmospheric CO2" tell a
different story?  The script quantifies, from data already cached in the
repo, how the fitted doubling time depends on the definition:

    A. fossil fuel + industry CO2        (what Figure 4 actually plots)
    B. A + land-use change CO2           (deforestation etc.)
    C. all greenhouse gases, CO2-eq      (CO2 + CH4 + N2O + F-gases, incl. LUC)
    D. cumulative CO2 since 1750         (A and B integrated over time)
    E. retained atmospheric CO2          (Mauna Loa minus 280 ppm pre-industrial)

It also computes the decadal airborne fraction (E's growth / B) as a direct
test of the claim that the natural sinks are being "crippled".  Feedback
sources (permafrost, soils, weakening ocean uptake) are not in any
emissions inventory; they show up only as changes in the sinks, which is
exactly what the airborne fraction tracks.

Data (cached, do not re-fetch):
    climate_intelligence/data/raw/owid-co2-data.csv
        Global Carbon Project / OWID, country == "World": columns ``co2``,
        ``co2_including_luc``, ``land_use_change_co2``, ``total_ghg``
        (all Mt CO2 or Mt CO2-eq per year), ``cumulative_co2``,
        ``cumulative_co2_including_luc`` (Mt CO2).
    CI_Reports/data/co2_mm_mlo.txt
        NOAA GML Mauna Loa monthly mean CO2 (ppm), 1958-present.

Usage:
    conda run -n ocean14 python blogs/blog001/calc_fig4_emissions_definitions.py

Outputs:
    Printed table of doubling times and airborne fractions, and
    blogs/blog001/fig4_alt_emissions_definitions.png  (a two-panel
    comparison figure: annual flows on the left, stocks on the right).
"""

import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Paths anchored to this script's directory so it runs from anywhere.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
OWID_CSV = os.path.join(
    REPO_DIR, "climate_intelligence", "data", "raw", "owid-co2-data.csv")
MLO_TXT = os.path.join(REPO_DIR, "CI_Reports", "data", "co2_mm_mlo.txt")
OUT_PNG = os.path.join(SCRIPT_DIR, "fig4_alt_emissions_definitions.png")

# Physical constants.
PREINDUSTRIAL_PPM = 280.0   # pre-industrial CO2 (AR6: ~278 ppm in 1750)
GTCO2_PER_PPM = 7.78        # 1 ppm CO2 = 2.124 GtC = 7.78 GtCO2 (AR6 WGI)

# Fit windows used in Figure 4 and for the comparison.
FIT_WINDOWS = [(1850, 1970), (1970, 2024), (2010, 2024)]


def load_owid_world(csv_path):
    """Load the OWID/GCP world series needed here.

    Parameters
    ----------
    csv_path : str
        Path to owid-co2-data.csv.

    Returns
    -------
    world : pandas.DataFrame
        Indexed by ``year``; columns ``co2``, ``co2_including_luc``,
        ``land_use_change_co2``, ``total_ghg``, ``cumulative_co2``,
        ``cumulative_co2_including_luc`` (Mt CO2 or Mt CO2-eq).
    """
    cols = ["country", "year", "co2", "co2_including_luc",
            "land_use_change_co2", "total_ghg", "cumulative_co2",
            "cumulative_co2_including_luc"]
    df = pd.read_csv(csv_path, usecols=cols)
    world = (df[df["country"] == "World"].drop(columns="country")
             .set_index("year").sort_index())
    return world


def load_mauna_loa_annual(txt_path):
    """Load NOAA Mauna Loa monthly CO2 and reduce to annual means.

    Parameters
    ----------
    txt_path : str
        Path to co2_mm_mlo.txt (NOAA GML format; '#' comment lines;
        columns year, month, decimal date, monthly mean, de-seasonalized,
        ndays, sdev, unc; missing monthly means are -99.99).

    Returns
    -------
    annual : pandas.Series
        Annual mean CO2 (ppm) indexed by year, full calendar years only.
    """
    df = pd.read_csv(txt_path, comment="#", sep=r"\s+", header=None,
                     usecols=[0, 1, 3], names=["year", "month", "ppm"])
    df = df[df["ppm"] > 0]  # drop -99.99 missing flags
    counts = df.groupby("year")["month"].count()
    full_years = counts[counts == 12].index
    annual = df[df["year"].isin(full_years)].groupby("year")["ppm"].mean()
    return annual


def doubling_time(series, start, end):
    """Least-squares exponential fit; return the doubling time in years.

    Parameters
    ----------
    series : pandas.Series
        Positive values indexed by year.
    start, end : int
        Inclusive year bounds of the fit window.

    Returns
    -------
    t_double : float
        Doubling time (years) from a straight-line fit to log2(value).
        NaN if fewer than 3 points fall in the window.
    """
    win = series.loc[start:end].dropna()
    win = win[win > 0]
    # Refuse windows the series does not actually cover (e.g. asking the
    # 1959-present Mauna Loa series for an 1850-1970 fit), so a short tail
    # of data is not reported as if it were the full window.
    if len(win) < 3 or win.index.min() > start + 5:
        return np.nan
    slope, _ = np.polyfit(win.index.to_numpy(float),
                          np.log2(win.to_numpy(float)), 1)
    return 1.0 / slope


def airborne_fraction_by_decade(excess_gtco2, emissions_mt):
    """Fraction of emitted CO2 that stayed in the atmosphere, per decade.

    Parameters
    ----------
    excess_gtco2 : pandas.Series
        Atmospheric CO2 above pre-industrial, in GtCO2, indexed by year.
    emissions_mt : pandas.Series
        Annual fossil + land-use CO2 emissions (Mt CO2/yr) indexed by year.

    Returns
    -------
    table : pandas.DataFrame
        One row per decade: ``retained`` and ``emitted`` (GtCO2) and
        ``airborne_fraction`` = retained / emitted.
    """
    rows = []
    for d0 in range(1960, 2030, 10):
        d1 = min(d0 + 10, int(excess_gtco2.index.max()))
        if d1 <= d0 or d0 not in excess_gtco2.index:
            continue
        retained = excess_gtco2.loc[d1] - excess_gtco2.loc[d0]
        # Emissions during years d0+1 .. d1 drive the change d0 -> d1.
        emitted = emissions_mt.loc[d0 + 1:d1].sum() / 1000.0
        rows.append({"decade": f"{d0}-{d1}", "retained": retained,
                     "emitted": emitted,
                     "airborne_fraction": retained / emitted})
    return pd.DataFrame(rows).set_index("decade")


def make_figure(world, excess_ppm, out_png):
    """Two-panel comparison of the candidate "emissions" definitions.

    Left: annual flows (fossil+industry, fossil+LUC, all-GHG CO2-eq) on a
    log axis.  Right: stocks (cumulative emitted CO2 vs. CO2 retained in
    the atmosphere) on a log axis in GtCO2 so they share a scale; the gap
    between them is what the ocean and land sinks have taken up.

    Parameters
    ----------
    world : pandas.DataFrame
        From :func:`load_owid_world`.
    excess_ppm : pandas.Series
        Mauna Loa annual mean minus pre-industrial (ppm), indexed by year.
    out_png : str
        Output PNG path.
    """
    plt.rcParams.update({
        "figure.dpi": 130, "savefig.dpi": 130, "font.family": "sans-serif",
        "font.size": 10.5, "axes.titlesize": 12.5, "axes.labelsize": 11,
        "axes.edgecolor": "#9aa4af", "axes.linewidth": 0.8,
        "xtick.color": "#3d434a", "ytick.color": "#3d434a",
        "text.color": "#21262b", "axes.labelcolor": "#21262b",
    })
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.2))
    last_year = int(world.index.max())

    # --- Left panel: annual flows, Gt/yr ---
    flows = [
        ("co2", "fossil fuel + industry CO$_2$ (Figure 4)", "#2b6cb0", 2.2),
        ("co2_including_luc", "+ land-use change CO$_2$", "#38a169", 1.6),
        ("total_ghg", "all greenhouse gases (CO$_2$-eq)", "#805ad5", 1.6),
    ]
    for col, label, color, lw in flows:
        s = world[col].dropna()
        s = s[s > 0]
        ax1.plot(s.index, s / 1000.0, color=color, lw=lw, label=label,
                 zorder=3)
    ax1.set_yscale("log")
    ax1.set_xlim(1845, last_year + 5)
    ax1.set_ylim(0.1, 100)
    ax1.set_yticks([0.1, 1, 10, 100])
    ax1.set_yticklabels(["0.1 Gt", "1 Gt", "10 Gt", "100 Gt"])
    ax1.set_ylabel("emitted per year (log scale)")
    ax1.set_title("Annual flows: three definitions of \"emissions\"",
                  loc="left", fontweight="bold")
    ax1.legend(frameon=False, loc="lower right", fontsize=9.5)

    # --- Right panel: stocks, GtCO2 ---
    cum = world["cumulative_co2_including_luc"].dropna() / 1000.0
    cum_f = world["cumulative_co2"].dropna() / 1000.0
    excess_gt = excess_ppm * GTCO2_PER_PPM
    ax2.plot(cum.index, cum, color="#38a169", lw=1.6,
             label="cumulative emitted, fossil + land use", zorder=3)
    ax2.plot(cum_f.index, cum_f, color="#2b6cb0", lw=1.6,
             label="cumulative emitted, fossil only", zorder=3)
    ax2.plot(excess_gt.index, excess_gt, color="#c05621", lw=2.4,
             label="retained in atmosphere (Mauna Loa $-$ 280 ppm)",
             zorder=4)
    # Exponential fit to the retained excess over the full Mauna Loa span.
    y0, y1 = int(excess_gt.index.min()), int(excess_gt.index.max())
    t2 = doubling_time(excess_gt, y0, y1)
    slope, icpt = np.polyfit(excess_gt.index.to_numpy(float),
                             np.log2(excess_gt.to_numpy(float)), 1)
    yrs = np.arange(y0, y1 + 1)
    ax2.plot(yrs, 2.0 ** (slope * yrs + icpt), color="#c05621", lw=1.2,
             ls="--", alpha=0.8, zorder=4)
    ax2.annotate(f"retained CO$_2$ doubling every ~{t2:.0f} yr\n"
                 f"(exponential fit, {y0}–{y1})",
                 xy=(1992, 2.0 ** (slope * 1992 + icpt)), xycoords="data",
                 xytext=(1975, 60), textcoords="data", fontsize=9.5,
                 color="#8a3f18", ha="center",
                 arrowprops=dict(arrowstyle="-", color="#c05621", lw=0.9,
                                 shrinkA=4, shrinkB=6))
    ax2.set_yscale("log")
    ax2.set_xlim(1845, last_year + 5)
    ax2.set_ylim(10, 5000)
    ax2.set_yticks([10, 100, 1000])
    ax2.set_yticklabels(["10 Gt", "100 Gt", "1000 Gt"])
    ax2.set_ylabel("CO$_2$ stock (log scale)")
    ax2.set_title("Stocks: emitted so far vs. still in the air",
                  loc="left", fontweight="bold")
    ax2.legend(frameon=False, loc="lower right", fontsize=9.5)

    for ax in (ax1, ax2):
        ax.grid(True, which="major", axis="y", color="#d7dce1", lw=0.7,
                zorder=0)
        ax.grid(True, which="major", axis="x", color="#e6eaee", lw=0.6,
                zorder=0)
        ax.yaxis.set_minor_locator(plt.NullLocator())
        ax.yaxis.set_minor_formatter(plt.NullFormatter())
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)

    fig.text(0.01, 0.012,
             "Data: Global Carbon Budget via Our World in Data "
             f"(emissions, 1850–{last_year}); NOAA GML Mauna Loa CO$_2$ "
             f"({y0}–{y1}). 1 ppm = 7.78 GtCO$_2$.",
             fontsize=7.5, color="#6b7280")
    fig.text(0.99, 0.012, "Figure 4 (alt)", ha="right", fontsize=9.5,
             fontweight="bold", color="#6b7280")
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    fig.savefig(out_png)
    plt.close(fig)


def main():
    """Compute and print the definitions table; save the figure."""
    world = load_owid_world(OWID_CSV)
    mlo = load_mauna_loa_annual(MLO_TXT)
    excess_ppm = mlo - PREINDUSTRIAL_PPM
    excess_gt = excess_ppm * GTCO2_PER_PPM
    last = int(world.index.max())

    print(f"OWID world series: {world.index.min()}-{last}; "
          f"Mauna Loa annual means: {mlo.index.min()}-{mlo.index.max()}")

    # 1. Composition in the latest year and in 1850.
    for yr in (1850, 1970, last):
        r = world.loc[yr]
        print(f"\n{yr}: fossil+industry {r['co2'] / 1e3:6.1f} Gt | "
              f"land-use {r['land_use_change_co2'] / 1e3:5.1f} Gt | "
              f"fossil+LUC {r['co2_including_luc'] / 1e3:6.1f} Gt | "
              f"all GHG {r['total_ghg'] / 1e3:6.1f} GtCO2e")

    # 2. Doubling times under each definition.
    series = {
        "A fossil+industry CO2 (Fig 4)": world["co2"],
        "B fossil + land-use CO2": world["co2_including_luc"],
        "C all GHG, CO2-eq": world["total_ghg"],
        "D cumulative CO2 (fossil+LUC)": world["cumulative_co2_including_luc"],
        "E retained atmospheric CO2": excess_gt,
    }
    hdr = "".join(f"{f'{a}-{b}':>12}" for a, b in FIT_WINDOWS)
    print(f"\nDoubling time (yr) by definition and fit window:\n"
          f"{'':34}{hdr}{'1959-2025':>12}")
    for name, s in series.items():
        vals = [doubling_time(s, a, b) for a, b in FIT_WINDOWS]
        vals.append(doubling_time(s, 1959, 2025))
        print(f"{name:34}" + "".join(
            f"{v:12.1f}" if np.isfinite(v) else f"{'--':>12}" for v in vals))

    # 3. Is the retained excess still exponential?  Compare the doubling
    #    time of the first and second halves of the Mauna Loa record, and
    #    the mean growth rate in ppm/yr per decade.
    print("\nRetained atmospheric CO2 above 280 ppm:")
    for a, b in [(1959, 1990), (1990, 2025), (2005, 2025)]:
        print(f"  {a}-{b}: doubling every {doubling_time(excess_gt, a, b):5.1f} yr")
    print("  mean CO2 growth rate by decade (ppm/yr):")
    for d0 in range(1960, 2030, 10):
        d1 = min(d0 + 10, int(mlo.index.max()))
        if d1 > d0 and d0 in mlo.index:
            rate = (mlo.loc[d1] - mlo.loc[d0]) / (d1 - d0)
            print(f"    {d0}-{d1}: {rate:4.2f}")
    print(f"  excess in {mlo.index.min()}: {excess_ppm.iloc[0]:.0f} ppm; "
          f"in {mlo.index.max()}: {excess_ppm.iloc[-1]:.0f} ppm "
          f"({excess_gt.iloc[-1]:.0f} GtCO2)")

    # 4. Airborne fraction by decade -- the sink-health test.
    af = airborne_fraction_by_decade(
        excess_gt, world["co2_including_luc"].dropna())
    print("\nAirborne fraction by decade (retained / emitted fossil+LUC):")
    print(af.round(2).to_string())
    cum_emitted = world.loc[last, "cumulative_co2_including_luc"] / 1e3
    print(f"\nSince 1750: emitted {cum_emitted:.0f} GtCO2 (fossil+LUC); "
          f"retained {excess_gt.loc[min(last, excess_gt.index.max())]:.0f} "
          f"GtCO2 -> long-run airborne fraction "
          f"{excess_gt.loc[min(last, excess_gt.index.max())] / cum_emitted:.2f}")

    make_figure(world, excess_ppm, OUT_PNG)
    print(f"\nWrote {OUT_PNG}")


if __name__ == "__main__":
    main()
