#!/usr/bin/env python3
"""Extract searchable text from supplied PHYS4055 exams and assignment questions.

Requires: pip install pymupdf
Run from repository root: python scripts/extract_exam_text.py
Never trust extraction alone for math glyphs, subscripts or diagrams.
"""
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ROOT / "source_material" / "past_exams",
    ROOT / "source_material" / "assignments" / "questions",
]
OUT = ROOT / "exam_prep" / "source_extractions"

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for folder in SOURCES:
        for source in sorted(folder.rglob("*.pdf")):
            category = "exam" if folder.name == "past_exams" else "assignment"
            year = source.parent.name if category == "exam" else ""
            destination = OUT / (f"{category}_{year}_{source.stem}.txt")
            with fitz.open(source) as pdf:
                sections = [f"Source: {source.relative_to(ROOT)}",
                            f"Pages: {len(pdf)}",
                            "WARNING: Verify all maths/diagrams against original PDF."]
                for i, page in enumerate(pdf):
                    sections.extend([f"\n===== PAGE {i+1} =====\n",page.get_text("text")])
            destination.write_text("\n".join(sections),encoding="utf-8")
            print(f"{source.relative_to(ROOT)} -> {destination.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
