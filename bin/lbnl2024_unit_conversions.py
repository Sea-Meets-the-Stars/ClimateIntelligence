#!/usr/bin/env python
"""Unit conversions and derived ratios for the LBNL 2024 US Data Center
Energy Usage Report (Shehabi et al. 2024, LBNL-2001637).

All input numbers are stated directly in the report (page numbers refer to
the report's own pagination, not the PDF file):
  - Direct (on-site) water use: 21.2 billion L (2014), 66 billion L (2023),
    hyperscale share 2028: 60-124 billion L  [pp. 55-56]
  - Indirect water via electricity generation, 2023: ~800 billion L  [p. 57]
  - GHG from data-center electricity, 2023: 61 billion kg CO2e  [p. 57]
  - Total electricity 2023: 176 TWh; 2028 scenario range 325-580 TWh [pp. 5-6, 52]

This script only converts units (L -> US gallons, kg -> million metric tons)
and computes simple ratios, so every derived number in the blog/knowledge
base is reproducible.
"""

L_PER_GAL = 3.785411784  # US liquid gallon, exact definition


def liters_to_gal(liters: float) -> float:
    return liters / L_PER_GAL


def main():
    direct_2014_L = 21.2e9
    direct_2023_L = 66e9
    hyper_2028_low_L, hyper_2028_high_L = 60e9, 124e9
    indirect_2023_L = 800e9
    ghg_2023_kg = 61e9
    twh_2023 = 176.0
    twh_2028_low, twh_2028_high = 325.0, 580.0

    print(f"Direct water 2014: {direct_2014_L/1e9:.1f} B L "
          f"= {liters_to_gal(direct_2014_L)/1e9:.2f} B gal")
    print(f"Direct water 2023: {direct_2023_L/1e9:.1f} B L "
          f"= {liters_to_gal(direct_2023_L)/1e9:.2f} B gal")
    print(f"Hyperscale direct water 2028: {hyper_2028_low_L/1e9:.0f}-"
          f"{hyper_2028_high_L/1e9:.0f} B L = "
          f"{liters_to_gal(hyper_2028_low_L)/1e9:.1f}-"
          f"{liters_to_gal(hyper_2028_high_L)/1e9:.1f} B gal")
    print(f"Indirect water 2023: {indirect_2023_L/1e9:.0f} B L "
          f"= {liters_to_gal(indirect_2023_L)/1e9:.1f} B gal")
    print(f"Indirect/direct water ratio 2023: "
          f"{indirect_2023_L/direct_2023_L:.1f}x")
    print(f"GHG 2023: {ghg_2023_kg/1e9:.0f} B kg CO2e "
          f"= {ghg_2023_kg/1e9:.0f} million metric tons CO2e")
    print(f"Direct-water growth 2014->2023: "
          f"{direct_2023_L/direct_2014_L:.2f}x")
    print(f"Electricity growth 2023->2028: "
          f"{twh_2028_low/twh_2023:.2f}x (low) to "
          f"{twh_2028_high/twh_2023:.2f}x (high)")


if __name__ == "__main__":
    main()
