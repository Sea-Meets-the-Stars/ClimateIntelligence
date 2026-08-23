#!/usr/bin/env python
"""
Build co2_by_country.json and co2_by_sector.json for the Climate Intelligence
blog from downloaded Our World in Data (OWID) CSV extracts.

Data sources (downloaded via curl from ourworldindata.org/grapher/*.csv on
2026-08-23):
  - annual-co2-emissions-per-country.csv  -> owid_co2_country.csv
      (fossil + industry CO2, tonnes; citation: Global Carbon Budget (2025))
  - co-emissions-per-capita.csv           -> owid_co2_percapita.csv
      (tonnes CO2 per capita; citation: Global Carbon Budget (2025) + UN population)
  - cumulative-co-emissions.csv           -> owid_co2_cumulative.csv
      (cumulative tonnes CO2 since 1750; citation: Global Carbon Budget (2025))
  - share-of-cumulative-co2.csv           -> owid_co2_cumshare.csv
      (share of global cumulative CO2, already expressed as a PERCENTAGE
      0-100, not a 0-1 fraction; citation: Global Carbon Budget (2025))
  - co-emissions-by-sector.csv            -> owid_co2_by_sector.csv
      (CO2 emissions by economic sector, tonnes; citation: Climate Watch (2026))

Raw CSVs are cached under climate_intelligence/data/raw/ alongside this
script's output directory, so this script can be re-run without re-fetching
from the network (re-download manually if you want fresher data).

This script only aggregates/reshapes already-published numbers into the
project's JSON schema -- it does not derive new statistics.
"""
import csv
import json
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(REPO_ROOT, "climate_intelligence", "data", "raw")
OUT_DIR = os.path.join(REPO_ROOT, "climate_intelligence", "data")
ACCESSED = "2026-08-23"

# Non-country aggregate entities present in the OWID GCP-based files that we
# want to exclude from the "top N countries" ranking (continents, income
# groups, historical/political aggregates, international transport bunkers).
AGGREGATE_ENTITIES = {
    "Africa (GCP)", "Asia (GCP)", "Asia (excl. China and India)",
    "Central America (GCP)", "Europe (GCP)", "Europe (excl. EU-27)",
    "Europe (excl. EU-28)", "European Union (27)", "European Union (28)",
    "International aviation", "International shipping",
    "Kuwaiti Oil Fires (GCP)", "Middle East (GCP)", "Non-OECD (GCP)",
    "North America (GCP)", "North America (excl. USA)", "OECD (GCP)",
    "Oceania (GCP)", "Ryukyu Islands (GCP)", "South America (GCP)",
    "World", "Africa", "Asia", "Europe", "North America", "South America",
    "Oceania", "Antarctica", "European Union (27)",
    "High-income countries", "Low-income countries",
    "Lower-middle-income countries", "Upper-middle-income countries",
}


def read_csv(fname, value_col):
    path = os.path.join(RAW_DIR, fname)
    out = {}
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            entity = row["entity"]
            year = int(row["year"])
            val = row.get(value_col, "")
            if val == "" or val is None:
                continue
            out[(entity, year)] = float(val)
    return out


def latest_year_for_entity(data, entity):
    years = [y for (e, y) in data.keys() if e == entity]
    return max(years) if years else None


def build_country_dataset():
    totals = read_csv("owid_co2_country.csv", "emissions_total")
    percap = read_csv("owid_co2_percapita.csv", "emissions_total_per_capita")
    cumulative = read_csv("owid_co2_cumulative.csv", "cumulative_emissions_total")
    cumshare = read_csv("owid_co2_cumshare.csv", "cumulative_emissions_total_as_share_of_global")

    world_year = latest_year_for_entity(totals, "World")
    assert world_year is not None

    # Build per-entity latest-year (<= world_year) totals for ranking.
    entities = {}
    for (entity, year), val in totals.items():
        if entity in AGGREGATE_ENTITIES:
            continue
        if year != world_year:
            continue
        entities[entity] = val

    ranked = sorted(entities.items(), key=lambda kv: kv[1], reverse=True)
    top_n = ranked[:35]

    data = []
    # World total first.
    world_total_t = totals[("World", world_year)]
    data.append({
        "category": "World",
        "year": world_year,
        "value": round(world_total_t / 1e6, 1),
        "unit": "MtCO2",
        "source": "Global Carbon Project - Global Carbon Budget 2025",
        "notes": "Fossil fuel and industry CO2 only; excludes land-use change and international aviation/shipping bunkers are included only in this world total, not in individual countries.",
    })

    for entity, total_t in top_n:
        year = world_year
        rec = {
            "category": entity,
            "year": year,
            "value": round(total_t / 1e6, 1),
            "unit": "MtCO2",
            "source": "Global Carbon Project - Global Carbon Budget 2025",
        }
        pc = percap.get((entity, year))
        if pc is not None:
            rec["per_capita_tCO2"] = round(pc, 2)
        cum = cumulative.get((entity, year))
        if cum is not None:
            rec["cumulative_MtCO2_since_1750"] = round(cum / 1e6, 1)
        cs = cumshare.get((entity, year))
        if cs is not None:
            # The OWID "share-of-cumulative-co2" column is already expressed
            # as a percentage (e.g. 15.42 means 15.42%), not a 0-1 fraction.
            rec["cumulative_share_of_global_pct"] = round(cs, 2)
        data.append(rec)

    dataset = {
        "title": "Global CO2 Emissions by Country",
        "description": (
            "Annual territorial CO2 emissions from fossil fuels and industry "
            f"for the world total and the top {len(top_n)} emitting countries in "
            f"{world_year}, plus per-capita and cumulative-historical (since 1750) "
            "figures where available."
        ),
        "unit": "MtCO2",
        "data": data,
        "provenance": [
            {
                "source_name": "Global Carbon Project - Global Carbon Budget 2025",
                "url": "https://globalcarbonbudget.org/",
                "publisher": "Global Carbon Project",
                "publication_year": 2025,
                "accessed_date": ACCESSED,
                "notes": "Retrieved via Our World in Data grapher CSV exports (annual-co2-emissions-per-country, co-emissions-per-capita, cumulative-co-emissions, share-of-cumulative-co2), which republish Global Carbon Budget national fossil CO2 + industry data.",
            },
            {
                "source_name": "Our World in Data - CO2 and Greenhouse Gas Emissions",
                "url": "https://ourworldindata.org/co2-and-greenhouse-gas-emissions",
                "publisher": "Our World in Data (Ritchie, Rosado, Roser)",
                "publication_year": 2023,
                "accessed_date": ACCESSED,
            },
        ],
        "caveats": (
            "Figures are territorial (production-based) CO2 emissions from fossil "
            "fuel combustion, cement, and other industrial processes; they exclude "
            "land-use change/LULUCF emissions and are NOT adjusted for trade "
            "(consumption-based accounting would shift emissions from exporters like "
            "China toward importers like the US/EU). International aviation and "
            "shipping ('bunker fuels') are included only in the World total, not "
            "attributed to individual countries. The 2025 Global Carbon Budget's "
            "current-year figure for the most recent year is a projection at the "
            "time of publication and subject to later revision. Per-capita values "
            "use UN population estimates; cumulative figures are historical sums "
            "since 1750 and are sensitive to how far back the underlying series "
            "extends for each country. Country borders/entities follow OWID's "
            "current-day definitions, which can complicate long-run cumulative "
            "comparisons for countries that split or merged (e.g. USSR, "
            "Czechoslovakia)."
        ),
    }
    return dataset


SECTOR_COLS = {
    "electricity_and_heat_co2_emissions": "Electricity & Heat",
    "transport_co2_emissions": "Transport",
    "manufacturing_and_construction_co2_emissions": "Manufacturing & Construction",
    "industry_co2_emissions": "Industry (other, non-combustion & direct)",
    "buildings_co2_emissions": "Buildings",
    "other_fuel_combustion_co2_emissions": "Other Fuel Combustion",
    "fugitive_co2_emissions": "Fugitive Emissions",
    "aviation_and_shipping_co2_emissions": "International Aviation & Shipping",
    "land_use_change_and_forestry_co2_emissions": "Land-Use Change & Forestry",
}


def build_sector_dataset():
    path = os.path.join(RAW_DIR, "owid_co2_by_sector.csv")
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["entity"] == "World":
                rows.append(row)
    latest = max(rows, key=lambda r: int(r["year"]))
    year = int(latest["year"])

    # World fossil+industry total for that year (Global Carbon Budget series)
    # for a cross-check / share-of-total context field.
    gcb_totals = read_csv("owid_co2_country.csv", "emissions_total")
    world_gcb_total_t = gcb_totals.get(("World", year))

    data = []
    sector_sum_t = 0.0
    for col, label in SECTOR_COLS.items():
        val = latest.get(col, "")
        if val in ("", None):
            continue
        val_t = float(val)
        sector_sum_t += val_t
        data.append({
            "category": label,
            "year": year,
            "value": round(val_t / 1e6, 1),
            "unit": "MtCO2",
            "source": "Climate Watch (2026) - Greenhouse Gas Emissions by Sector",
        })

    # Sort descending by value for readability, keep a "Total (sector sum)"
    # entry for transparency about how it compares to the GCB fossil+industry
    # total (they use different methods/scopes so will not match exactly).
    data.sort(key=lambda d: d["value"], reverse=True)
    data.append({
        "category": "Total (sum of sectors above, Climate Watch basis)",
        "year": year,
        "value": round(sector_sum_t / 1e6, 1),
        "unit": "MtCO2",
        "source": "Climate Watch (2026) - Greenhouse Gas Emissions by Sector",
        "notes": "Sum of the CO2-by-sector categories above; included for reference. This differs from the Global Carbon Project fossil+industry CO2 total for the same year because the two datasets use different sources, sector definitions, and (for Climate Watch) include CO2 from land-use change/forestry.",
    })
    if world_gcb_total_t is not None:
        data.append({
            "category": "Total (Global Carbon Project fossil + industry CO2, for comparison)",
            "year": year,
            "value": round(world_gcb_total_t / 1e6, 1),
            "unit": "MtCO2",
            "source": "Global Carbon Project - Global Carbon Budget 2025",
            "notes": "Independent world total from the Global Carbon Budget, shown for comparison with the Climate Watch sector sum above; excludes land-use change CO2.",
        })

    # Also add the widely-cited IPCC AR6 WGIII sectoral breakdown of ALL
    # anthropogenic GHG (not CO2-only) for 2019, since it is the standard
    # policy reference point (Figure SPM.2) and the task explicitly asks for
    # "any standard sub-breakdown a source like IEA or IPCC WGIII uses".
    ipcc_2019 = [
        ("Energy Supply (IPCC AR6 WGIII, all GHG, 2019)", 20000),
        ("Industry (IPCC AR6 WGIII, all GHG, 2019)", 14000),
        ("AFOLU - Agriculture, Forestry & Other Land Use (IPCC AR6 WGIII, all GHG, 2019)", 13000),
        ("Transport (IPCC AR6 WGIII, all GHG, 2019)", 8700),
        ("Buildings (IPCC AR6 WGIII, all GHG, 2019)", 3300),
    ]
    for label, mt_co2eq in ipcc_2019:
        data.append({
            "category": label,
            "year": 2019,
            "value": mt_co2eq,
            "unit": "MtCO2eq",
            "source": "IPCC AR6 WGIII (2022), Figure SPM.2",
            "notes": "This is ALL greenhouse gases (CO2 + CH4 + N2O + F-gases) expressed as CO2-equivalent, not CO2 alone -- included for comparison against the standard IPCC sectoral framing used in policy discussions. Energy supply, industry, transport, and buildings sum to 78% of the total; AFOLU adds the remainder (~22%). If indirect emissions from electricity/heat are reallocated to end-use sectors, industry's and buildings' shares rise from 24%->34% and 6%->16% respectively.",
        })

    dataset = {
        "title": "Global CO2 Emissions by Sector",
        "description": (
            f"Global CO2 emissions in {year} broken down by economic sector "
            "(Climate Watch / OWID data, energy- and process-based CO2 only), "
            "plus the standard IPCC AR6 WGIII all-greenhouse-gas sectoral "
            "breakdown for 2019 shown for policy-context comparison."
        ),
        "unit": "MtCO2",
        "data": data,
        "provenance": [
            {
                "source_name": "Climate Watch (2026) - Greenhouse Gas Emissions by Sector",
                "url": "https://www.climatewatchdata.org/ghg-emissions",
                "publisher": "World Resources Institute (Climate Watch)",
                "publication_year": 2026,
                "accessed_date": ACCESSED,
                "notes": "Retrieved via Our World in Data grapher CSV export (co-emissions-by-sector), which republishes Climate Watch's CO2-only sectoral series (1990-2023).",
            },
            {
                "source_name": "Global Carbon Project - Global Carbon Budget 2025",
                "url": "https://globalcarbonbudget.org/",
                "publisher": "Global Carbon Project",
                "publication_year": 2025,
                "accessed_date": ACCESSED,
                "notes": "Used only for the independent world fossil+industry CO2 total shown for comparison.",
            },
            {
                "source_name": "IPCC AR6 WGIII (2022), Figure SPM.2",
                "url": "https://www.ipcc.ch/report/ar6/wg3/figures/summary-for-policymakers/figure-spm-2/",
                "publisher": "Intergovernmental Panel on Climate Change, Working Group III",
                "publication_year": 2022,
                "accessed_date": ACCESSED,
                "notes": "Sectoral breakdown of total anthropogenic GHG emissions (all gases, CO2eq) for 2019, from the AR6 WGIII Summary for Policymakers.",
            },
        ],
        "caveats": (
            "The Climate Watch/OWID sector series is CO2 only (not all GHG) and "
            "uses a different sectoral taxonomy and total than the Global Carbon "
            "Project's fossil+industry figure shown here for comparison -- the two "
            "will not sum to the same world total, reflecting differences in "
            "underlying data sources, sector boundaries, and (for Climate Watch) "
            "inclusion of land-use-change CO2 and use of a 2023 data vintage. The "
            "'Industry' category in the Climate Watch data covers non-combustion "
            "industrial process emissions (e.g. cement calcination, chemical "
            "processes), while combustion-related industrial energy use is mostly "
            "captured under 'Manufacturing & Construction'; how a given source "
            "draws that line varies. The IPCC AR6 WGIII entries are ALL greenhouse "
            "gases in CO2-equivalent (not CO2 alone), for 2019 (the AR6 cutoff "
            "year), and are included because they are the standard policy "
            "reference framing (IPCC AR6 WGIII Figure SPM.2) -- do not sum or "
            "directly compare these CO2eq/2019 values against the CO2-only/2023 "
            "figures above without accounting for gas scope and year differences."
        ),
    }
    return dataset


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    country_ds = build_country_dataset()
    sector_ds = build_sector_dataset()

    with open(os.path.join(OUT_DIR, "co2_by_country.json"), "w") as f:
        json.dump(country_ds, f, indent=2)
        f.write("\n")

    with open(os.path.join(OUT_DIR, "co2_by_sector.json"), "w") as f:
        json.dump(sector_ds, f, indent=2)
        f.write("\n")

    print("Wrote co2_by_country.json with", len(country_ds["data"]), "records")
    print("Wrote co2_by_sector.json with", len(sector_ds["data"]), "records")


if __name__ == "__main__":
    main()
