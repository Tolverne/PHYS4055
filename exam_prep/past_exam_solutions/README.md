# PHYS4055 — Complete 2023–2025 past-examination solutions

**[Open the compiled, verified PDF](PHYS4055_Exams_2023_2025_Worked_Solutions.pdf)**  
[Editable LaTeX master](main.tex) · [12 individually editable question files](sections/) · [Original question and caveat map](SOURCE_MAP.md)

## Scope

All **12 questions** and every subpart across the 2023, 2024 and 2025 Semester 2 PHYS4055 exams are worked out step-by-step, including questions students were instructed to omit during an actual sitting. Each solution includes formulas, intermediate algebra, physical interpretation and an independent check.

| Exam | Questions | Content |
|---|---|---|
| **2023** | Q1–Q4 | Kerr-like nonlinear optical cat state; hydrogen/helium; squeezed-coherent Mach–Zehnder; Raman transitions |
| **2024** | Q1–Q4 | `^3D` spin–orbit; Zeeman absorption sensor; HOM and number statistics; lossy cavity and dual-rail gates |
| **2025** | Q1–Q4 | Hyperfine/Zeeman; Yb spectroscopy and cooling; NOON states; parametric cavity squeezing and Bell keys |

## Key source/convention notes

- **2023 Q1:** (p) is taken as a **positive even** integer for the cat-state special time; zero/negative exponents would need special treatment.
- **2023 Q3:** The squeezed-coherent-state **operator ordering** is stated explicitly. For the specified one-squeezed-input/one-vacuum-input and difference detection at (phi=pi/2), the noise equals the total input mean photon number, so squeezing does not automatically beat shot noise at equal energy.
- **2023 Q4:** The (pi)-pulse formula follows from the **resonant/constant-phase Bloch equations** in the paper. Finite detuning modifies those equations. No cavity response (alpha(delta)) is supplied, so the paper alone does not determine a unique general off-resonant pulse solution.
- **2024 Q2:** The optimal magnetic bias includes the factor (1/(2sqrt3|kappa|)). Omitting (kappa) would be dimensionally incorrect.
- **2025 Q2:** The original **Yb energy-level diagram** is needed to assign every arrow. Strict LS E1 rules and weak intercombination transitions are distinguished; numerical slowing assumes an explicit rms thermal speed and gives an alternative if a different speed convention is expected.
- **2025 Q4:** A noise spectral variance is not the square of a field's mean expectation; the output squeezing calculation correctly uses the fluctuation transfer coefficient.

These are independently derived worked-study solutions, not officially issued past-exam marking schemes. The original papers are in `../../source_material/past_exams/{2023,2024,2025}/`. For graphical source verification, selected original PDF pages were rendered in `../source_extractions/exam_figures/`.

## Build

The repo's [Build PHYS4055 printable revision PDFs](../../.github/workflows/build-study-pdfs.yml) GitHub Actions workflow produces a PDF artifact. The [publish workflow](../../.github/workflows/publish-past-exam-solutions.yml) verifies the question count, compiles the PDF and commits it directly to `main`.

To compile locally, run `pdflatex -interaction=nonstopmode -halt-on-error main.tex` **twice** inside this folder.

## Exam preparation

Print the 15-page overview, the worked-examples booklet and this past-paper book. Attempt a paper under timed conditions before consulting its solutions; then add errors/approaches that were difficult to `../mistakes_and_gaps/`.
