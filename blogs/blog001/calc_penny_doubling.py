"""The doubling-penny example for Blog 001's lay-reader definition of "exponential".

Created by JXP and Claude.

A penny that doubles every day: how much is it after a week, after a month,
and what share of the final pile did the last doubling add?  Written so the
numbers quoted in the Comments/Exponential suggestion are reproducible.

Usage:
    conda run -n ocean14 python blogs/blog001/calc_penny_doubling.py

Outputs: printed table only.
"""


def penny_after(days):
    """Value in dollars of a penny that doubles once a day.

    Parameters
    ----------
    days : int
        Number of days elapsed. Day 1 is the original penny (no doubling
        yet), so after ``days`` days the penny has doubled ``days - 1`` times.

    Returns
    -------
    dollars : float
        Value in dollars.
    """
    cents = 2 ** (days - 1)
    return cents / 100.0


def main():
    """Print the penny's value at a few milestones and the last-doubling share."""
    for days in (1, 8, 15, 22, 30):
        print(f"day {days:2d}: ${penny_after(days):,.2f}")
    # The last doubling adds as much as every earlier doubling combined, plus
    # the original penny: 2**(n-1) = 1 + sum_{k<n-1} 2**k, so the final day's
    # gain is just over half the total.
    total = penny_after(30)
    gain_last = total - penny_after(29)
    print(f"last doubling added ${gain_last:,.2f} of ${total:,.2f} "
          f"({100 * gain_last / total:.1f}% of the final pile)")


if __name__ == "__main__":
    main()
