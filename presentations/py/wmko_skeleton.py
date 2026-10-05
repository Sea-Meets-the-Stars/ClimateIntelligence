"""Slide-by-slide skeleton for the WMKO Oct 2026 staff talk.

Source of truth for slide order, titles, and speaker notes (intended
figure / instrument / source). Derived from the Round-2 slide budget and
the Q&A answers in claude_prompts/presentations/wmko_oct2026.md.

Each entry: (section, title, subtitle, notes). Empty title/subtitle = blank
slide for the author to fill.
"""

TITLE = "title"      # uses the template's title-slide layout
CONTENT = "content"  # uses the template's title-only layout
DIVIDER = "divider"  # section divider: title centered vertically, may wrap

SECTIONS = ["Opening", "Climate: Top 10 facts", "Artificial Intelligence: Top 10", "Close"]

SLIDES = [
    # --- Opening ---------------------------------------------------------
    dict(section="Opening", kind=TITLE, title="Sea meets the stars",
         subtitle="Climate Intelligence",
         notes="Title slide carried over from Kraw_2024 slide 1 (sea|sky hero image, same title).\n"
               "Author line still reads Kraw 2024 affiliations (Kavli IPMU, Simons Pivot Fellow) — author to update."),
    dict(section="Opening", kind=CONTENT, title="My AI Team", subtitle="",
         notes="PLACEHOLDER: author will paste slide 6 of AOGS_2026 ('My AI Team') here by hand (Q22/Q42).\n"
               "Also serves as the acknowledgment slide (Q21)."),
    dict(section="Opening", kind=CONTENT, title="Climate Intelligence", subtitle="",
         notes="Figure: docs/CI_graphic.png (banner, five topic icons, warming curve).\n"
               "Source: Climate Intelligence blog."),
    dict(section="Opening", kind=CONTENT, title="The two exponentials", subtitle="",
         notes="Figure (new, B5): presentations/py/two_exponentials.py — AI training compute (Epoch AI, ~4x/yr) "
               "beside fossil CO2 emissions (OWID/GCP), log axes.\n"
               "Note: CO2 emissions stopped growing exponentially (blog001 fig4) — nuance for the narration.\n"
               "Source: Epoch AI; Global Carbon Project via Our World in Data."),
    dict(section="Opening", kind=CONTENT, title="Humans suck at exponentials", subtitle="",
         notes="Figure: blogs/blog001/fig1_covid_us_cases.png (2.4-day doubling, spring 2020).\n"
               "Source: NYT / JHU COVID-19 case data."),
    dict(section="Climate: Top 10 facts", kind=DIVIDER,
         title="Top 10 things we should all know about the Climate Crisis", subtitle="",
         notes="Section divider for the climate Top 10 (B8b; replaces the second 'Humans suck at "
               "exponentials' slide). Alternate figure for slide 5 if wanted: blogs/blog001/"
               "fig2_population_growth.png (log-log, four doubling eras; HYDE / UN WPP via OWID)."),

    # --- Climate: Top 10 -------------------------------------------------
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="1: CO₂ has been rising for 50+ years", subtitle="",
         notes="Figure (restyle, B2): CI_Reports/fig1_keeling_curve.png -> slide copy.\n"
               "Instrument: Mauna Loa Observatory CO2 analyzer (photo, B7). Local hook: measured next door.\n"
               "Source: NOAA GML Mauna Loa / Scripps."),
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="2: The U.S. has dominated greenhouse gas release", subtitle="",
         notes="Figure (restyle, B2): CI_Reports/fig24_country_breakdown.png right panel — US 23.5% of cumulative CO2 since 1750.\n"
               "Source: Global Carbon Project via Our World in Data."),
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="3: Heat in vs. heat out", subtitle="",
         notes="Figure (new, B3): presentations/py/energy_budget_arrows.py — AR6 WGI Fig 7.2 budget; "
               "imbalance ~0.76 W/m², doubled 2005-2019 (Loeb et al. 2021).\n"
               "Instrument: CERES (on Terra/Aqua). Source: IPCC AR6 WGI Ch.7; Loeb et al. 2021 GRL."),
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="3: Heat in vs. heat out: the CO₂ bite", subtitle="",
         notes="Figure (new, B3): presentations/py/olr_spectrum.py — computed SCHEMATIC outgoing IR spectrum: "
               "Planck 288 K vs ~220 K, CO2 band at 667 cm^-1. Labeled 'schematic' (Q37).\n"
               "Instrument: Nimbus-4 IRIS (credit). Source: Planck law; Hanel et al. 1972 for context."),
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="4: The ocean is warming: surface", subtitle="",
         notes="Figure (new, B4): presentations/py/sst_global.py — NOAA ERSSTv5 global ocean-surface anomaly.\n"
               "Instrument: ships, drifting buoys, satellites. Source: NOAA NCEI ERSSTv5."),
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="4: The ocean is warming: depth", subtitle="",
         notes="Figure (new, B4): presentations/py/ohc_by_depth.py — NCEI OHC 0-700 m and 700-2000 m (base: CI_Reports fig4).\n"
               "Instrument: Argo float (photo, B7). Source: NOAA NCEI ocean heat content."),
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="5: The ocean isn't done warming", subtitle="",
         notes="Figure (new, B3): presentations/py/committed_warming.py — BOTH framings (Q38c): committed-vs-realized bar "
               "(~2.2 °C equilibrium for today's forcing vs ~1.2 °C realized; Murphy 1.7 °C marker) AND ocean heat / "
               "sea-level inertia. Small-print caveat: AR6 zero-emissions commitment ≈ 0.\n"
               "Source: IPCC AR6 WGI (ERF 2.72 W/m², ECS 3 °C); Murphy textbook."),
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="6: Sea level is rising", subtitle="",
         notes="Figure (new, B4): presentations/py/gmsl_to_2025.py — Church & White tide gauges + satellite altimetry to 2025 (3.2 mm/yr; last decade 3.7).\n"
               "Instrument: Jason-3 / Sentinel-6 altimeter. Source: Church & White 2011; NOAA Laboratory for Satellite Altimetry (required credit: 'Altimetry data are provided by NOAA Laboratory for Satellite Altimetry')."),
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="6: Sea level is rising: Honolulu", subtitle="",
         notes="Figure (new, B4): presentations/py/honolulu_tide_gauge.py — NOAA station 1612340, monthly means since 1905, trend.\n"
               "Instrument: tide gauge. Source: NOAA CO-OPS."),
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="7: Biodiversity is declining fast", subtitle="",
         notes="Softened from 'exponentially' (Q11). 'Declining fast, by three independent metrics.'\n"
               "Figure (new, B5): presentations/py/biodiversity_lpi_biomass.py — Living Planet Index 1970-2020 "
               "(geometric-mean caveat in small print) + Bar-On 2018 biomass (wild mammals vs livestock vs humans).\n"
               "Source: WWF/ZSL LPI via OWID; Bar-On et al. 2018 PNAS."),
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="7: Biodiversity is declining fast: extinctions", subtitle="",
         notes="Figure (new, B5): presentations/py/extinction_rate.py — cumulative vertebrate extinctions vs 2 E/MSY background.\n"
               "Source: Ceballos et al. 2015 Science Advances."),
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="8: Planetary boundaries are being exceeded", subtitle="",
         notes="Figure (restyle, B2): CI_Reports/fig15_planetary_boundaries.png (7 of 9 exceeded, 2025).\n"
               "Source: Richardson et al. 2023; Planetary Health Check 2025."),
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="9: Population growth is poised to decline", subtitle="",
         notes="Figure (restyle, B2): CI_Reports/fig7_world_population.png (or blog001 fig2).\n"
               "Source: UN World Population Prospects 2024."),
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="9: Fertility has fallen below replacement", subtitle="",
         notes="Figure (restyle, B2): blogs/blog001/fig5_fertility_decline.png or CI_Reports/fig19_fertility_map.png (vs 2.1).\n"
               "Source: UN World Population Prospects 2024."),
    dict(section="Climate: Top 10 facts", group="climate10", kind=CONTENT, title="10: Most economists believe technology will save us", subtitle="",
         notes="Provocation (Q12c) + survey panel (Q29b, Q41): two columns — 'Alarmed' (74% immediate & drastic action; "
               "76% expect lower long-run growth) vs '...and still betting on technology' (65% expect cost collapses to repeat; "
               ">50% zero-emission energy by 2050). Sub-line: 'Alarmed — and still betting on technology.'\n"
               "Figure (new, B5): presentations/py/economist_survey.py. Source: Howard & Sylvan 2021, Institute for Policy Integrity (n=738)."),

    # --- Transition -------------------------------------------------------
    dict(section="Artificial Intelligence: Top 10", kind=CONTENT, title="", subtitle="",
         notes="TRANSITION — blank for now (Q33). Author to fill."),

    # --- AI: Top 10 --------------------------------------------------------
    dict(section="Artificial Intelligence: Top 10", group="ai10", kind=CONTENT, title="1: AI has surpassed me as a scientist", subtitle="",
         notes="Image: presentations/2026_WMKO/sacbee.png as-is (Q36). Sacramento Bee op-ed, 21 Aug 2026.\n"
               "Source: Prochaska, Sacramento Bee / McClatchy, Aug 21 2026."),
    dict(section="Artificial Intelligence: Top 10", group="ai10", kind=CONTENT, title="2: AI can already help create a deadly pandemic", subtitle="",
         notes="Gates's words carry the claim (Q26a): 'A.I. has crossed the threshold that its ability to empower a "
               "bioterrorist to kill hundreds of millions — that exists today.' (Fortune, 30 Sep 2026).\n"
               "Figure (new, B6): presentations/py/bio_uplift_arc.py — RAND & OpenAI 2024 (~1x) -> Anthropic Opus 4 2025 (2.53x) "
               "-> Zhang et al. 2026 (4.16x); VCT annotated as a different metric.\n"
               "Sources (small print): Mouton et al. 2024 (RAND); Patwardhan et al. 2024 (OpenAI); Anthropic 2025; "
               "Götting et al. 2025 arXiv:2504.16137; Zhang et al. 2026 arXiv:2602.23329."),
    dict(section="Artificial Intelligence: Top 10", group="ai10", kind=CONTENT, title="3: AI can already hack nearly every system on Earth", subtitle="",
         notes="One slide (Q27). Mythos Preview withheld (Apr 2026): critical vulns in every major OS/browser, 99% unpatched; "
               "UK AISI 73% success on expert hacking tasks. 'An AI agent broke into Hugging Face; a week later OpenAI said its models had too.' (Jul 2026)\n"
               "Sources: Scientific American 17 Apr 2026; Axios 7 Apr 2026; CNBC 22 Jul 2026; Varonis."),
    dict(section="Artificial Intelligence: Top 10", group="ai10", kind=CONTENT, title="4: Resistance to data centers is a (valuable) distraction", subtitle="",
         notes="Figure (restyle, B2): CI_Reports/fig13_us_datacenter_electricity.png (4.7% -> 9.5-15%) + fig14 water inset.\n"
               "Source: LBNL 2024 US data-center energy report; see context §14."),
    dict(section="Artificial Intelligence: Top 10", group="ai10", kind=CONTENT, title="5: AI will force the collapse of peer review", subtitle="",
         notes="Figure (new, B6): presentations/py/arxiv_submissions.py — arXiv monthly submissions 1991-2026, log axis; "
               "Sep 2024 20,569 -> Sep 2026 40,363 ('doubled in two years'); rate limit annotated (1 Oct 2026, max 2/month).\n"
               "Source: arxiv.org/stats; arXiv blog 1 Oct 2026."),
    dict(section="Artificial Intelligence: Top 10", group="ai10", kind=CONTENT, title="6: AI may end grant competition", subtitle="",
         notes="Image/sketch. 'Everyone can write the same, best proposal.'"),
    dict(section="Artificial Intelligence: Top 10", group="ai10", kind=CONTENT, title="7: AI will steeply raise the value of data collection", subtitle="",
         notes="Images (B7): Keck segmented primary + HIRES, 'Courtesy W. M. Keck Observatory'. Message: expensive one-offs that cannot be replicated.\n"
               "Caption: HIRES — PI S. Vogt, built 1988-93, first light 16 Jul 1993 (Vogt et al. 1994, SPIE 2198). No cost shown."),
    dict(section="Artificial Intelligence: Top 10", group="ai10", kind=CONTENT, title="8: The skills humans need", subtitle="",
         notes="Sketch. Order-of-magnitude thinking; rapid reading with comprehension; reading and creating figures (sketches are fine!)."),
    dict(section="Artificial Intelligence: Top 10", group="ai10", kind=CONTENT, title="9: The AI bubble will pop (with a few major winners)", subtitle="",
         notes="Figure (new, B6): presentations/py/ai_capex.py — Microsoft, Alphabet, Amazon, Meta annual capex 2019-2025 "
               "from 10-K filings + 2026 guidance (Q35a). Source: company 10-K filings."),
    dict(section="Artificial Intelligence: Top 10", group="ai10", kind=CONTENT, title="10: The Eye of Sauron", subtitle="",
         notes="Image: actual Eye of Sauron still (Q17; fair use, credit New Line Cinema). "
               "'Will vaporize many areas of science and academia.'"),

    # --- Close --------------------------------------------------------------
    dict(section="Close", kind=CONTENT, title="Summary", subtitle="",
         notes="SUMMARY — author will write (Q34)."),
]
