# Source audit — worked PHYS4055 examinations

These solutions use the original uploaded exam papers, not reconstructions from prior chat. All question headings and marks are based on the source papers.

| Year | Original paper | Printed pages | Solutions |
|---|---|---:|---|
| 2023 | `source_material/past_exams/2023/Semester_Two_Examinations_2023_PHYS4055 (8).pdf` | 2–6 | `sections/2023_q1.tex` to `2023_q4.tex` |
| 2024 | `source_material/past_exams/2024/Semester_Two_Examinations_2024_PHYS4055.pdf` | 2–5 | `sections/2024_q1.tex` to `2024_q4.tex` |
| 2025 | `source_material/past_exams/2025/Semester_Two_Examinations_2025_PHYS4055.pdf` | 2–5 | `sections/2025_q1.tex` to `2025_q4.tex` |

## Important verification assumptions

1. `2023 Q1`: Cat-state time requires positive even nonlinear exponent (p). Number statistics remain Poissonian despite quantum coherences.
2. `2023 Q2`: Sketch displays qualitative helium term separation; original paper does not provide exact term energies.
3. `2023 Q3`: Squeezed-coherent-state convention (D(\alpha)S(\xi)|0\rangle) declared; difference-output noise at the balanced operating phase is (N). Ordering (SD) yields a different expression for (N), not a change to the general noise argument.
4. `2023 Q4`: Separates on-resonance Bloch pulse-area derivation from the genuinely detuned Hamiltonian. The latter cannot be uniquely solved from a cavity response that was not given.
5. `2024 Q2`: An AC-drive term requires correct dimensions. Optimised bias field must be (±\sqrt{\gamma^2+8\Omega^2}/(2\sqrt3|\kappa|)). This is an explicit mathematical correction if the original printed target lacks those factors.
6. `2024 Q4`: At critical coupling (γ_1=γ_2) there is zero **coherent reflection** at resonance, but loss-port vacuum noise remains.
7. `2025 Q1`: Weak-field (F,m_F) and strong-field (m_I,m_J) bases are distinct. Rank-2 quadrupole tensor cannot have a diagonal matrix element at (J=1/2).
8. `2025 Q2`: The source contains a rasterised energy-level diagram. Rough OCR of the diagram was retained under `../source_extractions/exam_figures/diagram_labels/yb_2025.txt`; check every term label against the **original PDF image**. Exact strict LS arrows are distinguished from intercombination E1. The standard ({}^1S_0\leftrightarrow{}^3P_0) clock line is physically valid, even if an individual diagram displays a different subset. Numerical beam speed is not prescribed; solutions state the 3D rms convention and the Maxwell most-probable alternative.
9. `2025 Q3`: Balanced beam-splitter sign convention comes directly from the paper.
10. `2025 Q4`: The prompt's variance notation conflates μsquared and fluctuation spectrum; the latter determines squeezing.

Original question PDFs are the authority for all printed diagrams, signs and constants. The full searchable text index lives under `../source_extractions/problem_sources/`; rendered source page previews under `../source_extractions/exam_figures/` are for local checking, not substitutes for the originals.

## Editorial status

- **Source questions matched:** 12 of 12.
- **All requested parts drafted:** yes.
- **Mechanical PDF compilation:** checked by GitHub Actions.
- **Official marking-scheme comparison:** not available; these are independent solutions.
- **Specific figure/text caveats documented:** yes.
