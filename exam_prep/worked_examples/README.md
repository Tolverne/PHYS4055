# PHYS4055 — Worked Examples and Exam Methods

The companion to [the 15-page course overview](../reference_booklet/PHYS4055_Course_Overview_15pp.pdf).

## Deliverable

- **[Compiled worked-examples PDF](PHYS4055_Worked_Examples.pdf)** (built and committed by GitHub Actions).
- Editable LaTeX master: [`main.tex`](main.tex).
- Twenty individually editable, source-linked examples in [`sections/`](sections/).

## Coverage

| Part | Examples | Source question types |
|---|---|---|
| I. Quantum optics | QO-01 to QO-04 | Week 1–3 tutorials, Optics Assignment 1, 2025 exam Q3 |
| II. Applications of optics | OA-01 to OA-08 | Optics Assignment 2, Week 4–6 tutorials, 2025 exam Q4, Week 6 metrology slides |
| III. Atomic physics | AT-01 to AT-05 | Atomic Assignments 3 and 4, 2025 exam Q1, Week 8–9 lectures |
| IV. Applications of atomic physics | AA-01 to AA-03 | Week 9–13 slides, Atomic Assignment 4, 2025 exam Q2 |

Every example follows **recognise the problem → physical model → intermediate algebra → boxed result → physical check**. The final page provides a question-type finder.

The optics assignments have released solutions in `source_material/assignments/feedback_and_solutions/`, used when available. Atomic assignments without official solutions are independently derived worked-study examples, *not* presented as official marking guides. The booklet includes numeric examples explicitly labelled illustrative.

## PDF compilation

From this directory run `pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice (for contents). The [GitHub Actions build](../../.github/workflows/build-study-pdfs.yml) compiles automatically and provides a PDF artifact. A separate publishing workflow commits the final named PDF to `main`.

## Next extension

Add verified question-specific solutions for all 2023–2025 past papers to `../past_exam_solutions/`. Keep the original source figures visible when answering tasks that depend on level diagrams or handwritten equations.
