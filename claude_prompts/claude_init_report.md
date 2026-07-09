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
