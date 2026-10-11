"""
Build data/co2_by_fuel_type.json from the Global Carbon Project's fossil CO2
emissions dataset, as redistributed by Our World in Data (OWID) in
owid-co2-data.csv (https://github.com/owid/co2-data).

OWID's per-fuel columns (coal_co2, oil_co2, gas_co2, cement_co2, flaring_co2,
other_industry_co2) are themselves a pass-through of the Global Carbon
Project's "Global Carbon Budget" fossil CO2 emissions dataset (Friedlingstein
et al., Earth System Science Data), which is the standard authoritative
source for global CO2 emissions by fuel type. Units in the raw file are
million tonnes of CO2 (MtCO2).

Run:
    conda run -n ocean14 python build_co2_by_fuel_type.py

Input:
    ../raw/owid-co2-data.csv  (downloaded from
        https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv )
Output:
    ../co2_by_fuel_type.json
"""

import csv
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
RAW_CSV = HERE.parent / "raw" / "owid-co2-data.csv"
OUT_JSON = HERE.parent / "co2_by_fuel_type.json"

ACCESSED_DATE = "2026-08-23"

# Map OWID column name -> (category label, notes)
FUEL_COLUMNS = {
    "coal_co2": ("coal", None),
    "oil_co2": ("oil", None),
    "gas_co2": ("gas", "Natural gas."),
    "cement_co2": ("cement", "Process emissions from cement production (before subtracting the cement carbonation sink)."),
    "flaring_co2": ("flaring", "Gas flaring."),
    "other_industry_co2": ("other_industry", "Other industrial process emissions (e.g. non-cement mineral processes) not captured in the coal/oil/gas/cement/flaring categories."),
}

YEARS_WANTED = [2019, 2020, 2021, 2022, 2023]


def main():
    rows = []
    with open(RAW_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["country"] != "World":
                continue
            try:
                year = int(row["year"])
            except (ValueError, TypeError):
                continue
            if year not in YEARS_WANTED:
                continue
            rows.append(row)

    rows.sort(key=lambda r: int(r["year"]))

    data = []
    for row in rows:
        year = int(row["year"])
        total_co2 = row.get("co2")
        for col, (label, note) in FUEL_COLUMNS.items():
            val = row.get(col)
            if val in (None, ""):
                continue
            entry = {
                "category": label,
                "year": year,
                "value": round(float(val), 1),
                "unit": "MtCO2",
                "source": "Global Carbon Project - Global Carbon Budget (via Our World in Data)",
            }
            if note:
                entry["notes"] = note
            data.append(entry)
        # Also record the reported total fossil CO2 (coal+oil+gas+cement+flaring+other)
        if total_co2 not in (None, ""):
            data.append(
                {
                    "category": "total_fossil_co2",
                    "year": year,
                    "value": round(float(total_co2), 1),
                    "unit": "MtCO2",
                    "notes": "Sum of coal + oil + gas + cement + flaring + other industry CO2 (excludes land-use change).",
                    "source": "Global Carbon Project - Global Carbon Budget (via Our World in Data)",
                }
            )

    out = {
        "title": "World CO2 Emissions by Fuel Type",
        "description": (
            "Global annual CO2 emissions from fossil fuels and industry, broken down by fuel/source "
            "category (coal, oil, gas, cement, flaring, other industrial processes), 2019-2023. "
            "Land-use-change CO2 emissions are excluded."
        ),
        "unit": "MtCO2",
        "data": data,
        "provenance": [
            {
                "source_name": "Global Carbon Project - Global Carbon Budget 2024",
                "url": "https://essd.copernicus.org/articles/17/965/2025/",
                "publisher": "Global Carbon Project / Earth System Science Data (Friedlingstein et al. 2024)",
                "publication_year": 2024,
                "accessed_date": ACCESSED_DATE,
            },
            {
                "source_name": "Our World in Data - CO2 and Greenhouse Gas Emissions (owid-co2-data.csv)",
                "url": "https://github.com/owid/co2-data",
                "publisher": "Our World in Data",
                "publication_year": 2024,
                "accessed_date": ACCESSED_DATE,
            },
            {
                "source_name": "Global Carbon Budget 2025 (preliminary 2025 estimate, fuel-type shares)",
                "url": "https://globalcarbonbudget.org/fossil-fuel-co2-emissions-hit-record-high-in-2025/",
                "publisher": "Global Carbon Project",
                "publication_year": 2025,
                "accessed_date": ACCESSED_DATE,
            },
        ],
        "caveats": (
            "The most recent full-detail, per-fuel breakdown available in the OWID/Global Carbon Project "
            "dataset at time of access is for 2023 (from Global Carbon Budget 2024, released Nov 2024); "
            "2024 final and 2025 fuel-level absolute figures were not yet available in machine-readable form "
            "at access time. The Global Carbon Budget 2025 report (Nov 2025) states preliminary/projected "
            "2025 shares of total fossil CO2 emissions as: coal ~41%, oil ~32%, gas ~21%, cement+other ~6%, "
            "on a projected 2025 total of 38.1 GtCO2 (up 1.1% from 2024); growth by fuel in 2025 was "
            "coal +0.8%, oil +1.0%, gas +1.3%. These 2025 figures are NOT included in the 'data' array above "
            "because they are projections/shares rather than final published absolute values per fuel; only "
            "verified 2019-2023 absolute values are included. 'total_fossil_co2' here excludes land-use-change "
            "(deforestation, etc.) emissions, which the Global Carbon Project reports separately and which are "
            "large, uncertain, and not attributable to a 'fuel type'. Cement figure is gross process emissions "
            "and does not net out the cement carbonation sink (a small CO2 reabsorption by cement products), "
            "which the Global Carbon Project treats as a separate sink term. IEA's Global Energy Review 2025 "
            "reports a related but not directly comparable total energy-related CO2 figure of 37.8 GtCO2 for "
            "2024 (different scope/methodology than the Global Carbon Project's fossil CO2 total)."
        ),
    }

    OUT_JSON.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_JSON} with {len(data)} data points.")


if __name__ == "__main__":
    main()
