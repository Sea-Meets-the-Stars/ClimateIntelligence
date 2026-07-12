#!/usr/bin/env python
"""Created by JXP and Claude.

Verify that downloaded PDF reports are complete and readable.

For every ``*.pdf`` in a directory this checks (1) the file starts with the
``%PDF`` magic bytes, (2) an ``%%EOF`` marker appears near the end (truncated
downloads usually lack it), and (3) the file opens and reports a page count via
pypdf when available. Intended for the IPCC reports staged in
``context/Reports/`` before they are copied to the shared Google Drive.

Usage::

    conda run -n ocean14 python bin/verify_pdf_reports.py [directory]
"""

# Imports at the top of the file (project coding guideline).
import sys
from pathlib import Path


def check_pdf(path):
    """Created by JXP and Claude.

    Check a single PDF for signs of truncation or corruption.

    Inputs
    ------
    path : pathlib.Path
        The PDF file to check.

    Outputs
    -------
    (bool, str)
        ``(ok, message)`` — ``ok`` is True when all checks pass; ``message``
        summarizes the result (size, page count, or the failure reason).
    """
    data_head = path.open("rb").read(8)
    # Check 1: PDF magic bytes at the start of the file.
    if not data_head.startswith(b"%PDF"):
        return False, "missing %PDF header (not a PDF or corrupt)"

    # Check 2: %%EOF marker in the last 2 KB — absent in truncated downloads.
    with path.open("rb") as fh:
        fh.seek(max(0, path.stat().st_size - 2048))
        tail = fh.read()
    if b"%%EOF" not in tail:
        return False, "no %%EOF marker near end (likely truncated)"

    # Check 3 (best effort): open with pypdf and count pages.
    try:
        from pypdf import PdfReader
        n_pages = len(PdfReader(str(path)).pages)
        return True, f"{path.stat().st_size/1048576:.0f} MB, {n_pages} pages"
    except ImportError:
        return True, f"{path.stat().st_size/1048576:.0f} MB (pypdf not installed; header/EOF ok)"
    except Exception as exc:  # pypdf parse failure means a damaged file
        return False, f"pypdf failed to parse: {exc}"


def main():
    """Created by JXP and Claude.

    Verify every PDF in the target directory and print a status table.

    Inputs
    ------
    (command line) optional directory argument; defaults to context/Reports/
    relative to the repository root.

    Outputs
    -------
    None. Prints one line per PDF; exits nonzero if any file fails.
    """
    repo_root = Path(__file__).resolve().parents[1]
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else repo_root / "context" / "Reports"

    pdfs = sorted(target.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs found in {target}")
        sys.exit(1)

    n_bad = 0
    for pdf in pdfs:
        ok, msg = check_pdf(pdf)
        status = "OK " if ok else "BAD"
        n_bad += (not ok)
        print(f"{status}  {pdf.name}: {msg}")

    sys.exit(1 if n_bad else 0)


if __name__ == "__main__":
    main()
