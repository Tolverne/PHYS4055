#!/usr/bin/env python3
"""Extract searchable page-separated text from supplied PHYS4055 lecture slides."""
from pathlib import Path
import re
import fitz

ROOT = Path(__file__).resolve().parents[1]
src = ROOT / "source_material" / "lectures" / "slides_and_handouts"
outdir = ROOT / "exam_prep" / "source_extractions" / "lecture_slides"
outdir.mkdir(parents=True, exist_ok=True)
lines = ["# Source-linked slide-text index", "",
         "Machine-extracted text only; verify equations and figures against original PDFs.", "",
         "| Source file | Pages | Pages with text | Characters |",
         "|---|---:|---:|---:|"]
for pdf in sorted(src.glob("*.pdf")):
    with fitz.open(pdf) as doc:
        out = [f"Source: {pdf.relative_to(ROOT)}", f"Pages: {len(doc)}",
               "WARNING: Extracted PDF text can distort math and omit figures.", ""]
        usable = 0
        size = 0
        for i, page in enumerate(doc):
            text = page.get_text("text", sort=True)
            text = re.sub(r"\n{4,}", "\n\n", text)
            if len(text.strip()) > 40:
                usable += 1
            size += len(text)
            out.extend([f"====== PAGE {i+1} ======", text, ""])
        stem = re.sub(r"[^A-Za-z0-9_-]+", "_", pdf.stem).strip("_")
        (outdir / (stem + ".txt")).write_text("\n".join(out), encoding="utf-8")
        lines.append(f"| `{pdf.name}` | {len(doc)} | {usable} | {size} |")
(outdir / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
