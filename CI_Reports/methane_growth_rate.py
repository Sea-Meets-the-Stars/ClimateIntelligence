"""Created by JXP and Claude.

Quantify the atmospheric methane (CH4) growth rate over time, to test a
reviewer's claim (R. comments, 2026-07-14) that CH4 is currently accelerating
rather than slowing. This is the reproducible calculation behind the report's
statement on the methane trend (Principle 6: mathematics trumps all).

Data: NOAA GML globally averaged marine surface monthly mean CH4,
CI_Reports/data/ch4_mm_gl.txt (columns: year month decimal average
average_unc trend trend_unc; -9.99 = preliminary/missing uncertainty).

We use NOAA's own deseasonalized "trend" column and difference it to get the
annual growth rate (ppb/yr), then average by decade and report the last full
years, so the recent slope is compared to history on equal footing.

Run under the project conda environment:
    conda run -n ocean14 python CI_Reports/methane_growth_rate.py
"""

# Imports at the top of the file (project coding guideline).
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"


def load_ch4_trend():
    """Created by JXP and Claude.

    Load NOAA's deseasonalized CH4 trend series.

    Inputs
    ------
    (none) reads data/ch4_mm_gl.txt

    Outputs
    -------
    (np.ndarray, np.ndarray)
        decimal_year, trend_ppb  (monthly, deseasonalized).
    """
    dyr, trend = [], []
    with open(DATA / "ch4_mm_gl.txt") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.split()
            if len(parts) < 6:
                continue
            dyr.append(float(parts[2]))
            trend.append(float(parts[5]))  # deseasonalized trend column
    return np.array(dyr), np.array(trend)


def annual_growth(dyr, trend):
    """Created by JXP and Claude.

    Year-over-year growth of the deseasonalized series (Dec-to-Dec proxy via
    12-month differencing of the monthly trend).

    Inputs
    ------
    dyr, trend : np.ndarray — decimal year and deseasonalized CH4 (ppb).

    Outputs
    -------
    (np.ndarray, np.ndarray) — mid-year, growth (ppb/yr).
    """
    growth = trend[12:] - trend[:-12]          # ppb over 12 months
    mid = 0.5 * (dyr[12:] + dyr[:-12])
    return mid, growth


def main():
    """Created by JXP and Claude.

    Print decadal-average and recent-year CH4 growth rates.

    Inputs
    ------
    (none)

    Outputs
    -------
    None. Prints a small table to stdout.
    """
    dyr, trend = load_ch4_trend()
    mid, growth = annual_growth(dyr, trend)

    print(f"CH4 record: {dyr[0]:.2f}-{dyr[-1]:.2f}; "
          f"latest trend value {trend[-1]:.1f} ppb")
    print("\nDecade-average deseasonalized growth (ppb/yr):")
    for lo in range(1990, 2030, 10):
        m = (mid >= lo) & (mid < lo + 10)
        if m.any():
            print(f"  {lo}s: {growth[m].mean():5.2f}  "
                  f"(min {growth[m].min():.2f}, max {growth[m].max():.2f})")

    print("\nRecent full-year growth (12-mo diff, mid-year):")
    for yr in range(2018, 2026):
        idx = np.argmin(np.abs(mid - (yr + 0.0)))
        if abs(mid[idx] - yr) < 0.1:
            print(f"  ~{yr}: {growth[idx]:5.2f} ppb/yr")

    # The plateau, for context (Richard's point is that the recent slope is
    # steeper than the report's figure appears to show).
    m0 = (mid >= 2000) & (mid < 2007)
    m1 = (mid >= 2014) & (mid < 2024)
    print(f"\nPlateau 2000-2006 mean: {growth[m0].mean():.2f} ppb/yr")
    print(f"Renewed rise 2014-2023 mean: {growth[m1].mean():.2f} ppb/yr")


if __name__ == "__main__":
    main()
