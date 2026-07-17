# Planetary Boundaries

## Goals

This prompt doc will generate context related to planetary boundaries and calculations of energy balance in a future Earth with greatly reduced fossil fuels usage.

## Context

Here is a major website devoted to planetary boundaries:

- https://www.stockholmresilience.org/research/planetary-boundaries.html

Tom Murphy has published a set of calculations related to planetary boundaries and our future ability to live within them without fossil fuels.  You can find his textbook in `context/Murphy` as well as a summary of it that you produced.

## Prompts

1. Make a first pass on the materials above.  Your goals are going to be to:

    - Add to the `context/claudes_context.md` file
    - Add a new section to `CI_2026_07_09_climate_report.md` on the topics of this prompt doc.  It should include figures

Read the files and then start a conversation with me below in the Q&A section.  Log your work.  Use Fable if you can.

2. I have answered your questions.  Please read those and then proceed to write the context addition, the report section + figures, and log it.  Use Fable if you can.

## Q&A

### Claude's first pass & questions — planetary boundaries + future energy balance (2026-07-17)

**What I read (first pass).** Both source bodies are already distilled in my
context, so this pass was mostly synthesis rather than fresh reading:

- **Stockholm planetary boundaries** — captured earlier today as
  `claudes_context.md` §16: the nine boundaries, the 2009/2015/2023 lineage, the
  **2025 seven-of-nine-transgressed** status (ocean acidification newly crossed,
  Ω_arag ≈ 2.84 vs ~2.86), the control-variable table, and ozone as the one
  recovering boundary.
- **Murphy, *Energy and Human Ambitions*** — `claudes_context.md` §3.1: the
  physics-of-limits thesis, the **EROI** table (Hydro 40+ … Solar PV 6, Nuclear
  5), solar as the only alternative that *scales* (Earth intercepts ~123,000 TW;
  ~0.4% of land could meet demand) but capped by **intermittency/seasonal
  storage** and a ~$50T build-out, batteries at ~1/65th of gasoline's energy
  density, the **Energy Trap**, and the waste-heat limit (~18 TW today; 2.3%/yr →
  boils the surface in ~400 yr regardless of source).

**The one fork I need you to settle before I write the report section.** "Energy
balance in a future Earth with greatly reduced fossil fuels" can mean two very
different things, and the figures/calculations differ completely:

- **(A) Civilizational energy *supply* balance** — the Murphy/MacKay question:
  *can* renewables (mostly solar/wind) meet projected demand without fossil fuels,
  given EROI, seasonal storage, land, and materials? This is a supply-vs-demand
  accounting exercise. **← my recommended default**, because it's what pairs
  naturally with Murphy and with the planetary-boundaries framing (a solar/storage
  build-out itself pushes on the land-system, biogeochemical, freshwater, and
  novel-entities boundaries — a genuinely fresh synthesis).
- **(B) Planetary *radiative/thermal* energy balance** — Earth's heat budget
  itself: radiative forcing bookkeeping and Murphy's waste-heat ceiling. More
  physics-of-the-planet, less about the transition.

They're not mutually exclusive — I can lead with (A) and use (B)'s waste-heat
limit as a bounding sidebar — but I want your call on the emphasis.

**Questions (with my proposed defaults so you can just say "yes" to any):**

1. **Framing (A vs. B above)?** *Default: A, with B as a short bounding sidebar.*
>A.  Yes, lead with (A) and use (B) as a bounding sidebar.
2. **Future scenario to anchor the numbers on** — target year and demand path?
   *Default: global, to ~2050 and ~2100, comparing a flat-demand case against a
   modest-growth case (per Murphy's exponential caution), rather than picking one.*
>A. Let's use 2100.

3. **How much original calculation vs. reproducing Murphy?** Per CLAUDE.md I'll
   script anything I compute. *Default: a new `CI_Reports/planetary_boundaries_energy.py`
   that reproduces Murphy's headline solar-land / storage / EROI numbers from stated
   inputs (so they're reviewable), plus the boundaries status data — no black-box
   new modeling.*
>A. Follow Murphy's lead, but update numbers anywhere you can based on any new data you find.

4. **Report placement & number** — the report currently runs …§5 Future
   projections, §6 Biodiversity, §7 Homelessness…§10 scope. *Default: insert a new
   section right after §5 (Future projections) or §6 (Biodiversity), titled
   something like "Planetary boundaries and the energy balance of a low-carbon
   future," and renumber downstream. Tell me if you'd rather append it at the end.*
>A. Insert a new section right after §5 (Future projections) 
5. **Figures** (it must include figures) — my proposed set, tell me to add/cut:
   - (i) a **planetary-boundaries status** chart — my own redraw from the data
     (not the copyrighted SRC "wagon wheel"), showing 7 of 9 crossed;
   - (ii) an **EROI** comparison bar chart;
   - (iii) **solar land-area** needed to meet demand (Murphy's ~0.4%-of-land),
     and/or a **seasonal-storage** requirement figure;
   - (iv) optionally, the **waste-heat / growth** timeline (the ~400-yr ceiling).
>A. Include all of these
6. **Stance** — Murphy is limits/degrowth-leaning. *Default per Principles 2 & 4:
   present the physics-grounded limits case *and* the optimistic renewables case
   fairly, flag the values question, and don't plant a flag.* Confirm that's the
   tone you want.
>A. I confirm