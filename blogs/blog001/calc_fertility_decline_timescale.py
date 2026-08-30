"""Timescale of the sub-replacement fertility 'exponential decline'.

Supporting calculation for the editorial review of Blog 001 ("Humans Suck
at Exponentials"). The essay closes by promising that once global total
fertility rate (TFR) drops below the 2.1 replacement level, "we will begin
an exponential decline in population" that "should reduce nearly all of the
negative exponentials we have been driving for the past centuries."

That is true in form but the relevant question is the *rate*, since the
whole essay is organized around doubling times. Below replacement, each
generation is smaller than the last by the ratio r = TFR / 2.1, so the
population declines geometrically with a per-generation factor r and a
halving time

    t_half = T_gen * ln(2) / ln(1 / r)

for generation length T_gen (mean age at childbearing, ~30 yr globally).
This script reports:

  1. the year global TFR first drops below 2.1 in the UN medium variant,
  2. the implied halving time at several plausible end-of-century TFRs,
  3. the year world population is projected to peak (population momentum
     means the peak lags the TFR crossing by decades),

so the closing claim can be compared, in the essay's own currency, with
the ~22 yr CO2 doubling time quoted earlier in the piece.

Data (cached in-repo, not re-fetched):
    CI_Reports/data/owid_fertility_with_projections.csv
    CI_Reports/data/owid_population_long_run_projections.csv
    (Our World in Data / UN World Population Prospects 2024, medium variant)

Usage:
    conda run -n ocean14 python blogs/blog001/calc_fertility_decline_timescale.py
"""

import os

import numpy as np
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))

TFR_CSV = os.path.join(REPO_DIR, "CI_Reports", "data",
                       "owid_fertility_with_projections.csv")
POP_CSV = os.path.join(REPO_DIR, "CI_Reports", "data",
                       "owid_population_long_run_projections.csv")

REPLACEMENT = 2.1        # children per woman
GENERATION_YEARS = 30.0  # mean age at childbearing, global, approx.

# CO2 doubling time quoted in the essay (fitted 1850-1970 in
# make_fig4_co2_emissions.py), for comparison.
CO2_DOUBLING_YEARS = 22.0


def halving_time(tfr, replacement=REPLACEMENT, t_gen=GENERATION_YEARS):
    """Population halving time for a sustained sub-replacement TFR.

    Parameters
    ----------
    tfr : float
        Sustained total fertility rate (children per woman).
    replacement : float, optional
        Replacement-level TFR.
    t_gen : float, optional
        Generation length in years.

    Returns
    -------
    float
        Years for population to halve, or ``inf`` at/above replacement.
    """
    r = tfr / replacement
    if r >= 1.0:
        return np.inf
    return t_gen * np.log(2.0) / np.log(1.0 / r)


def crossing_year(csv_path, threshold=REPLACEMENT):
    """First projected year world TFR falls below ``threshold``."""
    df = pd.read_csv(csv_path)
    world = df[df["Entity"] == "World"]

    est = world[["Year", "Fertility rate (estimates)"]].dropna()
    est.columns = ["Year", "tfr"]
    proj = world[["Year", "Fertility rate (projections) (Projected)"]].dropna()
    proj.columns = ["Year", "tfr"]

    below = proj[proj["tfr"] < threshold]
    first = int(below["Year"].iloc[0]) if len(below) else None
    return est, proj, first


def peak_population(csv_path):
    """Year and size of the projected world population peak."""
    df = pd.read_csv(csv_path)
    world = df[df["Entity"] == "World"].copy()
    series = world["Population"].fillna(
        world["Population (projections) (Projected)"])
    world = world.assign(pop=series).dropna(subset=["pop"])
    idx = world["pop"].idxmax()
    return int(world.loc[idx, "Year"]), float(world.loc[idx, "pop"])


def main():
    est, proj, cross = crossing_year(TFR_CSV)

    last_est_year = int(est["Year"].iloc[-1])
    last_est_tfr = float(est["tfr"].iloc[-1])
    end_tfr = float(proj["tfr"].iloc[-1])
    end_year = int(proj["Year"].iloc[-1])

    print("Global TFR, UN WPP medium variant (via OWID)")
    print(f"  latest estimate : {last_est_tfr:.3f} in {last_est_year}")
    print(f"  first year < {REPLACEMENT}: {cross}")
    print(f"  value in {end_year}   : {end_tfr:.3f}")

    pk_year, pk_pop = peak_population(POP_CSV)
    print(f"  projected population peak: {pk_pop/1e9:.2f} billion "
          f"in {pk_year}")

    print("\nPopulation halving time for a sustained TFR "
          f"(generation = {GENERATION_YEARS:.0f} yr)")
    for tfr in [2.0, 1.9, float(f"{end_tfr:.2f}"), 1.6, 1.4, 1.2]:
        th = halving_time(tfr)
        ratio = th / CO2_DOUBLING_YEARS
        print(f"  TFR {tfr:4.2f} -> halving time {th:7.1f} yr "
              f"({ratio:5.1f}x the {CO2_DOUBLING_YEARS:.0f}-yr CO2 "
              "doubling time)")

    print("\nTakeaway: the promised decline is exponential, but its "
          "halving time is")
    print("an order of magnitude longer than the doubling time of the "
          "exponential")
    print("it is offered as an antidote to, and the population peak "
          f"({pk_year}) lags the")
    print(f"TFR crossing ({cross}) by roughly "
          f"{pk_year - cross if cross else float('nan')} yr of momentum.")


if __name__ == "__main__":
    main()
