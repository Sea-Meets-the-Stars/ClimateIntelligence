"""Figure 3 for Blog 001 ("Humans Suck at Exponentials").

Plots the training compute (FLOP) of notable AI models since 2010 -- the
start of the deep-learning era -- on a log y-axis, fits an exponential
trend to the era, and annotates the fitted doubling time. A handful of
landmark models (AlexNet, GPT-2, GPT-3, GPT-4, ...) are called out.

Data source (cached locally in data/epoch_notable_ai_models.csv):
    https://epoch.ai/data/notable_ai_models.csv
    (Epoch AI, "Notable AI Models" dataset; retrieved 2026-08-29.)

Usage:
    conda run -n ocean14 python blogs/blog001/make_fig3_ai_compute_growth.py

Outputs:
    blogs/blog001/fig3_ai_compute_growth.png
"""

import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Paths anchored to this script's directory so it runs from anywhere.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_CSV = os.path.join(SCRIPT_DIR, "data", "epoch_notable_ai_models.csv")
OUT_PNG = os.path.join(SCRIPT_DIR, "fig3_ai_compute_growth.png")

DATA_URL = "https://epoch.ai/data/notable_ai_models.csv"

# Start of the deep-learning era. Epoch AI's own trend analysis (Sevilla
# et al. 2022, "Compute Trends Across Three Eras of Machine Learning")
# places the break at ~2010, and the fitted doubling time here is nearly
# insensitive to this choice (5.0-5.8 months for start years 2008-2016).
ERA_START_YEAR = 2010

# Landmark models to call out: exact dataset name -> (display label,
# text x-offset in years, text y-offset in decades of FLOP).
CALLOUTS = {
    "AlexNet": ("AlexNet", -0.3, 2.2),
    "DQN": ("DQN (Atari)", 0.6, -2.2),
    "AlphaGo Zero": ("AlphaGo Zero", 0.7, -2.4),
    "GPT-2 (1.5B)": ("GPT-2", -1.0, 1.8),
    "GPT-3 175B (davinci)": ("GPT-3", -1.2, 1.5),
    "GPT-4 (Mar 2023)": ("GPT-4", -1.6, 1.2),
    "Grok 4": ("Grok 4", -0.4, 1.4),
}


def load_models(csv_path):
    """Load notable models with a known date and training compute.

    Parameters
    ----------
    csv_path : str
        Path to the Epoch AI notable models CSV.

    Returns
    -------
    pandas.DataFrame
        Columns ``model`` (str), ``date`` (datetime64), ``year``
        (float decimal year), and ``flop`` (float); rows lacking a
        publication date or compute estimate are dropped.
    """
    df = pd.read_csv(
        csv_path,
        usecols=["Model", "Publication date", "Training compute (FLOP)"],
    )
    df = df.rename(columns={
        "Model": "model",
        "Publication date": "date",
        "Training compute (FLOP)": "flop",
    })
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["flop"] = pd.to_numeric(df["flop"], errors="coerce")
    df = df.dropna(subset=["date", "flop"]).sort_values("date")
    df["year"] = (df["date"].dt.year
                  + (df["date"].dt.dayofyear - 1) / 365.25)
    return df.reset_index(drop=True)


def fit_doubling_time(df, start_year):
    """Fit an exponential compute trend to models from ``start_year`` on.

    Fits a straight line to log10(FLOP) vs. decimal year (least squares),
    equivalent to C(t) = C0 * 2**((t - t0) / t_double).

    Parameters
    ----------
    df : pandas.DataFrame
        Output of :func:`load_models`.
    start_year : int
        First calendar year included in the fit.

    Returns
    -------
    doubling_months : float
        Fitted doubling time in months.
    growth_per_year : float
        Fitted multiplicative growth factor per year.
    trend_years : numpy.ndarray
        Decimal years spanning the fit window.
    trend_flop : numpy.ndarray
        Fitted (model) compute on those years.
    n_fit : int
        Number of models in the fit.
    """
    era = df[df["year"] >= start_year]
    slope, intercept = np.polyfit(era["year"], np.log10(era["flop"]), 1)
    doubling_months = 12.0 * np.log10(2.0) / slope
    growth_per_year = 10.0 ** slope
    trend_years = np.linspace(start_year, era["year"].max(), 200)
    trend_flop = 10.0 ** (slope * trend_years + intercept)
    return doubling_months, growth_per_year, trend_years, trend_flop, len(era)


def make_figure(df, doubling_months, growth_per_year, trend_years,
                trend_flop, out_png):
    """Render and save the log-axis compute-trend figure.

    Parameters
    ----------
    df : pandas.DataFrame
        Output of :func:`load_models` (all eras; only the deep-learning
        era is plotted).
    doubling_months : float
        Fitted doubling time (months).
    growth_per_year : float
        Fitted growth factor per year.
    trend_years, trend_flop : numpy.ndarray
        Fitted trend line over the era.
    out_png : str
        Output PNG path.
    """
    plt.rcParams.update({
        "figure.dpi": 130,
        "savefig.dpi": 130,
        "font.family": "sans-serif",
        "font.size": 11,
        "axes.titlesize": 14,
        "axes.labelsize": 11.5,
        "axes.edgecolor": "#9aa4af",
        "axes.linewidth": 0.8,
        "xtick.color": "#3d434a",
        "ytick.color": "#3d434a",
        "text.color": "#21262b",
        "axes.labelcolor": "#21262b",
    })

    era = df[df["year"] >= ERA_START_YEAR]

    fig, ax = plt.subplots(figsize=(9, 5.5))

    # One notable model per dot.
    ax.scatter(era["year"], era["flop"], s=16, color="#2b6cb0",
               alpha=0.35, lw=0, zorder=3)

    # Fitted exponential trend.
    ax.plot(trend_years, trend_flop, color="#c05621", lw=2.2, ls="--",
            zorder=4)

    # Landmark callouts: darker marker plus a short leader line.
    for name, (label, dx, dy) in CALLOUTS.items():
        row = era[era["model"] == name]
        if row.empty:
            continue
        x, y = row["year"].iloc[0], row["flop"].iloc[0]
        ax.scatter([x], [y], s=34, color="#1a365d", zorder=5)
        ax.annotate(
            label, xy=(x, y), xycoords="data",
            xytext=(x + dx, y * 10.0 ** dy), textcoords="data",
            fontsize=9.5, color="#1a365d", fontweight="bold",
            ha="center", va="center",
            arrowprops=dict(arrowstyle="-", color="#8a97a6", lw=0.8,
                            shrinkA=2, shrinkB=3),
            zorder=6,
        )

    ax.set_yscale("log")
    ax.set_ylim(1e12, 3e28)
    ax.set_xlim(ERA_START_YEAR - 0.5, era["year"].max() + 1.2)

    # Recessive grid, no chartjunk.
    ax.grid(True, which="major", axis="y", color="#d7dce1", lw=0.7,
            zorder=0)
    ax.grid(True, which="major", axis="x", color="#e6eaee", lw=0.6,
            zorder=0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)

    ax.set_xticks(np.arange(2010, 2027, 2))
    ax.xaxis.set_major_formatter(plt.FuncFormatter(
        lambda v, _: f"{int(v)}"))
    ax.set_yticks([1e12, 1e15, 1e18, 1e21, 1e24, 1e27])
    ax.yaxis.set_minor_locator(plt.NullLocator())

    ax.set_ylabel("Training compute (FLOP, log scale)")
    ax.set_title("AI training compute: a sixteen-year exponential",
                 loc="left", pad=12, fontweight="bold")

    # Figure number for the blog post's sequence (bottom-right corner,
    # mirroring the data-source footer at bottom-left).
    fig.text(0.99, 0.012, "Figure 3", ha="right", fontsize=9.5,
             fontweight="bold", color="#6b7280")

    # Annotation: fitted doubling time, anchored to the trend line.
    ax.text(
        2011.0, 3e22,
        f"compute doubling every ~{doubling_months:.0f} months\n"
        f"since {ERA_START_YEAR}  (×{growth_per_year:.0f} per year)",
        fontsize=11.5, color="#8a3f18", ha="left", va="center",
    )

    # Direct label for the dot cloud (no legend box needed).
    ax.text(2021.7, 2e16, "one dot = one notable AI model",
            color="#2b6cb0", fontsize=10)

    # Footer citing the data source.
    fig.text(0.01, 0.012,
             f"Data: Epoch AI, Notable AI Models — {DATA_URL} "
             "(retrieved 2026-08-29)",
             fontsize=7.5, color="#6b7280")

    fig.tight_layout(rect=(0, 0.035, 1, 1))
    fig.savefig(out_png)
    plt.close(fig)


def main():
    """Load data, fit the era trend, print the fit, and save the figure."""
    df = load_models(DATA_CSV)
    (doubling_months, growth_per_year, trend_years, trend_flop,
     n_fit) = fit_doubling_time(df, ERA_START_YEAR)
    era = df[df["year"] >= ERA_START_YEAR]
    print(f"Models with date + compute: {len(df)} "
          f"({df['date'].iloc[0].date()} to {df['date'].iloc[-1].date()})")
    print(f"Fit era: {ERA_START_YEAR}+ ({n_fit} models)")
    print(f"Fitted doubling time: {doubling_months:.1f} months "
          f"(x{growth_per_year:.2f} per year)")
    print(f"Compute span in era: {era['flop'].min():.1e} to "
          f"{era['flop'].max():.1e} FLOP")
    make_figure(df, doubling_months, growth_per_year, trend_years,
                trend_flop, OUT_PNG)
    print(f"Wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
