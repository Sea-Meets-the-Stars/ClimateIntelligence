"""Created by JXP and Claude.

Estimate the annual cost to house every homeless person in the United States,
built from the data gathered for the Climate Intelligence homelessness section
(CI report Section 7; context claudes_context.md Section 11).

The estimate is a transparent bottom-up model with an explicit LOW / CENTRAL /
HIGH range. It is intentionally simple so every assumption is visible and
auditable — per the project rule that calculations live in a reusable script,
not inline.

METHOD
------
Split the point-in-time (PIT) homeless population into two groups that need
two different (evidence-based) interventions, cost each, sum, then net out the
public-service savings that supportive housing is documented to generate.

  cost_gross = N_chronic     * cost_PSH_per_person_yr
             + N_non_chronic * cost_RRH_per_person_yr
  cost_net   = cost_gross - (N_chronic * offset_per_person_yr)

  * Chronic homeless -> Permanent Supportive Housing (PSH): a subsidy plus
    intensive services, open-ended. Expensive, but it is what this population
    needs and what the RCT evidence (Denver SIB) tested.
  * Everyone else -> Rapid Re-Housing (RRH) / lighter assistance: time-limited
    rent + case management. Most homelessness is brief; this is the cheaper,
    higher-throughput intervention.

DATA / ANCHORS (see the report's references)
--------------------------------------------
  * PIT population: HUD AHAR Part 1 — 771,480 (Jan 2024, record); 745,652
    (Jan 2025). We report on 2024 and show 2025 as a sensitivity.
  * Chronically homeless individuals: 152,585 (HUD 2024, ~1 in 3 of individuals).
  * PSH per-person-year cost band: $20,000 (NAEH national ~$20,115/household,
    2022$) to $36,000 (Denver SIB high provider), central $25,000.
  * RRH per-person-year cost band: $8,500 (NAEH ~$8,486/household, 2022$) to
    $17,000 (NAEH Housing First median ~$16,479), central $12,000.
  * Offset (chronic only): supportive housing offsets ~half its cost via avoided
    jail/ER/shelter/detox use (Denver SIB: ~$7,000/person-yr, ~50% offset). We
    apply a 40% (low) / 50% (central) / 60% (high) offset to the PSH group only.

CAVEATS (printed with the result; do not quote the number without them)
-----------------------------------------------------------------------
  * This is an OPERATING-SUBSIDY estimate (rent + services). It does NOT include
    the capital cost of BUILDING housing where supply is short — the binding
    constraint in high-cost metros.
  * PIT is a single-night count; the number of people who experience
    homelessness OVER A YEAR is ~2-3x larger, so an annual-flow program serves
    more people than the PIT headcount.
  * Costs are in mixed recent-year dollars (2022-2025) and are not inflation-
    harmonized; treat the range, not the point, as the answer.

Run under the project conda environment:
    conda run -n ocean14 python CI_Reports/cost_to_house_homeless.py
"""

# Imports at the top of the file (project coding guideline).
from dataclasses import dataclass


@dataclass
class Scenario:
    """Created by JXP and Claude.

    One column of assumptions (LOW / CENTRAL / HIGH).

    Fields
    ------
    name : str
    psh_cost : float           # PSH $ per person-year
    rrh_cost : float           # RRH $ per person-year
    offset_frac : float        # fraction of PSH cost offset by avoided services
    """
    name: str
    psh_cost: float
    rrh_cost: float
    offset_frac: float


# PIT populations (HUD AHAR Part 1).
PIT_2024 = 771_480
PIT_2025 = 745_652
CHRONIC_2024 = 152_585  # chronically homeless individuals, 2024

SCENARIOS = [
    Scenario("LOW", psh_cost=20_000, rrh_cost=8_500, offset_frac=0.60),
    Scenario("CENTRAL", psh_cost=25_000, rrh_cost=12_000, offset_frac=0.50),
    Scenario("HIGH", psh_cost=36_000, rrh_cost=17_000, offset_frac=0.40),
]


def estimate(total_pit, chronic, sc):
    """Created by JXP and Claude.

    Compute gross and net annual housing cost for one scenario.

    Inputs
    ------
    total_pit : int
        Point-in-time homeless population.
    chronic : int
        Chronically homeless individuals (get PSH).
    sc : Scenario
        Assumption column.

    Outputs
    -------
    dict
        gross, offset, net (all in USD/year), plus the split populations.
    """
    non_chronic = total_pit - chronic
    psh_total = chronic * sc.psh_cost
    rrh_total = non_chronic * sc.rrh_cost
    gross = psh_total + rrh_total
    offset = chronic * sc.psh_cost * sc.offset_frac
    net = gross - offset
    return {
        "non_chronic": non_chronic,
        "psh_total": psh_total,
        "rrh_total": rrh_total,
        "gross": gross,
        "offset": offset,
        "net": net,
    }


def bn(x):
    """Created by JXP and Claude.

    Format a dollar amount in billions.

    Inputs
    ------
    x : float  (USD)

    Outputs
    -------
    str  (e.g. '$11.2B')
    """
    return f"${x / 1e9:.1f}B"


def main():
    """Created by JXP and Claude.

    Print the full estimate table and context comparisons.

    Inputs
    ------
    (none)

    Outputs
    -------
    None. Prints to stdout.
    """
    print("Annual cost to house every homeless person in the U.S.")
    print("=" * 60)
    print(f"PIT population (2024): {PIT_2024:,}   chronic: {CHRONIC_2024:,} "
          f"({100*CHRONIC_2024/PIT_2024:.0f}%)")
    print(f"Non-chronic (RRH): {PIT_2024 - CHRONIC_2024:,}")
    print()
    results = {}
    for sc in SCENARIOS:
        r = estimate(PIT_2024, CHRONIC_2024, sc)
        results[sc.name] = r
        print(f"[{sc.name}] PSH ${sc.psh_cost:,}/pp  RRH ${sc.rrh_cost:,}/pp  "
              f"offset {sc.offset_frac:.0%}")
        print(f"    gross = {bn(r['gross'])}   "
              f"offset = -{bn(r['offset'])}   NET = {bn(r['net'])}")
    print()
    lo, ce, hi = (results["LOW"]["net"], results["CENTRAL"]["net"],
                  results["HIGH"]["net"])
    # Note: LOW scenario has the largest offset, so its NET can differ from the
    # naive min; report the actual min/max across scenarios.
    nets = [results[s]["net"] for s in ("LOW", "CENTRAL", "HIGH")]
    grosses = [results[s]["gross"] for s in ("LOW", "CENTRAL", "HIGH")]
    print(f"HEADLINE (2024 PIT):")
    print(f"  gross ~ {bn(min(grosses))} to {bn(max(grosses))} "
          f"(central {bn(results['CENTRAL']['gross'])})")
    print(f"  net   ~ {bn(min(nets))} to {bn(max(nets))} "
          f"(central {bn(ce)}) after service-cost offsets")
    print()
    # 2025 sensitivity (population only).
    r25 = estimate(PIT_2025, CHRONIC_2024, SCENARIOS[1])
    print(f"2025 PIT sensitivity (central): net {bn(r25['net'])}")
    print()
    # Context comparisons.
    us_pop = 340_000_000
    fed_outlays_2024 = 6.75e12  # ~$6.75T federal outlays FY2024
    mid_deduction = 30e9        # ~ mortgage-interest deduction, order of magnitude
    print("Context:")
    print(f"  central net per U.S. resident: "
          f"${results['CENTRAL']['net']/us_pop:.0f}/person/year")
    print(f"  central net as share of federal outlays (~$6.75T): "
          f"{100*results['CENTRAL']['net']/fed_outlays_2024:.2f}%")
    print(f"  vs. homeowner mortgage-interest deduction (~{bn(mid_deduction)}/yr): "
          f"comparable order of magnitude")
    print(f"  vs. HUD Homeless Assistance Grants (~$4.05B/yr enacted FY2024)")


if __name__ == "__main__":
    main()
