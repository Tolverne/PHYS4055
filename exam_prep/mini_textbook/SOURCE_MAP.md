# PHYS4055 mini-textbook source and notation map

The mini-textbook is a pedagogical synthesis of the uploaded slides and transcripts. Its worked examples combine tutorial, assignment and past-exam styles without claiming to reproduce official marking schemes. The original lecture PDFs remain the primary authority for figure details, handwritten derivations and course-specific notation.

| Chapter | Topic | Source lecture packs |
|---|---|---|
| 1 | Field quantisation and photon modes | W1L1 Introduction, W1L2 Propagating Fields and Coherent States |
| 2 | Coherent, thermal, Fock and paired states | W1L2, W2L1 Photon Statistics; Assignment 1 |
| 3 | Beam splitters, HOM, photodetection and homodyne | W2L2 Beam Splitter, W2L3 Photodetection |
| 4 | Quadratures, uncertainty, quasiprobabilities | W1L3 Quadratures and Phase Space, W3L1 Quasiprobability |
| 5 | Squeezing and coherence | W3L2 Squeezing, W3L3 Coherence |
| 6 | Photonic qubits, Bloch representation and Bell states | W4L1, W4L2 |
| 7 | Teleportation, dense coding and BB84 | W4L2, W4L3; Assignment 2 |
| 8 | Optical channels, loss, dephasing and Kraus operators | W5L1 Quantum Optical Channels; Week 5 tutorials |
| 9 | Langevin, input--output and master equations | W5L2 Open Quantum Systems; 2024 and 2025 exams |
| 10 | Conditional optics, heralding and distillation | W5L3 Conditional Quantum Optics; Week 4/6 tutorials |
| 11 | Jaynes--Cummings and Tavis--Cummings models | W6L1, W6L2; Week 6 tutorial |
| 12 | Metrology and Fisher information | W6L3 Quantum Optical Metrology; 2023 exam |
| 13 | Hydrogen wavefunctions, radial equation and nuclear size | PHYS4055 Week 8; Assignment 3; 2023 exam |
| 14 | Many-electron structure, Hartree--Fock and term notation | Week 8; Assignments 3 and 4 |
| 15 | Angular momentum, CG, 3-j, Wigner--Eckart | Week 8; Assignment 4 |
| 16 | Fine/hyperfine, Zeeman/Stark effects | Week 8, PHYS4055 Week9 annotated; Assignment 3; 2025 exam |
| 17 | E1/M1/E2, Einstein coefficients and lifetimes | PHYS4055 Week9, PHYS4055 Week10; Assignment 4 |
| 18 | Rabi driving, optical molasses, slower and MOT | PHYS4055 Week10; 2025 exam; tutorials |
| 19 | Atomic parity violation, weak charge, EDM | PHYS4055 Week12 |
| 20 | Caesium and optical atomic clocks | Week13 |
| 21–22 | Mathematical toolkit, index and units | Cross-course revision and verified worked solutions |

## Important conventions and simplifications

- **Quadratures:** (x=a+a^\dagger), (p=i(a^\dagger-a)), ([x,p]=2i), vacuum variance (1). Other texts use a factor (1/\sqrt2).
- **Beam-splitter signs:** A self-consistent real or complex unitary convention is stated in each example. Global and port phases may differ among the original slide packs.
- **Optical channels:** Loss includes an environment vacuum mode to preserve canonical commutators.
- **Langevin:** The Fourier sign and input--output convention must be declared. Noise variance refers to correlations, not a mean-field square.
- **Angular momentum:** (l,s) for individual electrons; (L,S) for combined electronic angular momenta; (J=L+S); (F=I+J). 3-j and Wigner--Eckart reduced-element phase conventions differ between references.
- **Hyperfine:** The magnetic-dipole formula omits higher-rank terms. Weak-field (F,m_F) and strong-field (m_I,m_J) descriptions apply in different regimes.
- **E1/M1/E2:** Both angular rank and parity must be checked. Strict LS-coupling selection rules are approximations for mixed atomic states.
- **Sodium lifetime:** The main text illustrates the method; independent numerical results and precise assumptions are in the assignment-solutions code and booklet.
- **Cesium clock:** The physical clock transition is (F=3,m_F=0\leftrightarrow F=4,m_F=0). An apparent Week13 slide typo states (F=3\to F=3); do not copy that.
- **Fundamental symmetry tests:** The weak charge formula is schematic/tree-level; precision calculations require radiative and many-body corrections.
- **Fisher information:** Resource definitions and generator normalisation affect numerical prefactors; comparisons should state the physical parameter and measured observable.

The diagrams in this mini-textbook were drawn directly in LaTeX/TikZ to make the explanations easier to understand without reproducing the original slide artwork. All worked exercises are original teaching derivations or carefully adapted mathematical approaches from the course.
