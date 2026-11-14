# PHYS4055 — Complete 2026 Assignment Solutions

**[Open the compiled PDF](PHYS4055_All_Assignments_Worked_Solutions.pdf)**  
[Editable LaTeX master](main.tex) · [All 12 question files](sections/) · [Source and numerical audit](SOURCE_MAP.md)

This booklet contains detailed solutions to **every question and subpart** in all four uploaded PHYS4055 assignments. It includes derivations, clear calculation sequences, physical interpretation, data comparisons and a complete numerical-code appendix.

| Assignment | Questions | Coverage | Verification |
|---|---:|---|---|
| **1. Introduction to Quantum Optics** | 2 | Thermal reductions of squeezed vacuum; correlations, heralding; Fock/coherent states through beam splitters | Cross-checked with released assignment solutions |
| **2. Quantum Optics Applications** | 3 | Bell basis and partial traces; dense coding and linear-optical Bell detection; BB84, losses and QBER | Cross-checked with released assignment solutions |
| **3. Atomic Physics** | 4 | Nuclear-size shifts for hydrogen-like bismuth; equivalent (d^2) terms and NIST Ti I; Stark polarisability; electronic/nuclear Landé factors | Independently derived, with numerical and NIST checks |
| **4. Atomic Applications** | 3 | Full Hartree–Fock direct/exchange shell sums matching Johnson Eqs. 3.64 and 3.66; Zeeman-slower b–e diagrams; calculated sodium lifetimes with reference comparisons | Independently derived, original diagrams checked; numeric code provided |

## Reproducible numeric results

Run from the root of this repository:

```powershell
python -m pip install numpy scipy
python scripts/assignment_numerical_solutions.py
```

The script includes:

- First-order finite-nucleus integrals for (1s), (2p) and (3d) of hydrogen-like (^{209}mathrm{Bi}), compared with a Dirac point-nucleus calculation.
- A finite-difference radial Schrödinger eigensolver for Na, using `V(r) = -1/r - 10 exp(-r/0.4072)/r` (atomic units).
- Wavefunction normalisation, transition energies, radial dipole integrals, E1 angular factors and radiative lifetimes of Na (3p), (4s), (3d).
- A basic grid-refinement check.

## Editorial notes

Assignments **1 and 2 have official released solutions** stored under `../../source_material/assignments/feedback_and_solutions/`. The booklet explains those independently and checks the results against them.

**No official solutions for Assignments 3 and 4** were found in the uploaded repository. Their solutions in this booklet are independently derived and are not represented as official marking guidance.

The original Assignment 4 Zeeman-slower panels were visually inspected. Panel b can slow over a longer length, c demands an excessive initial deceleration, d contains a physically untrackable rising field portion, and e is sensitive to rapid field fluctuations. The actual outcome may depend on field calibration, effective linewidth and capture range.

For Assignment 4 sodium lifetime data, comparisons to published **theoretical** reference values are labelled as such, distinct from a verified **direct experimental** measurement of the 3p lifetime. See the source audit for URLs and limitations.

## PDF generation

The [GitHub PDF build](../../.github/workflows/build-study-pdfs.yml) and [published assignment book workflow](../../.github/workflows/publish-assignment-solutions.yml) compile and validate the book. To compile locally from this directory, run `pdflatex -halt-on-error main.tex` twice.

Each question is an individually editable `.tex` file so future official answers or corrections can be applied without rewriting the whole booklet.
