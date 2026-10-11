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
And, add "Figure XX" to each of the figures.
Log your work.  Use Fable if you can.

### Editing

1. Please examine the `Blog 001` file on my shared Google Drive named `Climate Intelligence` and discuss whether it follows the Guiding Principles listed in `principles.md`.  Put questions or comments in the Q&A/Editing section.  Log your work.  Use Opus if you can.

## Q&A

### Editing

## Review against the Guiding Principles (`principles.md`)

### Principle 1 — Let fact trump opinion, but recognize all human measurements bear uncertainty (and bias!)

- **Comment:** The revised draft is much better here than the placeholder version — "a doubling time of ~22 years from 1850-1970" states its fit window in the prose, which is exactly right and matches the fit in `make_fig4_co2_emissions.py` (21.6 yr). Same for the AI paragraph. That convention should be applied uniformly.
- **Q:** The COVID number is the one left un-updated: the essay still says "it had a doubling time of 1 to 2 *days*," but the exponential fit to the actual U.S. case series (`make_fig1_covid_us_cases.py`, 2020-03-01 to 2020-04-01) gives **2.37 days**, which is what Figure 1 will be annotated with. A reader who looks from prose to figure sees a contradiction. Do you want to change the text to "~2.4 days," or is "1 to 2 days" meant to refer to a different series (some individual countries/regions did hit ~1.5 d briefly)? If the latter, it needs a source.
- **Comment (the "bias!" clause):** Early-2020 *case* doubling is partly a testing-capacity doubling, not purely a transmission doubling — the U.S. was ramping tests over precisely the fit window. This is a gift of an example for the principle: your single best-known exponential is measured through an instrument that was itself growing exponentially. One clause acknowledging it would strengthen rather than weaken the paragraph.
- **Q:** "In any AI metric you can construct, the growth has been exponential with a doubling time of approximately 6 months." Figure 3 plots frontier *training compute*, an input, and ~6 months is Epoch's number for that specific series. "Any metric you can construct" is a much stronger claim than the figure supports — capability benchmarks saturate at a ceiling, METR's task-horizon doubling is ~7 months, cost-per-token has *fallen*. Would you soften to "in essentially every input metric, and in the capability metrics we can measure"?
- **Q:** "real-world examples of exponentials are rare: compound interest, Moore's Law, NYSE, U.S. home prices" — U.S. home prices are the weak link. In *real* terms the Shiller index is roughly flat from 1890 to 1990; the exponential is mostly inflation, which is also what makes "compound interest" and "NYSE" partly the same example. Is the list worth trimming to the ones that survive deflating?
- **Q:** "anyone over the age of 30 *knows* the planet is warming because they have experienced the change first-hand." This grounds the central fact of the blog in personal anecdote — the one epistemology Principle 1 exists to subordinate. The instrumental record is decisive on its own; do you want to keep the felt-experience framing as *rhetoric* while making clear the evidence is the record, not the memory?
- **Comment:** "the ocean has kindly absorbed ~90% of the excess heat to date" is right (~89-91% in the IPCC AR6 energy budget), but it is doing odd work in that sentence: ocean heat uptake delays the *warming*, it does not make the *emissions* exponential slow or delayed. As written the "and worse – delayed – because…" clause attaches the ocean to the wrong quantity.

### Principle 2 — Welcome all viewpoints, but do not accept them equally

This is where the draft is furthest from the principle, and furthest from the project's own stated norm in `context/claudes_context.md` (steel-man the heterodox case, credit real expertise, cite the published rebuttals, never strawman).

- **Q:** "a small set of powerful humans could convince the bulk of us otherwise." The Oreskes/Conway thesis is *documented* — API, the Global Climate Coalition, the Exxon internal-projection paper (Supran, Rahmstorf & Oreskes 2023). So the claim is defensible, but here it arrives with no citation and in a form that collapses two very different groups: funded disinformation operations, and credentialed scientists (Lindzen, Christy, Curry, Koonin) who argue about sensitivity, attribution, and impacts rather than about the greenhouse effect. Does the paragraph want to distinguish them? As written, everyone who disagreed is a deceiver.
- **Q:** "every scientist worth their salt knew we were in trouble" is a no-true-Scotsman: dissenters are defined out of the set rather than answered. The actual record (Charney 1979, IPCC FAR 1990) is strong enough to make the point without the construction — is there a reason to prefer the rhetorical version?
- **Q:** "the voices of deception have finally silenced (mostly)." Is this empirically true in 2026, or is it that the argument *moved* — from "it isn't warming" to "it's warming but adaptation is cheaper / the models run hot / policy is the real harm"? If it moved rather than stopped, the sentence both misstates the state of play and tells the very readers you most want (the persuadable skeptic) that this blog isn't listening.
- **Q:** "Don't let the geniuses at the AI companies tell you otherwise." This rejects a position by pointing at who holds it. What is the actual argument being dismissed — that scaling will plateau on its own, that alignment is tractable, that fast feedback loops enable fast correction? Principle 2 permits ranking these below your view; it doesn't obviously permit skipping them.
- **Comment (credit where due):** "And are we entirely screwed? I don't know; see: prediction=hard" is genuine epistemic humility and is the tone the rest of the essay's contested passages could borrow.

### Principle 3 — All life on Earth is relevant and human life need not be prioritized

- **Comment:** The essay is almost entirely anthropocentric, which is notable for a blog whose scope includes biodiversity. Every exponential chosen is human (human disease, human population, human AI, human CO2, human fertility); the non-human world appears only as comic props in the whack-a-mole bestiary ("a coyote, a mountain lion, a lion lion, and a hippo").
- **Q:** "That should reduce nearly all of the negative exponentials we have been driving for the past centuries." Which exponentials? The most on-brand answer for this blog is the non-human one — vertebrate population decline, extinction rate, habitat conversion, human appropriation of net primary production. Naming even one would make the closing paragraph carry Principle 3 explicitly instead of implicitly.
- **Comment:** Conversely, treating a below-replacement fertility rate as unambiguously *good news* is a real, if unremarked, Principle 3 move — the conventional (economic, human-first) framing calls the same curve a demographic crisis. Is that contrast worth one sentence? It would let the principle do visible work rather than sit under the surface.
- **Q:** Is there an argument that the *steepest* exponential humans have ever experienced, from the perspective of most life on Earth, is one this essay doesn't plot at all — e.g. the post-1950 Great Acceleration curves? That would be a natural Figure 6 and would answer the "human life need not be prioritized" principle head-on.

### Principle 4 — Leave religion (and political viewpoints) out of this, whenever possible

- **Q:** "which involves all the human sins, especially greed, gluttony and sloth" — those are three of the seven deadly sins and "sins" names the frame outright. Is this deliberate rhetorical borrowing of a now-secular idiom, or does it import a moral-theological framework the principle asks you to leave aside? If you want the punch without the frame, avarice / overconsumption / complacency does the same work.
- **Comment:** The essay does avoid naming parties, politicians, or countries — worth noting, because the topic makes that hard, and the piece stays clean of it.
- **Q:** That said, "a small set of powerful humans" and "the voices of deception" are political claims delivered by innuendo; every U.S. reader will fill in a name, and they will not all fill in the same one. Would naming the *documented* actors and citing the primary sources actually be more Principle-4-compliant than the unnamed version, since it converts a political vibe into a checkable fact?
- **Comment (minor):** "the ocean has kindly absorbed" gives the ocean intent. Harmless as a joke; just flagging it since the piece elsewhere is careful about agency.

### Principle 5 — Statistics must be respected. A low-probability event really does have a low probability of occurring

- **Q:** "What will be the consequences? No one knows. Prediction is hard; see: sports gambling, weather, pandemics." This abandons probability in a place where the science supplies calibrated ranges (AR6 likely ECS 2.5-4.0 °C; scenario-conditioned warming ranges). "No one knows" is also precisely the lukewarmer's preferred sentence. Do you mean "the distribution is wide," which is defensible, or "there is no distribution," which contradicts the principle? Also note the examples cut against you: weather forecasting and betting markets are among the *best-calibrated* probabilistic enterprises we have — they're evidence that prediction under uncertainty works, not that it fails.
- **Q:** "an El Nino is brewing to push us farther over the top." ENSO forecasts are explicitly probabilistic (CPC publishes percentages), and this sentence is date-stamped — the 2023-24 event is long over and conditions have since swung the other way. Either attach the probability and the date, or cut the clause; as it stands it will read as wrong to a 2026 reader.
- **Q:** "an exponential that is certain to help out" and "All arrows point to." Figure 5 plots the UN *medium* variant. The high variant does not cross 2.1 this century. Stating a single scenario as certainty is the exact failure mode this principle guards against — and it sits three sentences after "I don't know; see: prediction=hard," which is a visible internal inconsistency.
- **Comment:** The whack-a-hippo passage is a tail-risk argument, and a good one, but "Either the exponential will break or they will" states a dichotomy with certainty. Principle 5 permits — arguably requires — saying instead that the tail is fat and the downside is unbounded, which is both truer and rhetorically stronger.

### Principle 6 — But mathematics trumps all. An equal sign means equals

There are no equations in the draft, so this principle bites as *internal numerical consistency*, and there are three places where the arithmetic contradicts the prose.

- **Q (the flagship one):** "That's the second most powerful exponential we have ever experienced. Number 2 only to human population growth." By the essay's own organizing quantity — doubling time — this ranking is inverted by its own figures. Fitted: COVID **2.37 days**; CO2 **21.6 years** (1850-1970); the fastest population era, the post-war boom, **36.1 years** (`make_fig2_population_growth.py`). Population isn't #1; on doubling time it isn't even #2 in this essay. What does "powerful" mean here — total factor of increase, consequence, duration? Whatever the definition, it should be stated, because right now Figures 1, 2 and 4 rank the three differently than the sentence between them does.
- **Q:** Relatedly, is human population growth an exponential at all? Figure 2 fits *four different* doubling times (1600 yr → 141 yr → 81 yr → 36 yr), which is the definition of not-a-single-exponential; 1700-1960 is better described as hyperbolic (von Foerster), and growth rate peaked ~1968 and has fallen ever since. Calling it "the most powerful exponential" while the figure shows four regimes and a break is the kind of thing this principle exists to catch.
- **Q:** "All arrows point to the human fertility rate will soon drop below 2.1." In the data behind Figure 5 (UN WPP medium variant), the 2023 estimate is **2.251** and the first projected year below 2.1 is **2050**. "Soon" is 24 years out — and the figure will annotate the crossing year, so prose and figure will disagree the same way the COVID number does.
- **Q (the one that may matter most for the ending):** "when it does we will begin an exponential decline in population. That should reduce nearly all of the negative exponentials." Two arithmetic problems, both worked in `blogs/blog001/calc_fertility_decline_timescale.py` (new script, written to check this claim — see `conda run -n ocean14 python blogs/blog001/calc_fertility_decline_timescale.py`):
  - *Momentum:* population keeps rising after the crossing. UN medium variant peaks at **10.29 billion in 2084** — 34 years after TFR drops below replacement.
  - *Rate:* below replacement, population halves with time `T_gen · ln2 / ln(2.1/TFR)`. At the medium variant's end-of-century TFR of 1.84, that's a **~157-year halving time** — about 7× the 22-year CO2 doubling time you quote earlier in the same essay. Even at TFR 1.6 it's ~77 years. So the closing "positive" is an exponential roughly an order of magnitude weaker than the one it's offered as an antidote to, and it arrives a century late. Is that a concession you want to make explicitly (it's honest, and it fits the essay's thesis — we are bad at exponentials in *both* directions), or does the ending need rethinking?
- **Comment:** Also worth a line: emissions ≈ population × per-capita (Kaya). Fewer people only reduces the negative exponentials if per-capita impact doesn't grow faster — which, over the last two centuries, it has. "Should reduce nearly all" is doing a lot of unexamined multiplication.

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