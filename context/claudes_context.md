# Claude's Context — Climate Intelligence

> **Purpose.** A *living* knowledge base that Claude maintains and consults while
> writing the Climate Intelligence blog. It distills the primary sources we have
> collected so posts can be grounded, cited, and internally consistent.
>
> **Status:** living document — updated ad infinitum as we add sources.
> **Last updated:** 2026-07-09 (added §10 Biodiversity & the sixth mass
> extinction; §9 heterodox voices + §9.1 DOE exchange and §8 recent developments
> on 2026-07-08; initial build 2026-07-05 from the Murphy textbook + seven IPCC
> AR6-cycle reports).
>
> **Companion file:** `context/references.md` — a curated directory of *where to
> look* (assessment bodies, data feeds, journals, journalism, trackers). This
> file distills *what the sources say*; that one catalogs the sources.
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
| DOE CWG | A Critical Review of Impacts of GHG Emissions on the U.S. Climate (Christy, Curry, Koonin, McKitrick, Spencer) | 2025 | `context/Reports/DOE_CWG_Critical_Review_July2025.pdf` |
| CWG Rebuttal | Climate Experts' Review of the DOE CWG Report (85+ authors; eds. Dessler & Kopp) | 2025 | `context/Reports/Climate_Experts_Review_of_DOE_CWG_Sept2025.pdf` |

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

## 8. Recent developments (mid-2025 – mid-2026)

> From web research on 2026-07-08 (details + sources in `references.md` §7).
> Several items post-date the Jan-2026 knowledge cutoff and rest on web results —
> **verify figures against the primary reports before publishing.** The IPCC
> reports in §3 remain the settled-science backbone; this section is the moving
> frontier on top of them.

- **The 2020s are running hot.** 2024 was the warmest year on record (~1.6 °C) and
  the first full calendar year above 1.5 °C; 2025 came in 2nd–3rd (~1.43–1.47 °C),
  and **2023–2025 is the first 3-year stretch averaging above 1.5 °C.** This is a
  multi-year run, *not yet* a formal breach of the Paris long-term (~20-yr) goal —
  a crucial distinction for careful writing. UNEP now expects the long-term mean to
  breach 1.5 °C, at least temporarily, within ~a decade.
- **CO₂ passed 430 ppm** at the 2025 Mauna Loa peak (~431 ppm by mid-2026) — up from
  the 410 ppm the AR6 reports cite for 2019, and ~280 ppm pre-industrial.
- **Emissions still rising:** Global Carbon Budget 2025 put fossil CO₂ at a record
  ~38.1 Gt. The remaining 1.5 °C budget is down to **~170 GtCO₂ — roughly four years**
  at current rates (vs the ~500 GtCO₂ from-2020 figure in §2, now largely spent).
- **The gap is narrowing slowly:** current policies point to ~2.6 °C (Climate Action
  Tracker) and full NDC implementation to ~2.3–2.5 °C (UNEP 2025) — better than the
  ~3.2 °C of a few years ago, still far from 1.5 °C.
- **COP30 (Belém, Nov 2025)** delivered finance commitments (tripled adaptation
  finance; $1.3 trn/yr roadmap; Tropical Forests Forever Fund) but **no agreed
  fossil-fuel phase-out** in the formal text — a "stabilization," not an ambition,
  outcome.
- **The transition is visibly accelerating:** solar was the single largest source of
  energy-demand growth for the first time (2025), and EV sales topped 20 million
  (~1 in 4 new cars) — real-world confirmation of WGIII's cost-decline story.
- **Frontier / contested (flag carefully):** the *Global Tipping Points Report 2025*
  declared warm-water coral reefs the first crossed tipping point (expert assessment,
  not undisputed observation); some 2025 modelling flags earlier AMOC-collapse risk
  (single-study, highly uncertain). Present both as strong-but-debated, not settled.
- **IPCC AR7** is underway (664 authors selected Aug 2025; reports ~2028–29) but
  governments have failed to agree a timeline — called "unprecedented" in IPCC history.

## 9. Heterodox voices — the strongest opposing arguments

> Added 2026-07-08 at the author's request. Full works/platform lists in
> `references.md` §8. Rule for the blog: engage the **steel-man** version of each
> argument, credit genuine expertise plainly, and cite the published rebuttals —
> never the strawman ("they deny the greenhouse effect"; none of them do).

**Who they are, in one line each:**
- **Judith Curry** (climatologist, ex-Georgia Tech chair): the *epistemic* critic —
  "uncertainty monster," natural variability underweighted, climate is a "wicked
  problem" better met with adaptation/resilience than emissions targets. Technical
  anchor: Lewis & Curry energy-budget ECS estimates (~1.5–1.65 °C).
- **Richard Lindzen** (MIT, NAS; first-rank dynamics theorist): the *physical*
  critic — iris hypothesis: tropical cirrus contract with warming, a strong
  negative feedback ⇒ low ECS (~0.5–1.5 °C).
- **John Christy & Roy Spencer** (UAH; created the satellite temperature record):
  the *observational* critics — tropical troposphere warms ~half as fast as
  CMIP models simulate ⇒ model feedbacks too strong; surface records inflated by
  urbanization; Spencer adds cloud-causality arguments (ECS ≈ 1.9 °C, 2023).
- **Steven Koonin** (physicist, NAS; ex-Obama DOE Under Secretary): the *framing*
  critic — *Unsettled* (2021/24) argues summaries and media overstate confidence
  relative to the underlying reports; wants red-team review; prefers adaptation.
- **William Happer** (Princeton atomic physicist, NAS): the *radiative* critic —
  CO2 bands "saturated" so forcing grows only logarithmically; CO2 fertilization a
  net benefit. (His own line-by-line forcing calculations match mainstream values;
  the dispute is feedbacks and the benefits inference.)
- **Roger Pielke Jr.** (policy scientist, AEI): the *attribution/policy* critic —
  accepts the physics, supports a carbon tax; argues normalized disaster losses
  show no trend, extreme-event claims are overstated, RCP8.5 is misused as
  business-as-usual; "Iron Law": growth beats emissions cuts politically.
- **Roger Pielke Sr.** (CSU meteorologist emeritus): land-use/aerosol forcings
  underweighted vs CO2; ocean heat content the better metric. (Always disambiguate
  Jr./Sr.)

**How the mainstream answered (the short version):**
- The **iris hypothesis** was tested and largely rejected (Hartmann & Michelsen
  2002; Lin et al. 2002); a weak iris-like effect may exist (Mauritsen & Stevens
  2015) but nowhere near Lindzen's sensitivity values.
- The **UAH record's history** cuts both ways: two major errors (orbital decay
  1998; diurnal-drift sign 2005) were found by *outside* groups and raised the
  trend; but NOAA STAR v5 (2023) later moved toward UAH for mid-troposphere
  trends, so satellite structural uncertainty is real. Current trends: UAH
  +0.16 °C/decade vs RSS ~+0.21 and surface ~+0.20.
- The **tropical-troposphere discrepancy** (McKitrick & Christy) is acknowledged
  as real in AR6; Santer et al. 2017 shrink it (~1.7×, not 3×) and attribute much
  to forcing errors and internal variability (Po-Chedley et al. 2021), not low ECS.
- **Low energy-budget ECS** (Lewis & Curry) is taken seriously but judged biased
  low by "pattern effects" — Sherwood et al. 2020 (ECS likely 2.6–3.9 °C)
  effectively rules out the sub-2 °C values.
- **Saturation** fails because forcing grows in band wings and at the cold upper
  troposphere (Pierrehumbert/Weart, RealClimate 2007); Happer's own numbers agree
  on forcing.
- **Normalized-loss "no trend"** (Weinkle et al. 2018) vs Grinsted et al. 2019
  (*PNAS*, "area of total destruction" shows a trend) is a live, legitimate
  scientific exchange — the best current example of a genuinely open dispute.
- **Koonin's *Unsettled*** drew detailed rebuttals (Scientific American 2021,
  Yale Climate Connections, Science Feedback) charging outdated sourcing and
  selective emphasis rather than fabrication.

**The 2025–26 DOE episode (watch this):** Christy, Curry, Koonin, McKitrick and
Spencer authored the July 2025 DOE *Critical Review* commissioned to support the
EPA endangerment-finding repeal. An 85-scientist rebuttal followed (Sept 2025);
the working group was disbanded; a federal court found FACA violations (Jan
2026); EPA's final rule (Feb 2026) says it is "not relying on" the report. This
is now the definitive case study of contrarian science meeting institutional and
legal review — strong blog material with both sides fully on the record (see also
the 2014 APS workshop transcript for the earlier equivalent).

**Editorial guidance:** (1) credentials are real — say so; (2) each critic's
*data* has generally fared better than the *inferences* built on it; (3) the
sharpest engagements are Lindzen↔Dessler, Christy↔Santer, Pielke↔Grinsted,
Koonin↔Oreskes — cite the exchanges, not just one side; (4) fact-check numbers
against §2 and the primary datasets in `references.md` §3.

### 9.1 The DOE report ↔ expert rebuttal exchange (both read in full, 2026-07-08)

Both documents are in our library (§1) and on the Drive. This is the richest
single case study we have: the complete contrarian argument and the complete
mainstream answer, section by section, both on the record.

**The DOE report** (*A Critical Review…*, July 23, 2025; Christy lead, with
Curry, Koonin, McKitrick, Spencer; commissioned by Energy Secretary Wright):
- **Concedes more than its reputation suggests:** CO2 is a GHG and the largest
  human influence on climate; warming is real; global sea-level rise is real;
  hot extremes have increased since the 1950s; AR6's ECS upper-bound cut to
  4.0 °C is "well justified."
- **Its central claims:** CO2 fertilization/greening is a large understated
  benefit; "acidification" is better termed "neutralization"; RCP8.5 misuse
  inflates the impacts literature; UHI residually biases the land record;
  data-driven ECS ≈ 2.2 °C (disputes AR6's 2.5 °C floor); models overpredict
  tropospheric warming (McKitrick & Christy) and are "not fit for purpose"
  regionally; most **U.S.** extreme-weather series show no trend (1930s anchor);
  U.S. tide gauges show "no obvious acceleration" (subsidence dominates local
  problems); attribution methods (optimal fingerprinting, WWA rapid studies) are
  unreliable; warming is net-small-to-beneficial for U.S. agriculture and the
  economy (SCC assumption-driven; Dayaratna/McKitrick ~\$19 or less); U.S. policy
  has "undetectably small" climate effect (cars = "3% of global energy CO2").
- **Framing signatures to notice:** US-only scope for "no trend" claims vs the
  IPCC's global statements; early-20th-century baselines (1930s heat, 1886/1935
  hurricanes); metric choices (rural summer Tmax; absolute vs relative sea
  level; losses as %GDP); "detection before attribution" logic; heavy
  self-citation (Ch. 3 and 5 exceed 25% self-citation vs IPCC's ~2.4% mean).

**The rebuttal** (*Climate Experts' Review…*, Aug 30, 2025; eds. Dessler &
Kopp; 85+ authors, 48 section-by-section comments, ~400 pp., submitted to DOE
docket DOE-HQ-2025-0207):
- **Strongest technical counters:** the "models vs data" ECS dichotomy is false
  (Sherwood et al. synthesizes process + historical + paleo; <2 °C hard to
  reconcile with any line) — and DOE's own favored ECS (~2.2 °C) sits *inside*
  the range where, by DOE's own stated threshold, emission controls pass
  cost-benefit; the tropical-troposphere "fatal test" is a strawman (the CO2
  signal emerges first in the stratosphere; NOAA STAR v5 halved the claimed
  discrepancy); the Corn Belt figure is "a textbook case of cherry picking"
  (the single worst region in the NH; globally, models exceed observations over
  48% of area — as expected); "no acceleration" in sea level is "a vibes-based
  assessment" (satellite acceleration 0.084 ± 0.025 mm/yr²; CONUS aggregate
  0.7 → 4.7 mm/yr since the 1970s); the record-highs/record-lows ratio ran
  2–3× vs <0.5× chance in 2010–2019 and 2023 beat the 1930s for record-hot
  days in homogenized data; global burned-area decline is a grassland/land-use
  signal masking a doubling of boreal/western-US *forest* fire; the US vehicle
  figure was simply wrong (~16.9% of global road-transport CO2, not 3%); and
  the "US cuts don't matter" logic is the "fallacy of inconsequentialism" —
  the US is the largest *cumulative* emitter (~21–24% since 1850).
- **Process findings:** ≥22% of DOE citations inaccurate or misrepresentative
  (some references don't exist); review by DOE employees only, despite Highly
  Influential Scientific Assessment obligations; 30-day comment window.
- **Notably fair:** concedes no-trend hurricane landfalls ("none were
  expected"), real CO2 fertilization, cold deaths currently exceeding heat
  deaths, genuinely open questions (albedo decline, prior-choice in ECS), and
  its own possible errors given the rushed window.

**Aftermath (from §8/§9):** working group disbanded Sept 2025; federal court
found FACA violations Jan 30, 2026; EPA's final endangerment-finding repeal
(Feb 2026) states it is "not relying on" the report.

**How to use this pair:** quote claim-and-answer side by side; the DOE report's
concessions (§5 of our summary) and the rebuttal's concessions (§6) are the
honest common ground — start posts there, then show precisely where and why the
documents diverge (scope, baselines, metrics, statistics).

## 10. Biodiversity & the sixth mass extinction

> Added 2026-07-09 from the reading list in `context/Murphy/` (Tom Murphy's
> "Do the Math" posts + `Chap1_bibtex.txt` primary literature). Biodiversity is
> squarely in the blog's purview and connects to Principle 3 — *all life on Earth
> is relevant; human life need not be prioritized.* This is the biosphere half of
> the story that §§2–8 tell for the physical climate.

### 10.1 The scale: life on Earth is plants, and the animal sliver is now us

The quantitative baseline (Bar-On, Phillips & Milo 2018, *PNAS*): total living
biomass ≈ **550 Gt C**, of which **plants ≈450 Gt C (~80%)** and **all animals
≈2 Gt C (~0.4%)**. Within that animal sliver, humans and livestock now dominate:
humans ≈0.06 Gt C, livestock ≈0.1 Gt C, **wild mammals only ≈0.007 Gt C** —
livestock outweighs all wild mammals ~14×. Greenspoon et al. (2023, *PNAS*) put
current wild land mammals at ≈**20 Mt** wet weight (~3 kg per person) vs humans
≈390 Mt and livestock ≈630 Mt — **>50 kg of humans + domesticated animals for
every 1 kg of wild land mammal.** Since the dawn of civilization, human activity
has **roughly halved plant biomass** and cut **wild land-mammal biomass ~7-fold**.

Barnosky (2008, *PNAS*) supplies the mechanism: there is an **energetic ceiling**
on how much large-animal (megafauna, >44 kg) biomass the biosphere can carry, set
by net primary productivity. For ~50,000 years human expansion has drawn down that
budget at the expense of wild megafauna; modern abundance *above* the natural
ceiling is sustained only by the fossil-fuel energy subsidy — tying biodiversity
directly to the energy-limits thesis of the Murphy textbook (§3.1).

### 10.2 The sixth mass extinction: onset, not yet completion

The honest framing (this matters for Principle 1 and 5): a **true** mass extinction
means losing **>75% of species** in a geologically short interval — this has
happened **5 times in ~540 Myr**. By that strict paleontological bar **we are NOT
there yet** — documented losses so far are ~1–2% of species in well-studied groups
(Barnosky et al. 2011, *Nature*), rising to a contested ~7.5–13% once
under-assessed invertebrates are included (Cowie, Bouchet & Fontaine 2022, *Biol.
Reviews*). What is *not* seriously disputed is the **rate**: current extinctions run
~**100–1,000× the background rate** (≈114× for vertebrates under Ceballos et al.
2015's deliberately conservative assumptions). At sustained current rates the 75%
threshold arrives in ~3–22 centuries — i.e. we are plausibly at the **onset** of a
sixth mass extinction, not in a completed one. Write it as trajectory, not
accomplished fact.

The sharper near-term signal is **population decline / defaunation**, not species
counts: Ceballos, Ehrlich & Dirzo (2017) found **32%** of ~27,600 vertebrate
species declining, and among 177 mammals studied *all* lost ≥30% of range and >40%
lost >80%. Finn et al. (2023, *Biol. Reviews*) across ~71,000 species: **48%
declining, 49% stable, 3% increasing** ("more losers than winners"), with a third
of *non-threatened* species already declining. Ceballos et al. (2020) count 515
land-vertebrate species with <1,000 individuals left.

### 10.3 The scientific debate (present it fairly — Principle 2)

- **Consensus:** rates far above background; overwhelmingly human-caused; rapid
  population-level erosion. Essentially no credible biologist disputes this.
- **Legitimate dispute:** whether the strict >75% definition is met (no, not yet);
  reliance on IUCN data with taxonomic/geographic gaps; extrapolation from
  island faunas (higher extinction) to continents; "possibly extinct" vs confirmed
  ("Romeo error"); marine biota showing far lower extinction than terrestrial.
  Data bias cuts both ways — Cowie turns the under-assessment of invertebrates into
  an argument that the crisis is *worse* than the IUCN's 882-species (0.04%) count.
  A rebuttal literature exists (e.g. "Questioning the sixth mass extinction," *TREE*
  2025) — cite it for balance.

### 10.4 Drivers: where climate fits

Per IPBES (2019), the driver ranking is (1) land/sea-use change (habitat loss),
(2) direct overexploitation (hunting/fishing), (3) **climate change**,
(4) pollution, (5) invasive species. So the crisis was **set in motion mainly by
land use, exploitation and invasives; climate change is currently a secondary but
the fastest-accelerating driver**, projected toward co-dominant. The two crises are
mutually reinforcing: habitat destruction releases carbon and removes sinks, while
warming degrades the ecosystems that store it. IPBES's headline: ~**1 million
species threatened with extinction.**

### 10.5 The worldview frame (Murphy / Quinn) — flagged, used carefully

Murphy's "Do the Math" ecological posts ("Ecological Cliff Edge," "Is the 6ME
Hyperbole?") read the biomass collapse as the *biological invoice* for the same
growth-and-overshoot the energy math predicts. He argues it is **not hyperbole** to
speak in sixth-mass-extinction terms even though a formal 6ME hasn't occurred (his
"two seconds into a fall off a skyscraper" analogy — trajectory over present
status), backed by an asymmetric-risk/precautionary argument. He grounds the moral
stance in Daniel Quinn's *Ishmael* trilogy — the **"Taker vs Leaver"** framing
("the world was made for us" vs "humans belong to the world"), agriculture as the
fatal turn, and "the world was not made for humans alone." This maps directly onto
Principle 3. **Editorial caution:** Quinn's philosophy and Murphy's civilizational
pessimism are *viewpoints*, not data — present them as framing to engage, keep them
clearly distinct from the peer-reviewed biomass/extinction numbers, and honor
Principle 4 (leave religion/politics out) by treating the animism as one lens, not
doctrine.

**Blog hooks:** (1) "For every kilogram of wild land mammal, there are more than
fifty kilograms of humans and their livestock." (2) Life on Earth is ~80% plants;
all animals are ~0.4% — and within that, we and our cattle are most of the
mammals. (3) We are not *in* a sixth mass extinction by the 75%-of-species
definition — but extinctions run 100–1,000× normal, which is how one *begins*.
(4) Only ~3 kg of wild land mammal exists per person alive, down ~30-fold from
1800. (5) Deep-time precedent (Smart et al. 2023): in the Late Devonian, land
plants spreading triggered ocean anoxia and a marine mass extinction — life can
disrupt the system that sustains it. (6) Kolbert's *The Sixth Extinction* (2014
Pulitzer) mainstreamed the framing.

## 11. Changelog

- **2026-07-09** — Added §10 (Biodiversity & the sixth mass extinction) from the
  `context/Murphy/` reading list (7 "Do the Math" posts + 17 papers), via three
  parallel reader agents. Refreshed header; renumbered changelog to §11.
- **2026-07-08 (later still)** — Downloaded, verified, uploaded to Drive, and
  read in full the July 2025 DOE CWG report and its 85-author rebuttal; added
  both to the source library (§1) and wrote §9.1 distilling the exchange.
- **2026-07-08 (later)** — Added §9 (heterodox voices): fair profiles, mainstream
  rebuttals, and editorial guidance for Curry, Lindzen, Christy, Spencer, Koonin,
  Happer, and both Pielkes, from four parallel research passes (context.md
  prompt 4).
- **2026-07-08** — Added §8 (recent developments, mid-2025–mid-2026) from four
  parallel web-research passes, and created the companion `context/references.md`
  source directory. Refreshed the header and cross-references.
- **2026-07-05** — Initial build. Read and distilled all 8 sources (Murphy + 7 IPCC
  AR6-cycle reports) via parallel reader agents working from `pdftotext` extractions;
  uploaded `Books/` and `Reports/` to the `ClimateIntelligence:` Drive. Established
  §§1–6 structure.
