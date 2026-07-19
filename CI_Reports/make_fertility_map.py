"""Created by JXP and Claude.

Generate the world total-fertility-rate (TFR) choropleth (Figure 19) for the
Climate Intelligence report (CI_2026_07_09_climate_report.md, sec 9 "Global
population"). Each country is colored by its most recent TFR, on a diverging
scale centered on the replacement level of 2.1 births per woman: countries below
replacement are blue, above are red.

The figure is drawn with matplotlib only (no geopandas/plotly), by parsing a
GeoJSON of country polygons and shading each by a value joined on ISO-3 code.

Data sources (cached under CI_Reports/data/, fetched 2026-07-18):
  - Country boundaries: Natural Earth 1:110m admin-0 countries, GeoJSON
    (nvkelso/natural-earth-vector), data/world_countries_ne110m.geojson. Public
    domain. Plotted in plate-carree (lon/lat) with Antarctica clipped.
  - Total fertility rate by country: World Bank indicator SP.DYN.TFRT.IN (source:
    UN WPP 2024 and national statistics), years 2015-2023, data/wb_tfr_raw.json.
    We use each country's most recent non-null year (2023 for most).

Run under the project conda environment:
    conda run -n ocean14 python CI_Reports/make_fertility_map.py

Design choices follow the project coding guidelines: functions (no classes),
imports at top, inline comments, matplotlib for plotting, docstrings with
inputs/outputs, and "Created by JXP and Claude" on the file and each method.
"""

# Imports at the top of the file (project coding guideline).
import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")  # headless backend; we save PNGs, never display
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import TwoSlopeNorm
from matplotlib.cm import ScalarMappable

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

REPLACEMENT_TFR = 2.1  # births per woman for a stable population (the color center)

# World Bank "country/all" mixes real economies with regional/income aggregates.
# These aggregate codes are excluded so the summary counts are true country-level.
WB_AGGREGATE_CODES = {
    "WLD", "AFE", "AFW", "ARB", "CEB", "CSS", "EAP", "EAR", "EAS", "ECA", "ECS",
    "EMU", "EUU", "FCS", "HIC", "HPC", "IBD", "IBT", "IDA", "IDB", "IDX", "INX",
    "LAC", "LCN", "LDC", "LIC", "LMC", "LMY", "LTE", "MEA", "MIC", "MNA", "NAC",
    "OED", "OSS", "PRE", "PSS", "PST", "SAS", "SSA", "SSF", "SST", "TEA", "TEC",
    "TLA", "TMN", "TSA", "TSS", "UMC", "WLD",
}

plt.rcParams.update({
    "figure.dpi": 130,
    "savefig.dpi": 130,
    "font.size": 11,
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def load_tfr_by_iso3(path):
    """Created by JXP and Claude.

    Parse the World Bank JSON and return {ISO3: (tfr, year)} using each country's
    most recent non-null year. Input: path to wb_tfr_raw.json. Output: dict.
    """
    payload = json.loads(Path(path).read_text())
    rows = payload[1]  # payload[0] is metadata
    best = {}
    for r in rows:
        iso3 = r.get("countryiso3code")
        val = r.get("value")
        year = r.get("date")
        if not iso3 or val is None or iso3 in WB_AGGREGATE_CODES:
            continue
        year = int(year)
        # keep the latest year available for each country
        if iso3 not in best or year > best[iso3][1]:
            best[iso3] = (float(val), year)
    return best


def feature_iso3(props):
    """Created by JXP and Claude.

    Best ISO-3 code for a Natural Earth feature. Natural Earth stores '-99' for a
    few sovereign states (France, Norway, ...); fall back to the '_EH' variant,
    then ADM0_A3. Input: feature properties dict. Output: ISO3 string.
    """
    iso = props.get("ISO_A3")
    if iso in (None, "", "-99"):
        iso = props.get("ISO_A3_EH")
    if iso in (None, "", "-99"):
        iso = props.get("ADM0_A3")
    return iso


def polygons_from_geometry(geom):
    """Created by JXP and Claude.

    Yield exterior rings (lists of [lon, lat]) for Polygon/MultiPolygon geometry.
    Holes are ignored (immaterial at 1:110m for a choropleth). Input: GeoJSON
    geometry dict. Output: generator of coordinate rings.
    """
    if geom is None:
        return
    gtype = geom["type"]
    coords = geom["coordinates"]
    if gtype == "Polygon":
        yield coords[0]
    elif gtype == "MultiPolygon":
        for poly in coords:
            yield poly[0]


def make_map(geojson_path, tfr_by_iso3, out_path):
    """Created by JXP and Claude.

    Draw the choropleth and save it. Inputs: geojson path, {ISO3:(tfr,year)},
    output PNG path. Output: writes PNG; returns coverage stats dict.
    """
    features = json.loads(Path(geojson_path).read_text())["features"]

    # diverging scale centered on replacement; clamp the extremes for contrast
    norm = TwoSlopeNorm(vmin=1.0, vcenter=REPLACEMENT_TFR, vmax=6.5)
    cmap = plt.get_cmap("RdBu_r")  # low TFR -> blue, high TFR -> red
    no_data = "#d9d9d9"

    fig, ax = plt.subplots(figsize=(13.5, 7.2))
    matched, unmatched = [], []

    for feat in features:
        props = feat["properties"]
        name = props.get("NAME") or props.get("NAME_LONG")
        if name == "Antarctica":
            continue
        iso3 = feature_iso3(props)
        rec = tfr_by_iso3.get(iso3)
        color = cmap(norm(rec[0])) if rec else no_data
        (matched if rec else unmatched).append(name)

        patches = [Polygon(np.asarray(ring), closed=True)
                   for ring in polygons_from_geometry(feat["geometry"])]
        if patches:
            pc = PatchCollection(patches, facecolor=color,
                                 edgecolor="white", linewidths=0.3)
            ax.add_collection(pc)

    ax.set_xlim(-180, 180)
    ax.set_ylim(-58, 84)          # clip most of Antarctica for a tighter frame
    ax.set_aspect("equal")        # equirectangular (plate carree)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    # colorbar with the replacement level marked
    sm = ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, orientation="horizontal", fraction=0.045,
                        pad=0.02, aspect=45, extend="both",
                        ticks=[1.0, 1.5, REPLACEMENT_TFR, 3.0, 4.0, 5.0, 6.0])
    cbar.set_label("Total fertility rate (births per woman) — white = 2.1 replacement level")
    cbar.ax.axvline(REPLACEMENT_TFR, color="black", lw=1.4)  # mark 2.1 on the bar

    # grey swatch for no-data in the legend area
    ax.plot([], [], "s", color=no_data, label="no data")
    ax.legend(loc="lower left", frameon=False, fontsize=9)

    ax.set_title("Figure 19. Total fertility rate by country — most countries are now "
                 "below replacement (2.1)", fontsize=12)
    ax.text(-180, -57, "World Bank SP.DYN.TFRT.IN (latest available, mostly 2023; "
            "source UN WPP 2024). Natural Earth 1:110m boundaries.",
            fontsize=7.5, color="#555555")

    fig.tight_layout()
    fig.savefig(out_path)
    plt.close(fig)
    return {"matched": len(matched), "unmatched_names": sorted(unmatched)}


def print_stats(tfr_by_iso3, coverage):
    """Created by JXP and Claude. Print the numbers the report quotes. Output:
    stdout only."""
    vals = [v for v, _ in tfr_by_iso3.values()]
    below = sum(1 for v in vals if v < REPLACEMENT_TFR)
    print("=" * 66)
    print("TFR CHOROPLETH — coverage & summary")
    print("=" * 66)
    print(f"Countries/areas with a TFR value: {len(vals)}")
    print(f"  below replacement (<2.1): {below} ({below/len(vals)*100:.0f}%)")
    print(f"  at/above replacement:     {len(vals)-below}")
    print(f"  min {min(vals):.2f}, max {max(vals):.2f}, median {np.median(vals):.2f}")
    # the extremes
    items = sorted(tfr_by_iso3.items(), key=lambda kv: kv[1][0])
    print("  lowest 5:", [(k, round(v, 2)) for k, (v, _) in items[:5]])
    print("  highest 5:", [(k, round(v, 2)) for k, (v, _) in items[-5:]])
    print(f"Map polygons matched to a value: {coverage['matched']}")
    print(f"Map countries left grey (no join): {coverage['unmatched_names']}")
    print("=" * 66)


def main():
    """Created by JXP and Claude. Build the TFR choropleth (Figure 19)."""
    tfr = load_tfr_by_iso3(DATA / "wb_tfr_raw.json")
    coverage = make_map(DATA / "world_countries_ne110m.geojson", tfr,
                        HERE / "fig19_fertility_map.png")
    print_stats(tfr, coverage)
    print("\nWrote fig19_fertility_map.png")


if __name__ == "__main__":
    main()
