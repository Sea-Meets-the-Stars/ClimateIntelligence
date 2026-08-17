"""Created by JXP and Claude.

Estimate the ESSENTIAL LABOR-HOURS PER WEEK required per healthy working-age
US adult to sustain a sufficiency standard of living, split into

    TRADITIONAL      production of essential goods and non-care services
                     (shelter, food, clothing, furniture, water/sanitation,
                     electricity, essential freight, K-12 education) PLUS
                     essential medical care, and
    NON-TRADITIONAL  all care work wherever it occurs (childcare, eldercare,
                     disabled-adult care) and household tasks (cooking,
                     cleaning, laundry, shopping).

Medical care sits in TRADITIONAL by author decision (round 2), alongside the
K-12 carve-out: both are professionalized, credentialed services delivered by a
dedicated workforce rather than the diffuse unpaid care the non-traditional
bucket is meant to capture.

This is a NORMATIVE, NON-MONETARY estimate: it asks how many hours of human
labor a sufficiency standard REQUIRES, not how many hours the current economy
happens to employ, and it counts unpaid work identically to paid work. The
classification principle (settled with the author) is CLASSIFY BY ACTIVITY,
NOT BY WHO PAYS.

Every number carries a LOW / CENTRAL / HIGH column, propagated end-to-end.

--------------------------------------------------------------------------------
METHOD
------
1. Build an idealized STEADY-STATE population from the settled 80-year life
   cycle (below), applied against the real 2026 US population (~343M).
2. The DENOMINATOR is the "working adult" pool: ages 25-59 minus the fraction
   who do not work because of a work-limiting health condition.
3. TRADITIONAL: sum nine per-capita hour-rates (the eight goods/services lines
   plus essential medical care), multiply by TOTAL population.
4. NON-TRADITIONAL: sum the care/household demands over the populations that
   generate them, then SUBTRACT the non-traditional labor CONTRIBUTED by
   Tier-1 active elders (60-70), who are outside the traditional labor pool
   but are net contributors of care and household work.
5. Divide both national totals by the working-adult pool.

Childcare, household tasks and clothing are now NEEDS-BASED bottom-up
derivations (round-2 research passes) rather than behavioral benchmarks or
market-employment allocations; see DATA SOURCES and the RESOLVED notes below.

UNIT-CELL EQUIVALENCE (modeling note)
-------------------------------------
The author framed the model as a household unit cell: 2 working adults plus
their pro-rata share of dependents. Under a steady state that is mathematically
IDENTICAL to national totals divided by the national working population, so we
implement the national-totals form and do not track household lineages. Both
routes give the same hours/week per working adult.

SETTLED LIFE CYCLE (per author Q&A, rounds 1-3) — 80-year lifespan
-------------------------------------------------------------------
  Ages  0-19 (20 yr)  Children. 2 per household. Care recipients (non-school
                      hours); their schooling is TRADITIONAL (K-12 carve-out).
  Ages 20-24  (5 yr)  College students. Not working, not care recipients —
                      simply ABSENT from both sides of the ledger. The
                      disability fraction is deliberately NOT applied here.
  Ages 25-59 (35 yr)  Working. 12.4% have a work-limiting health condition
                      (the broader BLS measure, chosen by the author over the
                      narrower disability-employment-ratio measure), of whom
                      27% still work. So 12.4% x 73% = 9.05% of this band is
                      non-working-disabled: REMOVED from labor supply AND ADDED
                      to care demand at ~1/4 of Tier-3 institutional intensity.
  Ages 60-70 (10 yr)  TIER 1 "active elder". Outside the traditional labor pool
                      (the author's age-60 cutoff on traditional work) but a NET
                      CONTRIBUTOR of non-traditional labor (grandchild care,
                      household help). Also receives light support.
  Ages 70-75  (5 yr)  TIER 2 "frailty transition". Receives light support,
                      contributes no labor.
  Ages 75-80  (5 yr)  TIER 3 "full institutional care". Congregate/nursing-home
                      intensity, contributes no labor. Death at ~80.

SUFFICIENCY STANDARD (settled; already baked into the hour-rates below)
-----------------------------------------------------------------------
~250 sq ft of dwelling per person; ~2,300 kcal/day modest-meat diet, cooked at
home (no restaurant labor); a small DURABLE wardrobe (now made concrete as the
Hot or Cool 103-item, ~4.1-yr-service-life wardrobe); basic-tier medicine;
CFOC-standard child supervision during non-school waking hours.

POPULATION
----------
Total US population 2026 ~ 343,000,000 (Census Vintage 2025: ~341.8M at
mid-2025, extrapolating to ~343-345M in 2026).

The author directed: "use the 2026 population... assume it's steady state for
now." We therefore use the IDEALIZED steady-state age shares implied by the
life cycle (0-19 = 25%, 20-59 = 50%, 60-79 = 25%) applied to the REAL total
head-count. This is close to, but not identical to, the real 2026 age
structure (under-18 ~21.5%, 18-64 ~60.5%, 65+ ~18.0%). The idealized structure
has a somewhat larger child share and a notably larger old-age share than
reality, so it is if anything CONSERVATIVE (it overstates dependency). Accepted
simplification per author Q&A round 2.

Cross-checks: US life expectancy at birth (CDC, 2024) is 79.0 yr, consistent
with the ~80-yr lifespan. US total fertility rate (CDC, 2024) is 1.599 — see
FLAG 3 below.

--------------------------------------------------------------------------------
FLAGS — four of the five round-1 flags are now RESOLVED (author, round 2);
FLAG 3 stands as an accepted limitation; FLAG 6 is newly raised.
--------------------------------------------------------------------------------
FLAG 1  RESOLVED — MEDICAL CARE IS TRADITIONAL. The question was whether
        "classify by activity, not by who pays" forced nursing/doctoring into
        the care bucket. The author ruled in round 2 that essential medical
        care belongs in TRADITIONAL, parallel to the existing K-12 carve-out:
        it is a credentialed, institutionally organized service, not the
        diffuse unpaid care the non-traditional bucket exists to surface. The
        per-capita rate and its derivation (NAICS 621+622 x ~65% essential
        fraction) are UNCHANGED — only the bucket moved, so ~0.95
        hr/capita/week central (~2.4 hr/wk per working adult) shifted from the
        non-traditional column to the traditional one. The total is unaffected.

FLAG 2  RESOLVED — CHILDCARE AND HOUSEHOLD TASKS ARE NOW NEEDS-BASED. Both
        lines got the dedicated bottom-up research pass this flag called for,
        and both placeholders are gone.

        Childcare (2.94 / 5.29 / 7.93 hr/wk per working adult). CFOC (Caring
        for Our Children, the AAP/APHA national child-care health-and-safety
        standards) child:staff ratios by age — 3:1 infants, 4:1 toddlers,
        7:1-8:1 preschool, 10:1-12:1 school-age — applied to AASM-consensus
        waking hours by age, MINUS K-12 in-school hours (6.5 hr/day x 180
        days/yr, ages 5-17, already carried in the traditional K-12 line),
        summed over ages 0-17. That yields ~9.35 adult-hours/week of required
        supervision PER CHILD, scaled by the model's own children-per-
        working-adult ratio (0.5655 = the 18/80 child share divided by the
        0.3979 working-adult share) to a population average. An independent
        ATUS PRIMARY-childcare cross-check lands within 1%. This is about
        ONE THIRD of last round's placeholder (17.85) because that placeholder
        used ATUS SECONDARY childcare — merely having a child in one's care
        while doing something else (leisure, housework) — which a needs-based
        method must exclude as double-counting.

        Household tasks (7.14 / 12.74 / 16.11 hr/wk per working adult). USDA
        Thrifty Food Plan recipe-preparation-time studies (Rose 2007; Davis &
        You 2010-2011) for meal prep, ISSA 540/612 cleaning time-and-motion
        standards plus an independent hotel-housekeeping stopwatch study for
        cleaning, ENERGY STAR/DOE loads-per-week data for laundry, and a
        reasoned grocery/errands estimate. Career-weighted across the ~51.4%
        of a working career spent in a 4-person/1,000-sq-ft household with two
        children at home and the ~48.6% spent in a 2-person/500-sq-ft
        household. This is ~18% HIGHER than last round's placeholder (10.78) —
        the OPPOSITE direction from childcare — because a scratch-cooked,
        restaurant-free sufficiency diet takes more labor than current
        behavior, which is supplemented by restaurants and processed food.
        The two lines together are a good illustration that needs-based and
        ATUS-actual diverge in BOTH directions, not just one.

FLAG 3  OPEN (accepted) — STIPULATED FERTILITY (2 children/household,
        ~replacement) EXCEEDS REALITY (US TFR 1.599, CDC 2024). The model is
        explicitly normative and idealized here, not descriptive. A
        sub-replacement population has fewer children (less childcare) but a
        heavier elder dependency ratio than this steady state — the two
        effects push the answer in opposite directions. Discussed and accepted
        in author Q&A round 2; retained as a stated limitation, not a to-do.

FLAG 4  RESOLVED — CLOTHING IS NOW A BOTTOM-UP SUFFICIENCY WARDROBE. Round 1
        allocated the global garment workforce to US consumption (central 1.70
        hr/capita/wk). Round 2 built the requirement from the garment up: a
        103-item wardrobe per the Hot or Cool Institute's 2022 "1.5-degree
        wardrobe" sufficiency standard (85 four-season garments including
        footwear, plus underwear and socks), a stock-weighted average durable
        service life of ~4.1 years, and all-in labor-hours per garment covering
        fiber production, spinning/weaving, dyeing, cutting, sewing and
        finishing. Result: 0.15 / 0.45 / 1.00 hr/capita/wk — roughly a 4x
        reduction.

        Two findings worth keeping in view. (a) The old 1.70 implicitly assumed
        a ~1.8-year replacement cycle, i.e. it was measuring CURRENT
        fast-fashion THROUGHPUT, not the labor a durable wardrobe requires. It
        is retained as the named comparator CLOTHING_CURRENT_CONSUMPTION_HRWK
        for reporting only, and is NOT used in the model. (b)
        Counterintuitively, wardrobe SIZE barely matters for wear-limited
        garments: the requirement is stock/lifespan, and size largely cancels
        out of that ratio. It is the DURABILITY assumption, not the "small" in
        "small durable wardrobe," that drives the 4x.

        The round-1 asymmetry note still stands: clothing and furniture are
        import-adjusted (~97% of US apparel is imported, so a domestic-only
        BLS figure of ~0.10 hr/capita/wk would understate the requirement by
        more than an order of magnitude), while the other traditional
        categories are domestic-activity figures — so traditional hours remain
        somewhat understated for any category with hidden import content.

FLAG 5  RESOLVED — SCENARIO ALIGNMENT OF THE ELDER LABOR CONTRIBUTION. The
        Tier-1 elder contribution REDUCES the burden, so a coherent LOW
        *burden* column pairs low demand with the HIGH elder contribution.
        The author confirmed this default in round 2 ("this sounds sensible"):
        the columns are OUTCOME scenarios, not parameter columns. The
        parameter-aligned alternative is still printed, for transparency about
        how much the choice is worth.

FLAG 6  NEW, OPEN — THE ELDER CONTRIBUTION IS NOW LARGE RELATIVE TO A SMALLER
        DEMAND SIDE. The round-2 needs-based childcare and household figures
        cut gross non-traditional demand by roughly a third, but the Tier-1
        contribution parameters (5 / 12 / 22 hr/wk) were carried over unchanged
        from round 1. The offset therefore covers ~14% of gross demand at
        CENTRAL but ~43% in the LOW column, where a 60-69-year-old is credited
        with 22 hr/wk of care and household labor while a working adult carries
        only ~9 hr/wk of it. That inversion is at least odd and may mean the
        HIGH elder-contribution parameter needs a cap tied to the demand side.
        Printed in the elder-netting block. Author input welcome.

--------------------------------------------------------------------------------
DATA SOURCES (round-1 passes, updated by the round-2 needs-based passes)
--------------------------------------------------------------------------------
TRADITIONAL (hours per capita per week, whole-population denominator):
  Shelter      BLS Bulletins 1755/1892 construction labor-hours per sq ft;
               building service life 60-130 yr; JCHS paid-repair spend -> hours.
  Food         USDA ERS food-dollar/labor series + BLS CES NAICS 311/424/445,
               adjusted for waste reduction and a modest-meat diet; restaurants
               excluded (not a sufficiency requirement).
  Clothing     Bottom-up sufficiency wardrobe: Hot or Cool Institute (2022),
               "Unfit, Unfair, Unfashionable" 1.5-degree wardrobe standard —
               103 items, ~4.1-yr stock-weighted service life, all-in
               labor-hours per garment from fiber to finishing. See FLAG 4.
               The round-1 ILO global-garment-workforce allocation (central
               1.70) is kept only as a labeled current-consumption comparator.
  Furniture    BLS CES NAICS 337 + 4491 (domestic 0.073); ~60% imported, so the
               import-adjusted embodied figure is higher (HIGH column).
  Water/san.   BLS CES NAICS 2213 + waste management, PLUS Census ASPEP public
               water/sewer/solid-waste FTEs. BLS alone understates ~5x because
               most water utilities are municipal.
  Electricity  BLS CES NAICS 2211 + Census ASPEP public electric FTEs.
  Freight      BLS CES NAICS 484/482/493/492, times an ~50% essential-commodity
               fraction derived from the BTS/FHWA Freight Analysis Framework
               (FAF5.7) commodity split.
  K-12         NCES Digest staff/student ratio (7.3 pupils per staff member,
               ALL staff not just teachers) x NTPS teacher hours (~53 hr/wk).
  Medical      BLS CES NAICS 621 (ambulatory) + 622 (hospitals) only — NAICS
               623 long-term/nursing care is EXCLUDED because it is already
               counted in the eldercare tiers. An ~65% "essential fraction" is
               applied, net of administrative waste and low-value or elective
               care. Classified TRADITIONAL per FLAG 1 (author, round 2).

NON-TRADITIONAL:
  Tier-3 institutional care  CMS Payroll-Based Journal hours per resident day
               (HPRD). LOW 3.48 = the CMS regulatory-floor DIRECT-care figure;
               CENTRAL 5.0 = direct nursing care (3.78 HPRD, solid PBJ data)
               plus care-adjacent support staff (food, laundry, cleaning,
               activities) — a JUDGMENT-CALL BLEND, not a single cited figure;
               HIGH 7.0 approaches all-staff-including-overhead. x7 -> per week.
  Tiers 1-2 light support    Population-average (NOT conditional-on-need)
               hours received per week, from the eldercare research pass.
  Elder labor contributed    AARP grandparent-caregiving survey (510.9 hr/yr
               ~ 9.8 hr/wk among caregiving grandparents, ~52% incidence),
               plus the ATUS 65+ household-activity surplus over the
               working-age baseline (~5 hr/wk), plus unpaid eldercare of peers.
               Population-averaged across the WHOLE 60-70 band.
  Disabled-adult care        Set at ~1/4 of Tier-3 intensity per the author,
               mostly personal assistance rather than skilled nursing.
  Childcare (non-school)     CFOC / Caring for Our Children (AAP + APHA + HRSA
               MCHB), 4th ed., child:staff ratios by age band; AASM consensus
               sleep-duration recommendations by age (to get waking hours);
               NCES/state K-12 instructional-time norms for the school-hours
               subtraction. Cross-checked against ATUS PRIMARY childcare
               (within 1%). Needs-based, NOT a behavioral benchmark. FLAG 2.
  Household tasks            USDA Thrifty Food Plan preparation-time research
               (Rose, "Food Stamps, the Thrifty Food Plan, and meal
               preparation: the importance of the time dimension," J. Nutr.
               Educ. Behav. 2007; Davis & You, USDA ERS / Public Health Nutr.
               2010-2011 time-cost-of-TFP work) for meal prep; ISSA 540/612
               cleaning-times standards plus a published hotel-housekeeping
               time-and-motion study for cleaning; ENERGY STAR / DOE appliance
               data for laundry loads per week. Career-weighted over household
               composition. Needs-based. FLAG 2.

Run under the project conda environment:
    conda run -n ocean14 python CI_Reports/work_hours_needed.py
"""

# Imports at the top of the file (project coding guideline).
# No third-party dependencies: this is transparent arithmetic by design.
from math import isclose

# ----------------------------------------------------------------------------
# Scenario machinery.  Per CLAUDE.md ("use methods, not classes") we use plain
# dicts keyed by scenario name rather than dataclasses.
# ----------------------------------------------------------------------------
SCENARIOS = ("LOW", "CENTRAL", "HIGH")

# ----------------------------------------------------------------------------
# Population and life-cycle constants.
# ----------------------------------------------------------------------------
TOTAL_POP = 343_000_000       # US, 2026 (Census Vintage 2025 extrapolated)
LIFESPAN = 80                 # years, settled steady-state life cycle

# (label, start_age, end_age) — half-open [start, end), spanning 0..80.
AGE_BANDS = (
    ("children_0_19", 0, 20),
    ("students_20_24", 20, 25),
    ("adults_25_59", 25, 60),
    ("tier1_60_69", 60, 70),
    ("tier2_70_74", 70, 75),
    ("tier3_75_79", 75, 80),
)

# Work-limiting health condition, ages 25-59 only (BLS broader measure).
WORK_LIMIT_PREVALENCE = 0.124   # share of 25-59 with a work-limiting condition
WORK_LIMIT_STILL_WORK = 0.27    # of those, share who nonetheless work
# => non-working-disabled share of the 25-59 band:
DISABLED_NONWORKING_FRAC = WORK_LIMIT_PREVALENCE * (1.0 - WORK_LIMIT_STILL_WORK)

# Real 2026 age structure, for the printed cross-check only.
REAL_SHARE_UNDER_18 = 0.215
REAL_SHARE_18_64 = 0.605
REAL_SHARE_65_PLUS = 0.180

# Other context anchors.
LIFE_EXPECTANCY_2024 = 79.0     # CDC
TFR_2024 = 1.599                # CDC; model stipulates ~2.0 — see FLAG 3

# ----------------------------------------------------------------------------
# TRADITIONAL hour-rates: hours per capita per week, WHOLE-POPULATION denominator.
# ----------------------------------------------------------------------------
TRADITIONAL_RATES = {
    "Shelter (build+materials+maint)": {"LOW": 0.087, "CENTRAL": 0.134, "HIGH": 0.271},
    "Food (farm+process+distribute)":  {"LOW": 0.500, "CENTRAL": 0.630, "HIGH": 0.760},
    # Clothing: bottom-up sufficiency wardrobe (Hot or Cool Institute 2022
    # 1.5-degree standard, 103 items, ~4.1-yr stock-weighted service life,
    # all-in labor from fiber through finishing).  ~4x below the round-1
    # market-allocation figure; see CLOTHING_CURRENT_CONSUMPTION_HRWK and FLAG 4.
    "Clothing (sufficiency wardrobe, embodied)": {"LOW": 0.150, "CENTRAL": 0.450, "HIGH": 1.000},
    "Furniture (import-adjusted)":     {"LOW": 0.038, "CENTRAL": 0.100, "HIGH": 0.160},
    "Water / sanitation":              {"LOW": 0.043, "CENTRAL": 0.083, "HIGH": 0.120},
    "Electricity":                     {"LOW": 0.054, "CENTRAL": 0.063, "HIGH": 0.064},
    "Freight (essential goods only)":  {"LOW": 0.162, "CENTRAL": 0.263, "HIGH": 0.401},
    "K-12 education (all staff)":      {"LOW": 0.549, "CENTRAL": 0.633, "HIGH": 0.814},
}

# Round-1 clothing figure: the ILO global-garment-workforce allocation to US
# consumption.  It implicitly encodes a ~1.8-yr garment replacement cycle, i.e.
# it measures CURRENT US fast-fashion THROUGHPUT rather than the labor a durable
# sufficiency wardrobe requires.  Kept for side-by-side reporting only —
# NOT used in the model.  (Note: wardrobe SIZE turns out to matter little for
# wear-limited garments, since the requirement is stock/lifespan and size
# largely cancels; DURABILITY is what drives the ~4x gap.)
CLOTHING_CURRENT_CONSUMPTION_HRWK = {"LOW": 0.690, "CENTRAL": 1.700, "HIGH": 3.230}

# ----------------------------------------------------------------------------
# NON-TRADITIONAL hour-rates.
# ----------------------------------------------------------------------------

# Tier-3 institutional care: hours RECEIVED per resident-DAY (CMS PBJ, HPRD).
TIER3_HPRD = {"LOW": 3.48, "CENTRAL": 5.00, "HIGH": 7.00}

# Light support RECEIVED, hours/week, population-average over the whole band.
TIER1_SUPPORT_HRWK = {"LOW": 1.5, "CENTRAL": 3.5, "HIGH": 8.0}
TIER2_SUPPORT_HRWK = {"LOW": 7.0, "CENTRAL": 14.0, "HIGH": 25.0}

# Non-traditional labor CONTRIBUTED by Tier-1 active elders, hours/week,
# population-averaged across the whole 60-70 band (not just active grandparents).
TIER1_CONTRIB_HRWK = {"LOW": 5.0, "CENTRAL": 12.0, "HIGH": 22.0}

# Non-working disabled adults: care intensity ~1/4 of Tier-3, hours/week each.
DISABLED_CARE_INTENSITY = 0.25   # of Tier-3 weekly receive-rate

# Essential medical care (NAICS 621+622, ~65% essential fraction), hours per
# capita per week on the WHOLE-POPULATION denominator.  Classified TRADITIONAL
# per the author's round-2 decision (FLAG 1); the rate itself is unchanged.
MEDICAL_RATES = {"LOW": 0.73, "CENTRAL": 0.95, "HIGH": 1.25}

# --- NEEDS-BASED care and household rates (round-2 research, FLAG 2) --------
# Both dicts are ALREADY hours per week per WORKING ADULT (population- and
# career-averaged), so no incidence arithmetic happens in this module.
#
# Childcare, non-school hours.  CFOC (AAP/APHA) child:staff ratios by age
# applied to AASM-consensus waking hours, minus K-12 in-school hours
# (6.5 hr/day x 180 days/yr, ages 5-17, already in the traditional K-12 line),
# summed over ages 0-17 -> ~9.35 adult-hours/wk of required supervision PER
# CHILD, x 0.5655 children per working adult (the 18/80 child share divided by
# the 0.3979 working-adult share of this model's own steady state).
# Corroborated within 1% by an ATUS PRIMARY-childcare cross-check.  Note this
# is ~1/3 of last round's placeholder (17.85), which used ATUS SECONDARY
# childcare — supervision while doing something else — and so double-counted.
# (Minor conservatism: the per-child sum runs 0-17 while the model's child band
# is 0-19, so the population average is if anything slightly understated.)
CHILDCARE_NEEDS_HRWK = {"LOW": 2.94, "CENTRAL": 5.29, "HIGH": 7.93}

# Household tasks: cooking, cleaning, laundry, shopping.  EXCLUDES dwelling
# maintenance and lawn/garden, which remain in the shelter category.  USDA
# Thrifty Food Plan preparation-time research (Rose 2007; Davis & You 2010-11)
# for meal prep (16.1 hr/wk for a family of four on a scratch-cooked sufficiency
# diet, since the food category excludes restaurants), ISSA 540/612 cleaning
# time-and-motion standards plus a hotel-housekeeping stopwatch study for
# cleaning, ENERGY STAR/DOE loads-per-week for laundry, and a reasoned
# grocery/errands estimate.  Career-weighted over the ~51.4% of a working career
# in a 4-person/1,000-sq-ft household and the ~48.6% in a 2-person/500-sq-ft one.
# CONTRAST WORTH NOTING: this runs ~18% ABOVE last round's ATUS placeholder
# (10.78), the opposite direction from childcare, because a genuinely
# scratch-cooked, restaurant-free diet takes MORE labor than current behavior —
# needs-based estimates diverge from ATUS-actual in both directions.
HOUSEHOLD_NEEDS_HRWK = {"LOW": 7.14, "CENTRAL": 12.74, "HIGH": 16.11}

# By default, treat the columns as OUTCOME scenarios: the LOW-burden column
# pairs low demand with the HIGH elder contribution (see FLAG 5).
INVERT_ELDER_CONTRIBUTION = True

HOURS_PER_DAY_TO_WEEK = 7.0


def opposite_scenario(scenario):
    """Created by JXP and Claude.

    Map a scenario to its opposite, used for terms that REDUCE the burden.

    Inputs
    ------
    scenario : str
        One of 'LOW', 'CENTRAL', 'HIGH'.

    Outputs
    -------
    str
        'HIGH' for 'LOW', 'LOW' for 'HIGH', 'CENTRAL' for 'CENTRAL'.
    """
    return {"LOW": "HIGH", "CENTRAL": "CENTRAL", "HIGH": "LOW"}[scenario]


def population_breakdown(total_pop=TOTAL_POP):
    """Created by JXP and Claude.

    Build the idealized steady-state population by life-cycle band.

    Under a steady state with a fixed 80-year lifespan and a stationary birth
    cohort, every single year of age holds total_pop / 80 people, so a band's
    share is simply (its width in years) / 80.  The 25-59 band is then split
    into working adults and non-working disabled adults.

    Inputs
    ------
    total_pop : float
        Total population head-count (default: the real 2026 US figure).

    Outputs
    -------
    dict
        Keys: the six band labels, plus 'working_adults',
        'disabled_nonworking', 'total'.  Values are head-counts (floats).
    """
    per_year = total_pop / LIFESPAN
    pops = {label: per_year * (end - start) for label, start, end in AGE_BANDS}

    band_25_59 = pops["adults_25_59"]
    pops["disabled_nonworking"] = band_25_59 * DISABLED_NONWORKING_FRAC
    pops["working_adults"] = band_25_59 * (1.0 - DISABLED_NONWORKING_FRAC)
    pops["total"] = total_pop

    # Sanity check: the six bands must reconstitute the total.
    band_sum = sum(pops[label] for label, _, _ in AGE_BANDS)
    assert isclose(band_sum, total_pop, rel_tol=1e-9), "age bands do not sum to total"
    return pops


def traditional_national_hours(pops, scenario):
    """Created by JXP and Claude.

    National weekly TRADITIONAL labor hours, by category.

    Each traditional rate is expressed per capita of the WHOLE population, so
    the national requirement is simply rate x total population.

    Inputs
    ------
    pops : dict
        Output of population_breakdown().
    scenario : str
        'LOW', 'CENTRAL' or 'HIGH'.

    Outputs
    -------
    dict
        Category name -> national hours per week (float).
    """
    return {name: rates[scenario] * pops["total"]
            for name, rates in TRADITIONAL_RATES.items()}


def nontraditional_national_hours(pops, scenario,
                                  invert_elder=INVERT_ELDER_CONTRIBUTION,
                                  medical_is_nontraditional=False):
    """Created by JXP and Claude.

    National weekly NON-TRADITIONAL labor hours, by category.

    Demand terms are positive; the Tier-1 active-elder labor CONTRIBUTION is a
    NEGATIVE entry, because those hours are supplied from outside the
    working-adult pool and therefore reduce the burden that pool must carry.

    Inputs
    ------
    pops : dict
        Output of population_breakdown().
    scenario : str
        'LOW', 'CENTRAL' or 'HIGH'.
    invert_elder : bool
        If True, the elder contribution uses the OPPOSITE scenario, so that a
        LOW-burden column pairs low demand with a high offset (FLAG 5).
    medical_is_nontraditional : bool
        Default False: essential medical care is TRADITIONAL per the author's
        round-2 decision (FLAG 1). Set True only to reproduce the round-1
        classification.

    Outputs
    -------
    dict
        Category name -> national hours per week (float; the elder-contribution
        entry is negative).
    """
    out = {}

    # --- Demand generated by the working adults' own households -------------
    # CHILDCARE_NEEDS_HRWK / HOUSEHOLD_NEEDS_HRWK are already per WORKING ADULT,
    # so multiplying by the working-adult pool here (and dividing by it again in
    # hours_per_working_adult()) is numerically a no-op.  It is kept deliberately
    # so every category flows to the printed table by the same national-hours
    # route, with no special-cased path.
    out["Childcare (non-school, needs-based)"] = (
        CHILDCARE_NEEDS_HRWK[scenario] * pops["working_adults"])
    out["Household tasks (needs-based)"] = (
        HOUSEHOLD_NEEDS_HRWK[scenario] * pops["working_adults"])

    # --- Elder care demand, by tier -----------------------------------------
    out["Tier-1 elder light support (60-69)"] = (
        TIER1_SUPPORT_HRWK[scenario] * pops["tier1_60_69"])
    out["Tier-2 elder support (70-74)"] = (
        TIER2_SUPPORT_HRWK[scenario] * pops["tier2_70_74"])
    out["Tier-3 institutional care (75-79)"] = (
        TIER3_HPRD[scenario] * HOURS_PER_DAY_TO_WEEK * pops["tier3_75_79"])

    # --- Non-working disabled adults, ~1/4 of Tier-3 intensity --------------
    disabled_hrwk = (TIER3_HPRD[scenario] * HOURS_PER_DAY_TO_WEEK
                     * DISABLED_CARE_INTENSITY)
    out["Disabled-adult care (25-59)"] = disabled_hrwk * pops["disabled_nonworking"]

    # --- Essential medical care, whole-population rate ----------------------
    # Normally SKIPPED: medical care is traditional (FLAG 1, resolved).
    if medical_is_nontraditional:
        out["Essential medical care"] = MEDICAL_RATES[scenario] * pops["total"]

    # --- Labor SUPPLIED by Tier-1 active elders (negative) ------------------
    contrib_scenario = opposite_scenario(scenario) if invert_elder else scenario
    out["LESS: Tier-1 elder labor contributed"] = (
        -TIER1_CONTRIB_HRWK[contrib_scenario] * pops["tier1_60_69"])

    return out


def hours_per_working_adult(national_hours, pops):
    """Created by JXP and Claude.

    Convert a national weekly hour total into hours per working adult.

    Inputs
    ------
    national_hours : float
        National labor hours required per week.
    pops : dict
        Output of population_breakdown().

    Outputs
    -------
    float
        Hours per week per healthy working-age adult.
    """
    return national_hours / pops["working_adults"]


def compute_all(pops, invert_elder=INVERT_ELDER_CONTRIBUTION,
                medical_is_nontraditional=False):
    """Created by JXP and Claude.

    Run the full calculation for every scenario column.

    Inputs
    ------
    pops : dict
        Output of population_breakdown().
    invert_elder : bool
        Passed through to nontraditional_national_hours() (FLAG 5).
    medical_is_nontraditional : bool
        Default False: medical care sits in the TRADITIONAL bucket (FLAG 1,
        resolved by the author in round 2). True reproduces the round-1
        classification; the bucket changes but the total never does.

    Outputs
    -------
    dict
        scenario -> dict with keys 'trad_detail', 'nontrad_detail',
        'trad_national', 'nontrad_national', 'trad_pwa', 'nontrad_pwa',
        'total_pwa'.
    """
    results = {}
    for scenario in SCENARIOS:
        trad = traditional_national_hours(pops, scenario)
        nontrad = nontraditional_national_hours(
            pops, scenario, invert_elder=invert_elder,
            medical_is_nontraditional=medical_is_nontraditional)

        if not medical_is_nontraditional:
            # Default path: medical care is a TRADITIONAL line (FLAG 1).
            trad = dict(trad)
            trad["Essential medical care"] = MEDICAL_RATES[scenario] * pops["total"]

        trad_national = sum(trad.values())
        nontrad_national = sum(nontrad.values())
        trad_pwa = hours_per_working_adult(trad_national, pops)
        nontrad_pwa = hours_per_working_adult(nontrad_national, pops)

        results[scenario] = {
            "trad_detail": trad,
            "nontrad_detail": nontrad,
            "trad_national": trad_national,
            "nontrad_national": nontrad_national,
            "trad_pwa": trad_pwa,
            "nontrad_pwa": nontrad_pwa,
            "total_pwa": trad_pwa + nontrad_pwa,
        }
    return results


def bhr(x):
    """Created by JXP and Claude.

    Format a national weekly hour total in billions of hours.

    Inputs
    ------
    x : float
        Hours per week.

    Outputs
    -------
    str
        e.g. '1.24B'.
    """
    return f"{x / 1e9:6.3f}B"


def print_population(pops):
    """Created by JXP and Claude.

    Print the steady-state population breakdown and the reality cross-check.

    Inputs
    ------
    pops : dict
        Output of population_breakdown().

    Outputs
    -------
    None. Prints to stdout.
    """
    print("STEADY-STATE POPULATION (idealized 80-yr life cycle, real 2026 total)")
    print("-" * 78)
    labels = {
        "children_0_19":  "Children 0-19 (care recipients + K-12)",
        "students_20_24": "Students 20-24 (absent from both sides)",
        "adults_25_59":   "Adults 25-59 (labor-age band)",
        "tier1_60_69":    "Tier 1, 60-69 (net labor CONTRIBUTOR)",
        "tier2_70_74":    "Tier 2, 70-74 (light support)",
        "tier3_75_79":    "Tier 3, 75-79 (institutional care)",
    }
    for key, _, _ in AGE_BANDS:
        n = pops[key]
        print(f"  {labels[key]:42s} {n/1e6:7.2f}M  ({100*n/pops['total']:5.2f}%)")
    print()
    print(f"  of the 25-59 band, non-working disabled "
          f"({100*DISABLED_NONWORKING_FRAC:.2f}% = {100*WORK_LIMIT_PREVALENCE:.1f}%"
          f" x {100*(1-WORK_LIMIT_STILL_WORK):.0f}%):")
    print(f"      non-working disabled  {pops['disabled_nonworking']/1e6:7.2f}M"
          "   -> removed from labor, added to care demand")
    print(f"  >>> WORKING ADULTS (the denominator)  {pops['working_adults']/1e6:7.2f}M"
          f"  ({100*pops['working_adults']/pops['total']:5.2f}% of total pop)")
    print()
    print("  Cross-check vs the REAL 2026 age structure (accepted simplification):")
    print(f"    idealized  under-20 {100*pops['children_0_19']/pops['total']:4.1f}% | "
          f"20-59 {100*(pops['students_20_24']+pops['adults_25_59'])/pops['total']:4.1f}% | "
          f"60+ {100*(pops['tier1_60_69']+pops['tier2_70_74']+pops['tier3_75_79'])/pops['total']:4.1f}%")
    print(f"    real       under-18 {100*REAL_SHARE_UNDER_18:4.1f}% | "
          f"18-64 {100*REAL_SHARE_18_64:4.1f}% | "
          f"65+ {100*REAL_SHARE_65_PLUS:4.1f}%")
    print(f"    (life expectancy {LIFE_EXPECTANCY_2024} yr vs {LIFESPAN}-yr model; "
          f"TFR {TFR_2024} vs stipulated 2.0 — FLAG 3)")
    print()


def print_detail_table(title, detail_by_scenario, pops):
    """Created by JXP and Claude.

    Print a category breakdown as hours/week per working adult, LOW/CENTRAL/HIGH.

    Inputs
    ------
    title : str
        Section heading.
    detail_by_scenario : dict
        scenario -> {category: national hours/week}.
    pops : dict
        Output of population_breakdown().

    Outputs
    -------
    None. Prints to stdout.
    """
    print(title)
    print("-" * 78)
    print(f"  {'category':44s} {'LOW':>10s} {'CENTRAL':>10s} {'HIGH':>10s}")
    categories = list(detail_by_scenario["CENTRAL"].keys())
    for cat in categories:
        vals = [hours_per_working_adult(detail_by_scenario[s][cat], pops)
                for s in SCENARIOS]
        print(f"  {cat:44s} {vals[0]:10.2f} {vals[1]:10.2f} {vals[2]:10.2f}")
    totals = [sum(detail_by_scenario[s].values()) / pops["working_adults"]
              for s in SCENARIOS]
    print(f"  {'':44s} {'-'*10} {'-'*10} {'-'*10}")
    print(f"  {'SUBTOTAL (hr/wk per working adult)':44s} "
          f"{totals[0]:10.2f} {totals[1]:10.2f} {totals[2]:10.2f}")
    print()


def main():
    """Created by JXP and Claude.

    Print the full estimate: population, category breakdowns, headline numbers,
    the clothing sufficiency-vs-current comparison, and the FLAG 5 transparency
    sensitivity.

    Inputs
    ------
    (none)

    Outputs
    -------
    None. Prints to stdout.
    """
    print("=" * 78)
    print("ESSENTIAL LABOR-HOURS PER WEEK PER WORKING-AGE US ADULT")
    print("Normative, non-monetary sufficiency model — LOW / CENTRAL / HIGH")
    print("=" * 78)
    print()

    pops = population_breakdown()
    print_population(pops)

    results = compute_all(pops)

    print("  Note: medical care is classified TRADITIONAL per author decision, "
          "round 2 (FLAG 1).")
    print()

    print_detail_table(
        "TRADITIONAL — essential goods, non-care services, medical care",
        {s: results[s]["trad_detail"] for s in SCENARIOS}, pops)

    print_detail_table(
        "NON-TRADITIONAL — care work and household tasks "
        "(elder contribution is NEGATIVE)",
        {s: results[s]["nontrad_detail"] for s in SCENARIOS}, pops)

    # ---- Headline ----------------------------------------------------------
    print("=" * 78)
    print("HEADLINE — hours per week per healthy working-age adult")
    print("=" * 78)
    print(f"  {'':22s} {'LOW':>10s} {'CENTRAL':>10s} {'HIGH':>10s}")
    for label, key in (("TRADITIONAL", "trad_pwa"),
                       ("NON-TRADITIONAL", "nontrad_pwa"),
                       ("TOTAL", "total_pwa")):
        v = [results[s][key] for s in SCENARIOS]
        print(f"  {label:22s} {v[0]:10.1f} {v[1]:10.1f} {v[2]:10.1f}")
    print()
    c = results["CENTRAL"]
    print(f"  CENTRAL reads: {c['trad_pwa']:.1f} hr traditional + "
          f"{c['nontrad_pwa']:.1f} hr non-traditional = "
          f"{c['total_pwa']:.1f} hr/week per working adult")
    print(f"  ({c['total_pwa']/5:.1f} hr/day on a 5-day week; "
          f"{c['total_pwa']/7:.1f} hr/day spread over 7)")
    print()

    # ---- National totals ---------------------------------------------------
    print("NATIONAL WEEKLY HOUR TOTALS (billions of hours/week)")
    print("-" * 78)
    print(f"  {'':22s} {'LOW':>10s} {'CENTRAL':>10s} {'HIGH':>10s}")
    for label, key in (("Traditional", "trad_national"),
                       ("Non-traditional", "nontrad_national")):
        v = [results[s][key] for s in SCENARIOS]
        print(f"  {label:22s} {bhr(v[0]):>10s} {bhr(v[1]):>10s} {bhr(v[2]):>10s}")
    print()

    # ---- Elder-contribution arithmetic, shown explicitly -------------------
    print("ELDER LABOR NETTING (shown explicitly, per the model spec)")
    print("-" * 78)
    for s in SCENARIOS:
        det = results[s]["nontrad_detail"]
        contrib = -det["LESS: Tier-1 elder labor contributed"]
        gross = sum(v for v in det.values() if v > 0)
        net = gross - contrib
        print(f"  [{s:7s}] gross demand {bhr(gross)}  - elder supply {bhr(contrib)}"
              f"  = net {bhr(net)}   "
              f"({hours_per_working_adult(net, pops):5.1f} hr/wk per working adult)"
              f"   elders cover {100*contrib/gross:4.1f}%")
    print("  The offset share now varies sharply across columns because the "
          "round-2\n  needs-based demand side is ~1/3 smaller than the round-1 "
          "placeholders while\n  the elder-contribution parameters are unchanged. "
          "In the LOW column a\n  Tier-1 elder is credited with more weekly "
          "non-traditional labor "
          f"({TIER1_CONTRIB_HRWK['HIGH']:.0f} hr)\n  than a working adult carries "
          f"in total ({results['LOW']['nontrad_pwa']:.1f} hr) — worth a look.")
    print()

    # ---- FLAG 4: sufficiency wardrobe vs current consumption ---------------
    print("CLOTHING, FLAG 4 — sufficiency/durability standard vs current US "
          "consumption")
    print("-" * 78)
    suff = TRADITIONAL_RATES["Clothing (sufficiency wardrobe, embodied)"]
    curr = CLOTHING_CURRENT_CONSUMPTION_HRWK
    print(f"  {'hr/capita/wk':30s} {'LOW':>10s} {'CENTRAL':>10s} {'HIGH':>10s}")
    print(f"  {'sufficiency wardrobe (USED)':30s} "
          f"{suff['LOW']:10.2f} {suff['CENTRAL']:10.2f} {suff['HIGH']:10.2f}")
    print(f"  {'current consumption (ref only)':30s} "
          f"{curr['LOW']:10.2f} {curr['CENTRAL']:10.2f} {curr['HIGH']:10.2f}")
    print(f"  Current US clothing consumption would cost ~{curr['CENTRAL']:.2f} "
          f"hr/wk per capita;\n  the sufficiency/durability standard costs "
          f"~{suff['CENTRAL']:.2f} hr/wk — a "
          f"{curr['CENTRAL']/suff['CENTRAL']:.1f}x difference.")
    print("  The old figure implied a ~1.8-yr replacement cycle: it measured "
          "fast-fashion\n  THROUGHPUT, not the labor a durable wardrobe needs.")
    print("  Wardrobe SIZE barely matters for wear-limited garments (stock/lifespan,"
          "\n  and size largely cancels); DURABILITY drives the whole gap.")
    print()

    # ---- FLAG 5: elder-contribution alignment (author-confirmed default) ---
    print("ELDER-CONTRIBUTION ALIGNMENT, FLAG 5 — kept for transparency")
    print("-" * 78)
    alt5 = compute_all(pops, invert_elder=False)
    print(f"  {'':22s} {'LOW':>10s} {'CENTRAL':>10s} {'HIGH':>10s}")
    v = [alt5[s]["total_pwa"] for s in SCENARIOS]
    print(f"  {'TOTAL':22s} {v[0]:10.1f} {v[1]:10.1f} {v[2]:10.1f}")
    print("  This is the parameter-aligned variant (elder supply follows the "
          "column).\n  The author confirmed the default, which INVERTS it so LOW "
          "is a genuine\n  low-burden bound. Shown only so the size of the choice "
          "is visible.")
    print()

    # ---- FLAG 2: the two needs-based care/household lines, in proportion ---
    det = results["CENTRAL"]["nontrad_detail"]
    nb = (det["Childcare (non-school, needs-based)"]
          + det["Household tasks (needs-based)"])
    gross = sum(x for x in det.values() if x > 0)
    print("CARE + HOUSEHOLD SCALE CHECK, FLAG 2 — now needs-based, not placeholder")
    print("-" * 78)
    print(f"  Childcare + household tasks are {100*nb/gross:.1f}% of gross "
          f"non-traditional demand\n  and "
          f"{100*nb/(gross + results['CENTRAL']['trad_national']):.1f}% of ALL "
          f"gross demand at CENTRAL. They still dominate the\n  headline, but "
          f"they are now bottom-up needs-based derivations (CFOC/AASM\n  "
          f"ratios; USDA TFP prep-time and ISSA cleaning standards) rather than "
          f"raw\n  ATUS behavior — and they moved in OPPOSITE directions from "
          f"the placeholders:\n  childcare down ~3x (secondary-childcare "
          f"double-counting removed), household\n  tasks up ~18% (a "
          f"scratch-cooked, restaurant-free diet costs real labor).")
    print()
    print("See the module docstring for FLAGS 1-6 and full source citations.")
    print("  FLAGS 1, 2, 4, 5 resolved in round 2. FLAG 3 accepted as a stated")
    print("  limitation. FLAG 6 (elder-contribution scale) is newly open.")


if __name__ == "__main__":
    main()
