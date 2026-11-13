# PHYS4055 — Four-part, approximately 15-page course overview

**Master:** `main.tex`. **Source files:** `pages/01_course_guide.tex` through `pages/15_atomic_clocks_and_index.tex`.

**Purpose:** one concise study document that links each main physical idea to formulas, how they are derived/used, and quick worked methods. It is distinct from the separate formula sheets, worked examples and detailed solutions.

| Part | Pages | Coverage |
|---|---:|---|
| I. Quantum optics | 2–4 | Field quantisation, coherent/Fock/thermal light, photon statistics, beam splitters, photodetection, phase space, squeezing and coherence |
| II. Applications of optics | 5–9 | Photonic qubits, Bell states, teleportation, dense coding, BB84/CV-QKD, loss, Lindblad/Langevin, conditional operations, Jaynes–Cummings/Tavis–Cummings, metrology |
| III. Atomic physics | 10–12 | Central field, radial atoms, Hartree–Fock, exchange, angular momentum, 3-j/Wigner–Eckart, fine/hyperfine, Zeeman/Stark and isotope shifts |
| IV. Applications of atomic physics | 13–15 | Selection rules, Einstein coefficients and lifetimes, laser cooling/MOT, parity violation, EDMs, and atomic clocks |

Pages have an intentional one-topic-per-page design for quick open-book navigation. Page 15 contains a question-type index.

See [`SOURCE_MAP.md`](SOURCE_MAP.md) for the original lecture slide audit and known extraction cautions.

**To compile:** run `pdflatex -halt-on-error main.tex` in this directory; or open the [GitHub Actions PDF build](https://github.com/Tolverne/PHYS4055/actions/workflows/build-study-pdfs.yml) and download the `PHYS4055-course-overview` artifact.

**Editorial conventions:** optics quadratures `x=a+a†`, `p=i(a†−a)` with vacuum variance 1; atom quantum numbers `l,s,L,S,J,I,F`; operator parity and angular selection rules are both required; calculate all decay channels for a lifetime. Lecture slides and transcripts inform the notes, but an extracted OCR equation is never used uncritically.

**Status:** first source-grounded overview built 13 November 2026. Further formula-by-formula validation against individual handwritten equations and all tutorial/assignment answers remains useful before the exam.
