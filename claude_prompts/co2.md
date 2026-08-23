# CO2 Emissions and more

## Goals

This prompt doc will make calculations related to CO2 emissions and its impacts on the Earth.

## Context

See your context file `context/claudes_context.md` for the current context.

## Prompts

### Prep

1. Let's begin by exploring the world's CO2 emissions.  Please search the web for the following information:
    - The world's CO2 emissions by country
    - The world's CO2 emissions by sector
    - The world's CO2 emissions by fuel type
    - The world's CO2 emissions by transport type
    - The world's CO2 emissions by industry
    - The world's CO2 emissions by energy type
    - The world's CO2 emissions by sector
    - The world's CO2 emissions by fuel type

Record these in a machine readable format in a file in `Projects/ClimateIntelligence/climate_intelligence/data`.  Be sure to keep provenance information for each data point.  If you have any questions, put them in the Q&A section below under Prep.  Use Fable if you can.  Log your work.


## Q&A

### Prep

**Status (2026-08-23):** Prompt 1 executed. Three parallel research agents (model:
Fable) searched the web and wrote six machine-readable JSON datasets to
`climate_intelligence/data/`: `co2_by_country.json`, `co2_by_sector.json`,
`co2_by_fuel_type.json`, `co2_by_transport_type.json`, `co2_by_industry.json`,
`co2_by_energy_type.json`. Each file has a `provenance` array (source name, URL,
publisher, year, access date) and a `caveats` field. Sources: Global Carbon
Project (Global Carbon Budget 2025), Our World in Data, Climate Watch/CAIT, IEA
(via reports/search, site blocked direct scraping), Ember, ICCT, IATA, IPCC AR6
WGIII. Reproducible build scripts are included (`bin/build_co2_datasets.py` for
country/sector; `climate_intelligence/data/scripts/` for fuel/transport); raw
CSV inputs are cached in `climate_intelligence/data/raw/`.

**Open questions / things to check before publishing from this data:**

1. **Raw cache size.** `climate_intelligence/data/raw/owid-co2-data.csv` is ~14 MB
   (the other raw CSVs are ~0.5–0.9 MB each). Do you want this committed to git,
   or should `climate_intelligence/data/raw/` be added to `.gitignore` (the build
   scripts can re-download on demand)?
2. **Method mismatches, left unreconciled on purpose:** the Climate Watch sector
   total for 2023 (~37,963 Mt) doesn't match the Global Carbon Project country
   total (~38,094 Mt); IEA vs. Ember disagree on 2024 power-sector CO2 (13.8 vs
   14.6 Gt). Both figures are kept side-by-side with the discrepancy flagged in
   `caveats` rather than picked/reconciled — confirm that's the right call.
3. **IPCC WGIII sector figures are all-GHG CO2e (2019), not CO2-only** — included
   in `co2_by_sector.json` for policy context but flagged so they aren't summed
   with the CO2-only rows.
4. **Transport-by-mode has no single clean annual source** — the agent combined a
   2018 IEA percentage-share breakdown with more recent absolute totals from
   different datasets/years (Climate Watch, IEA Global Energy Review 2025, IATA,
   ICCT). Derived absolutes are labelled approximate; worth a manual sanity check
   before using in a post.
5. **IEA's site returned 403 on direct fetch** for all three agents — figures
   attributed to IEA came from its published reports/PDFs and search snippets,
   not a live scrape. Worth spot-checking key IEA numbers manually if they'll
   anchor a headline claim.
6. **"By fuel type" vs. "by energy type"** were treated as two distinct asks per
   your original list (fuel-type = coal/oil/gas/cement/flaring combustion
   categories from the Global Carbon Project; energy-type = power-sector
   generation-mix emissions from IEA/Ember) — confirm that split matches your
   intent, since the two categories overlap conceptually.
