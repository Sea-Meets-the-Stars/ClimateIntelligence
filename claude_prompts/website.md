# Climate Intelligence Websites

## Goals

This prompt doc will be used for the Climate Intelligence websites.  This includes both the GitHub facing site -- `https://github.com/Sea-Meets-the-Stars/ClimateIntelligence` and others to come.


## Prompts

1. Read this file.  Execute the 1st task under "GitHub Website"

## GitHub Website

### Tasks

1. Let's improve the GitHub website via our README.md file. Please:

    - Add a nice description of the project.  
    - Add the developer names: J. Xavier Prochaska (and allow for more to be added later) 

In addition, create a new graphic which summarizes the project.  Use your imagination, and feel free to ask questions first in the Q&A section.  I will also use this grahpic in talks and presentations.  If you can, use `matplotlib` to create the graphic and save the Python script as `CI_graphic.py` in the `docs/scripts` directory.  Log your work
    
2. I have answered the Q&A section below.  Read them and see if you have any additional questions.  If so, ask them.  Log your work.

3. I have answered the Q&A section below.  Read them and see if you have any additional questions.  If so, ask them.  Log your work.

4. Ok, please create the graphic.  Log your work.

5. That's a fine start.  Here are comments and criticism:

    - That AI graphic is trite.  Do better
    - The climate graphic is not intuitive
    - The text is too small
    - The boxes for the 4 subject areas are boring
    - I don't like the tag "The science of a changing planet".  Please suggest another 10 tag lines for this project in the Q&A and I'll try to choose one.

Make a new version of the graphic.  Log your work.

6. Ok, thanks.  Let's keep going.  First, use this as the tag line for now: "Where climate science meets artificial intelligence."  But also riff on that and generate another 10 tag lines for this project in the Q&A and I'll try to choose one.  Let me set you straight on something that should be added to your memory:

Artificial Intelligence is its own aspect of this.  Indeed, let's make it a 5th topic area.  Yes, we will use it to create the blog, examine the data, etc. but it is not simply a tool to be used but a major topic area in its own right.

With that understanding, work on the tag lines and a new graphic.  Log your work.

7.  More edits:
    - The red text on the left is too big and distracting
    - The figure suggests the role of AI in this project is to make climate predictions.  That is not true and therefore very misleading.  Please keep at it..
    - Log your work

## Q&A

### GitHub Website

Questions from Claude about the summary graphic (`docs/scripts/CI_graphic.py`).
Please answer inline below each question.

**A. Content and scope**

1. What should the graphic actually depict? Two rather different options come to
   mind — please pick one (or describe a third):
   - (a) A project-overview infographic: the Climate Intelligence mission, its
     topic areas (climate physics, biodiversity, population, homelessness), the
     human+AI collaboration, and the primary-source library.
   - (b) A specific scientific figure — later tasks in this file reference
     panels like "(1) Observe" with Rrs spectra, IOP retrieval algorithms, and
     the question "Which IOP algorithm performs the best?", which suggests an
     ocean-color / IOP-retrieval workflow figure rather than a blog overview.

   Answer: (a)

2. If it is a science figure (option b): what is the storyline, in one or two
   sentences? Which datasets/algorithms should appear, and what is the key
   takeaway a viewer should leave with?

   Answer: N/A

3. If it is an overview infographic (option a): should it include any key
   quantitative "climate numbers" (e.g. warming to date, CO2 concentration), or
   stay qualitative?

   Answer: Sure, spice it up

**B. Format and layout**

4. What is the primary use and therefore the aspect ratio / orientation?
   - 16:9 landscape (talk slide)?
   - Square (social / thumbnail)?
   - Wide banner (README header)?
   - If it will serve several of these, which one should drive the design?

   Answer: Make it mainly for the README header.  But I may use it in Google slides and presentations.

5. Roughly how many panels/sections, or should I decide?

   Answer:  Try to keep it simple.  

**C. Style and branding**

6. Color palette preferences? (e.g. ocean blues/greens, an existing palette you
   like, colorblind-safe requirements?)

   Answer:  Something clean and professional.

7. Light or dark background — and if it will be used in talks, do your slides
   have a light or dark theme?

   Answer: Light theme.

8. Any text, tagline, or title to include on the graphic itself (e.g.
   "Climate Intelligence")? Is there a logo or wordmark to incorporate, or
   should the graphic work as the de facto logo?

   Answer: Climate Intelligence

**D. Emphasis and exclusions**

9. How prominently (if at all) should the human+AI collaboration angle be
   featured?

   Answer: Make that connection subtle.  It should emphasize: (1) Climate crisis and (2) Artificial Intelligence.

10. Should the guiding principles (fact over opinion, all life matters, respect
    statistics, etc.) appear on the graphic, or stay on the website only?

    Answer: No.

11. Should the source library (IPCC AR6, Tom Murphy, James Hansen, ...) be
    represented visually?

    Answer: No.

12. Anything to explicitly avoid — clichéd imagery (burning globes, lone polar
    bears), political framing, specific colors, dense text?

    Answer: Not sure.

**Follow-up questions (round 2)**

Thanks for the answers. A few clarifications before I build the graphic.

13. Core message: is the one-line story essentially "harnessing Artificial
    Intelligence to understand the climate crisis"? If not, state the intended
    message in your own words.

    Answer:  Read the files in this Repo to get a sense of the project.  Ask again if you need further guidance.

14. How should "Artificial Intelligence" be depicted? Options: (a) an abstract
    network/node motif, (b) subtle circuitry lines, (c) the word/label only, or
    (d) something else. I plan to avoid a cliché robot unless you'd like one.

    Answer:  Be creative and graphical

15. Given "keep it simple" but "emphasize climate crisis + AI": should the four
    topic areas (climate physics, biodiversity, population, homelessness) still
    appear (e.g., as small tags or icons), or be dropped in favor of the
    two-theme emphasis?

    Answer:  Yes, try to weave in all 4.

16. Climate numbers: OK for me to pick 2-3 canonical, well-sourced figures
    (e.g., ~+1.1 C warming since pre-industrial, ~420+ ppm atmospheric CO2,
    sea-level rise)? Or are there specific numbers you want featured?

    Answer: Sure

17. Since Q12 was "not sure", my proposed defaults to avoid: burning globes,
    lone polar bears, overtly political imagery, and dense text. Confirm or
    adjust.

    Answer:

**Follow-up (round 3) — proposed concept for sign-off**

Having read the repo (context/claudes_context.md, principles.md, origins.md,
README.md), here is the concept I'd build. Please confirm or adjust the single
question at the end.

*Core message (inferred).* Climate Intelligence applies rigorous,
primary-source-grounded analysis to the defining challenge of our time — the
climate crisis — using the tools of modern Artificial Intelligence. Humans and
AI work side by side, but that partnership stays in the background; the two
things front and center are the **climate crisis** and **Artificial
Intelligence**.

*Proposed concept.*
- A wide, light-background README banner titled **"Climate Intelligence"**,
  clean and professional.
- A creative, graphical AI motif per Q14 — an abstract neural-network / node
  field (or data-driven flowing lines) rather than any cliché robot — visually
  fused with a climate/Earth element so "intelligence" and "climate" read as one
  idea.
- The four topic areas woven in subtly as small tags/icons: climate physics,
  biodiversity, global population, homelessness.
- 2–3 canonical, well-sourced climate numbers as accents (all traceable to
  context/claudes_context.md):
  1. **~+1.1 °C** observed warming (2011–2020 vs 1850–1900; IPCC AR6 WGI/SYR).
  2. **>430 ppm** atmospheric CO₂ (2025 Mauna Loa peak, vs ~280 ppm
     pre-industrial; AR6 WGI + Mauna Loa / §8).
  3. **~3.7 mm/yr** sea-level rise (2006–2018, roughly triple the early-20th-c.
     rate; IPCC AR6 WGI/SROCC).
- Avoiding the agreed list (burning globes, lone polar bears, overtly political
  imagery, dense text).

18. Does this concept and number selection match your intent? Confirm or adjust,
    and I'll build `docs/scripts/CI_graphic.py`.

    Answer: Agreed

**Tagline options (round 4)**

Ten candidate taglines for the banner/site. They aim to fit the project —
rigorous, primary-source-grounded climate science, the climate crisis met with
Artificial Intelligence — without being preachy, political, or cliché. Tone
varies from crisp to a touch more descriptive. Pick one (or mix/edit).

1. Reading the climate signal in the noise.
2. The climate, measured — not shouted.
3. Where climate science meets artificial intelligence.
4. Turning data into understanding of a warming world.
5. Rigorous climate science for the age of AI.
6. Finding the signal. Facing the crisis.
7. Primary sources. Hard numbers. Clear thinking.
8. Intelligence, applied to a changing climate.
9. The evidence on climate — read carefully.
10. From noisy data to a clearer view of Earth's future.

Chosen: 3 — "Where climate science meets artificial intelligence." (for now)

**Tagline options (round 5) — riffs on "Where climate science meets artificial intelligence."**

Ten variations on the chosen tagline's "meeting of two worlds" idea. Tone
varies; all aim to stay on-brand (rigorous, primary-source-grounded, climate +
AI) and clear of preachy/political/cliché phrasing.

1. Where the climate crisis meets artificial intelligence.
2. Where climate data meets artificial intelligence.
3. Climate science, meet artificial intelligence.
4. At the intersection of climate and intelligence.
5. Where a warming world meets machine intelligence.
6. Climate science and AI, working the same problem.
7. Where Earth science and artificial intelligence converge.
8. Where the evidence on climate meets the tools of AI.
9. Climate understanding, amplified by artificial intelligence.
10. Where planetary science meets artificial intelligence.

Chosen: