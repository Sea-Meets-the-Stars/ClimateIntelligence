# Claude's Context — Climate Intelligence

> **Purpose.** A *living* knowledge base that Claude maintains and consults while
> writing the Climate Intelligence blog. It distills the primary sources we have
> collected so posts can be grounded, cited, and internally consistent.
>
> **Status:** living document — updated ad infinitum as we add sources.
> **Last updated:** 2026-07-05 (initial build from the Murphy textbook + the seven
> IPCC AR6-cycle reports).
>
> **How to maintain:** when a new source is added to `context/Books/` or
> `context/Reports/`, read it, add a "Source" subsection below with citation +
> distilled findings + blog hooks, append to the changelog, and refresh any
> cross-cutting numbers that changed.

---

## 1. Source library

Staged locally in `context/` (git-ignored; large PDFs live on Google Drive) and
mirrored to the `ClimateIntelligence:` shared Drive (`Books/`, `Reports/`).

| Short name | Full title | Year | Local path |
|---|---|---|---|
| Murphy | Energy and Human Ambitions on a Finite Planet | 2021 | `context/Books/murphy_textbook.pdf` |
| AR6 WGI | Climate Change 2021: The Physical Science Basis | 2021 | `context/Reports/IPCC_AR6_WGI_FullReport.pdf` |
| AR6 WGII | Climate Change 2022: Impacts, Adaptation and Vulnerability | 2022 | `context/Reports/IPCC_AR6_WGII_FullReport.pdf` |
| AR6 WGIII | Climate Change 2022: Mitigation of Climate Change | 2022 | `context/Reports/IPCC_AR6_WGIII_FullReport.pdf` |
| AR6 SYR | Climate Change 2023: Synthesis Report | 2023 | `context/Reports/IPCC_AR6_SYR_FullVolume.pdf` |
| SR1.5 | Global Warming of 1.5°C | 2018 | `context/Reports/IPCC_SR15_FullReport.pdf` |
| SROCC | Ocean and Cryosphere in a Changing Climate | 2019 | `context/Reports/IPCC_SROCC_FullReport.pdf` |
| SRCCL | Climate Change and Land | 2019 | `context/Reports/IPCC_SRCCL_FullReport.pdf` |

The seven IPCC reports constitute the **complete AR6 assessment cycle** (three
Working Group reports + Synthesis Report + three Special Reports). AR7 has not yet
published. Earlier cycles (AR5 and before) are **not** yet collected — see the open
questions in `claude_prompts/context.md`.

---

## 2. Cross-cutting facts (the numbers to reach for)

These recur across sources; use them as the blog's quantitative backbone.

- **Observed warming:** 1.09 °C [0.95–1.20] in 2011–2020 vs 1850–1900; land 1.59 °C,
  ocean 0.88 °C. (AR6 WGI/SYR)
- **Attribution:** best estimate of human-caused warming ≈ 1.07 °C — essentially
  *all* observed warming. IPCC now calls human influence **"unequivocal."** (WGI)
- **GHG concentrations (2019):** CO₂ 410 ppm (highest in ≥2 million years); CH₄
  1866 ppb, N₂O 332 ppb (highest in ≥800,000 years). Pre-industrial CO₂ ≈ 280 ppm;
  now >420 ppm. (WGI / Murphy)
- **Equilibrium climate sensitivity:** best estimate **3 °C** per CO₂ doubling
  (likely 2.5–4 °C) — narrowed from AR5. (WGI; Murphy derives ≈3 °C independently.)
- **Carbon-budget dial (TCRE):** every **1000 GtCO₂ ≈ 0.45 °C** of warming. (WGI)
- **Remaining carbon budget (from 2020):** ≈ **500 GtCO₂** for a 50% chance of
  1.5 °C; ≈ 1150–1350 GtCO₂ for a 67% chance of 2 °C. Historical cumulative CO₂
  1850–2019 ≈ **2400 GtCO₂** — ~4/5 of the 1.5 °C budget already spent. (WGI/WGIII/SYR)
- **Emissions (2019):** ≈ **59 GtCO₂-eq** total net anthropogenic GHG — 54% above
  1990. (WGIII/SYR)
- **Ocean uptake:** the ocean has absorbed **>90%** of excess heat (91%). (WGI/SROCC)
- **Sea level:** +0.20 m over 1901–2018; rate accelerated 1.3 → 1.9 → **3.7 mm/yr**
  (2006–2018), roughly tripling. (WGI/SROCC)
- **Emissions vs pledges gap:** current policies → ≈ **3.2 °C** by 2100; pre-COP26
  NDCs → ≈ **2.8 °C**; 1.5 °C needs ≈ **−43% GHG by 2030** and net-zero CO₂ ≈ 2050.
  (WGIII/SYR)
- **Cost of technology:** 2010–2019 unit costs fell **~85% (solar), ~55% (wind),
  ~85% (batteries)**; solar deployed >10×, EVs >100×. (WGIII/SYR)
- **1.5 °C timing:** best estimate for crossing 1.5 °C lies in the near term
  (early-to-mid 2030s) under nearly all scenarios. (SYR/SR1.5)

---

## 3. Sources — distilled knowledge

### 3.1 Murphy — *Energy and Human Ambitions on a Finite Planet* (2021)

**Citation:** Murphy, Thomas W., Jr. (2021). *Energy and Human Ambitions on a Finite
Planet: Assessing and Adapting to Planetary Limits.* eScholarship, UC San Diego.
Open access, CC-BY-NC. DOI 10.21221/S2978-0-578-86717-5.

**Thesis.** Physics — thermodynamics and the math of exponential growth — imposes
hard limits on the human enterprise. Continued growth in energy, economy, and
population is impossible on a finite planet over civilization-relevant timescales.
The fossil-fueled boom is a one-time, abnormal "fireworks show" we mistake for
normal. Framed as a **predicament** (to be adapted to) rather than a **problem**
(to be solved). Self-described physics-grounded pessimism; modeled on David
MacKay's *Sustainable Energy — Without the Hot Air*.

**Signature arguments & numbers.**
- Global power use ≈ **18 TW**. At a conservative **2.3%/yr growth (10× per
  century)**, *waste heat alone* — independent of source, including fusion —
  boils Earth's surface in **~400 years** (Stefan–Boltzmann limit). Consuming the
  Sun's entire output ≈ 1400 yr; the visible universe's starlight ≈ 3600 yr.
- **Economic growth** is historically coupled to energy (~5 MJ/$); indefinite GDP
  growth on flat energy forces the physical economy toward absurdity (<0.1% of
  spending buys all essential physical goods).
- **EROI table:** Hydro 40+, Wind 20, Coal 18, Oil 16, Natural gas 7, Solar PV 6,
  Nuclear 5, Tar sands 3–5, Corn ethanol 1.4. Below ~1:1 a society is non-viable.
- **Solar** is the one alternative that scales (Earth intercepts ~123,000 TW,
  thousands of times demand; ~0.4% of land could meet current demand) but is capped
  by **intermittency/seasonal storage** and ~$50 trillion global build-out cost, and
  provides no liquid fuel.
- **Batteries** hold ~65× less energy per gram than gasoline → no drop-in liquid
  fuel replacement; an electric airliner is infeasible.
- **The Energy Trap:** new energy infrastructure costs energy up front; starting the
  transition late (after decline bites) demands painful diversion of scarce energy —
  hard for short-cycle democracies.
- Independently derives climate physics matching IPCC: RF = 5.35·ln(CO₂/280),
  sensitivity ≈ 0.8 °C per W/m², doubling CO₂ ≈ 3 °C; committed warming ≈ 1.7 °C at
  today's CO₂ (only ~55% realized because oceans lag).

**Editorial value:** the physics-first, "limits" voice — a useful counterweight and
complement to the IPCC's solution-oriented framing (see §5, Tensions).

### 3.2 AR6 WGI — *The Physical Science Basis* (2021)

**Scope:** the physical science only (how/why the climate is changing; attribution;
projections). 12 chapters + Interactive Atlas.

**Headlines:** human influence is **"unequivocal"** (stated as fact, no hedge);
present state is unprecedented over centuries–millennia; human-caused extremes are
in **every region**; warming will pass 1.5 °C and 2 °C this century absent deep
cuts; many changes (ocean heat, ice sheets, sea level) are irreversible for
centuries–millennia; low-likelihood high-impact outcomes can't be ruled out.

**Key numbers:** ECS 3 °C; total anthropogenic forcing 2.72 W/m² (2019 vs 1750);
energy imbalance 0.79 W/m² (2006–2018), 91% into the ocean; scenario warming
2081–2100: SSP1-1.9 **1.4 °C** → SSP5-8.5 **4.4 °C**; extreme daily precip +~7%/°C;
a 1-in-50-yr heat extreme ~4.8× more frequent at 1.5 °C, 8.6× at 2 °C, 39× at 4 °C;
Arctic likely practically ice-free in September at least once before 2050 under all
scenarios; AMOC very likely weakens (no abrupt collapse before 2100, medium conf.).

### 3.3 AR6 WGII — *Impacts, Adaptation and Vulnerability* (2022)

**Scope:** consequences for nature and people; who/what is vulnerable; adaptation.
Organizing concept: **risk = hazard × exposure × vulnerability** (+ response risks).
Identifies **127 key risks**. 18 chapters + 7 cross-chapter papers.

**Headlines & numbers:** **3.3–3.6 billion people** live in highly vulnerable
contexts; 2010–2020 disaster mortality **15× higher** in highly vulnerable regions;
~half of species already shifted poleward/upslope; the first climate-driven
extinctions have occurred; ~half the world faces severe water scarcity part of each
year; species very-high extinction risk 3–14% at 1.5 °C → up to 48% at 5 °C;
~1 billion at coastal-hazard risk by mid-century; US$8–14 trillion of assets in the
2100 100-yr coastal floodplain; some ecosystems have hit **hard adaptation limits**
(warm-water corals). Safeguarding biodiversity needs conservation of **30–50%** of
land/freshwater/ocean ("30×30" evidence base). Signature line: *"Climate change is a
threat to human well-being and planetary health… a brief and rapidly closing
window."*

### 3.4 AR6 WGIII — *Mitigation of Climate Change* (2022)

**Scope:** reducing/preventing emissions + CDR — technology, sectors, economics,
policy, finance, behaviour. New emphasis on demand-side and equity. 17 chapters.

**Headlines & numbers:** 2019 emissions ≈ **59 GtCO₂-eq** (highest-ever decade);
sector shares (direct): energy supply 34%, industry 24%, AFOLU 22%, transport 15%,
buildings 6%; cities ≈ 67–72%. Emissions must **peak before 2025** in 1.5 °C
pathways; GHG **−43% by 2030**, net-zero CO₂ ~early 2050s; committed CO₂ from
existing+planned fossil infrastructure (~850 GtCO₂) alone busts 1.5 °C. Solar/wind/
battery costs fell ~85/55/85%. **CDR is now "unavoidable"** to reach net zero, yet
only afforestation/soil methods run at scale. Options **≤US$100/tCO₂** could halve
2019 emissions by 2030; mitigation shaves only a few % off 2050 GDP (which still
~doubles). **Demand-side** measures can cut end-use emissions **40–70% by 2050**.
Mitigation investment must rise **3–6×**.

### 3.5 AR6 SYR — *Synthesis Report* (2023)

The capstone integrating the six reports above; approved Interlaken, March 2023.
18 headline statements in three parts (Current Status & Trends / Future Risks &
Long-Term Responses / Near-Term Responses). Best single-document source for the
consensus story. Emphasizes: unequivocal human causation; every increment of
warming intensifies hazards; net-zero CO₂ is required; existing fossil
infrastructure exceeds the remaining 1.5 °C budget; a rapidly closing window; equity
and finance (flows must rise many-fold) as central enablers. Consumption inequality:
top 10% of households = 34–45% of household emissions; bottom 50% = 13–15%.

### 3.6 SR1.5 — *Global Warming of 1.5°C* (2018)

Commissioned by the Paris Agreement decision (1/CP.21). Systematically contrasts
**1.5 °C vs 2 °C**. Crossing 1.5 °C likely between **2030 and 2052** at current
rates. The half-degree matters enormously: coral reefs **70–90% lost at 1.5 °C vs
>99% at 2 °C**; species range loss roughly doubles; ice-free Arctic summer once/
century (1.5 °C) vs once/decade (2 °C); up to 10 million fewer exposed to SLR at
1.5 °C. 1.5 °C pathways: CO₂ **−45% by 2030, net-zero ~2050**; all rely on CDR of
100–1000 GtCO₂/century; ~US$2.4 trillion/yr energy investment (~2.5% of GDP).
Current NDCs → ~3 °C.

### 3.7 SROCC — *Ocean and Cryosphere* (2019)

Ocean covers 71% of Earth and holds ~97% of its water. Ocean absorbed >90% of
excess heat; warming rate more than doubled since 1993; **marine heatwaves doubled
since 1982** (→ ~50× by 2100 under RCP8.5). Surface pH falling 0.017–0.027/decade;
acidification signal has emerged over >95% of the surface. GMSL +0.16 m (1902–2015)
at 3.6 mm/yr (2006–2015); projected +0.43 m (RCP2.6) to +0.84 m (RCP8.5) by 2100,
2.3–5.4 m by 2300 under RCP8.5. Greenland losing 278 Gt/yr, Antarctica 155 Gt/yr
(mass loss tripled). Permafrost holds **1460–1600 GtC (~2× the atmosphere)**; up to
69% of near-surface permafrost could vanish by 2100. Historically once-per-century
extreme sea levels become **at least annual** at many sites by 2050.

### 3.8 SRCCL — *Climate Change and Land* (2019)

Humans directly use **>70% of ice-free land**; ~**25% is degraded**. AFOLU ≈ **23%**
of net anthropogenic GHG; the whole food system **21–37%**. Land is a natural sink
absorbing ~29% of CO₂ emissions (11.2 GtCO₂/yr), but its persistence is uncertain.
Land air temperature has warmed **~1.53 °C** (nearly 2× the global mean). Agriculture
= 81% of human N₂O and 44% of CH₄. **25–30% of food is lost/wasted** (8–10% of
emissions). ~500 million people live in areas that desertified since the 1980s.
**Dietary change** could mitigate **0.7–8.0 GtCO₂-eq/yr by 2050**; but large-scale
BECCS/afforestation (up to several million km²) risks food/water/biodiversity
harm — no free lunch. Dryland restoration returns **US$3–6 per dollar**.

---

## 4. Blog story hooks (bank of vivid, citable angles)

Grouped by theme; each is traceable to a source in §3.

**Scale & inevitability (Murphy):**
- "Earth boils in ~400 years from waste heat *alone*" — clean energy doesn't escape
  thermodynamics.
- A Dyson sphere from Earth's mass would be a film <4 mm thick.
- "The Most Important Plot Ever": the entire fossil age is one narrow spike on a
  ±10,000-year timeline — we mistake an anomaly for normal.
- You can't fly a battery-powered airliner (jet fuel ~65× denser than Li-ion).
- The Energy Trap: transition costs energy up front; start late and it hurts.

**The physics of the budget (WGI/SYR):**
- "Unequivocal" — IPCC states human causation as fact, no hedge.
- Every 1000 GtCO₂ ≈ 0.45 °C — a clean dial from tonnes to degrees.
- ~500 GtCO₂ left for a coin-flip at 1.5 °C — about a decade at current rates.
- Aerosol pollution masks up to ~0.8 °C; cleaning the air unmasks heat → methane is
  the key near-term lever.

**Already locked in (WGI/SROCC):**
- The ocean has taken >90% of the heat and is paying in acidification + oxygen loss.
- Sea-level rise has nearly tripled; ice-sheet loss doubled–tripled in decades.
- Permafrost holds ~2× the atmosphere's carbon; up to 69% of the near-surface could
  thaw by 2100.
- A once-a-century coastal flood becomes near-annual at many coasts by 2050.

**The half-degree that matters (SR1.5):**
- Coral reefs: 70–90% gone at 1.5 °C, >99% at 2 °C.
- Ice-free Arctic summer: once/century vs once/decade.

**People & justice (WGII/SYR/SRCCL):**
- 3.3–3.6 billion people live in highly vulnerable contexts; 15× higher disaster
  mortality there.
- Top 10% of households emit up to 45%; bottom half barely 13%.
- We waste 25–30% of food (8–10% of emissions) while 821 million go hungry and
  2 billion are overweight.

**Reasons for hope / the toolbox (WGIII):**
- Solar and batteries got ~85% cheaper in nine years.
- Options under US$100/tonne could halve emissions by 2030; serious action costs
  only a few % of 2050 GDP, which still doubles.
- Demand-side changes alone could cut end-use emissions 40–70% by 2050.

---

## 5. Themes & editorial tensions

Useful framings for posts that go beyond fact-listing:

1. **Limits vs. solutions.** Murphy (physics of limits; growth must end; adapt to a
   predicament) vs. IPCC (deep but achievable transitions; a solvable problem with a
   closing window). Both agree on the physics and on net-zero-CO₂ necessity; they
   diverge on whether a high-energy modern civilization is sustainable. Rich material
   for balanced, honest posts.
2. **Speed vs. scale.** The budget math (WGI) and the peak-before-2025 deadline
   (WGIII) vs. the Energy Trap and infrastructure inertia (Murphy). Why "we have the
   technology" and "it's nearly too late" are both true.
3. **Mitigation ↔ land ↔ ocean interdependence.** CDR/BECCS (WGIII) competes for
   land (SRCCL) and can't offset delay; the ocean's uptake (SROCC) buys time while
   accruing irreversible damage. Systems-level story.
4. **Equity as physics-adjacent.** Emissions and impacts are radically unequal
   (WGII/SYR); "who caused it vs. who suffers" is quantifiable, not rhetorical.

---

## 6. Glossary (acronyms used above)

AR6 = Sixth Assessment Report. WGI/II/III = Working Groups I/II/III. SYR = Synthesis
Report. SR1.5 / SROCC / SRCCL = the three AR6 Special Reports. SPM = Summary for
Policymakers. TS = Technical Summary. GHG = greenhouse gas. AFOLU = Agriculture,
Forestry and Other Land Use. LULUCF = Land Use, Land-Use Change and Forestry.
ECS = equilibrium climate sensitivity. TCRE = transient climate response to
cumulative emissions. CDR = carbon dioxide removal. BECCS = bioenergy with carbon
capture and storage. DACCS = direct air carbon capture and storage. EROI/EROEI =
energy return on (energy) invested. NDC = Nationally Determined Contribution.
SSP/RCP = Shared Socioeconomic Pathway / Representative Concentration Pathway.
AMOC = Atlantic Meridional Overturning Circulation. GMSL = global mean sea level.

---

## 7. Changelog

- **2026-07-05** — Initial build. Read and distilled all 8 sources (Murphy + 7 IPCC
  AR6-cycle reports) via parallel reader agents working from `pdftotext` extractions;
  uploaded `Books/` and `Reports/` to the `ClimateIntelligence:` Drive. Established
  §§1–6 structure.
