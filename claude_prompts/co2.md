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

2. I have answered the questions in Q&A.  Please read them.  Then proceed to write a report named `Projects/ClimateIntelligence/CI_Reports/co2_report.md`.  Use Fable if you can.  Log your work.  The report should include:

    - A summary of the world's CO2 emissions
    - A breakdown of the world's CO2 emissions by country
    - A breakdown of the world's CO2 emissions by sector
    - A breakdown of the world's CO2 emissions by fuel type
    - A breakdown of the world's CO2 emissions by transport type
    - A breakdown of the world's CO2 emissions by industry
    - A breakdown of the world's CO2 emissions by energy type
    - A breakdown of the world's CO2 emissions by sector
    - A breakdown of the world's CO2 emissions by fuel type

Include figures.  Assess the growth in emissions, e.g. is it exponential?  What are the trends?  What are the drivers?  What are the implications?  What are the risks?  What are the opportunities?  What are the solutions?  What are the next steps?

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
>A. I've committed it to Git.  But thanks for the warning.

2. **Method mismatches, left unreconciled on purpose:** the Climate Watch sector
   total for 2023 (~37,963 Mt) doesn't match the Global Carbon Project country
   total (~38,094 Mt); IEA vs. Ember disagree on 2024 power-sector CO2 (13.8 vs
   14.6 Gt). Both figures are kept side-by-side with the discrepancy flagged in
   `caveats` rather than picked/reconciled — confirm that's the right call.
>A. That's the right call.

3. **IPCC WGIII sector figures are all-GHG CO2e (2019), not CO2-only** — included
   in `co2_by_sector.json` for policy context but flagged so they aren't summed
   with the CO2-only rows.
>A. ok

4. **Transport-by-mode has no single clean annual source** — the agent combined a
   2018 IEA percentage-share breakdown with more recent absolute totals from
   different datasets/years (Climate Watch, IEA Global Energy Review 2025, IATA,
   ICCT). Derived absolutes are labelled approximate; worth a manual sanity check
   before using in a post.
>A. ok

5. **IEA's site returned 403 on direct fetch** for all three agents — figures
   attributed to IEA came from its published reports/PDFs and search snippets,
   not a live scrape. Worth spot-checking key IEA numbers manually if they'll
   anchor a headline claim.
>A. ok
6. **"By fuel type" vs. "by energy type"** were treated as two distinct asks per
   your original list (fuel-type = coal/oil/gas/cement/flaring combustion
   categories from the Global Carbon Project; energy-type = power-sector
   generation-mix emissions from IEA/Ember) — confirm that split matches your
   intent, since the two categories overlap conceptually.
>A. That's fine

### Report

**Status (2026-08-23):** Prompt 2 executed. `CI_Reports/co2_report.md` written
(14 sections, all required breakdowns plus growth analysis, drivers,
implications, risks, opportunities, solutions, next steps), with figures
generated by the new `CI_Reports/make_co2_figures.py` (figs 23-29, continuing
the report's existing numbering). Delegated to a Fable subagent per the
prompt's "Use Fable if you can" instruction.

**Open question:**

7. **Possible internal inconsistency in the source data.** `co2_by_country.json`
   gives 2024 world CO2 = 38,598.6 Mt, but `co2_by_fuel_type.json`'s caveats cite
   a widely circulated **~38.1 GtCO2 "up 1.1% from 2024"** figure for 2025 — both
   attributed to the Global Carbon Budget 2025 report. 38.1 Gt is *lower* than
   38.6 Gt, which is inconsistent with "up 1.1%." This wasn't resolvable from the
   cached data alone (could be a scope difference between the two figures, or a
   transcription issue in one of the earlier research passes). Flagged honestly
   in the report's Summary rather than silently picking a number — worth
   checking against the primary Global Carbon Budget 2025 release before this
   anchors a headline claim in a published post.
>A.
