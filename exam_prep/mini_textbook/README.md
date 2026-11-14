# PHYS4055 mini-textbook — Atomic Physics and Quantum Optics

**[Open the complete illustrated mini-textbook PDF](PHYS4055_Mini_Textbook.pdf)**

This is the explanatory companion to the [15-page course overview](../reference_booklet/PHYS4055_Course_Overview_15pp.pdf). Unlike a formula sheet, it teaches the central physical ideas, develops the equations, and places worked examples beside the relevant theory.

## Organisation

| Part | Chapters | Main topics |
|---|---:|---|
| I. Quantum optics | 1–5 | Field quantisation, Fock/coherent/thermal light, photon statistics, HOM, detection, quadratures, Gaussian phase space and squeezing |
| II. Applications of optics | 6–12 | Photonic qubits, Bell states, teleportation, dense coding, BB84, optical loss, Kraus operations, conditional filtering, Langevin/Lindblad, Jaynes–Cummings/Tavis–Cummings, metrology |
| III. Atomic physics | 13–16 | Hydrogen radial equation, nuclear size, Hartree–Fock, (nd^2) terms, spin coupling, 3-j/CG, Wigner–Eckart, fine/hyperfine, Zeeman/Stark |
| IV. Atomic applications | 17–20 | E1/M1/E2 spectroscopy, radiative rates/lifetimes, laser cooling and MOT, atomic parity violation, EDM, atomic clocks |
| Appendices | 21–22 | Mathematics toolkit, selection rules, glossary, quick problem-type atlas, units, links to practice |

Each chapter includes intuitive explanations, displayed derivations, worked examples and concept checks. Optical and atomic sections use the source lecture notation and note whenever a convention can vary.

## Source files

- [Editable LaTeX master](main.tex) and [individual chapter sources](sections/).
- [Lecture-to-chapter source map](SOURCE_MAP.md).
- [Full revision index](../question_index.csv).
- [Worked examples](../worked_examples/), [assignment solutions](../assignment_solutions/), and [2023–2025 exam solutions](../past_exam_solutions/).

All content is independently written as a teaching guide based on the supplied course slides, transcripts, tutorials and assignment/exam topics. It is not an official university textbook or answer key. Original diagrams and handwritten lecture equations should be checked in the uploaded source PDFs.

## Compile

The [publishing workflow](../../.github/workflows/publish-mini-textbook.yml) compiles the PDF and validates the page count, chapter coverage and document structure. A standalone LaTeX build is also possible from this directory using `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.

The source uses the shared repository [`tex/common.tex`](../../tex/common.tex) definitions plus `tcolorbox`, `tikz` and `titlesec`. It remains editable chapter by chapter.
