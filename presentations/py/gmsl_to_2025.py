"""Created by JXP and Claude.

C6a "Sea level is rising" — global mean sea level 1880-2025: tide-gauge
reconstruction joined to satellite altimetry.

Data:
  Tide gauges: CSIRO Church & White (2011) GMSL reconstruction, 1880-2013,
    cached at CI_Reports/data/gmsl_church_white.csv (fetched 2026-07-09).
  Altimetry: NOAA Laboratory for Satellite Altimetry, global mean sea level
    anomaly, annual signals removed, no GIA correction, TOPEX/Poseidon ->
    Jason-1/2/3 -> Sentinel-6MF, 1993-2025, fetched 2026-10-05:
    https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/slr/slr_sla_gbl_free_ref_90.csv
    cached at presentations/data/noaa_star_gmsl.csv.
    Acknowledgment required by LSA: "Altimetry data are provided by NOAA
    Laboratory for Satellite Altimetry."
Joining: altimetry is offset to match the reconstruction's mean over the
overlap 1993-2013. Rates are least-squares fits computed here. Adding the
standard GIA correction (~+0.3 mm/yr) would raise the altimetry rates.

Usage:
    conda run -n ocean14 python presentations/py/gmsl_to_2025.py
"""
import numpy as np
import matplotlib.pyplot as plt

from slide_style import ROOT, DATA, MAIN, apply_style, save, BLUE, LBLUE, RED, INK


def load_church_white():
    """Created by JXP and Claude. Outputs: year, GMSL (mm), 1-sigma (mm)."""
    rows = np.genfromtxt(ROOT / "CI_Reports" / "data" / "gmsl_church_white.csv",
                         delimiter=",", skip_header=1)
    return rows[:, 0], rows[:, 1], rows[:, 2]


def load_altimetry():
    """Created by JXP and Claude. Merge the per-mission columns into one
    series. Outputs: decimal year, GMSL anomaly (mm)."""
    rows = np.genfromtxt(DATA / "noaa_star_gmsl.csv", delimiter=",", comments="#",
                         skip_header=6)
    t = rows[:, 0]
    sla = np.nanmean(rows[:, 1:], axis=1)  # one mission per row (overlaps averaged)
    good = ~np.isnan(sla)
    return t[good], sla[good]


def rate(t, y, t0, t1):
    """Created by JXP and Claude. Least-squares slope (mm/yr) over [t0, t1]."""
    m = (t >= t0) & (t <= t1)
    return np.polyfit(t[m], y[m], 1)[0]


def main():
    """Created by JXP and Claude. Build c6a_gmsl.png."""
    apply_style()
    cy, cg, cu = load_church_white()
    at, asla = load_altimetry()
    # Offset altimetry onto the reconstruction over the 1993-2013 overlap.
    overlap_c = cg[(cy >= 1993) & (cy <= 2013)].mean()
    overlap_a = asla[(at >= 1993) & (at < 2014)].mean()
    a_join = asla - overlap_a + overlap_c
    # Re-zero everything to the 1900-1910 mean of the reconstruction.
    zero = cg[(cy >= 1900) & (cy < 1910)].mean()
    cg, a_join = cg - zero, a_join - zero

    r_early = rate(cy, cg, 1901, 1990)
    r_alt = rate(at, asla, at[0], at[-1])
    r_recent = rate(at, asla, at[-1] - 10, at[-1])
    total_cm = (a_join[at >= at[-1] - 1].mean()) / 10
    print(f"tide gauges 1901-1990: {r_early:.2f} mm/yr; altimetry {at[0]:.1f}-{at[-1]:.1f}: {r_alt:.2f} mm/yr; "
          f"last 10 yr: {r_recent:.2f} mm/yr; rise since 1900s ~{total_cm:.0f} cm")

    fig, ax = plt.subplots(figsize=MAIN)
    ax.fill_between(cy, cg - cu, cg + cu, color=LBLUE, alpha=0.25, lw=0)
    ax.plot(cy, cg, color=BLUE, lw=2.2)
    ax.plot(at, a_join, color=RED, lw=1.6)
    ax.text(1905, 115, f"Tide gauges, 1901–1990:\n{r_early:.1f} mm/yr", fontsize=13, color=BLUE)
    ax.text(1958, 215, f"Satellites, 1993–{int(at[-1])}: {r_alt:.1f} mm/yr\nlast decade: {r_recent:.1f} mm/yr",
            fontsize=13, color=RED)
    ax.set_xlim(1880, 2027)
    ax.set_ylabel("Global mean sea level\nvs 1900–1910 (mm)")
    save(fig, "c6a_gmsl.png",
         "Tide gauges: CSIRO, Church & White 2011. Altimetry data are provided by NOAA Laboratory for "
         "Satellite Altimetry (TOPEX → Jason-1/2/3 → Sentinel-6MF; no GIA correction)",
         "C6a")


if __name__ == "__main__":
    main()
