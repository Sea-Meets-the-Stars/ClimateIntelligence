# Initial Report

## Goals

This prompt doc will help Claude generate an initial report on climate change.

## Context

Be sure to review the `context.md` document to understand the context of the project.  As necessary, refer to any/all of the other documents in the `context/` directory.

## Prompts

1. Given all of the context you have gathered, please prepare to generate your own well-crafted and comprehensive report on climate change.  It should include at a minimum:
    - Historical context
    - Current state of the Earth
       - Temperature
       - Sea Level
       - Ocean Acidification
       - Ocean Warming
       - CO2 and other atmospheric gases
    - When presenting data, be sure to include the uncertainty and bias of the data.
    - Future projections by the community
    - Figures
       - From the literature
       - Of your own creation; use matplotlib and save the Python scripts in the `CI_Reports/` directory.
    - A list of references

Be sure to maintain balance. Be sure to adhere to the guiding principles in the `principles.md` document.

Before beginning, please review the `principles.md` document and the `context.md` document to ensure you understand the guiding principles and the context of the project.  Then begin a Discussion in the section below with me about the report you will generate.  Log your work.

2. I have answered your questions below and also edited the 1st prompt.  Please review these and see if you have any further questions.  If you do, please ask.  If you don't, please proceed with the report.

3. Can you replace the current figure in the Report on Temperature increase as a function of CO2 increase with the one from this website: `https://www.environmentalgraphiti.org/all-series/emissions-levels-determine-temperature-rise`.  Log your work.

4. Here are Richard's first set of comments:

---
The RCP's say nothing of the fact that "emissions" can result not only from positive direct emissions by human activities, but by the increasing failure of natural systems to absorb CO2 at the rate they have been doing in the past. This is where tipping points are important to put on the table. The "Carbon Fertilization" effect, for example, is working at only half the level it did in 1980. That causes excess CO2 to be in the system w/o any actual increase in human direct emissions. 

Also I notice that the methane curve in your report seems at the most recent end, looks to be sloping less, whereas the data I'm seeing show it increasing faster, not slower.
These are all in the sources I've already linked in my presentations. Rather than try to individually dig them all out and re-invent that wheel. Have Claude just add them to it's diet and then we can talk.

Again, I disagree that the IPCC is the final word on the best science. The IPCC decides what they want modelled and decides what models they will include in their publications, and these have consistently been under-estimates of the later reality. The projections they prefer are always far rosier than the reality. 

Atmospheric CO2 trends are far closer to what determines our future than is "emissions" trends or reportings (dishonest too often, especially from China, 3rd world). The atmosphere doesn't lie. People do.  
---

Please consider all of the above critically and make any necessary changes to the report.  
Report on what you did below and what you did not do.  Log your work.

## Reports

### Richard's comments

#### Claude's response to Richard's first comments (2026-07-15)

Thank you — three of these four points were right and made the report better, and
I've changed it accordingly. Point by point, with what I did and did *not* do.

**(1) Natural-sink failure is "emissions" too; tipping points; CO₂ fertilization
at half its 1980 level. — Largely adopted; it was the strongest point.** You are
right that emission-driven scenarios (RCP/SSP) can understate atmospheric CO₂ if
the natural sinks weaken, and the data now back you loudly: in **2023 the Mauna
Loa CO₂ growth rate hit a record 3.37 ppm/yr — ~86% above 2022 — while global
fossil emissions rose only ~0.6%**, because the land sink was the weakest since
2003 (tropical El Niño heat/drought) [Ke et al. 2024; Global Carbon Budget]. I
added this to **§3.5** and, in **§5**, a structural caveat that scenarios convert
*emissions* to concentrations through carbon-cycle models whose sink assumptions
are not constants, so permafrost/wetland feedbacks and tipping elements (within
the Paris range per Armstrong McKay et al. 2022) sit on top of the near-linear
TCRE as an asymmetric upside risk. On the **CO₂-fertilization** decline
specifically: it is a real, published hypothesis (Wang et al. 2020) — but there is
a published rebuttal arguing the satellite trend is largely a calibration artifact
(Zhu et al. 2021). Per Principle 2 I present it as *important but unsettled*
rather than as the established "half of 1980" figure; if your presentation
sources pin the magnitude down more firmly, send them and I'll revisit.

**(2) The methane curve should be steepening, not flattening. — Adopted, with a
quantitative nuance.** Good catch on the figure. I computed the growth rate
directly from NOAA's deseasonalized series (`CI_Reports/methane_growth_rate.py`):
the **2020s are the fastest-growing decade in the record (~11 ppb/yr) vs the ~2
ppb/yr 2000s plateau, with a record 2021–22 surge of ~16–17 ppb/yr**. The one
honest wrinkle: growth has *eased* to ~6–8 ppb/yr in 2024–25, so the very tail is
slightly less steep than 2021–22 — but it sits atop the steepest decade ever
measured, and my old Figure 5 was hiding this because it plotted the raw monthly
mean, whose 2025 seasonal downturn masked the trend. I redrew Figure 5 to show
NOAA's **deseasonalized trend** (bold) with the decade growth rates annotated, and
added a methane paragraph to §3.5 noting the wetland-feedback attribution (a
carbon-cycle feedback, tying back to your point 1).

**(3) The IPCC is not the final word; it tends to under-predict. — Adopted.** I
added a caveat to **§1** ("used, not worshipped"): the IPCC is a consensus
*assessment* with a multi-year lag, and — the part that actually supports you — it
has historically *under*-predicted Arctic sea-ice loss, ice-sheet mass loss, and
sea-level rise. I did **not** adopt the stronger claim that its projections are
"always far rosier than reality," because that isn't symmetric: it has been close,
and occasionally high, on global-mean surface temperature. So the report now
treats IPCC-central as a conservative midpoint, gives both the low- *and*
high-sensitivity tails their due, and privileges direct measurements over any
assessment synthesis where the two can be compared.

**(4) Atmospheric CO₂ trends beat emissions trends; reporting is unreliable
(China, 3rd world). — The science adopted; the politics left out (Principle 4).**
I fully agree on the science and made it explicit in §3.5: the **measured
atmospheric concentration already integrates every source and sink**, so the
directly-observed Keeling curve is a firmer foundation than bottom-up national
inventories, whose uncertainties and gaps are real — and, per point 1, watching
the atmosphere's growth rate is exactly how the 2023 sink collapse was caught. I
did **not** include the attribution of dishonesty to specific countries: the blog
keeps politics out (Principle 4), and the scientific point ("the atmosphere is
ground truth; inventories are the estimate") stands on its own without it.

**On "add my sources to your diet."** The specific links from your presentations
weren't attached to this round, so I grounded the changes in the strongest primary
literature I could verify independently (added as report refs [46]–[50] and
`references.md` §12). Send the presentation source list and I'll fold it in
directly before we talk.

### Claude's plan & questions — initial report (2026-07-09)

I've re-read `principles.md`, `purview.md`, and my own `claudes_context.md` +
`references.md`. Before writing, here is the proposed shape and the decisions I
need from you.

**Proposed structure**
1. *Purpose & method* — what this report is, sources used, how uncertainty is
   handled, and an explicit statement of the guiding principles it follows.
2. *Historical context* — deep-time CO2/temperature (paleo), the Industrial
   Revolution inflection, the instrumental era, the arc of the science (Arrhenius
   → Keeling → Charney → IPCC).
3. *Current state of the Earth* — one subsection each, every data point with its
   uncertainty range AND known biases/structural caveats:
   - Temperature (the "big four" + reanalysis; why they differ)
   - Sea level (global mean; local = climate + vertical land motion)
   - Ocean acidification (pH trend; the "rate vs absolute" point)
   - Ocean warming (OHC, >90% of excess heat; the best-constrained metric)
   - CO2 & other gases (CO2/CH4/N2O; Keeling curve; airborne fraction)
4. *Attribution* — what is settled (near-linear CO2↔warming) vs genuinely open
   (cloud feedbacks, ECS tails, regional detection), presented with the mainstream
   view AND the strongest heterodox challenges from §9/§9.1 (Lindzen iris,
   Christy troposphere, Lewis/Curry low-ECS) and the published responses.
5. *Future projections* — SSP scenarios with ranges; the RCP8.5-as-baseline caveat
   (a point both mainstream and critics now make); carbon-budget arithmetic.
6. *Figures* — from the literature (cited) + my own (Python→`context/scripts/`).
7. *References / sources / citations.*

**Questions**
1. **Audience & length.** Who is this for — general public, or technically
   literate readers? Target length (e.g., ~3–5k words vs a long definitive
   piece)? This drives tone and math density.
>A. This report is for the writers of the blog "Climate Intelligence".  It should be 3-5k words. Use math and equations when you can.
2. **Global vs U.S. framing.** The IPCC corpus is global; the DOE/CWG material is
   U.S.-centric. Default: lead global, use the U.S. as a worked example and to
   illustrate how scope choice changes conclusions. OK?
>A. Ok
3. **"matlab" vs Python.** Prompt says "use matlab and save the Python scripts in
   `context/scripts/`." These conflict. I'll assume you mean **matplotlib** (fits
   the CLAUDE.md/coding rules and the existing Bokeh work) and save `.py` scripts
   to `context/scripts/`. Confirm, or do you actually want MATLAB `.m` files?
>A. Right, matplotlib. I have modified the prompt 
4. **Figure data sources.** My-own figures need real data. May I fetch public
   series at build time (NASA GISTEMP, NOAA CO2/Keeling, NSIDC, Global Carbon
   Budget) and cache them under `context/scripts/data/`? Or should figures be
   schematic/illustrative from values already in `claudes_context.md`?
>A. Yes, you have permission.  Don't ask again as you work.
5. **References vs sources vs citations.** The prompt lists these separately (and
   "sources" twice). I read them as: *citations* = works cited inline; *references*
   = full bibliography; *sources* = data/portals (from `references.md`). Good, or
   do you want a different split?
>A. Those were redundant. I have removed them.
6. **Output format & location.** Markdown at `context/` or a new `reports/` dir?
   Filename? (e.g., `reports/initial_climate_report.md`.) Any house style —
   headings, figure captions, citation style (author-year vs numbered)?
>A. Use markdown and place in `CI_Reports/` and name it `CI_2026_07_09_climate_report.md`.  Put all figures and any code you need to generate in that folder
7. **Heterodox balance.** Per principles 1–2 ("welcome all viewpoints, but do not
   accept them equally"), I plan to present credible challenges fairly and then
   weigh them against the evidence — not give false balance. Is that the calibration
   you want?
>A. Yes, that is the calibration I want.
8. **Scope discipline.** `purview.md` excludes politics; the DOE episode is
   partly political. I'll cover the *science* of that exchange and note the policy
   context factually without taking political sides. OK?
>A. Yes, that is the calibration I want.
