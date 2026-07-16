"""Created by JXP and Claude.

Estimate the annual cost to house every homeless person in the United States,
built from the data gathered for the Climate Intelligence homelessness section
(CI report Section 7; context claudes_context.md Section 11).

The estimate is a transparent bottom-up model with an explicit LOW / CENTRAL /
HIGH range. It is intentionally simple so every assumption is visible and
auditable — per the project rule that calculations live in a reusable script,
not inline.

--------------------------------------------------------------------------------
REVISION 2 (2026-07-13): rebuilt in response to a quantitative critique
(A. Thayer, `Rebuttals/thayer_2026jul12.txt`). Five changes, each mapped to a
critique point:

  (1) "Housing vs services are different questions." TRUE. We now separate the
      HOUSING-SUBSIDY-ONLY cost (a rent voucher; Denver's was ~$11k/yr) from the
      HOUSING-PLUS-SERVICES cost. The narrow question "put a roof over everyone"
      is answered by the housing-only figure; the services are what buy the
      RETENTION and the cost-offsets, so we report both and label them.
  (2) "You assume linear scaling; marginal costs rise." PARTLY TRUE. We cannot
      model the true marginal-cost curve, so we (a) label the estimate as a cost
      AT CURRENT AVERAGE RATES — a floor — and (b) add a marginal-cost stress
      multiplier the reader can dial.
  (3) "You assume the population is fixed; people respond to incentives." PARTLY
      TRUE. We add an ANNUAL-FLOW population scenario (~1.25M who use shelter
      over a year, vs the 771k single-night count) as an upper population bound,
      which also proxies induced take-up. Targeting (vulnerability indices) and
      the stigma/"trapped" evidence bound how large induced demand can be.
  (4) "This excludes the cost of BUILDING housing." TRUE and important — the
      binding constraint is units, not vouchers. We now add a CAPITAL cost line:
      units-to-build x per-unit development cost, one-time and amortized.
  (5) "You divided ~$9B by 350M; use taxpayers." FAIR. We report the per-capita
      cost against three denominators: all residents, working-age adults, and
      federal income-tax payers.
--------------------------------------------------------------------------------

METHOD (operating cost)
-----------------------
Split the homeless population into two groups needing two evidence-based
interventions, cost each, sum, then (for the services-inclusive variant) net out
the public-service savings supportive housing is documented to generate.

  * Chronic homeless      -> Permanent Supportive Housing (PSH): rent subsidy
                             (~$11k/yr) PLUS intensive services. RCT-tested
                             (Denver SIB; Canada At Home/Chez Soi).
  * Everyone else         -> Rapid Re-Housing (RRH): time-limited rent + light
                             case management. Most homelessness is brief.

DATA / ANCHORS (see the report references)
------------------------------------------
  * PIT population: HUD AHAR Part 1 — 771,480 (Jan 2024). Annual-flow: ~1.25M
    experience sheltered homelessness over 12 months (HUD AHAR Part 2).
  * Chronically homeless individuals: 152,585 (HUD 2024).
  * Housing-subsidy-only: ~$11,000/person-yr (Denver housing assistance payment
    ~$10,950; a scattered-site rent voucher). RRH is already mostly rent (~$8,500).
  * Services add-on (chronic): ~$9,000 (Denver CCH) to ~$25,000 (high-needs
    provider) per person-yr; central ~$14,000 -> PSH all-in $20k-36k, central $25k.
  * Offset (services-inclusive, chronic only): ~40/50/60% of PSH cost via avoided
    jail/ER/shelter/detox (Denver ~$7k/person-yr).
  * Construction: affordable/PSH development cost ~$200k/unit (national, lower-cost)
    to ~$550k/unit (California); central ~$350k. Amortized over 30 years.

Run under the project conda environment:
    conda run -n ocean14 python CI_Reports/cost_to_house_homeless.py
"""

# Imports at the top of the file (project coding guideline).
from dataclasses import dataclass


@dataclass
class Scenario:
    """Created by JXP and Claude.

    One column of operating-cost assumptions (LOW / CENTRAL / HIGH).

    Fields
    ------
    name : str
    psh_housing : float     # housing-subsidy-only $/person-yr, chronic (PSH)
    psh_services : float    # services add-on $/person-yr, chronic
    rrh_cost : float        # RRH $/person-yr (mostly rent)
    offset_frac : float     # fraction of full PSH cost offset by avoided services
    marginal_mult : float   # scale-up marginal-cost multiplier (>=1); crit. (2)
    """
    name: str
    psh_housing: float
    psh_services: float
    rrh_cost: float
    offset_frac: float
    marginal_mult: float


# Populations (HUD AHAR).
PIT_2024 = 771_480          # single-night count
CHRONIC_2024 = 152_585      # chronically homeless individuals
ANNUAL_FLOW = 1_250_000     # ~people using shelter over 12 months (AHAR Part 2)

# Construction / capital assumptions (crit. 4).
PER_UNIT_LOW = 200_000      # national, lower-cost markets
PER_UNIT_CENTRAL = 350_000
PER_UNIT_HIGH = 550_000     # California / high-cost metros
AMORT_YEARS = 30

# Denominators for per-person context (crit. 5).
DENOM_ALL = 340_000_000
DENOM_WORKING_AGE = 200_000_000     # ~adults 18-65
DENOM_TAXPAYERS = 115_000_000       # ~filers with positive federal income tax

SCENARIOS = [
    # marginal_mult rises with the scenario to reflect increasing marginal cost.
    Scenario("LOW", psh_housing=11_000, psh_services=9_000, rrh_cost=8_500,
             offset_frac=0.60, marginal_mult=1.00),
    Scenario("CENTRAL", psh_housing=11_000, psh_services=14_000, rrh_cost=12_000,
             offset_frac=0.50, marginal_mult=1.15),
    Scenario("HIGH", psh_housing=11_000, psh_services=25_000, rrh_cost=17_000,
             offset_frac=0.40, marginal_mult=1.35),
]


def operating_cost(total_pit, chronic, sc, housing_only):
    """Created by JXP and Claude.

    Compute annual operating cost for one scenario.

    Inputs
    ------
    total_pit : int
        Population to house (PIT single-night, or annual-flow).
    chronic : int
        Chronically homeless (get PSH); rest get RRH.
    sc : Scenario
        Assumption column.
    housing_only : bool
        If True, count only the rent subsidy (no services, no offset) — the
        narrow "put a roof over everyone" question (crit. 1).

    Outputs
    -------
    dict with gross, offset, net (USD/year).
    """
    non_chronic = max(total_pit - chronic, 0)
    if housing_only:
        psh_pp = sc.psh_housing
    else:
        psh_pp = sc.psh_housing + sc.psh_services
    psh_total = chronic * psh_pp
    rrh_total = non_chronic * sc.rrh_cost
    gross = (psh_total + rrh_total) * sc.marginal_mult
    # Offsets accrue to the full supportive-housing package, not a bare voucher.
    offset = 0.0 if housing_only else chronic * psh_pp * sc.offset_frac * sc.marginal_mult
    return {"gross": gross, "offset": offset, "net": gross - offset}


def capital_cost(units, per_unit):
    """Created by JXP and Claude.

    One-time and amortized capital cost of building `units` new units.

    Inputs
    ------
    units : int
    per_unit : float   # development cost per unit (USD)

    Outputs
    -------
    (float, float)  one_time_total, annual_amortized (straight-line over 30 yr).
    """
    one_time = units * per_unit
    return one_time, one_time / AMORT_YEARS


def bn(x):
    """Created by JXP and Claude.

    Format a dollar amount in billions.

    Inputs
    ------
    x : float (USD)

    Outputs
    -------
    str  e.g. '$11.2B'
    """
    return f"${x / 1e9:.1f}B"


def main():
    """Created by JXP and Claude.

    Print the full revised estimate: housing-only vs housing+services operating
    costs, a capital-cost line, population scenarios, and taxpayer denominators.

    Inputs
    ------
    (none)

    Outputs
    -------
    None. Prints to stdout.
    """
    print("Annual cost to house every homeless person in the U.S. (rev. 2)")
    print("=" * 66)
    print(f"PIT 2024: {PIT_2024:,}  (chronic {CHRONIC_2024:,}); "
          f"annual-flow ~{ANNUAL_FLOW:,}")
    print()

    # ---- Operating cost, two questions, on the PIT population ----
    for housing_only in (True, False):
        tag = "HOUSING SUBSIDY ONLY (a roof)" if housing_only else \
              "HOUSING + SERVICES (retention + offsets)"
        print(f"--- {tag} — PIT population ---")
        nets, grosses = [], []
        for sc in SCENARIOS:
            r = operating_cost(PIT_2024, CHRONIC_2024, sc, housing_only)
            nets.append(r["net"]); grosses.append(r["gross"])
            extra = "" if housing_only else \
                f"  offset -{bn(r['offset'])}  NET {bn(r['net'])}"
            print(f"  [{sc.name}] gross {bn(r['gross'])}{extra}")
        lo_key = "gross" if housing_only else "net"
        vals = grosses if housing_only else nets
        print(f"  => {lo_key} range {bn(min(vals))}–{bn(max(vals))} "
              f"(central {bn(vals[1])})")
        print()

    # ---- Induced-demand / turnover upper bound: annual-flow population ----
    r_flow = operating_cost(ANNUAL_FLOW, CHRONIC_2024, SCENARIOS[1],
                            housing_only=False)
    print(f"Annual-flow scenario (~{ANNUAL_FLOW:,}, central, w/ services): "
          f"NET {bn(r_flow['net'])}  (crit. 3: upper population bound)")
    print()

    # ---- Capital cost of building units (crit. 4) ----
    print("--- CAPITAL: building new units (the binding constraint) ---")
    for label, units in (("chronic only (152,585 units)", CHRONIC_2024),
                         ("all PIT (771,480 units)", PIT_2024)):
        for pu_label, pu in (("nat'l $200k", PER_UNIT_LOW),
                            ("central $350k", PER_UNIT_CENTRAL),
                            ("CA $550k", PER_UNIT_HIGH)):
            one, amort = capital_cost(units, pu)
            print(f"  {label:28s} @ {pu_label:14s}: "
                  f"one-time {bn(one)}  amortized {bn(amort)}/yr")
    print("  (In practice many are housed in EXISTING units via vouchers, so")
    print("   the true build need is a fraction of these headline figures.)")
    print()

    # ---- Per-person context, three denominators (crit. 5) ----
    central_net = operating_cost(PIT_2024, CHRONIC_2024, SCENARIOS[1],
                                housing_only=False)["net"]
    print(f"Per-person cost of the central services-inclusive net "
          f"({bn(central_net)}/yr):")
    for label, denom in (("all residents (340M)", DENOM_ALL),
                        ("working-age adults (200M)", DENOM_WORKING_AGE),
                        ("federal income-tax payers (115M)", DENOM_TAXPAYERS)):
        print(f"  ${central_net / denom:5.0f} / {label}")


if __name__ == "__main__":
    main()
