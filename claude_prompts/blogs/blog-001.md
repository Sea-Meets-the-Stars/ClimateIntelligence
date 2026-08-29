# Blog 001

## Goals

This prompt doc will help with the writing of Blog 001, my first.

## Context

See your context file `context/claudes_context.md` for the current context.

All of the figures (and related code) in this Repository.

## Prompts

### Figures

1. I have written a first draft of my first Blog for Climate Intelligence.  It is named `Blog 001` and is on my shared Google Drive named `Climate Intelligence`. Please review it and prepare to generate figures for it.  Ask me questions to aid your effort in the Q&A/Figures section.  Use Fable if you can.  Log your work.

2. I have answered the questions in Q&A/Figures.  Please read them, and then ask another round.  Log your work.  Use Fable if you can.

3. I have answered the questions in Q&A/Figures.  Please read them and then proceed to generate the figures.  
Log your work.  Use Fable if you can.

4. Let's edit Figure 2 on population growth.  Please:
   - Go back farther in time
   - Label and fit the main exponential periods
   - Use a log-scale x-axis if needed
Log your work.  Use Fable if you can.

## Q&A

### Figures

## Clarifying questions for Blog 001 figures

### Figure 1 — the sub-one-year-doubling exponential ("second most powerful we have ever experienced")

- **Q:** Is Figure 1 the early COVID-19 case-count curve (matching the "doubling time of 1 to 2 days" in the prose), or a different exponential entirely? If COVID: global confirmed cases, a single canonical country (e.g., U.S. or Italy, early 2020), or deaths instead of cases?
>A. Yes, it is the early COVID-19 case-count curve.
- **Q:** What date window should it cover — just the pure-exponential early phase (roughly Jan–Apr 2020, where the 1–2 day doubling actually holds), or the full pandemic arc showing the exponential eventually breaking (which would also visually support the later "either the exponential will break" point)?
>A. Yes, the full pandemic arc showing the exponential eventually breaking.
- **Q:** No COVID dataset exists in the repo yet — is a standard public archive (e.g., the JHU CSSE / Our World in Data COVID series, cached under `CI_Reports/data/` per house practice) acceptable as the source?
>A. Yes, the JHU CSSE / Our World in Data COVID series, cached under `CI_Reports/data/` per house practice is acceptable as the source.

### Figure 2 — human population growth ("the most powerful exponential")

- **Q:** Can the existing `fig7_world_population.png` (OWID/HYDE + UN WPP 2024, 1800–2100 with projections, from `CI_Reports/make_population_figures.py`) be reused directly, or do you want a blog-specific variant — e.g., historical-only (no projection fan), a longer 10,000-year run-up, and/or a log-scale version that makes the exponential character explicit? Note the prose calls population the #1 exponential, but strictly it stopped being exponential decades ago (growth rate peaked ~1968) — should the figure acknowledge that, or stay in the spirit of the essay?
>A. The existing `fig7_world_population.png` can be reused directly.

### Figure 3 — AI systems' exponential rise (~4-month doubling since "201X")

- **Q:** Which AI metric do you want plotted? Training compute of frontier models in FLOP (Epoch AI's dataset — the canonical curve, though its published doubling time is ~6 months since 2010, not 4), inference/benchmark capability (e.g., METR task-horizon doubling ~7 months), parameter counts, users/revenue, or something else? The "~4 months" claim in the prose needs to match whatever series we plot — are you open to revising that number to fit the data, or do you have a specific source in mind for 4 months?
>A. I can revise the number.  Let's use the Epoch AI's dataset.
- **Q:** What should "201X" resolve to — 2010 (start of the deep-learning compute era in Epoch's data), 2012 (AlexNet), or later (e.g., 2018/GPT-1)?
>A. I will edit it to match the figure.
- **Q:** The existing `make_ai_figures.py` covers only data-center electricity/water (figs 13–14), so this is a new dataset and script. Is Epoch AI's publicly downloadable notable-models database an acceptable source, cached under `data/` in the usual way?
>A. Yes, the Epoch AI's dataset is an acceptable source, cached under `data/` in the usual way.

### Figure XX — anthropogenic CO2 ("emitted by humans since 19XX", ~15-year doubling)

- **Q:** Which quantity: annual global fossil CO2 emissions (GtCO2/yr, as in the existing `fig23_global_co2_growth.png`), cumulative emissions since some start year, or atmospheric concentration (the Keeling curve, existing `fig1_keeling_curve.png`)? The "~15-year doubling" fits annual emissions only over roughly 1850–1970; since ~1970 the doubling time has stretched to 30+ years and emissions have nearly plateaued since ~2010. Do you want the fit restricted to the era where 15 years holds (with the recent flattening visible), or should the prose's number be adjusted?
>A. Let's use the Keeling curve.
- **Q:** What should "19XX" resolve to — 1850 (standard Global Carbon Project baseline, and what the existing scripts use), 1900, or 1950?
>A. I will edit it to match the figure
- **Q:** "Figure XX" appears twice — once for the CO2 exponential and once after "turning up the gas… Yet see Figure XX." Are both references to the same single CO2 figure, or is the second a different figure (e.g., emissions still rising / country breakdown for the "how did we get here" beat)?
>A. Yes, the same figure

### Population decline callback (currently no figure number)

- **Q:** The closing paragraph (R below 2.1, coming exponential decline) has no figure reference — do you want a fifth figure here (the existing `fig8_growth_rate.png` or `fig9_fertility.png` are natural candidates, possibly restyled), or should that paragraph stand on prose alone? (Small flag: replacement fertility is conventionally ~2.1 *TFR*, and world TFR already crossed it per UN WPP — "soon" may need a tweak depending on which series we show.)
>A. If you can generate a nice figure, I will use it.  I defer to your judgment.

### General

- **Q:** Figure numbering: should the blog use its own clean sequence (Figure 1, 2, 3, 4, 5 in order of appearance) independent of the CI_Reports fig1–fig31 numbering, with new blog-specific output filenames (e.g., `blogs/blog001/figN_*.png`)? And where should blog figures and their scripts live — a new `blogs/blog001/` directory, or inside `CI_Reports/`?
- **Q:** Style and provenance: same house style as the report figures (matplotlib rcParams from `make_figures.py`, provenance footers citing the cached data source, "Created by JXP and Claude" headers, data cached under `data/`), or a distinct lighter "blog" look? In particular, do you want each figure on a log y-axis with an annotated exponential fit and doubling time called out (1–2 days / ~4–6 months / ~15 years) so the figures directly carry the essay's argument?
- **Q:** Where existing PNGs could serve as-is, are you comfortable with the blog embedding the *same file* the report uses (so a future report regeneration silently changes the blog figure), or should every blog figure be an independently generated copy?

## Round 2 — clarifying questions for Blog 001 figures

### Figure 1 — the COVID-19 case-count curve

- **Q:** Global aggregate or a single country? The global cumulative curve smears out the sharp 1–2 day doubling (different countries' outbreaks start at different times), so a single early epicenter (e.g., U.S. or Italy) shows the log-linear early phase far more cleanly. And confirmed cases rather than deaths, correct?
>A. Ok, use the U.S.  And, cases, not deaths.
- **Q:** For the full pandemic arc, a log y-axis is essentially required to see the early doubling at all — and it will also expose the Delta/Omicron waves as later step-ups. Should only the original 2020 wave carry an annotated doubling-time fit, or each major wave? (Note: JHU CSSE stopped updating March 2023, so the "full arc" would come from OWID/WHO through ~2023–24.)
>A. Yes fit only the original 2020 wave.

### Figure 2 — human population growth

- **Q:** You approved reusing `fig7_world_population.png` as-is — but it is linear-scale with a UN projection fan. If the blog's unifying visual device becomes log-scale + annotated doubling times (see General below), this would be the one figure that breaks the pattern. Keep it exactly as-is anyway, or want a log-scale blog restyle?
>A. Ok, use the log-scale blog restyle and make a new figure.

### Figure 3 — AI systems' exponential rise

- **Q:** Epoch AI's notable-models database contains several series — training compute (FLOP), parameter count, dataset size, hardware cost. I assume training compute (FLOP), the metric behind the famous short doubling times — confirm? (Heads-up: Epoch's own headline figure is a doubling time closer to ~5–6 months, not ~4.)
>A. Yes, use the training compute (FLOP).
- **Q:** Division of labor on the numbers: once the fit is run, the actual doubling time and start year ("201X") will fall out of the data. Should the figure script simply report those numbers back to you so you hand-edit the prose (your stated plan), or do you want Claude to also edit the blog text directly to match — which is currently outside the figures-only scope?
>A. Simply report back

### Figure XX — the Keeling curve

- **Q:** There is a real mismatch between your figure choice and the prose's "~15-year doubling" claim: atmospheric CO2 concentration has risen only ~50% total (≈280 ppm pre-industrial → ~430 ppm today) and will never double on a 15-year cadence — the 15-year doubling describes *emissions* (GtCO2/yr), not concentration. Options: (a) reword the prose to what the Keeling curve genuinely shows (an accelerating rise — the growth *rate* went from ~0.8 ppm/yr in the 1960s to ~2.5 ppm/yr now); (b) keep a doubling-time annotation but on a derived quantity — the CO2 *excess above the 280 ppm pre-industrial baseline* is a genuine exponential, doubling roughly every ~30 years; or (c) revert to annual emissions, where ~15 years actually holds pre-1970. Which?
>A. Let's plot emissions instead of the Keeling curve.
- **Q:** Depending on the answer above: reuse the existing `fig1_keeling_curve.png` untouched, or generate a blog variant carrying the chosen annotation (log-scale excess, fitted curve, etc.)?
>A.  It will be a new figure.

### Population decline callback

- **Q:** You deferred to Claude's judgment — one confirming question before we run with it: the two candidate stories differ subtly. Fertility (TFR vs. the 2.1 replacement line, fig9-style) shows the threshold being crossed *now*; population growth rate turning negative (fig8-style) shows the shrinkage itself, which lags TFR by decades and better matches "coming exponential decline." Any preference, or genuinely Claude's pick with no further input?
>A. Go with fertility (TFR vs. the 2.1 replacement line, fig9-style).

### General (carried forward — unanswered in round 1)

- **Q:** Figure numbering and location: blog-clean sequence (Figure 1–5) with its own output filenames, and do the scripts/PNGs live in a new `blogs/blog001/` directory or inside `CI_Reports/`?
>A. Yes, blog-clean sequence (Figure 1–5) with its own output filenames, and the scripts/PNGs live in a new `blogs/blog001/` directory.
- **Q:** Style: house report style (rcParams, provenance footers, "Created by JXP and Claude" headers), or a lighter blog look? Specifically — should log y-axis + an annotated exponential fit with the doubling time called out be the *unifying device across all figures*, so the figures themselves carry the essay's argument? (This interacts with the Figure 2 and Keeling questions above.)
>A. Let's go with a lighter blog look.  No JXP and Claude headers.
- **Q:** For any reused PNG: embed the literal same file the report uses (so a future report regeneration silently changes the blog figure), or give every blog figure an independently generated copy frozen at publication?
>A. Give every blog figure an independently generated copy frozen at publication.