"""Created by JXP and Claude.

C3b "Heat in vs. heat out: the CO2 bite" — a computed SCHEMATIC of Earth's
outgoing infrared spectrum (Q37: schematic, clearly labeled; a real Nimbus-4
IRIS decode is a possible later upgrade).

Method: each wavenumber emits as a blackbody (Planck's law) at an assumed
effective emission temperature T_eff(nu):
  - atmospheric window (~800-1250 cm^-1): the surface, ~288 K;
  - CO2 15-um band (~590-750 cm^-1, centered 667 cm^-1): the cold upper
    troposphere / lower stratosphere, ~220 K;
  - O3 9.6-um band (~1040 cm^-1): ~255 K;
  - H2O rotation (<~550 cm^-1) and 6.3-um band (~1350-1800 cm^-1): ~255-260 K.
These temperatures are round, illustrative values chosen to reproduce the
familiar shape of satellite spectra (e.g. Nimbus-4 IRIS, Hanel et al. 1972,
J. Geophys. Res. 77, 2629). They are not fitted to any measurement.
"More CO2" widens the band edges (the absorption is logarithmic in CO2); the
dotted curve widens each edge by 12 cm^-1, again schematically.

Usage:
    conda run -n ocean14 python presentations/py/olr_spectrum.py
"""
import numpy as np
import matplotlib.pyplot as plt

from slide_style import MAIN, apply_style, save, RED, BLUE, GRAY, MUTED, INK

H, C, KB = 6.62607015e-34, 2.99792458e8, 1.380649e-23  # SI


def planck_wavenumber(nu_cm, temp_k):
    """Created by JXP and Claude. Planck radiance per wavenumber.
    Inputs: nu_cm (cm^-1), temp_k (K). Output: mW / (m^2 sr cm^-1)."""
    nu = nu_cm * 100.0  # m^-1
    b = 2 * H * C**2 * nu**3 / np.expm1(H * C * nu / (KB * temp_k))  # W/(m^2 sr m^-1)
    return b * 100.0 * 1e3  # per cm^-1, in mW


def band(nu, lo, hi, edge):
    """Created by JXP and Claude. Smooth top-hat (0..1) between lo and hi
    with tanh edges of width `edge` (cm^-1)."""
    return 0.5 * (np.tanh((nu - lo) / edge) - np.tanh((nu - hi) / edge))


def t_eff(nu, co2_widen=0.0):
    """Created by JXP and Claude. Schematic effective emission temperature
    (K) vs wavenumber; co2_widen (cm^-1) pushes the CO2 band edges outward."""
    t = np.full_like(nu, 288.0)                                    # window/surface
    t -= (288 - 258) * band(nu, 0, 560, 25)                        # H2O rotation
    t -= (288 - 255) * band(nu, 1330, 2100, 30)                    # H2O 6.3 um
    t -= (288 - 255) * band(nu, 1000, 1075, 8)                     # O3 9.6 um
    co2 = band(nu, 595 - co2_widen, 745 + co2_widen, 12)
    t = t - (t - 220.0) * co2                                      # CO2 15 um
    return t


def main():
    """Created by JXP and Claude. Build c3b_olr_spectrum.png."""
    apply_style()
    nu = np.linspace(100, 2000, 2000)
    fig, ax = plt.subplots(figsize=MAIN)

    ax.plot(nu, planck_wavenumber(nu, 288), "--", color=GRAY, lw=1.4)
    ax.text(1380, 60, "surface, 288 K", color=GRAY, fontsize=12)
    ax.plot(nu, planck_wavenumber(nu, 220), "--", color=BLUE, lw=1.2, alpha=0.7)
    ax.text(1250, 15, "220 K", color=BLUE, fontsize=12)

    earth = planck_wavenumber(nu, t_eff(nu))
    more = planck_wavenumber(nu, t_eff(nu, co2_widen=12))
    ax.fill_between(nu, earth, planck_wavenumber(nu, 288), color="#f4c7c0", alpha=0.6, lw=0)
    ax.plot(nu, more, ":", color="black", lw=1.6)
    ax.plot(nu, earth, color=RED, lw=2.6)

    ax.text(667, 92, "CO₂\nbite", fontsize=14, ha="center", va="center",
            color=INK, fontweight="bold")
    ax.text(1000, 118, "atmospheric\nwindow", fontsize=12, ha="center", color=MUTED)
    ax.text(1040, 66, "O₃", fontsize=12, ha="center", color=MUTED)
    ax.text(1700, 32, "H₂O", fontsize=12, ha="center", color=MUTED)
    ax.text(1420, 118, "shaded = heat that\ndoes not escape", fontsize=12, color="#b0473a")
    ax.annotate("more CO₂ →\nwider bite (dotted)", (588, 100), xytext=(130, 146),
                fontsize=12, color="black",
                arrowprops=dict(arrowstyle="-", color="black", lw=0.8))
    ax.text(0.99, 0.97, "SCHEMATIC (computed, not measured)", transform=ax.transAxes,
            ha="right", va="top", fontsize=11, color=MUTED, fontweight="bold")

    ax.set_xlim(100, 2000)
    ax.set_ylim(0, 175)
    ax.set_xlabel("Wavenumber (cm$^{-1}$)")
    ax.set_ylabel("Radiance to space\n(mW m$^{-2}$ sr$^{-1}$ / cm$^{-1}$)")
    top = ax.secondary_xaxis("top", functions=(lambda n: 1e4 / np.maximum(n, 1),
                                               lambda w: 1e4 / np.maximum(w, 1e-3)))
    top.set_xticks([50, 25, 15, 10, 8, 6])
    top.set_xlabel("Wavelength (µm)", fontsize=13)

    save(fig, "c3b_olr_spectrum.png",
         "Schematic: Planck emission at round effective temperatures per band (Planck's law); "
         "shape after satellite spectra, e.g. Nimbus-4 IRIS (Hanel et al. 1972)",
         "C3b")


if __name__ == "__main__":
    main()
