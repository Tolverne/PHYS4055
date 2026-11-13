# PHYS4055 — Atomic Physics and Optics | 2026 Open-Book Exam Revision

## New: complete 2023–2025 past-exam solutions

- **[Open the full worked past-exam PDF](exam_prep/past_exam_solutions/PHYS4055_Exams_2023_2025_Worked_Solutions.pdf)** — all 12 questions, all subparts, original paper references and exam-method checks.
- [Editable LaTeX solutions, separate files per question](exam_prep/past_exam_solutions/sections/)
- [Source and convention audit](exam_prep/past_exam_solutions/SOURCE_MAP.md)
- [2023–2025 question index](exam_prep/question_index.csv)

## New: complete 20-example worked booklet (2026)

- **[Open the compiled 22-page worked examples PDF](exam_prep/worked_examples/PHYS4055_Worked_Examples.pdf)** — full step-by-step calculations across all four course parts.
- [LaTeX master and twenty editable example sections](exam_prep/worked_examples/)
- [Question-to-source audit](exam_prep/worked_examples/SOURCE_MAP.md) — identifies tutorial, released-assignment and past-exam sources.
- [Page-preview contact sheet](exam_prep/worked_examples/PHYS4055_Worked_Examples_Contact_Sheet.jpg)

## New: four-part, 15-page source-reviewed course overview

- **[Open the compiled 15-page PDF](exam_prep/reference_booklet/PHYS4055_Course_Overview_15pp.pdf)** — physical ideas, key equations, common methods and a quick question-type index, organised across optics, applications of optics, atomic physics and applications of atomic physics.
- [Editable LaTeX source (15 topic pages)](exam_prep/reference_booklet/pages/)
- [Lecture slide/transcript source map and verification notes](exam_prep/reference_booklet/SOURCE_MAP.md)
- [15-page thumbnail contact sheet](exam_prep/reference_booklet/PHYS4055_Course_Overview_Contact_Sheet.jpg)


**Exam target: Friday 20 November 2026** (confirm exact time and permitted materials against the official 2026 exam instructions).

This repository follows the workflow of [PHYS7045](https://github.com/Tolverne/PHYS7045): preserve the source material, build clear topic notes, solve past papers in full, then assemble searchable/printable LaTeX reference documents.

## Where to upload original files

| Material | Upload destination |
|---|---|
| Course profile, learning objectives, official formula sheet and exam instructions | `source_material/course_information/` |
| Unsorted lecture slides or handwritten notes | `source_material/lectures/notes_to_identify/` |
| Identified lecture slides and handouts | `source_material/lectures/slides_and_handouts/` |
| Lecture transcripts (.txt) | `source_material/lectures/transcripts/` |
| Assignment question sheets | `source_material/assignments/questions/` |
| Submitted assignment answers | `source_material/assignments/my_solutions/` |
| Marked solutions and feedback | `source_material/assignments/feedback_and_solutions/` |
| Past papers | `source_material/past_exams/2023/`, `2024/`, `2025/` (or another year) |

Upload originals without renaming them initially; the lecture index will map filenames to topics. **The repository is public as of 12 Nov 2026.** University-provided PDFs/transcripts, exam papers, personal feedback and your assignment solutions may not be appropriate for public redistribution. Consider making the repository **private before uploading** restricted or copyrighted material.

## Study outputs

| Output | Path | Purpose |
|---|---|---|
| Course overview | `exam_prep/reference_booklet/` | Concept-first, topic-linked printable explanations |
| Worked examples | `exam_prep/worked_examples/` | Detailed exam-style methods and solved calculations |
| Formula and method sheet | `exam_prep/formula_sheets/` | Compact navigation: formula → method → checks |
| Past-paper solution book | `exam_prep/past_exam_solutions/` | Worked 2023–2025 paper solutions; no invented answers |
| Assignment methods | `exam_prep/assignment_formula_methods/` | Generalise 2026 assignment methods into reusable patterns |
| Topic notes | `notes/` | Deeper explanations keyed to the lecture index |
| Practice questions | `exam_prep/practice_questions/` | Retrieval practice and timed question sets |
| Mistake log | `exam_prep/mistakes_and_gaps/` | Correct misunderstandings before exam day |
| Extracted text | `exam_prep/source_extractions/` | Searchable helper text, never authoritative for symbols |
| Diagrams | `assets/` | Figures, energy level diagrams and angular-momentum diagrams |

## Working plan, 12–20 November

1. **12–13 Nov:** establish the repo; upload and index the course profile, lecture transcripts/notes, 2025 paper and assignment sources.
2. **13–15 Nov:** audit the entire 2025 paper question-by-question; draft complete solutions and collect recurring methods.
3. **16–17 Nov:** create the course overview, worked-example bank and assignment-to-exam method notes; spot-check against the lectures.
4. **18 Nov:** consolidate a five-page formula/method sheet; work backwards from 2024/2023 past questions where supplied.
5. **19 Nov:** run a timed mock; polish the error log and print/test the open-book navigation.
6. **20 Nov:** final reference check against authorised exam conditions.

This is a priority plan, not a claim that the uploaded source material has already been reviewed.

## Provisional topic map

The topics below are drawn from known PHYS4055 revision/assignment discussions; **confirm coverage** after indexing source lectures:

1. Angular momentum addition, term symbols, Clebsch–Gordan coefficients
2. Fine structure, hyperfine structure and magnetic-field regimes
3. Spherical tensors, Wigner–Eckart theorem and 3-j symbols
4. Electromagnetic multipoles, parity and transition selection rules
5. Electron configurations, antisymmetry and Hund's rules
6. Radial atomic structure, nuclear-size effects and model potentials
7. Electric dipole strengths, radiative rates and lifetimes
8. Other course optics topics — to be named after lecture audit

## Build PDFs

LaTeX documents are organised as small master files importing independently editable sections. From the repository root, on a machine with TeX Live:

```bash
cd exam_prep/reference_booklet && pdflatex -halt-on-error main.tex
cd ../worked_examples && pdflatex -halt-on-error main.tex
cd ../formula_sheets && pdflatex -halt-on-error main.tex
cd ../past_exam_solutions && pdflatex -halt-on-error main.tex
```

A GitHub Actions workflow also compiles these on push or manual dispatch; download PDFs from the **Actions** run artifacts. PDFs are not automatically pushed into source control.

## Editorial rules

- Every numerical result and diagram in worked past-exam solutions must be checked against the **original exam PDF**.
- Cite source filename, year, question number and lecture number when known; mark unverified details as `TODO (verify source)`.
- Use explicit quantum numbers, basis conventions, units, parity, sign conventions and triangle/selection rules.
- Each worked problem: recognise question → governing equation → calculation → result → physical check → common mistake.
- Do not silently infer exact syllabus, allowed materials or exam marks from past years.

See [exam preparation plan](exam_prep/EXAM_REFERENCE_PLAN.md) and [source index](source_material/lectures/lecture_index.csv).
