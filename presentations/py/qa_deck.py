"""Created by JXP and Claude.

B10 QA for the WMKO 2026 deck. Checks, per slide:
  1. slide count <= 40;
  2. edge margins: every shape we placed (pictures, text boxes, placeholder
     box) lies within 0.4" of the side edges and above 5.45" (the master's logo
     row and Kraw's own title box / slide number are exempt);
  3. fonts: every explicit typeface is Roboto (the Kraw master font); text that
     names no typeface inherits the master;
  4. a source line on every slide that shows a data figure (illustrations and
     placeholders are exempt);
  5. speaker notes present;
  6. numbered titles fit on one line (measured in Roboto Bold).
Exit status 1 if any check fails.

Usage:
    conda run -n ocean14 python presentations/py/qa_deck.py [deck.pptx]
"""
import sys

from pptx import Presentation
from pptx.util import Emu

from build_skeleton import TITLE_TEXT_W_IN, title_width_in
from slide_style import PRES

DECK = PRES / "2026_WMKO" / "WMKO_2026_Climate_Intelligence.pptx"
MAX_SLIDES = 40
EDGE = 0.4
BOTTOM = 5.45
PLACED = {"Figure", "Instrument", "Photo", "Caption", "Note", "Source", "Image placeholder"}
NO_SOURCE_NEEDED = {"Climate Intelligence", "6: AI may end grant competition", "8: The skills humans need",
                    "10: The Eye of Sauron"}


def inches(v):
    """Created by JXP and Claude. EMU -> inches."""
    return Emu(v).inches


def check(path):
    """Created by JXP and Claude. Run all checks; return a list of problems."""
    prs = Presentation(path)
    problems = []
    n = len(prs.slides)
    if n > MAX_SLIDES:
        problems.append(f"deck has {n} slides (> {MAX_SLIDES})")
    for i, slide in enumerate(prs.slides, start=1):
        title = next((sh.text_frame.text for sh in slide.shapes if sh.name == "Title"), "")
        names = [sh.name for sh in slide.shapes]
        for sh in slide.shapes:
            if sh.name in PLACED:
                l, t = inches(sh.left), inches(sh.top)
                r, b = l + inches(sh.width), t + inches(sh.height)
                if l < EDGE - 0.01 or r > 10 - EDGE + 0.01 or b > BOTTOM:
                    problems.append(f"slide {i} '{title[:30]}': {sh.name} outside margins "
                                    f"(l={l:.2f} r={r:.2f} b={b:.2f})")
            if sh.has_text_frame:
                for para in sh.text_frame.paragraphs:
                    for run in para.runs:
                        face = run.font.name
                        if face and face != "Roboto":
                            problems.append(f"slide {i}: font {face!r} in {sh.name}")
        if "Figure" in names and "Source" not in names and title not in NO_SOURCE_NEEDED:
            problems.append(f"slide {i} '{title[:30]}': data figure without a source line")
        if not slide.has_notes_slide or not slide.notes_slide.notes_text_frame.text.strip():
            problems.append(f"slide {i} '{title[:30]}': no speaker notes")
        if title[:3].rstrip(":").strip().isdigit() and ":" in title[:4]:
            size = next(sh for sh in slide.shapes if sh.name == "Title").text_frame.paragraphs[0].runs[0].font.size
            if size and title_width_in(title, size.pt) > TITLE_TEXT_W_IN:
                problems.append(f"slide {i} '{title[:30]}': title wraps at {size.pt:.0f} pt")
    print(f"{path.name}: {n} slides checked")
    return problems


def main():
    """Created by JXP and Claude. Print the QA report."""
    path = PRES.parent / sys.argv[1] if len(sys.argv) > 1 else DECK
    problems = check(path)
    for p in problems:
        print("FAIL", p)
    print("ALL CHECKS PASSED" if not problems else f"{len(problems)} problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
