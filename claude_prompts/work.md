# Work

## Goals

This prompt doc will make calculations on the "need" for work in the world, with emphasis on the United States.

## Context

See your context file `context/claudes_context.md` for the current context.

## Prompts

### Prep

1. We are going to give careful consideration to the number of people who need to work in the United States.  Or better the average number of hours per week under these assumptions:

    - Each healthy household will have 2 persons doing traditional and non-traditional work
    - Non-traditional work is caring for children, elderly, or disabled.  And cooking, cleaning, and other household tasks.
    - Traditional work is working in a factory, office, or other job that is not related to caring for children, elderly, or disabled.
    - Persons aged 20-60 will de both types of work.  They will not do any such work beyond age 60
    - A fraction of society will be unable to work due to disability, illness, or other reasons.

Initially, let us restrict the discussion to the United States.
Before we proceed, please search the web on this topic and add your findings to the Report section below.  Then ask me a series of questions in Q&A to proceed.  Log your work.

2. I have answered the questions in Q&A.  Please read them, and then ask another round.  Log your work.  Use Opus.

3. I have answered the 2nd round of questions in Q&A.  Please read them, and then ask another round if needed.  Log your work.  Use Opus.

### Calculations

1. Ok, I've answered the latest round of questions in Q&A.  Please read them. Then proceed to do your first round of calculations.  Log your work.  Use Opus.  If questions arise during your work, ask them in the Q&A/Calculations section below. 

2. Thanks for your first round of calculations.  Please read my answers to your 4 questions and then research the ones discussed.  Then update the calculations accordingly.  Log your work.  Use Opus.

3. Please be clear on the energy assumptions you are making for *all* of the work.  And, if possible, do one with signifiant fossil fuel use (i.e. today's level) and one with minimal fossil fuel use.  Use Fable if you can.  Log your work.  Then add a new prompt to the Report section below that I'll then execute separately.

### Report

1. We are about ready to generate a full report, as a separate markdown file named 
`CI_Reports/work_hours_needed_report.md`.  Before proceeding, please let me know if you have any questions.  If so, add them to the Q&A/Report section below.  Use Opus. Log your work.

2. I have answered the latest round of questions in Q&A.  Please read them. Then proceed to write the report.  Log your work.  Use Opus.  If questions arise during your work, ask them in the Q&A/Report section below.

3. Please update `CI_Reports/work_hours_needed_report.md` (and the companion figures, if a figure earns its place) to incorporate the energy assumptions and the FOSSIL_BASELINE vs. MINIMAL_FOSSIL comparison from Calculations round 3 — the per-category fossil-fuel-sensitivity reasoning, and the finding that the headline total barely moves even though several individual categories move by double digits. Log your work. Use Opus.

## Enhancements

1.  It will be important to summarize what these humans would have and what they wouldn't (relative to 21st century humans) in the report.  Please provide a table of each.  For example:
    - Would they have access to a hospital?  If so, what level of surgery?
    - How would they obtain tools?
    - How would they create energy?
Use Fable, log your work.    

## Q&A

### Report

### Claude's questions — Report round 1 (2026-08-17, drafted by Opus)

The model itself is settled (modulo FLAG 6), so these are scoping questions about the *document*, not the calculation. I've proposed a default for each so you can confirm quickly rather than specify from scratch.

1. **FLAG 6 first, or flag it in the report?** It is the one live technical thread, and it only bites the LOW column (a 60-69-year-old credited with 22 hr/wk of care labor while a working adult carries 9.2 hr). It does not move CENTRAL at all. Proposed default: I write the report now, present CENTRAL/HIGH as the real result, and label the LOW column **provisional** with FLAG 6 spelled out as a named open limitation alongside FLAG 3 (stipulated fertility) and the import-adjustment asymmetry. Alternatively, give me a one-line ruling now — my own recommendation would be to cap the elder contribution at the per-capita non-traditional demand of a working adult, which removes the inversion without re-deriving anything — and I fold the fix into the script and the report together.
>A. I like your Proposed default.

2. **Blog voice or methods report?** These are different documents. Proposed default: the same voice as `CI_2026_07_09_climate_report.md` — rigorous but accessible prose, tables where they earn their place, caveats stated in the open rather than buried — targeting **~3,000–4,000 words**, comparable to the report's homelessness (§8) and population (§9) sections. The alternative is a much longer technical/methods document that re-derives every category. Confirm the voice and the length target, or name a different one.
>A. Use the Proposed default.

3. **Is the 46.0 → 32.2 story the spine, or a coda?** There is a genuinely good narrative in *why* the number moved — childcare (ATUS secondary-care double-counting), clothing (durability, not wardrobe size), and household tasks (needs-based can go *up*, not just down) each teach a different methodological lesson, and together they are a case study in how a normative estimate should be built. Proposed default: lead with the final model as the result, then a dedicated near-the-end section on the revision and its three lessons — so the reader gets the answer first and the epistemics second. The alternative is to present only the settled model and drop round 1 to a footnote. Which?
>A. Use the Proposed default.

4. **Does the report draw the conclusion, or stop at the estimate?** 32.2 hr/week per working adult covers *everything* — all essential production plus all care and household work — against a current US reality of ~34 hr/wk of paid work *on top of* substantial unpaid labor. That comparison is the obvious punchline and it points somewhere normative (Keynes' 15-hour week, post-work, and Murphy-style sufficiency/degrowth). Proposed default: state the comparison explicitly and honestly, note what the model does and does not license (it says nothing about *distribution*, coordination, or transition), but stop short of policy advocacy. Related and worth your view: how explicitly should the piece tie itself to the blog's climate/energy throughline — i.e. why a labor-hours exercise belongs on Climate Intelligence at all? I'd make that the framing of the opening rather than an afterthought.
>A. Use the Proposed default.

5. **Figures?** Every other quantitative topic in this project got a companion plotting script (`make_homelessness_figures.py`, `make_population_figures.py`, `make_ai_figures.py`) and numbered figures in the main report (currently up through Figure 19). Proposed default: yes — a `CI_Reports/make_work_figures.py` producing three, continuing the existing sequence as **Figures 20–22**: (a) the traditional/non-traditional category breakdown as a stacked or horizontal bar, (b) the LOW/CENTRAL/HIGH range on the headline total, (c) a waterfall reconciling 46.0 → 32.2. Or defer all visuals to a separate prompt and ship a text-and-tables report now — say which, since it changes what I write into the markdown.
>A. Use the Proposed default.

6. **Standalone piece, or a future section of the main report?** The homelessness calculation became §8 of `CI_2026_07_09_climate_report.md`, and this one could plausibly follow the same path as a new numbered section after §10 (AI). That decision affects heading levels, whether the piece re-establishes shared context, and citation style — the main report uses numbered `[n]` references with a consolidated reference section, whereas the prompt doc uses inline markdown links. Proposed default: write it as a self-contained standalone document with its own inline-link sources (easier to fold in later), and treat the script docstring as the authoritative methods reference rather than re-deriving all of it in prose. Confirm, or tell me it's headed for the main report and I'll match that format from the start.
>A. Use the Proposed default.

### Calculations

### Claude's questions — Calculations round 1 (2026-08-16, drafted by Opus)

The script ran cleanly (`CI_Reports/work_hours_needed.py`, full results below). Building it surfaced four things that are genuine forks or noteworthy findings, not implementation details I should quietly decide myself.

1. **Is medical care traditional or non-traditional?** The settled rule is "classify by activity, not by who pays" — nursing/doctoring is a care activity, so I put it in non-traditional. But you carved K-12 OUT of care and INTO traditional despite it also being "about children," and medical care was never separately re-confirmed the same way. It's a real swing: reclassifying it to traditional moves the split from 9.1/36.9 to 11.5/34.5 hours (traditional/non-traditional) at CENTRAL — the TOTAL (46.0 hr/week) doesn't change either way, only the labels. Confirm non-traditional (current default), or move it.
>A. Move it to traditional.

2. **The two least-researched numbers dominate the answer.** Childcare (non-school) and general household tasks (cooking/cleaning/laundry) were NOT given a dedicated needs-based research pass this round — unlike every other category, they're raw ATUS behavioral benchmarks (what people currently do), not independent derivations of what's required, which was your stated preferred method. They turn out to be **70% of all non-traditional demand and 58% of the entire headline total** at CENTRAL. The headline "46 hours/week" is therefore mostly resting on the weakest-sourced part of the model. I'd recommend a dedicated research round for these two (parallel to what we did for eldercare this round) before treating the headline number as solid enough to write about. Agree?
>A. I agree.  Let's do a dedicated research round for these two.

3. **Elder-contribution scenario alignment.** Tier-1 elders (60-69) both receive light support AND contribute non-traditional labor (grandchild care, household help) — a genuine net offset. I paired the LOW-burden demand column with the HIGH elder-contribution offset (and vice versa) to get an honest low/high *outcome* bound, rather than naively matching same-named columns, which would understate the plausible low end. Default gives TOTAL range 25.6–46.0–69.5 hr/week; the naive parameter-aligned alternative gives 30.9–46.0–64.1. Confirm the outcome-scenario convention (default), or prefer the simpler parameter-aligned one?
>A. This sounds sensible.

4. **Clothing is, unexpectedly, nearly half of all traditional hours** (4.27 of 9.06 hr/week at CENTRAL) — because ~97% of US apparel is imported, so counting the true embodied offshore labor (rather than the tiny domestic BLS figure) makes clothing dominate shelter, food, and everything else combined. This is a real, sourced finding (two independent estimation routes converge), not a bug, but it's surprising enough that it's worth you eyeballing before it goes in a post — sanity-check the ~1.7 hr/capita/week figure against your own intuition?
>A. What does this assume about the size of the wardrobe?  And what does it assume about the quality and duration of the clothing? Let's scrutinize these further.

**Full script output, headline numbers, and modeling notes are in the Report section below** (see "Calculations round 1").

### Claude's questions — Calculations round 2 (2026-08-17, drafted by Opus)

Implemented all four of your answers (medical care → traditional; dedicated needs-based research for childcare and household tasks; kept the elder-contribution outcome-scenario convention; rebuilt clothing as a bottom-up sufficiency-wardrobe estimate). The script re-ran cleanly. One genuinely new issue turned up as a side effect — not manufactured, a real artifact of the other changes.

1. **The elder labor-contribution parameters need re-scaling now that demand shrank.** The needs-based childcare/household research cut total demand by about a third (46.0 → 32.2 hr/week at CENTRAL). The Tier-1 active-elder contribution (5/12/22 hr/week, set last round against the old, larger demand) didn't move with it, so its offset share swings wildly across columns: elders cover 43% of gross non-traditional demand at LOW, only 4% at HIGH. Worse, in the LOW column a single 60-69-year-old is credited with more weekly non-traditional labor (22 hr) than a working adult carries in total (9.2 hr) — an inversion that's at least odd. I flagged this as FLAG 6 in the script rather than quietly rescaling it myself, since it's a real modeling choice (cap the elder contribution relative to per-capita demand? re-derive it as a fraction of the childcare/household total instead of an independent absolute figure? leave it as-is and treat the LOW column as a labeled edge case?). How would you like to handle it?

**Updated headline (CENTRAL): 32.2 hr/week per working adult (8.3 traditional + 23.9 non-traditional), down from 46.0 last round** — full breakdown and the exact category-by-category reconciliation are in the Report section below (see "Calculations round 2").

### Prep

### Claude's questions — prompt 1 (2026-08-15)

Before building any calculation, the model in Prompts §1 has several free parameters
that the web research can't settle on its own — they're modeling choices. Please
answer what you can; "use your judgment" is a fine answer for any of these.

1. **What defines "need"?** Should hours-needed be (a) *descriptive* — how much
   paid + unpaid labor Americans actually perform today, taken from BLS/ATUS
   empirical averages, or (b) *normative* — an independently derived estimate of
   the labor a household objectively requires (e.g. time-motion needs for cooking/
   cleaning/care, or an "essential goods and services" cut of the economy à la the
   Murphy-textbook essential/discretionary distinction already in our context
   file)? This choice drives which data source anchors the whole calculation.
>A. Indeed, we should avoid money and stay normative.  And, yes, let's use the Murphy-textbook essential/discretionary distinction already in our context

2. **Traditional-work total.** For the paid-work side, do you want total hours
   actually worked in the US economy (employment × average weekly hours, all
   sectors) as the "need," or a narrower subset — e.g. excluding sectors you'd
   call discretionary/non-essential (finance, marketing, luxury retail, etc.)?
>A. I should have been more clear in the prompt.  We want to estimate the number of hours needed to shelter, feed, and care for each other.  We should also assume a minimum set of goods (clothing, basic furniture) and services (education) that are essential to life.  But ignore the frivilous luxuries.

3. **Non-traditional-work total.** For household/caregiving hours, should I use
   ATUS *actual* averages (what people currently report doing), or a needs-based
   estimate independent of current practice (e.g., what a household of a given
   size objectively requires for meals, cleaning, and care regardless of who
   currently supplies it or how well)?
>A. Let's aim for a needs-based estimate independent of current practice but use ATUS as a good benchmark.

4. **Household model.** The prompt specifies exactly 2 working-age (20–60) adults
   per "healthy household." Real US households vary a lot — average size is 2.5
   persons, ~29% are single-person, married-couple households are down to ~47% of
   all households, and many households have 0, 1, 3, or more adults aged 20–60.
   Should we (a) treat "2 adults per healthy household" as a stipulated idealized
   unit and compute the model on that abstraction, using national dependency
   ratios to size the dependents each such household supports, or (b) try to
   weight by the actual distribution of household compositions?
>A. This is a bit more complicated.  Assume:
   - 2 adults per household until death
   - 2 children per household until age 20
   - The adults work until age 60 and then are cared for by others

5. **Who counts as a dependent?** Children under 20, adults over 60, and disabled
   working-age adults are candidates. Under your rule that nobody works past 60,
   should the 60+ population itself be treated as needing *care* (eldercare
   hours), or simply as retired-but-self-sufficient unless disabled?
>A. Yes, under 20 and over 60.

6. **Which disability/incapacity measure?** Two very different BLS figures are on
   the table: (a) the disability employment-population ratio, implying ~75–77% of
   people *with a disability* are not working, or (b) the broader "work-limiting
   health condition" prevalence, ~12.4% of ages 16–75, of whom ~27% still
   participate in the labor force. These imply very different "fraction unable to
   work" inputs — which should anchor the model, or would you rather I derive a
   blended figure?
>A. Let's use (b)

7. **Students aged 20–24.** A large share of the participation gap at 20–24
   (participation ~72% vs. ~83% for 25–54) is school enrollment, not caregiving or
   disability. Should full-time students be counted as "working" for this model,
   excluded from the working pool entirely, or treated as a third category?
>A. Agreed, assume college for now

8. **Time horizon.** Present-day (2025/2026) snapshot using current empirical
   data, or do you also want the sensitivity of the answer to future demographic
   shifts (aging population, falling birth rates) explored later?
>A. Lets aim for present-day for now.

9. **Geographic aggregation.** Confirming US-only, national-aggregate for now
   (no state/regional breakdown) — correct?
>A. Yes, US-only.

### Claude's questions — prompt 2 (2026-08-16, drafted by Opus)

Your answers to round 1 fix the framing (normative, non-monetary, Murphy essential/discretionary) and the household stipulations. Before I can write a calculation script, nine structural choices remain. Where useful I've proposed a concrete default — confirm, reject, or modify.

**Household and generational structure**

1. **Does the household recycle?** Proposed default: a steady-state *unit cell* in which the 2 children, on turning 20, leave and each pair with an unrelated partner to found a new 2-adult household, which in turn has 2 children — so every household is at some point in the same repeating life-cycle. The alternative is a single multi-generational co-resident household (children never leave, grandparents live in). The first keeps the arithmetic clean; the second changes both eldercare logistics and housing-hours-per-person. Which?
>A. Yes, assume recycling of all households, including the house itself.

2. **Who provides eldercare, and for how long?** Proposed default: adults become dependent at 60 and are cared for until death at ~80 (US life expectancy ≈ 78-79; round to 20 dependent years), with care intensity ramped — light support ages 60-75, intensive care 75+ — and the care performed by their own working-age children as non-traditional work. Confirm the death age, the ramp (or a flat intensity), and whether the caregiver is the adult child or a congregate/institutional arrangement. If institutional, see question 4.
>A. Care by a congregate/institutional arrangement.  And that death age is fine.

3. **Real 2026 population, or idealized steady state?** "2 children per household" implies TFR = 2.0, versus the actual US TFR of ~1.6, and "work until 60" implies a retirement age below the real one. Proposed default: build the *synthetic* steady-state pyramid implied by your stipulations (2 kids, 20-year childhood, 40-year working life, 20-year dependent old age), and report the real US pyramid only as a benchmark comparison — the same way ATUS is a benchmark, not the target. Agree, or should the real age structure size the dependent population?
>A. Use the 2026 population.  But I'm not sure it matters provided it is steady state.  Assume that for now.

**Traditional / non-traditional boundary**

4. **Where does paid care work go?** The original framing defined traditional work as paid work *not* related to caring for children/elderly/disabled — which strands nurses, aides, daycare staff, and teachers. Proposed default: classify by *activity, not by payment* — all care hours are non-traditional wherever they occur, so a nursing-home aide's hours are non-traditional work counted once, and traditional work covers only production of goods and non-care services. This avoids double-counting but means "non-traditional" no longer maps to "unpaid." Accept that, or would you rather define non-traditional as strictly in-household and treat professional care as an essential traditional service sector?
>A. Yes, classify by activity, not by payment.

5. **Is schooling child-care, essential service, or both?** Proposed default: K-12 (and pre-K from age 3) counts as an essential *service* — teacher hours enter the model as care/instruction hours at a stipulated student-teacher ratio — and household child-care hours cover only the non-school hours (evenings, weekends, summers, ages 0-3). Confirm the school-age boundaries, the ratio, and whether the 20-24 college students from round 1 also require instructor hours or are simply absent from the labor pool.
>A. K-12 is an essential service.  College is not.

**Non-monetary quantification**

6. **How do we get hours-to-produce without prices?** Since money is off the table, the only routes I see are (a) *labor-embodied physical estimates* — construction-hours per dwelling amortized over a ~75-year lifespan, agricultural-plus-processing hours per person-year of calories, garment-hours per person-year of clothing — or (b) *sector employment counts* in the essential NAICS categories, converted to hours per capita, which uses BLS headcounts rather than dollars. Proposed default: (a) as the primary normative estimate, with (b) as a sanity check. Confirm — (a) is a substantially heavier data-gathering task than round 1's participation-rate work, so it's worth being deliberate.
>A. I confirm. (a) is the primary normative estimate and (b) is a sanity check.

7. **Is the essential list closed?** Round 1 named shelter, food, care, minimal clothing and furniture, and education. Proposed additions, each of which is arguably prerequisite to the named items: water and sanitation, electricity, basic medical care (distinct from eldercare — surgeries, antibiotics, obstetrics), and the transport/logistics needed to move food and materials. Which of these are in? In particular, is medical care an essential service (traditional, question 4) or care work (non-traditional)?
>A. I like your list of additional essentials.  Use them

**Aggregation and output**

8. **Unit cell or national totals?** Proposed default: compute per unit cell (2 working adults plus their dependent shares — 2 children, a fractional share of elderly parents, a fractional share of the disabled and student populations) and then express everything per working adult. The alternative is national totals divided by the working population. Also confirm the denominator: does it exclude all 12.4% with work-limiting conditions, or only the ~73% of them who don't work — and do that group's *care needs* enter the numerator, and at what intensity?
>A. Yes, unit cell is best.

9. **What is the headline number?** Proposed default: hours per week per working-age adult, reported as three figures — traditional, non-traditional, and total — with the non-traditional load split evenly between the two adults in a household (an explicitly normative choice worth flagging in the post, since ATUS shows it isn't). Confirm the units and the split, and say whether you want a central estimate with an uncertainty range on each essential category, or a single point estimate with the sensitivities discussed in prose.
>A. Confirme.  Hours per week per working-age adult reported as three figures.  I like central estimate with an uncertainty range on each essential category.

### Claude's questions — prompt 3 (2026-08-16, drafted by Opus)

**Verdict.** Two rounds have settled essentially all of the structural choices, and most of what remains is data-gathering I should just go do — nursing-home staffing ratios, student-teacher ratios, construction-hours per dwelling, agricultural hours per person-year. Three things, however, are genuine forks that I should not decide for you. Two of them are questions from round 2 that your answers only half-covered (the eldercare intensity ramp in Q2, and the second half of Q8 on the disabled), and the third is the one dial that has never been pinned down and that moves the headline number more than anything else: *how minimal is "minimal."* Everything else — how eldercare-institution staff hours are attributed (same logic as K-12 teachers), whether to count embodied hours in capital goods, how wide to draw the uncertainty bands, pre-K boundaries, dwelling lifespan — I'll decide and document inline in the script.

---

1. **How many of the 20 dependent years are institutional?** Round 2 fixed congregate/institutional eldercare and death at ~80, but didn't settle the intensity profile. Taken literally, "cared for by others from 60" means 20 years of staffed residential care per person, which would likely dominate the entire non-traditional total and is far from any real society's practice (~4% of Americans 65+ live in institutions; median nursing-home stay is 1-2 years). Proposed default: the 60+ cohort leaves the labor force at 60 but remains self-sufficient in housing and daily living until frailty, with congregate care concentrated in the last ~5 years of life (~75-80) at full staffing intensity, plus a light support tier (meals, transport, medical) for 60-75. Confirm, or set a different ramp — including "no, assume full institutional care for all 20 years" if that's the normative point you want to make.
>A. I like your ramp up and default.  

2. **Do disabled working-age adults generate care demand, or only remove labor?** Round 1's dependent list named only under-20 and over-60; round 2's Q8 asked this directly and the answer addressed the unit cell but not this part. The ~9% of working-age adults with a work-limiting condition who don't work are, under the current spec, fed and housed but receive zero care hours. Proposed default: they *do* enter the numerator, at a care intensity well below the frail elderly — say roughly a quarter of institutional intensity, mostly personal assistance rather than skilled care — since a work-limiting condition is not the same as needing daily attendance. Confirm or set the intensity. Related and quick: for the headline denominator, is "per working-age adult" the two able adults in the unit cell (i.e. the disabled and the 20-24 students are burdens, not divisors)? That's what the unit-cell framing implies and it's what I'll use unless you say otherwise.
>A. They generate care demand.  And it is actually ok to assume that they provide non-traditional work for the first 10 years of retirement.

3. **What standard of living defines "essential"?** This is the largest un-pinned lever. "Minimum goods, ignore frivolous luxuries" admits a factor-of-two range: an essential dwelling could be 1,000 or 2,000 sq ft; an essential diet could be current US consumption minus waste, or a nutritionally adequate lower-input diet; essential medicine could be the full modern hospital-and-pharma apparatus or a basic tier of surgery, obstetrics, antibiotics, and vaccines. Proposed default: a *sufficiency* standard rather than a scaled-down-current-consumption standard — modest but genuinely decent, roughly mid-20th-century US material provision delivered with present-day (2026) technology and productivity. Concretely: ~250 sq ft of dwelling per person, ~2,300 kcal/day with meat as a modest rather than central component, a small durable wardrobe, and a basic-tier medical system. Confirm the *principle*, and flag any of those anchors you'd move — I'll source and justify the rest.
>A. I confirm the principle.  No anchors to move for now.

---

**Next research steps (no input needed):**

- Direct labor-hours per new dwelling (residential construction hours per unit), plus dwelling service life, for the amortized shelter estimate.
- Agricultural + processing + distribution hours per person-year of food, US industrial system.
- Nursing-home and assisted-living direct-care hours per resident-day (CMS payroll-based journal data gives this cleanly).
- K-12 student-teacher ratio and total school-staff-to-student ratio (teachers alone understate it).
- Garment, furniture, water/sanitation, electricity, and freight-logistics hours per capita — likely via sector employment as the primary route for the ones where no physical labor-embodiment estimate exists.
- BLS sector employment in the essential NAICS categories, converted to hours per capita, as the round-2 method (b) sanity check.
- 2026 US population by single year of age, for the unit-cell dependency shares.

## Report

### Calculations round 1 (2026-08-16)

Script: [`CI_Reports/work_hours_needed.py`](../CI_Reports/work_hours_needed.py) — run with
`conda run -n ocean14 python CI_Reports/work_hours_needed.py`. Full method,
every settled assumption, all data sources, and five explicit modeling flags
are documented in the script's module docstring; the headline numbers below
are its actual printed output.

**Headline — hours per week per healthy working-age (25-59) adult:**

| | LOW | CENTRAL | HIGH |
|---|---|---|---|
| Traditional | 5.3 | **9.1** | 14.6 |
| Non-traditional | 20.3 | **36.9** | 54.9 |
| **Total** | **25.6** | **46.0** | **69.5** |

CENTRAL reads as 9.1 hours of traditional (goods/services) work plus 36.9
hours of non-traditional (care/household) work = 46.0 hours/week per working
adult — i.e. under this sufficiency standard, non-traditional work is roughly
4x the traditional load, not remotely a 50/50 split.

**How the population divides** (idealized steady-state 80-year life cycle,
applied to the real 2026 US population of ~343M): children 0-19 25.0%,
college students 20-24 6.25%, working adults 25-59 43.75% (of whom 9.05% are
non-working-disabled — removed from the labor pool, added to care demand),
Tier-1 active elders 60-69 12.5%, Tier-2 frail elders 70-74 6.25%, Tier-3
institutional-care elders 75-79 6.25%. The "working adult" denominator is
136.5M people (39.8% of the total population).

**Traditional category breakdown (hr/week per working adult, CENTRAL):**
shelter 0.34, food 1.58, clothing 4.27, furniture 0.25, water/sanitation 0.21,
electricity 0.16, essential freight 0.66, K-12 education 1.59.

**Non-traditional category breakdown (hr/week per working adult, CENTRAL):**
childcare (non-school) 17.85 [placeholder — see Q&A flag 2], household tasks
10.78 [placeholder], Tier-1 light support 1.10, Tier-2 support 2.20, Tier-3
institutional care 5.50, disabled-adult care 0.87, essential medical care
2.39, minus Tier-1 elder labor contributed −3.77 (elders supply ~9.3% of
gross non-traditional demand back).

**Research conducted this round:** four parallel deep-dive passes (shelter
construction/maintenance labor; food-system labor; institutional eldercare,
disability, and medical-care labor; K-12/clothing/furniture/utilities/freight
labor via BLS sector-employment method), each returning LOW/CENTRAL/HIGH with
primary sources (CMS Payroll-Based Journal, NCES, BLS CES/OEWS/ECEC, USDA ERS,
Census ASPEP, BTS/FHWA Freight Analysis Framework, AARP, JCHS, and others).
Full citations are in the script docstring rather than duplicated here.

**Known gaps flagged for a follow-up round:** childcare (non-school) and
general household tasks are ATUS actual-behavior benchmarks, not independent
needs-based derivations — see Q&A flag 2. They currently drive most of the
headline number, so a dedicated research pass on these two (matching the rigor
applied to eldercare this round) is the recommended next step before treating
46 hr/week as a stable estimate.

### Calculations round 2 (2026-08-17)

Script updated in place: [`CI_Reports/work_hours_needed.py`](../CI_Reports/work_hours_needed.py).
Implements all four round-1 answers: medical care reclassified to traditional;
childcare and household tasks rebuilt as needs-based derivations (replacing
the ATUS-benchmark placeholders); clothing rebuilt as a bottom-up sufficiency-
wardrobe estimate; the elder-contribution outcome-scenario convention kept as
confirmed. Full method, sources, and the FLAGS 1-6 history are in the script's
module docstring.

**Updated headline — hours per week per healthy working-age (25-59) adult:**

| | LOW | CENTRAL | HIGH | (was, round 1) |
|---|---|---|---|---|
| Traditional | 5.8 | **8.3** | 12.2 | (5.3 / 9.1 / 14.6) |
| Non-traditional | 9.2 | **23.9** | 37.8 | (20.3 / 36.9 / 54.9) |
| **Total** | **15.0** | **32.2** | **50.0** | (25.6 / 46.0 / 69.5) |

CENTRAL fell from 46.0 to **32.2 hours/week** (−30%). Exact reconciliation,
CENTRAL, hr/week per working adult:

- Childcare: 17.85 → 5.29 = **−12.56** (the dominant move — the round-1
  placeholder used ATUS "secondary childcare," which counts a child merely
  being present during leisure/housework; the needs-based figure, built from
  AAP/APHA child-care staffing ratios applied to waking hours minus school
  time, removes that double-counting. Independently corroborated by ATUS
  *primary* childcare, which lands within 1% of the same number.)
- Clothing: 4.27 → 1.13 = **−3.14** (durability, not wardrobe size, drives
  this — see below)
- Household tasks: 10.78 → 12.74 = **+1.96** (the opposite direction: a real
  scratch-cooked, restaurant-free sufficiency diet costs *more* labor than
  people's current, restaurant- and processed-food-supplemented behavior —
  built from USDA Thrifty Food Plan meal-prep-time studies and ISSA
  industry cleaning-time standards)
- Medical care: net zero on the total — moved from non-traditional to
  traditional (2.39 hr/week at CENTRAL), only the bucket changed

**Clothing finding worth keeping for the post:** the round-1 figure (1.70
hr/wk) implicitly assumed a ~1.8-year garment replacement cycle — it was
measuring current US fast-fashion *throughput*, not what a durable wardrobe
requires. Rebuilding bottom-up from an explicit "sufficiency wardrobe" (103
items — the Hot or Cool Institute's 2022 "1.5-degree wardrobe" standard, 85
four-season garments including footwear plus underwear/socks — at a
stock-weighted average 4.1-year durable service life) gives 0.45 hr/wk, a
3.8x reduction. Counterintuitively, wardrobe *size* barely matters for
wear-limited garments (it largely cancels out of the stock÷lifespan ratio);
it is specifically *durability* that buys the reduction, not "small."

**New issue surfaced, not yet resolved (FLAG 6):** the Tier-1 active-elder
labor-contribution parameters (5/12/22 hr/week) were calibrated last round
against non-traditional demand that has since shrunk by about a third. Their
offset share now swings from 43% of gross demand at LOW to just 4% at HIGH,
and in the LOW column a single elder is credited with more weekly labor (22
hr) than a working adult's entire non-traditional burden (9.2 hr) — see the
new Q&A question above.

*(FLAG 6 was resolved in the Report round, via an exact closed-form cap —
`gross demand / (working adults + Tier-1 population)` — that ensures a Tier-1
elder's credited contribution can never exceed a working adult's own final net
burden. Only the LOW column moved as a result: 15.0 → 18.1 hr/week total,
12.2 hr/week non-traditional. CENTRAL and HIGH were unaffected. Full
derivation is FLAG 6 in the script.)*

### Calculations round 3 — energy assumptions (2026-08-24)

Every rate in the model up to this point is, implicitly, a **FOSSIL_BASELINE**
rate: it comes from labor data describing the actual 2025-2026 US economy,
which runs on today's energy mix. Stated precisely (EIA, 2025): fossil fuels
are **~82% of total US primary energy** (petroleum ~38%, natural gas ~35%,
coal ~9%; nuclear ~9%, renewables ~9%), and **~58% of electricity generation**
specifically (renewables ~24-26%, nuclear ~18%). That mix is baked into every
BLS/USDA/NCES/CMS figure the model uses, because those figures describe how
goods and services are *actually* produced right now.

This round adds a second scenario, **MINIMAL_FOSSIL**: the same sufficiency
standard, produced with predominantly non-fossil primary energy and, where
relevant, without fossil-derived inputs (synthetic nitrogen fertilizer;
petroleum-based synthetic fiber) — deliberately *not* a de-mechanization or
collapse scenario, just a change in energy carrier and a few fossil-specific
inputs. Per-category reasoning (full detail and citations in the script's new
ENERGY ASSUMPTIONS docstring section):

| Category | Multiplier | Why |
|---|---|---|
| Electricity | ×1.25 | Most uncertain line in the table. Mature wind/solar need far fewer O&M workers per TWh than fossil (20-30 vs ~100-260 jobs/TWh), but construction-phase labor is much higher (250-500 jobs/TWh) and a high-renewables grid needs extra storage/balancing labor. The literature does not converge; range is genuinely ~0.90-1.60. |
| Food | ×1.15 | Proxied by organic-vs-conventional labor studies (organic also forgoes synthetic fertilizer): crop-specific studies find 7-34% more field labor; a CA/WA employment survey finds 2-12% more workers per acre. Applied to the whole food category since farming is ~1/3 of food-chain labor. |
| Clothing | ×1.12 | Shift from petroleum-derived synthetic fiber toward natural fiber (cotton, wool), which is more land/labor-intensive to grow. |
| Shelter | ×1.08 | Cement/steel process emissions are fuel-independent; on-site labor-hours-per-sqft is a function of trade practice, not fuel choice. Modest bump for materials-sourcing friction only. |
| Freight | ×1.08 | Electrified trucking/rail needs the same drivers; modest logistics-coordination overhead. |
| Furniture | ×1.05 | Same materials-sourcing logic as shelter, smaller category. |
| Water/sanitation | ×1.00 | Labor is operation/maintenance-bound, not fuel-choice-bound. |
| K-12, essential medical care | ×1.00 | Human-attention-bound professional services — decarbonizing the power behind a classroom or clinic doesn't change how many hours of teaching or clinical care are needed. |
| **All non-traditional categories** | ×1.00 | Same reasoning: childcare, eldercare, disabled-adult care, and household tasks are bound by the number of people needing attention and by physical tasks, not by how the building is powered. |

**Result (CENTRAL, hr/week per working adult):**

| | FOSSIL_BASELINE | MINIMAL_FOSSIL | Change |
|---|---|---|---|
| Traditional | 8.3 | 8.8 | +6.1% |
| Non-traditional | 23.9 | 23.9 | 0% |
| **Total** | **32.2** | **32.7** | **+1.6%** |

**The headline finding:** the total is remarkably *insensitive* to the
fossil-fuel transition, even though individual categories move by double
digits (clothing +12%, electricity +25%, food +15%). This is because the two
largest traditional lines (essential medical care, K-12 education) and the
entire non-traditional side — three-quarters of the whole model — are
human-attention-bound rather than energy-throughput-bound. Put differently:
the "essential vs. discretionary" energy story this model set out to explore
turns out, on this accounting, to really be a "goods/materials vs.
care/services" story. Full LOW/CENTRAL/HIGH tables for both scenarios, and the
per-category before/after breakdown, are in the script's `main()` output.

These multipliers are **reasoned sensitivities**, not researched rates like
the rest of the model — each is a central estimate over a real range, built
from the best available proxy literature (no direct minimal-fossil-fuel labor
study exists at this resolution). Treat MINIMAL_FOSSIL as an order-of-
magnitude sensitivity check on the model's energy dependence, not a rate with
the same evidentiary standing as FOSSIL_BASELINE.

**Sources for this round:**
- [U.S. energy facts explained — EIA](https://www.eia.gov/energyexplained/us-energy-facts/) (total primary energy mix, 2025)
- [Electricity generation, capacity, and sales in the US — EIA](https://www.eia.gov/energyexplained/electricity/electricity-in-the-us-generation-capacity-and-sales.php) (electricity generation mix, 2025)
- [Does organic farming present greater opportunities for employment...? — PDX Scholar, 2018](https://pdxscholar.library.pdx.edu/pubadmin_fac/24/) (CA/WA organic-vs-conventional employment survey)
- [Module V: The Economics of Organic Agriculture — UW-Madison CIAS](https://cias.wisc.edu/curriculum-new/module-v/module-v-section-d/) (crop-specific labor-hour comparisons)
- [Putting Renewables to Work: How Many Jobs Can the Clean Energy Industry Generate? — Berkeley](https://www.localcleanenergy.org/files/040413_renewables_berkeley%20(good%20jobs%20per%20mw%20table%20pg3).pdf) (construction vs. operational jobs per TWh)

---

*Web research conducted 2026-08-15 in support of Prompts §1 (hours of work needed
per person under the household model). All figures are current US data (BLS,
Census) unless noted; treat as time-stamped empirical inputs, not the final model.*

### Working-age population & labor force participation (BLS)

- **Prime-age (25–54) participation:** ~83.3% are in the labor force — the
  benchmark "fully engaged" cohort.
- **Young adults (20–24):** ~72% participation (Mar 2025) — the gap versus prime-age
  is largely school enrollment, not non-participation for other reasons.
- **Older workers (55+):** ~37–38% participation overall; narrowing to 65+:
  ~19.1% still in the labor force in 2025 (men 23.1%, women 15.7%) — i.e. a
  substantial minority keep working well past the prompt's age-60 cutoff, which is
  useful context even though the model stipulates nobody works past 60.
- No official BLS table breaks participation into 5-year bins for 55–59/60–64
  specifically; only "55 and older" and "65 and older" bins were found. A more
  granular breakdown, if wanted, would require pulling BLS's underlying CPS
  microdata rather than the published summary tables.

### Actual hours worked (BLS Current Employment Statistics)

- Average weekly hours for **all** employees on private nonfarm payrolls: **34.2
  hours** (Aug 2025) — this blends full- and part-time workers across every
  industry.
- Full-time-only average runs higher (historically ~40–42 hrs/week for full-time
  workers specifically), but a precise, current full-time-only national figure
  wasn't isolated in this pass — flagged for a follow-up, more targeted BLS table
  pull if the model needs it.

### Unpaid household work & caregiving (BLS American Time Use Survey, ATUS)

- **Household activities** (housework, cooking, lawn care, household management):
  81% of people engage in some household activity on an average day; among women,
  87% do so (averaging 2.8 hrs on days they do it); among men, 75% do so
  (averaging 2.1 hrs).
- **Childcare:** adults in households with a child under 13 spend an average of
  **5.1 hours/day** providing secondary childcare (i.e., childcare done while also
  doing something else — not 5.1 hours of undivided attention).
- **Eldercare:** 14% of the civilian population 15+ (38.2 million people) provide
  unpaid eldercare; of those, 28% do so on a given day, averaging **3.9 hours** on
  the days they provide it.
- These are *averages across providers*, not per-household totals — translating
  them into "hours needed per household" will require an explicit modeling step
  (see Q&A #3).

### Household composition (US Census Bureau)

- Average household size: **2.5 persons** (2024 ACS), continuing a long historical
  decline.
- Married-couple households: down to **~47%** of all households (2022/2024), from
  71% in 1970; ~74% of *family* households (64% of all households) are
  married-couple.
- No figure was found in this pass for "2-adult, working-age households" as a
  distinct share — the Census tables split by household *type* (family/nonfamily,
  married-couple, etc.) and by *size*, not directly by "exactly 2 adults aged
  20–60."

### Disability / incapacity to work (BLS)

- **Employment-population ratio for people with a disability:** 22.7% (2024),
  22.8% (2025) — i.e., only ~23% of the disability-identified population is
  employed; ~75% are not in the labor force at all (vs. ~32% of people with no
  disability).
- **Broader "work-limiting health condition" measure:** 30.7 million people aged
  16–75 (12.4% of that age range, July 2024) report a health condition or
  difficulty that limits work; of these, 27.1% still participate in the labor
  force.
- These two disability-related figures answer different questions (identifies-as-
  disabled vs. has-a-work-limiting-condition) and give quite different "fraction
  unable to work" inputs — see Q&A #6.

### Gaps / follow-up flagged for later

- No single BLS table gives 5-year age-bin (55–59, 60–64) labor force
  participation; would need CPS microdata for that granularity.
- A precise, current, full-time-only average weekly hours figure (as opposed to
  the all-employees blended 34.2 hrs) wasn't isolated and should be pulled
  directly from BLS Table B if the model needs it.
- No Census breakdown found for households by exact adult count in the 20–60
  range specifically (only by total size and family/nonfamily type).

**Sources:**
- [American Time Use Survey — 2025 A01 Results (BLS)](https://www.bls.gov/news.release/atus.nr0.htm)
- [American Time Use Survey — 2025 Results (PDF)](https://www.bls.gov/news.release/pdf/atus.pdf)
- [Unpaid Eldercare in the United States — BLS](https://www.bls.gov/news.release/archives/elcare_09212023.htm)
- [Nearly one in five older Americans in the labor force in 2025 — BLS](https://www.bls.gov/opub/ted/2026/nearly-one-in-five-older-americans-in-the-labor-force-in-2025.htm)
- [Labor Force Participation Rate (CIVPART) — FRED](https://fred.stlouisfed.org/series/CIVPART)
- [Labor Force Participation Rate — 25-54 Yrs (LNS11300060) — FRED](https://fred.stlouisfed.org/series/LNS11300060)
- [Labor Force Participation Rate — 20-24 Yrs (LNU01300036) — FRED](https://fred.stlouisfed.org/series/LNU01300036)
- [Civilian labor force participation rate by age, sex, race, ethnicity — BLS](https://www.bls.gov/emp/tables/civilian-labor-force-participation-rate.htm)
- [Average weekly hours, US — Trading Economics](https://tradingeconomics.com/united-states/average-weekly-hours)
- [People with a Disability: Labor Force Characteristics — 2025 (BLS PDF)](https://www.bls.gov/news.release/pdf/disabl.pdf)
- [People with Health Conditions or Difficulties that Limit Work — BLS](https://www.bls.gov/news.release/archives/dissup_09302025.htm)
- [Average Household Size by State 2026 — World Population Review](https://worldpopulationreview.com/state-rankings/average-household-size-by-state)
- [Married Couple Households Still the Majority… — US Census Bureau](https://www.census.gov/library/stories/2024/03/coupled-households.html)
- [Nearly Two-Thirds of U.S. Households are Family Households — US Census Bureau](https://content.govdelivery.com/accounts/USCENSUS/bulletins/3c16e18)
