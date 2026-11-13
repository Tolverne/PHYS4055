#!/usr/bin/env python3
"""Page-aware source index for tutorials, assignments and past exams."""
from pathlib import Path
import fitz, re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT / "exam_prep" / "source_extractions" / "problem_sources"
OUT.mkdir(parents=True,exist_ok=True)
PATHS=[
 ROOT / "source_material" / "tutorials",
 ROOT / "source_material" / "assignments" / "questions",
 ROOT / "source_material" / "assignments" / "feedback_and_solutions",
 ROOT / "source_material" / "past_exams"
]
index=["# Tutorial, assignment and exam source-text index","","Raw text extraction is for finding questions only: original PDF equations/figures are authoritative.","","| File | Pages | Text characters |","|---|---:|---:|"]
for directory in PATHS:
 for f in sorted(directory.rglob("*.pdf")):
  with fitz.open(f) as doc:
   p=[f"Source: {f.relative_to(ROOT)}",f"Pages: {len(doc)}","WARNING: math from PDFs needs visual verification."]
   n=0
   for i,page in enumerate(doc):
    txt=page.get_text("text",sort=True)
    n+=len(txt)
    p.extend(["",f"======== PAGE {i+1} ========",txt])
   name=re.sub("[^a-zA-Z0-9_-]+","_",str(f.relative_to(ROOT)).removesuffix(".pdf"))
   (OUT/(name+".txt")).write_text("\n".join(p),encoding="utf-8")
   index.append(f"| `{f.relative_to(ROOT)}` | {len(doc)} | {n} |")
(OUT/"INDEX.md").write_text("\n".join(index)+"\n",encoding="utf-8")
print("\n".join(index))
