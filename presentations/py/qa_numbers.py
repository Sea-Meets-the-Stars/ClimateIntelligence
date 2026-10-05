"""Created by JXP and Claude.

B10 number cross-check: for each headline number shown on a slide, search
context/claudes_context.md and the Q&A of the prompt file for a supporting
string. "context" / "Q&A" = found there; "data" = computed from a cached
dataset by the named script (reproducible, not in the text sources);
"MISSING" = needs a look.

Usage:
    conda run -n ocean14 python presentations/py/qa_numbers.py
"""
import re

from slide_style import ROOT

CONTEXT = (ROOT / "context" / "claudes_context.md").read_text()
QA = (ROOT / "claude_prompts" / "presentations" / "wmko_oct2026.md").read_text()

# (slide, number as shown, regex to find support, or script that computes it)
CLAIMS = [
    ("C1", "CO2 ~430 ppm (2026)", r"4[23]\d ppm", None),
    ("C2", "U.S. 23.5% of cumulative CO2", r"23\.5\s?%", None),
    ("C3a", "imbalance 0.7 W/m² (AR6 Fig 7.2); 0.79 for 2006-2018", r"0\.79 W/m", None),
    ("C3a", "imbalance doubled 0.42 -> 1.12 W/m² (Loeb 2021)", r"doubl", "energy_budget_arrows.py (Loeb et al. 2021)"),
    ("C3a", "~360 TW = 18x human energy use", None, "heat_scale.py"),
    ("C4a", "2024 warmest ocean surface, +0.95 C vs 1901-2000", None, "sst_global.py (NOAA NCEI)"),
    ("C4b", "~39e22 J since late 1950s, 31% below 700 m", r"91\s?%", "ohc_by_depth.py (NOAA NCEI)"),
    ("C5", "1.09 C realized (2011-2020)", r"1\.1[–-]1\.2|1\.09", None),
    ("C5", "ERF 2.72 W/m², ECS 3 C", r"2\.72 W/m", None),
    ("C5", "Murphy committed ~1.7 C", r"1\.7 °C", None),
    ("C5", "sea level 2-3 m (1.5 C) / 2-6 m (2 C) over 2000 yr", None, "AR6 SPM B.5.4 (extracted 2026-10-05)"),
    ("C6a", "satellites 3.2 mm/yr; last decade 3.7 mm/yr", r"3\.7", "gmsl_to_2025.py (NOAA LSA)"),
    ("C6b", "Honolulu +1.6 mm/yr, ~19 cm since 1905", None, "honolulu_tide_gauge.py (NOAA CO-OPS)"),
    ("C7a", "LPI -73%", r"73\s?%", None),
    ("C7a", "mammal mass 60/36/4%", r"Bar-On|biomass", None),
    ("C7b", "477 / 198 extinctions vs 9 expected", r"100[–-]1000|E/MSY", "extinction_rate.py (Ceballos 2015, Table 1)"),
    ("C8", "7 of 9 boundaries transgressed", r"7 of 9|seven of nine", None),
    ("C9a", "peak 10.3 billion in 2084", r"10\.3", None),
    ("C10", "74 / 76 / 65 / >50% (Howard & Sylvan 2021, n=738)", r"74\s?%", None),
    ("4", "CO2 doubling 22 yr; AI compute ~6 months", None, "two_exponentials.py (Blog 001 fits)"),
    ("5", "COVID doubling 2.4 days", None, "covid_slide.py (Blog 001 fit)"),
    ("A2", "uplift 2.53x (Anthropic) and 4.16x (Zhang 2026)", r"2\.53|4\.16", None),
    ("A3", "Mythos 99% unpatched; UK AISI 73%", r"99\s?%", None),
    ("A4", "data centers 4.7% (2024) -> 9.5-15% (2030)", r"4\.7\s?%", None),
    ("A5", "arXiv 9,869 / 20,569 / 40,363 per month", r"40,363", None),
    ("A9", "capex $69B (2019) -> $358B (2025) -> ~$732B (2026 guidance)", None, "ai_capex.py (SEC EDGAR 10-Ks)"),
    ("A7", "HIRES first light 16 Jul 1993", r"16 Jul 1993", None),
]


def main():
    """Created by JXP and Claude. Print the cross-check table."""
    missing = 0
    for slide, claim, pattern, script in CLAIMS:
        where = []
        if pattern and re.search(pattern, CONTEXT):
            where.append("context")
        if pattern and re.search(pattern, QA):
            where.append("Q&A")
        if script:
            where.append(f"data: {script}")
        status = ", ".join(where) if where else "MISSING"
        missing += not where
        print(f"{slide:4s} {claim:58s} {status}")
    print(f"\n{len(CLAIMS)} claims, {missing} without support")


if __name__ == "__main__":
    main()
