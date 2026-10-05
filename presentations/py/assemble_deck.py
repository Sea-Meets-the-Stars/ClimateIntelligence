"""Created by JXP and Claude.

Assemble the WMKO 2026 deck: rebuild the skeleton on the Kraw master
(build_skeleton.build), then place each slide's figure, instrument photo and
~16pt source line (Q10), and append the full figure source to the speaker
notes (from figs/sources.json).

B8 = slide 4 + the climate half (C1-C10). B9 will add the intro / AI half to
PLACEMENTS below.

Layout (slide 10" x 5.625"; nothing within 0.4" of the side edges):
  - content area starts below the title (1 line ~0.95", 2 lines ~1.5");
  - source text sits above the master's UCSC logo (y >= 5.24") and left of
    the slide number (x >= 9.27");
  - a figure with an instrument photo gets the left ~6.4"; the photo the
    right ~2.6"; both scaled to fit, aspect preserved, vertically centered.

Usage:
    conda run -n ocean14 python presentations/py/assemble_deck.py [-o OUT.pptx]
"""
import argparse
import json
import os

from PIL import Image
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt

from build_skeleton import build
from slide_style import FIGS, PRES

TEMPLATE = PRES / "2026_WMKO" / "Kraw_2024.pptx"
OUT = PRES / "2026_WMKO" / "WMKO_2026_Climate_Intelligence.pptx"
IMG = FIGS / "images"

X0, X1 = 0.4, 9.6            # usable width (inches)
SRC_X, SRC_W = 0.4, 8.75     # source line box (ends before the slide number)
SRC_TOP_1LINE = 4.92         # top of a one-line source; content ends above it
SRC_LINE_H = 0.27            # 16 pt line height (inches)
SRC_CHARS_PER_LINE = 80      # ~16 pt Roboto across SRC_W
PHOTO_W = 2.6
GAP = 0.2

# Slide title (exact skeleton title) -> (figure, instrument photo or None, slide source line)
PLACEMENTS = {
    "The two exponentials": (
        "s4_two_exponentials.png", None,
        "Data: Global Carbon Project via Our World in Data (left); Epoch AI, Notable AI Models (right)"),
    "1. CO₂ has been rising for 50+ years": (
        "c1_keeling.png", "mauna_loa_observatory.jpg",
        "Data: NOAA GML / Scripps, Mauna Loa Observatory · Photo: Brian Vasel/NOAA"),
    "2. The U.S. has dominated greenhouse gas release": (
        "c2_us_cumulative.png", None,
        "Data: Global Carbon Project, Global Carbon Budget 2025, via Our World in Data"),
    "3. Heat in vs. heat out": (
        "c3a_energy_budget.png", "ceres_instrument.jpg",
        "Data: IPCC AR6 WGI Fig. 7.2; CERES satellites (Loeb et al. 2021) · Photo: NASA"),
    "3. Heat in vs. heat out: the CO₂ bite": (
        "c3b_olr_spectrum.png", None,
        "Schematic from Planck's law; shape after satellite spectra (Nimbus-4 IRIS, Hanel et al. 1972)"),
    "4. The ocean is warming: surface": (
        "c4a_sst_global.png", None,
        "Data: NOAA NCEI, NOAAGlobalTemp / ERSSTv5 (ships, buoys, Argo)"),
    "4. The ocean is warming: depth": (
        "c4b_ohc_by_depth.png", "argo_float.jpg",
        "Data: NOAA NCEI ocean heat content (XBT/CTD, then Argo) · Photo: NOAA GOMO"),
    "5. The ocean isn't done warming": (
        "c5_committed_warming.png", None,
        "IPCC AR6 WGI (SPM A.1.2, B.5.4; Ch. 4, 7); Murphy 2021"),
    "6. Sea level is rising": (
        "c6a_gmsl.png", "sentinel6.jpg",
        "Tide gauges: CSIRO (Church & White 2011). Altimetry data are provided by NOAA "
        "Laboratory for Satellite Altimetry · Image: NASA"),
    "6. Sea level is rising: Honolulu": (
        "c6b_honolulu.png", "honolulu_tide_station.jpg",
        "Data and photo: NOAA CO-OPS, Honolulu Harbor tide gauge 1612340"),
    "7. Biodiversity is declining fast": (
        "c7a_lpi_biomass.png", None,
        "Data: WWF/ZSL Living Planet Index 2024 via Our World in Data; Bar-On et al. 2018 (PNAS)"),
    "7. Biodiversity is declining fast: extinctions": (
        "c7b_extinctions.png", None,
        "Data: Ceballos et al. 2015, Science Advances (IUCN Red List)"),
    "8. Planetary boundaries are being exceeded": (
        "c8_planetary_bounds.png", None,
        "Data: Richardson et al. 2023 (Science Advances); Planetary Health Check 2025"),
    "9. Population growth is poised to decline": (
        "c9a_population.png", None,
        "Data: UN World Population Prospects 2024 via Our World in Data; IHME (Vollset et al. 2020)"),
    "9. Fertility has fallen below replacement": (
        "c9b_fertility.png", None,
        "Data: UN World Population Prospects 2024 via Our World in Data"),
    "10. Most economists believe technology will save us": (
        "c10_economist_survey.png", None,
        "Survey: Howard & Sylvan 2021, Institute for Policy Integrity, NYU Law (738 economists)"),
}


def title_lines(title):
    """Created by JXP and Claude. Rough line count of a 38 pt Kraw title
    across 9.75" (observed: titles over ~40 characters wrap)."""
    return 1 if len(title) <= 40 else 2


def fit(path, box_w, box_h):
    """Created by JXP and Claude. Largest (w, h) in inches with the image's
    aspect ratio that fits inside box_w x box_h."""
    with Image.open(path) as im:
        aspect = im.width / im.height
    w = min(box_w, box_h * aspect)
    return w, w / aspect


def add_source(slide, text, top, n_lines):
    """Created by JXP and Claude. ~16 pt gray source line in the Kraw font."""
    tb = slide.shapes.add_textbox(Inches(SRC_X), Inches(top), Inches(SRC_W),
                                  Inches(SRC_LINE_H * n_lines + 0.05))
    tf = tb.text_frame
    tf.word_wrap = True
    for side in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, side, 0)
    run = tf.paragraphs[0].add_run()
    run.text = text
    run.font.size = Pt(16)
    run.font.name = "Roboto"
    run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    tb.name = "Source"


def place(slide, title, fig_name, photo_name, source):
    """Created by JXP and Claude. Lay out one slide's figure, photo, source."""
    top = 0.95 if title_lines(title) == 1 else 1.5
    n_src = -(-len(source) // SRC_CHARS_PER_LINE)
    src_top = SRC_TOP_1LINE - SRC_LINE_H * (n_src - 1)
    bottom = src_top - 0.08
    avail_h = bottom - top

    fig_box_w = (X1 - X0) - (PHOTO_W + GAP if photo_name else 0)
    fw, fh = fit(FIGS / fig_name, fig_box_w, avail_h)
    fx = X0 + (fig_box_w - fw) / 2
    slide.shapes.add_picture(str(FIGS / fig_name), Inches(fx), Inches(top + (avail_h - fh) / 2),
                             Inches(fw), Inches(fh)).name = "Figure"
    if photo_name:
        pw, ph = fit(IMG / photo_name, PHOTO_W, avail_h * 0.9)
        slide.shapes.add_picture(str(IMG / photo_name), Inches(X1 - PHOTO_W + (PHOTO_W - pw) / 2),
                                 Inches(top + (avail_h - ph) / 2), Inches(pw), Inches(ph)).name = "Instrument"
    add_source(slide, source, src_top, n_src)


def main():
    """Created by JXP and Claude. Rebuild the deck and place B8 content."""
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-o", "--output", default=str(OUT))
    args = p.parse_args()

    sources = json.loads((FIGS / "sources.json").read_text())
    prs = build(TEMPLATE)
    placed = set()
    for i, slide in enumerate(prs.slides, start=1):
        titles = [sh.text_frame.text for sh in slide.shapes if sh.name == "Title"]
        if not titles or titles[0] not in PLACEMENTS:
            continue
        title = titles[0]
        fig_name, photo_name, source = PLACEMENTS[title]
        place(slide, title, fig_name, photo_name, source)
        notes = slide.notes_slide.notes_text_frame
        notes.text = notes.text + f"\n\nFull figure source ({fig_name}): {sources[fig_name]['source']}"
        placed.add(title)
        print(f"slide {i:2d}: {title[:45]:45s} <- {fig_name}" + (f" + {photo_name}" if photo_name else ""))
    missing = set(PLACEMENTS) - placed
    assert not missing, f"titles not found in skeleton: {missing}"

    prs.save(args.output)
    print(f"wrote {args.output}: {len(prs.slides)} slides, {os.path.getsize(args.output) / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
