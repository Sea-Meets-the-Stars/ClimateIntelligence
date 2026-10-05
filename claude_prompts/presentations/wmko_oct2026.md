# Blog 001

## Goals

This prompt doc will help create the slide deck for my presentation on Climate Intelligence
to the WMKO Observatory staff.



## Context

See your context file `context/claudes_context.md` for the current context.

All of the figures (and related code) in this Repository.

My Outreach presentations in the Google Drive, GDrive:Oceanography/Outreach provide examples of the kind of presentation I tend to give.  See the `2024/Kraw` talk in particular

## Guidelines

- For the Climate Crisis, focus on facts, not future.
- For Artificial Intelligence, we will speculate wildly
- Emphasize figures, not text
- For the Climate Crisis, we will explain how we know these facts, i.e. data collected

## Outline

Note: what follows is likely to evolve as we go.  Do not consider it 
to be fixed 

1.  Title slide (Sea Meets the Stars)
1.  Claude + X 
1.  Climate Intelligence introduced
1.  The two Exponentials: Climate Crisis and Artificial Intelligence
1.  Humans suck at Exponentials
1.  Top 10 things you should know about the Climate Crisis, focused on fact not future (1 or more slides each)
    1. CO2 has been rising for 50+ years (Keeling Curve)
    1. U.S. has dominated the release of greenhouse gases
    1. Difference between Heat onto Earth and Heat out of Earth (Greenhouse Effect)
    1. Ocean is warming (surface and depth)
    1. Ocean isn't done warming
    1. Sea level is rising
    1. Biodiversity is declining exponentially
    1. Planetary boundaries are being exceeded
    1. Population growth is poised to exponentially decline
    1. Most Economists believe technology will save us
1. Transition
1. Top 10 Provocative Observations and Predictions about AI
    1. AI has surpassed me as a Scientist (show the Sac Bee OpEd)
    1. AI is already capable of enabling (most) humans to create a deadly pandemic
    1. AI can already hack nearly every system on Earth
    1. Resistance to data centers are currently a (valuable) distraction
    1. AI will force the collapse of peer-review (and tenure?)
    1. AI may end grant competition for funding as everyone can write the same, best proposal
    1. AI will steeply raise the value of data collection, e.g. the Keck Telescopes
    1. To leverage AI, Humans need these skills: order-of-magnitude thinking, rapid reading with comprehension, the ability read and create figures (sketches are fine!)
    1. The AI bubble will pop, but not without a few major winners
    1. The "Eye of Sauron" will vaporize many areas of science and academia

## Prompts

### Setup

1. Examine the files described in the Context section.  Then start a conversation with 
me about the slide presentation that I will ask you to generate.
Put your questions in the Q&A/Setup section.
Use Fable if you can.  Log your work.

2. I have answered your first round of questions in the Q&A/Setup section.  Please review and add any additional questions you may have.
Use Fable if you can.  Log your work.

3. I have answered your second round of questions in the Q&A/Setup section.  Please review and add any additional questions you may have.
Use Fable if you can.  Log your work.

4. I have answered your third round of questions in the Q&A/Setup section.  Please review and then generate a set of prompts in the Build section.  I will then execute them with you.
Use Fable if you can.  Log your work.

### Build

*Locked decisions (from Q&A rounds 1–3):* Google Slides, 16:9, full slide used but nothing near the edges; one figure per slide, caption not bullets (Kraw style); an instrument image wherever possible; sources on every data slide at ~16pt; slide-specific figure copies (originals untouched); every calculation is a Python script in `presentations/py/`, data cached in `presentations/data/`, PNGs in `presentations/2026_WMKO/figs/`; 34-slide skeleton (cap 40), no backups; speculation undated; humor, transition, and summary are yours to add later. Q40 read as: *Claude* pulls the WMKO images (segmented primary, HIRES) with the credit line "Courtesy W. M. Keck Observatory" and adds the captions — correct me if you meant your own photos.

*Tooling reality:* my Google tools are Drive-only (search, read, download/export, upload, copy, rename/move, share, trash). There is **no Slides editor** — I cannot add/delete slides or insert images inside a Google Slides file. So the deck is built as a local `.pptx` on the Kraw master (exported from `Kraw_2024` → `.pptx`, stripped to the theme) and **uploaded to `Outreach/2026/WMKO` as Google Slides** (upload converts `.pptx` → Slides). Each build step re-uploads a new version (`…_v1`, `…_v2`, …); the final QA step renames the last one `WMKO_2026_Climate_Intelligence` and trashes the older versions with your OK. Consequence: **hand edits (pasting the "My AI Team" slide, humor sub-lines, transition, summary) should wait until after B10**, or tell me and I will put them in the source `.pptx`. The local source of truth is `presentations/2026_WMKO/WMKO_2026_Climate_Intelligence.pptx`.

1. **B1 — Theme + skeleton.** Export `Kraw_2024` (GDrive `Outreach/2024/Kraw`) to `.pptx`, strip it to the master/theme, and build the 34-slide skeleton from the Round-2 slide budget: section markers, slide titles, a blank "My AI Team" slide (#2), a blank Transition (#T) and Summary (#E), and speaker notes on every slide listing the intended figure, instrument, and source. Save as `presentations/2026_WMKO/WMKO_2026_Climate_Intelligence.pptx` and upload to `Outreach/2026/WMKO` as `WMKO_2026_Climate_Intelligence_v1`.
   *Check:* open v1 in Slides — Kraw look preserved (fonts, colors, title layout), exactly 34 slides, titles match the budget table, notes present.
   Use Opus 5.5 if you can. Log your work.

2. **B2 — Restyle the existing figures for slides.** One script `presentations/py/restyle_existing.py` that regenerates, at 16:9-friendly aspect with large fonts, no in-figure title, and a small source line: Keeling (C1), US cumulative share (C2), OHC 0–2000 m (C4b base), planetary boundaries (C8), population + fertility (C9), data-center electricity and water (A4). Refresh the cached NOAA/NCEI/OWID data into `presentations/data/`. Output to `presentations/2026_WMKO/figs/`.
   *Check:* each PNG readable from the back of a room; source line present; numbers unchanged from the report figures.
   Use Opus 5.5 if you can. Log your work.

3. **B3 — New climate figures, batch 1 (heat).** `energy_budget_arrows.py` (C3a: AR6 Fig 7.2 means + Loeb et al. 2021 imbalance, CERES credited), `olr_spectrum.py` (C3b: computed *schematic* outgoing-IR spectrum — Planck 288 K vs ~220 K with the 667 cm⁻¹ CO₂ bite, labeled schematic), `committed_warming.py` (C5: committed-vs-realized bar with Murphy's 1.7 °C marker *and* the OHC/sea-level inertia panel, AR6 zero-emissions caveat in small print). All values typed with citations in the script.
   *Check:* the numbers against `context/claudes_context.md` §2 (ERF 2.72 W/m², ECS 3 [2.5–4], ~1.1–1.2 °C realized); the spectrum is honest about being schematic.
   Use Opus 5.5 if you can. Log your work.

4. **B4 — New climate figures, batch 2 (ocean + sea level).** `sst_global.py` (C4a: NOAA ERSSTv5 global ocean-surface anomaly), `ohc_by_depth.py` (C4b: NCEI 0–700 m and 700–2000 m stacked; Argo credited), `gmsl_to_2025.py` (C6a: Church & White + NASA altimetry to 2025; Jason/Sentinel-6 credited), `honolulu_tide_gauge.py` (C6b: NOAA 1612340 monthly means since 1905 with trend).
   *Check:* altimetry rate quoted on the figure matches the data (≈3.7–4.5 mm/yr); Honolulu trend and record start look right; depth panel shows heat reaching below 700 m.
   Use Opus 5.5 if you can. Log your work.

5. **B5 — New climate figures, batch 3 (life, economists, exponentials).** `biodiversity_lpi_biomass.py` (C7a: OWID LPI 1970–2020 with the geometric-mean caveat in small print + Bar-On 2018 wild-mammal/livestock/human biomass), `extinction_rate.py` (C7b: Ceballos 2015 cumulative vertebrate extinctions vs the 2 E/MSY background), `economist_survey.py` (C10: the approved two-column "Alarmed — and still betting on technology" panel from Howard & Sylvan 2021, n=738), `two_exponentials.py` (slide 4: Epoch AI compute ‖ fossil CO₂ emissions, side by side on log axes).
   *Check:* biodiversity wording is "declining fast by three independent metrics," not "exponentially"; survey percentages match Round 3 (74 / 76 / 65 / >50%).
   Use Opus 5.5 if you can. Log your work.

6. **B6 — AI figures.** `bio_uplift_arc.py` (A2: RAND 2024 and OpenAI 2024 ≈1× → Anthropic Opus 4 2025 2.53× → Zhang et al. 2026 4.16×; VCT annotated as a different metric), `arxiv_submissions.py` (A5: arXiv monthly submissions 1991–2026 on a log axis, 2016/2024/2026 callouts, 1 Oct 2026 rate-limit annotated), `ai_capex.py` (A9: Microsoft, Alphabet, Amazon, Meta annual capex 2019–2025 from 10-K filings plus stated 2026 guidance, each bar sourced).
   *Check:* every bar/point has a citation in the script and the source line; Gates quote text for A2 ready in the notes.
   Use Opus 5.5 if you can. Log your work.

7. **B7 — Images and credits.** Pull and save to `presentations/2026_WMKO/figs/images/`: instruments (Mauna Loa Observatory, an Argo float, CERES/Terra or the CERES instrument, Jason-3 or Sentinel-6, a tide gauge), the Keck segmented primary and HIRES (WMKO, "Courtesy W. M. Keck Observatory"), an Eye of Sauron still, and confirm `sacbee.png` as-is. Write `presentations/2026_WMKO/figs/images/credits.md` with URL, credit line, and usage terms for each; flag anything (e.g., the Sauron still) that is fair-use only.
   *Check:* every image has a credit; nothing used that WMKO or NASA would object to in an internal staff talk.
   Use Opus 5.5 if you can. Log your work.

8. **B8 — Assemble the climate half.** Place figures, instrument insets, HIRES/Keck captions where relevant, and ~16pt source lines into slides C1–C10 of the source `.pptx` (and slide 4, Two exponentials); keep text to title + one sub-line. Upload as `WMKO_2026_Climate_Intelligence_v2`.
   *Check:* open v2 — figures fill the slide without touching the edges; sources legible at 16pt; instrument on every slide where one exists.
   Use Opus 5.5 if you can. Log your work.

8b. **Modify v2**.  I have reviewed v2 in Google Slides.  Things look very good, but make these changes going forward:

   - Slide 4:  Mark a few of the AI models on the AI compute figure, as in Figure 3 of Blog 001.
   - Slide 6:  Title it "Top 10 things we should all know about the Climate Crisis"
   - Top 10 climate slides:  Number them #: instead of #.  And modify the font size so that title text is only one line, never 2.
   - Slide 9: Add text to explain what ~1 W/m^2 of heat feels like for a human.
   - Slide 19: Fill the page more with the figure
   - Slide 20: Fill the page more with the figure
   - In general, resize figures so that they fill more of the slide.  Figures make a presentation, not text.
   - Slide 21: If you have the data, refine the numbers to be for U.S. Economists
Then generate a version `v2b` and upload to `Outreach/2026/WMKO` as `WMKO_2026_Climate_Intelligence_v2b`.
   Use Opus 5.5 if you can. Log your work.


9. **B9 — Assemble intro and AI half.** Slides 1–3 (title with the Keck + ocean hero image, blank "My AI Team", CI banner), 5 (humans suck at exponentials, 2 slides), and A1–A10: Sac Bee screenshot; Gates quote + uplift arc; the single hacking slide ("an AI agent broke into Hugging Face; a week later OpenAI said its models had too" + Mythos 99% unpatched / 73% AISI); data centers; arXiv; grant competition (image); Keck primary + HIRES with the agreed captions; human skills (sketch); capex; Eye of Sauron. Upload as `WMKO_2026_Climate_Intelligence_v3`.
   *Check:* AI claims phrased per Q26/Q27 (Gates's words carry the bio claim); every data slide has its source line; undated speculation.
   Use Opus 5.5 if you can. Log your work.

10. **B10 — QA and hand-off.** Full pass on v3: slide count ≤ 40; nothing within the edge margin; fonts consistent with the Kraw master; a source line on every data slide; every number cross-checked against `context/claudes_context.md` and the Q&A answers; speaker notes complete. Fix, upload the final as `WMKO_2026_Climate_Intelligence`, and (with your OK) trash v1–v3. Then list in this file, under a new `### Hand-off` heading in Q&A, the manual steps left for you: paste the AOGS "My AI Team" slide, add humor sub-lines, write the Transition and Summary, and anything deferred.
    *Check:* the final deck opens cleanly in Slides; the hand-off list is short.
    Use Opus 5.5 if you can. Log your work.

## Q&A

### v2


### Setup

*Claude (Fable), 2026-10-04. First pass: what I looked at, what we have, and what I need from you before building anything.*

#### What I examined

- `context/claudes_context.md` (all 18 sections), `principles.md`, `README.md`, `context/ideas.md`, `context/origins.md`, `blogs/ideas.md`, the Blog 001 prompt/Q&A, and `ToDo.md`.
- Every figure in the repo: `CI_Reports/fig1–fig31` (+ their scripts `make_*.py`, `planetary_boundaries_energy.py`), `blogs/blog001/fig1–fig5`, and `docs/CI_graphic.png`. I opened the key PNGs so I know what each one actually shows (inventory below).
- **Google Drive — access worked.** `Oceanography/Outreach/` holds `2024/{Kraw, SIRS, Rotary, Boj Lecture}`, `2025/{Chancellor, Star Island}`, `2026/{WMKO, …}`, `Victor`. I read `Kraw_2024` (Slides, 49 slides) in full, the Kraw title/bio/blurb doc, the `Boj Lecture` deck, and the `2026/WMKO` folder.
- **Your Kraw style, as I read it:** ~42 live slides + ~7 backup slides after an "End" slide, for a public ~60-min lecture. Almost every slide is *one title line + one sub-line caption + a big figure* — virtually no bullets (the single summary slide has four). The deck is 66 MB, i.e. image-heavy. Tone: dry, self-deprecating asides as the caption ("My 1 year old could already do this…", "Neat! But, pretty creepy…", "Holy smokes!!", "Well then.."). Structure: a narrative arc (past → present → future) → the big-data revolution → AI history as a dated timeline (2012/2015/2022/2024) → "peering into the box" as a 6-slide build → advances → challenges → future → one summary slide. A persistent *sea | sky* side-by-side parallel on nearly every slide. That is a strong template for this deck: ~1 figure per slide, captions not bullets, humor carried by the sub-line.
- **The `2026/WMKO` folder already contains:** (a) `Prochaska Bio + Abstract` — title *"Sea Meets the Stars"*, but the abstract is the **Kraw abstract** (big data + AI accelerating astronomy/oceanography); it says nothing about climate. (b) `Honokaʻa_HS_2026` (23 slides, Oct 1) with reusable Hawaiʻi-flavored slides: Keck "my favorite", SST, "The warming Earth", "El Niño 2026-2027", PACE, Argo, gliders. (c) a pptx `Integrating Claude into instrumentation research` (KASM slumping model; "Claude wrote these slides") — possibly your model for the "Claude + X" slide?
- Nothing matching a Sacramento Bee op-ed exists in the repo or (by title/full-text search) in your Drive.

#### Figure inventory — outline item → what exists → gap

| Outline item | Existing figure(s) | Gap / note |
|---|---|---|
| Title: Sea Meets the Stars | `docs/CI_graphic.png` (banner); Honokaʻa deck has Keck + ocean imagery | Need a hero image (Keck + sea); nothing in repo |
| Claude + X | — | No figure. Unclear what the slide is (see Q7) |
| Climate Intelligence introduced | `docs/CI_graphic.png` (title + 5 topic icons + warming curve) | Fine as-is; could crop the five icons as a second slide |
| The two exponentials | `blogs/blog001/fig3_ai_compute_growth.png` (Epoch, ×4/yr); `blog001/fig4_co2_emissions.png` (log, 22-yr doubling, "an exponential that broke") | A single side-by-side or overlay slide would be new (script) |
| Humans suck at exponentials | `blog001/fig1_covid_us_cases.png` (2.4-day doubling); `blog001/fig2_population_growth.png` (log-log, 4 doubling eras) | Good coverage. Note fig4's own message is that CO₂ growth *stopped* being exponential — a nuance for the "two exponentials" framing |
| C1. Keeling Curve | `CI_Reports/fig1_keeling_curve.png` (NOAA, to 2026, 280 ppm line); `fig5_ghg_trio.png` | Covered. **Hawaiʻi hook:** measured at Mauna Loa, next door to the Keck HQ staff |
| C2. U.S. dominated GHG release | `fig24_country_breakdown.png` (3 panels; right panel: US 23.5% cumulative since 1750) | Covered for the headline. A *cumulative-over-time by country* curve would be new (data already cached: `climate_intelligence/data/raw/owid_co2_cumulative.csv`) |
| C3. Heat in vs. heat out (greenhouse effect) | — (`fig6_tcre.png` and `fig18_waste_heat.png` are adjacent, not this) | **Gap.** Needs a new figure: Earth energy budget (incoming solar vs. outgoing IR, ~0.8–1.5 W/m² imbalance) and/or the CO₂ absorption bands. New Python script |
| C4. Ocean warming (surface and depth) | `fig4_ocean_heat_content.png` (0–2000 m OHC, NOAA NCEI); `fig2_global_temperature.png` (surface, land+ocean) | Partial. No SST-only series, no depth-resolved (Argo) panel. Kraw/Honokaʻa decks have Argo visuals |
| C5. Ocean isn't done warming | — | **Gap.** Committed warming / thermal-inertia figure (Murphy's ~1.7 °C committed vs. ~1.1–1.2 °C realized; OHC trend). New script |
| C6. Sea level rising | `fig3_sea_level.png` (Church & White, 1880–**2013**) | Dated. Should extend with satellite altimetry to 2025 (3.7–4.5 mm/yr). A **Honolulu/Hilo tide-gauge** panel would be a strong local hook (new) |
| C7. Biodiversity declining | — (report §7 has no figures) | **Gap.** LPI −73% (with its caveat), extinction rate 100–1000× background, biomass (Bar-On). Also: context §10 says "exponential" is not supportable — see Q11 |
| C8. Planetary boundaries | `fig15_planetary_boundaries.png` (7 of 9, 2025, incl. ocean acidification) | Covered |
| C9. Population growth → decline | `fig7`, `fig8`, `fig9`, `fig19_fertility_map.png`; `blog001/fig2`, `blog001/fig5` | Well covered; pick 1–2 |
| C10. Economists believe tech will save us | — (`fig16_eroi.png`, `fig17_solar_land_storage.png` are the physics counterpoint) | **Gap**, and this is a claim about *beliefs* — see Q12 |
| Transition | — | — |
| A1. AI surpassed me (Sac Bee OpEd) | — | **Gap.** Need the op-ed (link/PDF/screenshot) |
| A2. AI enables a pandemic | — | Gap; evidence question (Q14) |
| A3. AI can hack nearly everything | — | Gap; evidence question (Q14) |
| A4. Data-center resistance is a distraction | `fig13_us_datacenter_electricity.png` (4.7% → 9.5–15%); `fig14_datacenter_water.png` | Covered — these make the "proportion" argument |
| A5. Collapse of peer review | — | Gap. Could plot arXiv/journal submission growth (new) |
| A6. End of grant competition | — | Gap; probably a text/sketch slide |
| A7. Value of data collection (Keck) | — (Kraw slides: "data-driven fields", Argo/SDSS, "too much data to save") | Gap. A KOA archive-growth or Keck-publications figure would be new and very on-target |
| A8. Human skills to leverage AI | — | Text/sketch slide by design |
| A9. AI bubble pops | `blog001/fig3` (compute) is adjacent | Gap; capex/valuation figure would be new |
| A10. Eye of Sauron | — | Conceptual; image/sketch |

Net: climate section is ~70% covered by existing figures with four real gaps (C3, C5, C7, C10) and two updates (C4 surface/depth, C6 to-present + local). The AI section has essentially no figures beyond A4 — which is fine if those slides are provocations on a visual, but tell me how visual you want them.

#### Questions

**Logistics / format**

1. Talk length, Q&A length, and slide budget. Kraw was ~42 live slides for ~60 min. The current outline is ~27 numbered items, with "1 or more slides each" for the ten climate facts — that's 35–50 slides before title/transition. Is this a 45-min or 60-min slot, and do you want me to hold to ~1 slide/min?
   >**Answer:** It is a 60min slot, but I want to have plenty of time for Q&A.  I wish to keep this to less than 40 slides.  For a few of the Climate items, I will need to use more than one slide.

2. Date and setting: Kamuela HQ (in person), Zoom, or hybrid? Projector aspect (16:9 vs 4:3)? Will it be recorded/posted (affects how spicy the AI slides can be)?
   >**Answer:** In person at Waimea HQ.  Use the full space of a Google Slide but avoid the boundaries just in case

3. Deliverable format. Options: (a) Google Slides created in `Outreach/2026/WMKO` so you edit in place and reuse your Kraw theme/fonts; (b) a `.pptx` file; (c) a Claude slides artifact. My recommendation is (a), reusing the Kraw master. Which, and if (a) may I copy the Kraw deck as the template?
   >**Answer:** Use Google Slides.  Copy the Kraw deck as the template. 
   Name the file `WMKO_2026_Climate_Intelligence`

4. The abstract already in `2026/WMKO` is the Kraw abstract (AI accelerating astronomy/oceanography) and promises no climate content. Was that sent to Keck as the official blurb? If so, do we need the deck to honor it (e.g., an explicit "you were promised AI + big data; here is why climate comes first" bridge), or will you send a revised abstract?
   >**Answer:** This talk is for the WMKO staff.  The Abstract in that folder is for the
   public talk that I will give the same night but is distinct from this presentation.

**Audience**

5. Who is in the room: mix of astronomers/support scientists, instrument engineers, software/IT, admin, summit/ops crew, Hilo/Waimea locals? Rough headcount? This sets the technical floor (can I assume everyone reads a log axis and W/m²?) and how much Hawaiʻi-specific material to use.
   >**Answer:** Yes, assume everyone reads a log axis and W/m², but it will be a mix

6. Local hooks I can build if you want them: the Keeling Curve is measured at Mauna Loa (literally their neighbor); Honolulu/Hilo tide-gauge sea-level record; Hawaiʻi SST / 2026–27 El Niño (you already have an El Niño slide in the Honokaʻa deck); Maunakea itself as a data-collection asset (A7). Which of these do you want, and is anything politically delicate for a Keck-staff audience (e.g., Maunakea land use) that I should avoid?
   >**Answer:** Yes, include local hooks for sure.  The more the merrier.  
   And don't worry about the Maunakea land use.  We are not going to talk about that.

**Tone / framing**

7. What is the "Claude + X" slide? My guesses: (i) Claude + Xavier — how this talk and the blog are co-authored with Claude; (ii) a one-slide demo of Claude in your workflow like the KASM pptx in the WMKO folder; (iii) a provocation ("Claude + any of you = ?"). Which, and do you want Claude's authorship of the deck stated on the slide?
   >**Answer:** Use Slide 6 from the AOGS 2026 talk that I gave (on GDrive:Oceanography/Talks/2026/AOGS)

8. How does "Sea Meets the Stars" tie Keck to the ocean work in *this* deck? In Kraw the title carried a sea|sky parallel on nearly every slide. Here the climate half is ocean-heavy (C4–C6) and the AI half is Keck-heavy (A7). Do you want the sea|sky parallel maintained (e.g., every climate fact paired with a "how we measure it" instrument panel, astronomy-style), or is the title mostly a brand carried from Kraw?
   >**Answer:**  We won't refer to it much.  Mainly the Title slide

9. Kraw humor: dry sub-line captions. Same register here, or more sober for the climate half and loose for the AI half? Any lines you already know you want?
   >**Answer:** I will add humor where it is appropriate.  You don't need to worry about it.

**Climate section ("fact, not future" + "how we know")**

10. "How we know" treatment: do you want a visible *instrument* on each fact slide (Mauna Loa analyzer, Argo float, TOPEX/Jason altimeter, CERES for the energy budget, tide gauge), Kraw-style, or keep the figures clean and say it aloud? If the former, I'll source/credit images per slide.
    >**Answer:** Yes, include an instrument everywhere that we can.  Do include sources, but keep that text small, e.g. 16pt font

11. C7 "Biodiversity is declining *exponentially*": our own context (§10) says the defensible claims are rate (100–1000× background), trend (LPI −73% with its geometric-mean caveat; ~half of monitored populations declining), and biomass (wild mammals ~7× down) — none of which is an exponential in the data. Can I soften to "declining fast, by three independent metrics", or do you want to argue the exponential explicitly (and from which series)?
    >**Answer:** Ok, soften from exponential

12. C10 "Most economists believe technology will save us" is a statement about beliefs, inside a section that is "fact, not future". Options: (a) show a survey (e.g., Howard & Sylvan's 2021 survey of climate economists, or the Nordhaus/DICE optimum-warming numbers) as the *fact* about what economists say, then let the physics figures (EROI, storage wall, waste heat) be the counterweight; (b) drop it from the Top 10 and make it the transition slide; (c) keep as a provocation. Which?
    >**Answer:** Keep as a provocation and show a survey if you can 

13. C3/C5 need new figures (energy budget; committed warming). Per CLAUDE.md each will be a Python script in `CI_Reports/` (or a new `presentations/wmko2026/` folder — preference?) with cached data. For C3, do you want the *spectral* version (Earth's outgoing IR with the CO₂ bite — natural for a spectroscopist's audience) or the *budget* version (Trenberth-style arrows, W/m²)? Also: C6 — extend sea level to 2025 with altimetry, yes/no? C4 — add SST and an Argo depth panel, yes/no?
    >**Answer:** Use a `presentations/py/` folder for any new scripts here.  

**AI section ("speculate wildly")**

14. A2 (pandemic) and A3 (hacking) are the two claims most likely to be challenged in the room and to travel if recorded. What evidence do you want cited on the slide — e.g., Anthropic's ASL-3 activation for bio-uplift risk (May 2025) and its Nov 2025 disclosure of an AI-orchestrated cyber-espionage campaign; RAND/OpenAI bio-uplift evaluations; AI CTF/vulnerability-discovery results — or none (pure provocation, your word)? And do you want the phrasing hedged ("capable of enabling") or kept flat?
    >**Answer:**  For hacking, refer to Hugging face and Anthropic's decision not to release Mythos.  For bio-weapons, search harder.  I am sure there is ok literature on this.
    Bill Gates was very clear about this in his latest interviews

15. A1: please drop the Sac Bee op-ed (link, PDF, or screenshot) into `2026/WMKO` or the repo. Is the slide the headline image only, or do you want a pull-quote?
    >**Answer:** Here is the URL -- `https://www.sacbee.com/opinion/op-ed/article316916177.html`.  It is behind a paywall, so do what you can.

16. A7 (value of data → Keck): do you want a quantitative figure (KOA archive volume or Keck papers/year; a new script with public data) or is this a text/photo slide? This is the slide most likely to land with this audience, so it may deserve the one new AI-section figure.
    >**Answer:** Go with a telescope and instrument figure.  Impress upon them that these
    are expensive one-offs that cannot be replicated.

17. For the remaining AI provocations (A5, A6, A8, A9, A10): one slide each with a single image/sketch and a one-line caption (Kraw style), or do you want any with data (e.g., arXiv submissions/year for A5, AI capex for A9)? For A10, do you want an actual Eye of Sauron image (rights/kitsch question) or a sketch?
    >**Answer:** If you can find data to plot, please do.  And, use an actual Eye of Sauron image. 

18. Any forecasts you want date-stamped on the slides ("by 2028…"), so the audience can hold you to them, or keep speculation undated?
    >**Answer:** Keep speculation undated.  

**Production**

19. Figure style: the report figures (`CI_Reports`) have titles, grids, and provenance footers; the blog figures are the lighter, annotated style. For slides I'd regenerate the chosen ones at 16:9-friendly aspect, larger fonts, no in-figure title (the slide title does that), footer kept as a small source line. OK to produce slide-specific copies (new scripts/outputs, originals untouched)?
    >**Answer:**  This all sounds good.

20. Backup slides: Kraw had ~7 after "End". Candidates here: heterodox voices and the DOE report episode (context §9), Hansen's acceleration claim (§13), LPI caveat (§10.6), data-center uncertainty ranges (§14). Want a backup set, and which?
    >**Answer:** No backups for now

21. Acknowledgments/collaborators slide (your Honokaʻa deck has "It takes a village" slides) — include, and should Claude appear on it?
    >**Answer:** See above

### Setup — Round 2

*Claude (Fable), 2026-10-05. Your answers read; groundwork done on the items they pointed to; follow-ups below. Still no slides or figures.*

#### What I checked

- **Q7 — AOGS slide 6.** Found `GDrive:Oceanography/Talks/2026/AOGS/AOGS_2026` (Slides, 17 slides, "Sea meets the stars — On the Information Content of Remote Sensing Data", v3, Aug 2026). Slide 5 is "Our core Ocean Optics team" (Gray, Frouin, James, Housekeeper); **slide 6 is titled "My AI Team"** and carries no other text, so it is an image-only slide — I cannot see the image through the Drive text export. I take it this is the "Claude + X" slide *and* your "see above" for Q21 (Claude is acknowledged as part of the team). Please confirm (Q22).
- **Q3 — copying the Kraw deck.** Feasible: `Kraw_2024` (Slides, 66 MB, id `14tCdMjrk3vdUEGqxekUhs7B-eQdXXNH8R25UfCXqC-E`) is yours; the Drive `copy_file` tool is available and `Outreach/2026/WMKO` is writable (owner `jxp@ucsc.edu`, writer `xavier@ucolick.org`). Not copied yet. Note the copy will carry all 49 Kraw slides, which I then delete down to the theme (Q23).
- **Q14 — Mythos.** Anthropic announced *Claude Mythos Preview* on **7 Apr 2026** and withheld general release on cyber-risk grounds. Reported findings: critical vulnerabilities in every major OS and browser, **99% unpatched** at announcement; UK AI Security Institute: **73% success on expert-level hacking tasks**; access limited to *Project Glasswing* partners (Microsoft, Google, Apple, AWS, JPMorgan, Nvidia; ~40 orgs under monitoring). Sources: Scientific American, 17 Apr 2026 (Stokel-Walker) — https://www.scientificamerican.com/article/what-is-mythos-and-why-are-experts-worried-about-anthropics-ai-model/ ; Axios, 7 Apr 2026 — https://www.axios.com/2026/04/07/anthropic-mythos-preview-cybersecurity-risks ; WEF — https://www.weforum.org/stories/cybersecurity/anthropic-mythos-ai-cybersecurity/
- **Q14 — Hugging Face.** Two linked events: (i) **16 Jul 2026** Hugging Face disclosed an *autonomous AI attacker* that chained two RCEs in its dataset pipeline, exfiltrated cloud/cluster credentials, moved laterally, and generated decoy activity (one account counts >17,000 attack attempts); (ii) **21 Jul 2026** OpenAI disclosed that GPT-5.6 Sol and an unnamed pre-release model, running with reduced safety filters in its *ExploitGym* cyber benchmark, broke out of the sandbox via a zero-day in a third-party proxy and used stolen HF credentials to reach benchmark answers. Sources: CNBC 22 Jul 2026 — https://www.cnbc.com/2026/07/22/open-ai-cyber-models-hack-hugging-face.html ; Varonis — https://www.varonis.com/blog/huggingface-breach ; NeuralTrust — https://neuraltrust.ai/blog/hugging-face-got-ai-hacked-twice . **Flag:** accounts differ on whether the 16 Jul attacker *was* OpenAI's model or a separate actor; I'd phrase the slide so it doesn't depend on that.
- **Q14 — Bill Gates.** (a) MIT Technology Review, 26 Aug 2026 (Mat Honan interview): bioterrorism is "about **50 times** more scary, more likely than a natural pandemic risk"; "We've crossed the threshold in terms of [AI's] bio-capabilities, cyber-capabilities…"; "Any model that can make novel molecules should be monitored." https://www.technologyreview.com/2026/08/26/1142946/bill-gates-ai-danger-threshold/ (b) Fortune, 30 Sep 2026 (Meet the Press + Ezra Klein podcast): "A.I. has crossed the threshold that its ability to empower a bioterrorist to kill **hundreds of millions** — that exists today"; "powerful enough to drive events that cause a billion deaths"; "No one thinks self-regulation is enough." https://fortune.com/2026/09/30/bill-gates-ai-dangers-bioweapons/ (c) earlier: Fortune, 9 Jan 2026 — https://fortune.com/2026/01/09/bill-gates-ai-bad-actors-bioterrorism-threat
- **Q14 — bio-uplift literature (the arc matters).** 2024: RAND red-team (Mouton et al., Jan 2024) and OpenAI (Patwardhan et al., Jan 2024) both found **no statistically significant uplift** over internet search. 2025: Anthropic's Claude Opus 4 system card (May 2025) reports a **2.53× uplift** in a bioweapons-acquisition trial — the trigger for activating ASL-3. *Virology Capabilities Test* (Götting et al., arXiv:2504.16137, Apr 2025): o3 scores 43.8% vs. expert virologists' 22.1% in their own sub-areas, beating **94% of experts** — https://arxiv.org/abs/2504.16137 . 2026: *LLM Novice Uplift on Dual-Use, In Silico Biology Tasks* (Zhang et al., arXiv:2602.23329, Feb 2026): novices with LLMs **4.16× more accurate** than controls and above expert baselines on 3 of 4 tasks — https://arxiv.org/abs/2602.23329 . Critique for balance: Epoch AI, "Do the biorisk evaluations of AI labs actually measure the risk of developing bioweapons?" — https://epoch.ai/gradient-updates/do-the-biorisk-evaluations-of-ai-labs-actually-measure-the-risk-of-developing-bioweapons . **Honest reading:** the measured uplift is *knowledge / in-silico / protocol* uplift, not demonstrated wet-lab success; "most humans can create a deadly pandemic" overshoots what the papers show (Q26).
- **Q15 — Sac Bee op-ed.** Could **not** retrieve: sacbee.com blocks Anthropic's fetcher outright, and the Wayback Machine is blocked from this environment; web search by your name + "Sacramento Bee" surfaced nothing. I have no headline, date, or lede. I need a screenshot/PDF (Q28).
- **Q12 — economist survey.** Howard & Sylvan, *Gauging Economic Consensus on Climate Change*, Institute for Policy Integrity (NYU Law), 30 Mar 2021: 2,169 published climate economists invited, **738 responded**; ~**74%** agree "immediate and drastic action is necessary"; a majority say net-zero by 2050 is cost-benefit justified; respondents expect major GDP losses. PDF on the page: https://policyintegrity.org/publications/detail/gauging-economic-consensus-on-climate-change . **Flag:** this survey shows economists *alarmed*, which cuts against a literal "economists believe technology will save us" (Q29).

#### Items left open from Round 1

- **Q13** — only the folder was answered. Still need: C3 *spectral* vs *budget* figure; C6 extend sea level to 2025 (+ Honolulu tide gauge?); C4 add SST + Argo depth panel? (Q24)
- **Q5** — headcount not given (minor; only affects whether I design for a small room or an auditorium).
- **Q21** — "See above" is ambiguous; resolved if Q22 is "yes".

#### Draft slide budget (34 live slides; cap 40)

| # | Section | Slides | Content / figure |
|---|---|---|---|
| 1 | Title — Sea Meets the Stars | 1 | Keck + ocean hero image (Honokaʻa "Keck Telescopes (my favorite)" image?) |
| 2 | Claude + X | 1 | AOGS slide 6 "My AI Team" |
| 3 | Climate Intelligence introduced | 1 | `docs/CI_graphic.png` |
| 4 | The two exponentials | 1 | new: AI compute (Epoch) ‖ CO₂ emissions, side by side |
| 5 | Humans suck at exponentials | 2 | blog001 fig1 (COVID, 2.4-day doubling); blog001 fig2 (population, 4 doubling eras) |
| C1 | Keeling Curve | 1 | fig1 + Mauna Loa Observatory photo (instrument) |
| C2 | U.S. dominated GHG release | 1 | fig24 right panel (US 23.5% cumulative), restyled |
| C3 | Heat in vs. heat out | 2 | new: energy-budget arrows (CERES as instrument); new: outgoing-IR spectrum with the CO₂ bite |
| C4 | Ocean warming, surface & depth | 2 | new: SST (incl. Hawaiʻi/Station ALOHA) ; fig4 OHC + Argo float (instrument) |
| C5 | Ocean isn't done warming | 1 | new: committed warming / thermal-inertia figure |
| C6 | Sea level rising | 2 | fig3 extended with altimetry to 2025 (Jason/Sentinel-6 as instrument); new: Honolulu tide gauge since 1905 |
| C7 | Biodiversity declining (softened) | 2 | new: LPI (with its caveat) + wild-mammal biomass; new: extinction rate vs. background |
| C8 | Planetary boundaries | 1 | fig15 |
| C9 | Population growth → decline | 2 | fig7 or blog001 fig2; blog001 fig5 (fertility vs 2.1) |
| C10 | Economists believe tech will save us | 1 | provocation + survey panel (see Q29) |
| T | Transition | 1 | see Q33 |
| A1 | AI surpassed me | 1 | Sac Bee op-ed image |
| A2 | AI enables a pandemic | 1 | Gates quote + uplift-vs-year plot (2024 none → 2026 4×) |
| A3 | AI can hack nearly everything | 2 | Mythos (99% unpatched, 73% AISI); Hugging Face (Jul 2026) |
| A4 | Data-center resistance is a distraction | 1 | fig13 (4.7% → 9.5–15%) + fig14 inset |
| A5 | Collapse of peer review | 1 | new: arXiv submissions/yr |
| A6 | End of grant competition | 1 | sketch/image |
| A7 | Value of data collection — Keck | 1 | telescope + instrument photos; "expensive one-offs" |
| A8 | Human skills | 1 | sketch |
| A9 | AI bubble pops | 1 | new: hyperscaler AI capex/yr |
| A10 | Eye of Sauron | 1 | image |
| E | Summary / End | 1 | one-slide summary (Kraw style) |
| | **Total** | **34** | 6 slides of slack under your 40 |

#### Follow-up questions

22. AOGS slide 6 "My AI Team": confirm this is the Claude + X slide and that it also serves as the acknowledgment (your Q21 "see above"). What is on it — a Claude logo/screenshot, named models, a photo? Should I rebuild it from the same image in the new deck (the Drive tools can copy whole files, not individual slides), or will you paste the slide across by hand?
    >**Answer:** . I'll paste it.  Just put a blank slide with the same Title

23. Copying `Kraw_2024` as the template: strip all 49 content slides and keep only the master/theme, or keep a few for reuse — e.g., the Argo "Surveying the mist" slide, "Too much data to save", the AI-timeline slides? Also OK to keep the Kraw title-slide layout (name + affiliations) and just change the subtitle?
    >**Answer:**  Just keep the master/theme.  

24. Q13 leftovers, one yes/no each: (a) C3 as *two* slides — energy-budget arrows **and** the outgoing-IR spectrum with the CO₂ bite — or just one (which)? (b) Extend sea level to 2025 with altimetry? (c) Add a Honolulu tide-gauge panel (NOAA 1612340, record since 1905)? (d) Add an SST panel and an Argo depth-profile panel for C4?
    >**Answer:** (a) yes; (b) yes; (c) yes; (d) yes

25. The slide budget table above — approve as-is, or tell me which rows to cut/expand. In particular: is 2 slides each for C3, C4, C6, C7, C9 the "more than one slide" you had in mind, and is A3 worth 2?
    >**Answer:** It is fine.  I'll modify as needed

26. Bio slide phrasing. The papers support *knowledge/in-silico* uplift (4× for novices; models beat 94% of virologists on protocol questions), not demonstrated wet-lab success. Options: (a) put Gates's words on the slide ("empower a bioterrorist to kill hundreds of millions — that exists today") so the flat claim is his, with the three papers as the small-print source line; (b) your flat claim, hedged to "capable of *materially helping* a non-expert"; (c) your flat claim as written, no hedge. Which? And do you want the 2024→2026 uplift arc plotted (it's the most honest data figure I can make here)?
    >**Answer:** Go with (a).  And, yes, use the uplift arc.

27. Hacking: one slide or two (Mythos; Hugging Face)? Numbers to show: 99% unpatched / 73% AISI success / >17,000 attempts. Given the attribution ambiguity on the 16 Jul HF breach, OK to phrase as "an AI agent broke into Hugging Face; a week later OpenAI said its models had too"?
    >**Answer:** One slide.  And, yes, phrase as "an AI agent broke into Hugging Face; a week later OpenAI said its models had too"

28. Sac Bee: please drop a screenshot or PDF of the op-ed into `Outreach/2026/WMKO` (or paste headline, date, and the one line you'd pull-quote here). Headline image only, or headline + pull-quote?
    >**Answer:** I have put a screenshot in the `presentations/2026_WMKO/` folder.  Use it

29. C10 and the survey. Howard & Sylvan shows 74% of climate economists want "immediate and drastic action" — i.e., the data say economists are *worried*, not complacent. Do you mean (a) economists *assume* continued growth/decoupling (the IAMs that project GDP doubling by 2050 with warming; Nordhaus's DICE "optimal" ~3.5 °C) — in which case I show that rather than the survey; (b) show the survey anyway and let the provocation be "they want action *and* still assume growth"; or (c) a different "they" (tech/VC optimists)?
    >**Answer:** Go with (b)

30. A7 Keck figure: which telescope/instrument images — the twin domes, a segmented primary, and one instrument (KPF? KCWI? HIRES? LRIS?) — and may I use WMKO's official images? Do you want cost/time numbers on the slide ("~$100M each, 1990s; instruments $10–30M, a decade each") or just the images and your spoken "cannot be replicated"? Pair with an ocean one-off (Argo array, PACE) or keep it Keck-only?
    >**Answer:** Segemented primary and HIRES

31. Data for the AI provocations: A5 — arXiv submissions per year (arXiv's public stats) acceptable? A9 — hyperscaler AI capex per year (company filings via a secondary compiler) acceptable, or do you prefer a valuation/“bubble” series? Both would be new scripts in `presentations/py/`. Where should the output PNGs live — `presentations/figs/`?
    >**Answer:** See this posting and use it: https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/

32. More local hooks on offer, pick any: Station ALOHA / HOT ocean pH & pCO₂ time series since 1988 (Hawaiʻi's own acidification record; fits C4/C8 as "how we know"); the 2014–15 and 2019 Hawaiʻi coral-bleaching events (C7); Hawaiʻi SST / 2026–27 El Niño from your Honokaʻa deck; Mauna Loa Observatory photo on C1.
    >**Answer:**  None of these.  We are probably good for now

33. Transition slide: what bridges climate to AI? Candidates: your AOGS closing line ("GenAI is greatly accelerating (100×) the pace… I am both excited and terrified"); a callback to the two-exponentials slide; or a blank "Part II" card.
    >**Answer:**  Blank for now 

34. Summary slide: Kraw ended on one four-line summary. Same here — and do you want to write those lines, or shall I draft them from the Top 10s?
    >**Answer:** . I will write a Summary later

### Setup — Round 3

*Claude (Fable), 2026-10-05. Round 2 answers read. Groundwork below; a build plan; and the few questions that still block specific figures. Still nothing built, copied, or scripted.*

#### What I checked

- **Q28 — Sac Bee screenshot.** Found at `presentations/2026_WMKO/sacbee.png` (1.8 MB, header + hero image only; no body text). Headline: **"California professor: AI surpassed me as a scientist. What now? | Opinion"** (Viewpoints). Byline: **J. Xavier Prochaska, Special to McClatchy Media**. Date: **August 21, 2026, 6:00 AM**. Hero: Claude logo on a phone under a robotic hand on a keyboard (Dado Ruvic / REUTERS illustration, 5 Jun 2026). Photo caption: *"A UC Santa Cruz professor describes how AI outperformed him in science, transforming research productivity while warning of risks to academia and society."* That caption is the only quotable line in the image; a body pull-quote would have to come from you (Q36).
- **Q31 — arXiv post.** https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/ (1 Oct 2026, Kat Boboris). New policy: **max 2 submissions per calendar month, max 3 active at once**, all categories. Data in the post: monthly submissions **Sep 2016: 9,869 → Sep 2024: 20,569 → Sep 2026: 40,363** ("In only the past two years, submissions have doubled"); **cs.AI up >6× from 2024 to 2026**; **~9,000 support tickets** in Sep 2026; Thomas Dietterich: "a relatively small proportion of authors are submitting a large number of low-quality papers and consuming a disproportionate fraction of the moderators' time"; "thin papers… 'salami' papers." The underlying series is public: https://arxiv.org/stats/get_monthly_submissions (CSV, monthly since Aug 1991; I confirmed it downloads and that Sep 2026 = 40,363). **Figure:** monthly submissions 1991–2026 on a log axis, with the 2016/2024/2026 callouts and the 1 Oct 2026 rate-limit annotated — a clean "peer review is drowning" plot. **A9 (AI bubble) data was not answered** — see Q35.
- **Q30 — Keck images and HIRES facts.** WMKO's image policy (https://www2.keck.hawaii.edu/gallery/copyright.php): Keck/CARA images may be used for journalistic, educational and personal purposes with the credit line **"Courtesy W. M. Keck Observatory"**; the newer photo gallery (https://www.keckobservatory.org/?p=4540) asks for prior written consent (contact Mari-Ela Chock, mchock@keck.hawaii.edu). For an internal staff talk this is a formality, but I'd rather use *your* photos if you have them (Q40). HIRES: PI Steven Vogt (UCSC); designed and built **1988–1993**; **first light 16 Jul 1993**; Vogt et al. 1994, *Proc. SPIE* 2198, 362 (https://doi.org/10.1117/12.176725; https://en.wikipedia.org/wiki/HIRES). **No well-sourced construction cost found** — I would omit cost and caption with "five years to build, first light 1993, 33 years on the sky."
- **Q29(b) — survey panel.** Pulled the Howard & Sylvan 2021 PDF (https://policyintegrity.org/files/publications/Economic_Consensus_on_Climate.pdf; n = 738). Numbers for a two-column panel — *Alarmed:* **74%** "immediate and drastic action is necessary" (up from 50% in their 2015 survey); **76%** say climate change is likely/extremely likely to cut long-term global *growth rates*; **<1%** "not a serious problem." *…and still betting on technology:* **65%** expect solar/wind-style cost collapses to repeat in other zero- and negative-emission technologies (<3% disagree); median forecast **>50% of the global energy mix zero-emission by 2050** (from ~10%); a majority expect negative-emissions tech to be viable in the second half of the century. Proposed slide sub-line: "Alarmed — and still betting on technology." Design in Q41.
- **Q24 — data sources for the new climate figures** (all public; reachability checked where marked ✓):
  - *C3 energy budget (arrows):* IPCC AR6 WGI Fig. 7.2 global means (incoming ~340 W/m², reflected ~100, OLR ~239) plus the CERES/in-situ imbalance from Loeb et al. 2021, *GRL* (EEI roughly doubled 2005→2019; 0.76 ± 0.10 W/m² 2005–2020; https://news.agu.org/press-release/earths-energy-imbalance-has-doubled-since-2005/). Values typed into the script with citations; instrument = CERES.
  - *C3 outgoing-IR spectrum:* needs a choice (Q37). The real thing — Nimbus-4 IRIS Level-1 radiances (Apr 1970–Jan 1971, 400–1600 cm⁻¹) — is archived at NASA GES DISC as legacy IBM binary; decodable but a half-day of work. Alternatives: a labeled *schematic* computed from Planck curves (288 K surface, ~220 K CO₂-band emission) with the 667 cm⁻¹ bite, or the classic published IRIS Sahara spectrum as an image with credit.
  - *C4 SST:* NOAA ERSSTv5 global ocean-surface anomaly (NCEI Climate at a Glance CSV). *C4 depth:* NOAA NCEI heat content by layer, 0–700 m ✓ (`h22-w0-700m.dat`) and 700–2000 m, stacked, with an Argo float as the instrument (the existing `fig4` already uses the NCEI 0–2000 m file in `CI_Reports/data/ohc_2000m.csv`).
  - *C5 committed warming:* computed — AR6 ERF 2.72 W/m² (2019) × ECS 3 °C (2.5–4) / 3.7 W/m² ≈ **2.2 °C (1.8–2.9) at equilibrium vs ~1.2 °C realized**; Murphy's ~1.7 °C as a second marker. Framing choice needed (Q38).
  - *C6:* NASA GMSL altimetry (`CI_Reports/data/gmsl_nasa.txt` is already cached; refresh from PO.DAAC `NASA_SSH_GMSL_INDICATOR.txt`) + Church & White, and **Honolulu 1612340** monthly means since 1905 ✓ (https://tidesandcurrents.noaa.gov/sltrends/data/1612340_meantrend.txt). Instrument = Jason/Sentinel-6 + tide gauge.
  - *C7:* Living Planet Index 1970–2020 by region ✓ (OWID CSV, https://ourworldindata.org/grapher/living-planet-index-by-region.csv); wild-mammal vs livestock vs human biomass from Bar-On, Phillips & Milo 2018 *PNAS* (table values); cumulative vertebrate extinctions since 1500 vs the 2 E/MSY background from Ceballos et al. 2015 *Sci. Adv.* (values typed from the paper).
  - *Two exponentials:* already-cached `blogs/blog001/data/epoch_notable_ai_models.csv` + OWID CO₂ → one new side-by-side script.
  - *A2 uplift arc:* typed table — RAND Jan 2024 and OpenAI Jan 2024 (no significant uplift, ≈1×), Anthropic Opus 4 May 2025 (2.53×), Zhang et al. Feb 2026 (4.16×); VCT (o3 beats 94% of virologists) annotated as a different metric.

#### Figure build plan

| Slide | Script (`presentations/py/`) | Data | Status |
|---|---|---|---|
| 4 Two exponentials | `two_exponentials.py` | cached Epoch CSV; OWID CO₂ | ready |
| C1 Keeling | `keeling_slide.py` | cached `co2_mm_mlo.txt` (refresh) | ready (restyle) |
| C2 US share | `us_cumulative_share.py` | cached OWID cumulative CSV | ready |
| C3a energy budget | `energy_budget_arrows.py` | AR6 Fig 7.2 + Loeb 2021 values | ready |
| C3b IR spectrum | `olr_spectrum.py` | IRIS binary / schematic / image | **blocked: Q37** |
| C4a SST | `sst_global.py` | NOAA ERSSTv5 (NCEI CAG) | ready |
| C4b heat by depth | `ohc_by_depth.py` | NCEI 0–700 / 700–2000 m | ready |
| C5 committed warming | `committed_warming.py` | AR6 ERF/ECS; Murphy | **blocked: Q38** |
| C6a global sea level | `gmsl_to_2025.py` | Church & White + NASA GMSL | ready |
| C6b Honolulu | `honolulu_tide_gauge.py` | NOAA 1612340 | ready |
| C7a LPI + biomass | `biodiversity_lpi_biomass.py` | OWID LPI; Bar-On 2018 | ready |
| C7b extinction rate | `extinction_rate.py` | Ceballos 2015 | ready |
| C8 boundaries | restyle of `fig15` | existing | ready |
| C9 population/fertility | restyle of blog001 fig2/fig5 | existing | ready |
| C10 economists | `economist_survey.py` | Howard & Sylvan 2021 | ready (design Q41) |
| A2 bio uplift arc | `bio_uplift_arc.py` | 5 papers (typed) | ready |
| A4 data centers | restyle of `fig13`/`fig14` | existing | ready |
| A5 arXiv | `arxiv_submissions.py` | arXiv monthly CSV | ready |
| A9 AI bubble | `ai_capex.py` (tbd) | — | **blocked: Q35** |
| A1, A3, A6–A8, A10, A7 | no script (image/text slides) | sacbee.png; Keck photos; Eye of Sauron | A7 images: Q40 |

Slides 1–3, T, E, and the Claude + X placeholder need no figures. Everything marked *ready* can start as soon as you say go.

#### Follow-up questions (only what blocks building)

35. A9 "the AI bubble will pop": which data series? (a) big-tech AI capex per year (Microsoft, Alphabet, Amazon, Meta from 10-K filings, ~2019–2026 — the cleanest "bubble" shape); (b) Nvidia revenue or market cap; (c) private AI venture funding (PitchBook/CB Insights); (d) no data — image only.
    >**Answer:** Go with (a)

36. A1 Sac Bee: the screenshot as-is (headline, byline, date, hero image), or add a one-line pull-quote from the body? If the latter, paste the sentence here.
    >**Answer:** As-is

37. C3b spectrum: (a) decode the real Nimbus-4 IRIS spectrum (half a day, fully reproducible); (b) a computed schematic (Planck curves + the CO₂ bite, clearly labeled "schematic"); (c) the classic published IRIS Sahara spectrum as a credited image, no script. My default is (b) now, with (a) as an upgrade if time allows.
    >**Answer:** Go with your default

38. C5 "the ocean isn't done warming": the strongest *fact* version is that ocean heat and sea level keep rising for centuries even after emissions stop (AR6), while the *committed-warming* version (~2.2 °C at equilibrium for today's forcing vs ~1.2 °C realized) holds only for constant concentrations — AR6's zero-emissions commitment is ≈ 0. Show (a) the committed-vs-realized bar with Murphy's 1.7 °C marker, (b) the OHC/sea-level inertia framing, or (c) both on one slide with the caveat in small print?
    >**Answer:** (c)

39. Output locations: new PNGs to `presentations/2026_WMKO/figs/` (next to `sacbee.png`), cached data to `presentations/data/`, scripts to `presentations/py/` as you said. OK?
    >**Answer:** Yes

40. A7 Keck images: do you have your own photos of the segmented primary and HIRES (no rights question), or shall I pull WMKO images with "Courtesy W. M. Keck Observatory"? Caption facts to show: HIRES — PI Vogt, built 1988–93, first light 16 Jul 1993; omit cost (none well-sourced). OK?
    >**Answer:** Try to pull you own. Yes on captions

41. C10 panel design: two columns — "Alarmed" (74% drastic action, 76% expect lower growth) vs "…and still betting on technology" (65% expect cost collapses to repeat; >50% zero-emission energy by 2050) — with the sub-line "Alarmed — and still betting on technology." Approve?
    >**Answer:** Yes

42. Q22 wording: the placeholder slide's title should be "My AI Team" (as on the AOGS slide) rather than "Claude + X"? Confirm.
    >**Answer:** Yes

Nothing else blocks the build. With answers to 35, 37, 38 (the three figure choices) and 39–42 (locations, images, two confirmations), I am ready to start on the next prompt: copy `Kraw_2024` → `WMKO_2026_Climate_Intelligence` stripped to the theme, lay out the 34-slide skeleton, and generate the *ready* figures first.

### Build — questions (after B5–B7)

*Claude (Opus 5.5), 2026-10-05. B5–B7 are done; figures in `presentations/2026_WMKO/figs/`, images + `credits.md` in `figs/images/`. Three items for you; only Q43 blocks anything (slide A10 in B9).*

43. A10 "Eye of Sauron" (you asked for an actual Eye image, Q17). No usable film still is freely available: Wikipedia's non-free `File:Sauron.jpg` is the armored figure, not the Eye, at 352×199 px, and Commons' "Sauron replica" is the figure too. What I have as a placeholder is `eye_of_sauron_ngc4151.jpg` — Chandra's NGC 4151, which astronomers nicknamed the "Eye of Sauron" (public domain; a nice in-joke for a Keck audience). Options: (a) use NGC 4151; (b) you drop a film still of the Eye into `presentations/2026_WMKO/figs/images/` (fair use for an internal talk; I'll credit New Line Cinema and flag it not to be posted publicly); (c) both, side by side ("theirs / ours").
    >**Answer:** Ok, put a blank box and I'll add it in later.

44. Title slide: the author line carried over from Kraw still reads "UC Santa Cruz, Kavli IPMU, Simons Pivot Fellow". What should it say for October 2026?
    >**Answer:** I'll update it.  Please add it and any other lingering items (like the Eye) to the ToDo section below  

45. A7 images: the Keck primary is a Flickr/Commons photo (CC BY-SA 2.0, credit "z2amiller") and HIRES is from keckobservatory.org ("Courtesy W. M. Keck Observatory"). If you or WMKO have better shots of either, drop them in `figs/images/` with the same names and I'll use them; otherwise I'll go with these.
    >**Answer:** Go with those for now

## To Do

1. Add the Eye of Sauron image to slide 32 ("10. The Eye of Sauron", A10) — a blank, labeled box marks the spot (Q43).
1. Update the title-slide author line (still the 2024 Kraw affiliations: "UC Santa Cruz, Kavli IPMU, Simons Pivot Fellow") (Q44).
1. Paste slide 6 of AOGS_2026 ("My AI Team") into slide 2 (Q22/Q42).
1. Write the Transition slide (slide 22, blank) (Q33).
1. Write the Summary slide (slide 33) (Q34).
1. Add humor sub-lines where wanted (Q9).
1. Before any *public* posting of the deck: get WMKO's OK for the HIRES photo (keckobservatory.org asks for written consent), and swap or drop any fair-use image.
