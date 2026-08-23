"""
Build data/co2_by_transport_type.json for the Climate Intelligence blog.

Unlike the fuel-type dataset, there is no single clean, downloadable
time series that splits *global* transport CO2 emissions into
road-passenger / road-freight / aviation / shipping / rail every year.
Instead we combine:

  1. IEA's most detailed publicly available global transport sub-sector
     breakdown (percentage shares of transport-sector CO2), for 2018,
     as reproduced by Our World in Data:
     https://ourworldindata.org/co2-emissions-from-transport
  2. The total global transport-sector CO2 emissions time series
     (2015-2023), from Climate Watch / CAIT, as republished by OWID
     (https://ourworldindata.org/grapher/co2-emissions-transport.csv).
  3. Independently sourced, mode-specific absolute figures for more
     recent years:
       - Road-sector CO2 emissions, 2024: IEA Global Energy Review 2025
       - Global aviation CO2 emissions, 2019: Bergero et al. (2023,
         Nature Sustainability), as reproduced by OWID
       - Global aviation CO2 emissions, 2023 & 2024 (commercial
         aviation, gross): IATA
       - Global shipping GHG emissions, 2023: ICCT "Greenhouse gas
         emissions and air pollution from global shipping, 2016-2023"
         (note: CO2e using GWP100, tank-to-wake -- not pure CO2)

Where we derive an approximate absolute MtCO2 value for a transport
mode by applying the 2018 IEA percentage share to the 2018 OWID/Climate
Watch total transport CO2 figure, this is clearly labelled as a
derived/approximate figure in both the "notes" field and the top-level
"caveats" field, since it combines two different underlying datasets.

Run:
    conda run -n ocean14 python build_co2_by_transport_type.py

Output:
    ../co2_by_transport_type.json
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT_JSON = HERE.parent / "co2_by_transport_type.json"

ACCESSED_DATE = "2026-08-23"

IEA_SRC = "IEA (2018 global transport sub-sector shares, via Our World in Data)"
OWID_TOTAL_SRC = "Climate Watch / CAIT (via Our World in Data)"
IEA_GER_SRC = "IEA - Global Energy Review 2025"
OWID_AVIATION_SRC = "Bergero et al. 2023, Nature Sustainability (via Our World in Data)"
IATA_SRC = "IATA - 2024 Aviation Emissions: Efficiency Gains vs. Rising Totals"
ICCT_SRC = "ICCT - Greenhouse gas emissions and air pollution from global shipping, 2016-2023"

# IEA 2018 percentage shares of TOTAL TRANSPORT CO2 (not total global CO2)
IEA_2018_SHARES = {
    "road_passenger": 45.1,
    "road_freight": 29.4,
    "aviation": 11.6,
    "shipping": 10.6,  # international shipping
    "rail": 1.0,
    "other_transport": 2.2,  # e.g. pipelines
}

# OWID/Climate Watch total global transport CO2, MtCO2 (tonnes / 1e6)
TOTAL_TRANSPORT_CO2_MT = {
    2015: 7727.77,
    2016: 7888.82,
    2017: 8080.22,
    2018: 8281.75,
    2019: 8358.38,
    2020: 7241.51,
    2021: 7810.29,
    2022: 8102.42,
    2023: 8276.30,
}


def main():
    data = []

    # --- Total transport CO2 by year (2015-2023) ---
    for year, val in sorted(TOTAL_TRANSPORT_CO2_MT.items()):
        data.append(
            {
                "category": "total_transport",
                "year": year,
                "value": round(val, 1),
                "unit": "MtCO2",
                "source": OWID_TOTAL_SRC,
                "notes": "Total CO2 emissions from the transport sector, all modes.",
            }
        )

    # --- IEA 2018 mode shares (percent of transport-sector CO2) ---
    for mode, pct in IEA_2018_SHARES.items():
        data.append(
            {
                "category": mode,
                "year": 2018,
                "value": pct,
                "unit": "% of transport-sector CO2",
                "source": IEA_SRC,
            }
        )

    # --- Derived absolute 2018 MtCO2 by mode = share x 2018 total transport CO2 ---
    total_2018 = TOTAL_TRANSPORT_CO2_MT[2018]
    for mode, pct in IEA_2018_SHARES.items():
        approx_value = round(total_2018 * pct / 100.0, 1)
        data.append(
            {
                "category": mode,
                "year": 2018,
                "value": approx_value,
                "unit": "MtCO2",
                "source": f"Derived: {IEA_SRC} share x {OWID_TOTAL_SRC} total",
                "notes": "Approximate: IEA's 2018 percentage share of transport CO2 applied to the "
                         "OWID/Climate Watch total transport CO2 figure for 2018. Combines two "
                         "different underlying datasets/methodologies; treat as indicative, not exact.",
            }
        )

    # --- Independently sourced recent absolute figures ---
    data.append(
        {
            "category": "road",
            "year": 2024,
            "value": 6000.0,
            "unit": "MtCO2",
            "source": IEA_GER_SRC,
            "notes": "IEA reports road-sector CO2 emissions 'just over 6 GtCO2' in 2024, 8% higher than "
                     "2015; growth averaged only 0.2%/yr from 2019-2024. Combined road passenger + freight.",
        }
    )
    data.append(
        {
            "category": "aviation",
            "year": 2019,
            "value": 1000.0,
            "unit": "MtCO2",
            "source": OWID_AVIATION_SRC,
            "notes": "~2.5% of global CO2 emissions from fossil sources and land-use change in 2019 (pre-pandemic peak).",
        }
    )
    data.append(
        {
            "category": "aviation",
            "year": 2023,
            "value": 882.0,
            "unit": "MtCO2",
            "source": IATA_SRC,
            "notes": "Gross CO2 emissions from commercial aviation.",
        }
    )
    data.append(
        {
            "category": "aviation",
            "year": 2024,
            "value": 942.0,
            "unit": "MtCO2",
            "source": IATA_SRC,
            "notes": "Gross CO2 emissions from commercial aviation.",
        }
    )
    data.append(
        {
            "category": "shipping",
            "year": 2023,
            "value": 911.0,
            "unit": "MtCO2e (GWP100, tank-to-wake)",
            "source": ICCT_SRC,
            "notes": "CO2-equivalent (includes methane and N2O, not pure CO2), tank-to-wake, 100-year GWP. "
                     "925 Mt using 20-year GWP. ~86% international shipping, ~10% domestic, ~4% fishing. "
                     "Grew ~12% (CAGR ~1.4%/yr) from 2016 to 2023.",
        }
    )

    out = {
        "title": "World CO2 Emissions by Transport Type",
        "description": (
            "Global CO2 emissions from the transport sector, broken down by mode (road passenger, road "
            "freight, aviation, shipping, rail, other), combining IEA's most detailed public sub-sector "
            "percentage-share breakdown (2018) with total transport-sector CO2 time series (2015-2023) and "
            "independently sourced, more recent mode-specific figures for road (2024), aviation (2019, 2023, "
            "2024), and shipping (2023)."
        ),
        "unit": "MtCO2",
        "data": data,
        "provenance": [
            {
                "source_name": "IEA (2018 transport sub-sector shares, via Our World in Data)",
                "url": "https://ourworldindata.org/co2-emissions-from-transport",
                "publisher": "International Energy Agency / Our World in Data",
                "publication_year": 2020,
                "accessed_date": ACCESSED_DATE,
            },
            {
                "source_name": "Climate Watch / CAIT total transport CO2 (via Our World in Data)",
                "url": "https://ourworldindata.org/grapher/co2-emissions-transport",
                "publisher": "Climate Watch (World Resources Institute) / Our World in Data",
                "publication_year": 2024,
                "accessed_date": ACCESSED_DATE,
            },
            {
                "source_name": "IEA - Global Energy Review 2025",
                "url": "https://www.iea.org/reports/global-energy-review-2025",
                "publisher": "International Energy Agency",
                "publication_year": 2025,
                "accessed_date": ACCESSED_DATE,
            },
            {
                "source_name": "Bergero et al. 2023, Nature Sustainability (global aviation emissions, via Our World in Data)",
                "url": "https://ourworldindata.org/global-aviation-emissions",
                "publisher": "Nature Sustainability / Our World in Data",
                "publication_year": 2023,
                "accessed_date": ACCESSED_DATE,
            },
            {
                "source_name": "IATA - 2024 Aviation Emissions: Efficiency Gains vs. Rising Totals",
                "url": "https://www.iata.org/en/iata-repository/publications/economic-reports/2024-aviation-emissions-efficiency-gains-vs.-rising-totals",
                "publisher": "International Air Transport Association",
                "publication_year": 2024,
                "accessed_date": ACCESSED_DATE,
            },
            {
                "source_name": "ICCT - Greenhouse gas emissions and air pollution from global shipping, 2016-2023",
                "url": "https://theicct.org/publication/greenhouse-gas-emissions-and-air-pollution-from-global-shipping-2016-2023-apr25/",
                "publisher": "International Council on Clean Transportation",
                "publication_year": 2025,
                "accessed_date": ACCESSED_DATE,
            },
        ],
        "caveats": (
            "No single authoritative source publishes an annually updated, full mode-by-mode (road "
            "passenger / road freight / aviation / shipping / rail) breakdown of global transport CO2 at "
            "the time of writing; the widely cited detailed percentage breakdown (45.1% road passenger, "
            "29.4% road freight, 11.6% aviation, 10.6% international shipping, 1.0% rail, 2.2% other) is "
            "IEA data for 2018, reproduced by Our World in Data. Absolute MtCO2 values by mode for 2018 in "
            "this file are DERIVED by applying those 2018 percentage shares to a total transport CO2 figure "
            "for 2018 from a different dataset (Climate Watch/CAIT, via OWID) -- treat these as approximate, "
            "order-of-magnitude figures, not official statistics. The road-sector 2024 figure ('just over 6 "
            "GtCO2') is from IEA's Global Energy Review 2025 and is NOT strictly comparable to the IEA 2018 "
            "road_passenger+road_freight figures because methodologies/scopes may differ slightly between "
            "IEA publications and vintages. The ICCT shipping figure (911 Mt for 2023) is CO2-EQUIVALENT "
            "(includes methane and N2O using 100-year GWP), not pure CO2, and is tank-to-wake (fuel "
            "combustion only, excludes well-to-tank upstream emissions) -- it is therefore not directly "
            "additive with the pure-CO2 figures for other modes. Aviation figures differ by source: OWID's "
            "academic-literature-based estimate (~1,000 Mt in 2019) covers all aviation (commercial + other), "
            "while IATA's more recent 882/942 Mt figures (2023/2024) cover commercial aviation only and use "
            "IATA's own accounting; the two series should not be spliced together as if fully consistent. "
            "'Total transport CO2' (Climate Watch/CAIT) will not exactly equal the sum of by-mode figures "
            "here because those individual mode entries mix vintages, sources, and (for shipping) gas "
            "scope. Transport is commonly cited as roughly 21-24% of global energy-related/fossil CO2 "
            "emissions, with road transport alone historically accounting for roughly three-quarters of "
            "transport-sector CO2."
        ),
    }

    OUT_JSON.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_JSON} with {len(data)} data points.")


if __name__ == "__main__":
    main()
