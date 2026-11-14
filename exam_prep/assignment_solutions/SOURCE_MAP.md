# Original-source audit, published data and known assumptions

**Source questions:** 

- A1: `source_material/assignments/questions/PHYS4055 Assignment 1 (2).pdf` — 2 questions, 1 page.
- A2: `source_material/assignments/questions/PHYS4055 Assignment 2 (2).pdf` — 3 questions, 4 pages.
- A3: `source_material/assignments/questions/PHYS4055_A3.pdf` — 4 questions, 2 pages.
- A4: `source_material/assignments/questions/PHYS4055_A2-3.pdf` — 3 questions, 2 pages. The document is titled **Assignment 4** despite the filename.
- Official releases for A1/A2: `source_material/assignments/feedback_and_solutions/PHYS4055 Assignment 1 - SOLUTIONS.pdf` and `PHYS4055 Assignment 2 - SOLUTIONS.pdf`.

## External numeric references

| Used for | Reference and link | Treatment |
|---|---|---|
| `209Bi` charge radius (R_{\rm rms}=5.5211\,\mathrm{fm}) | Angeli & Marinova (2013), *Table of experimental nuclear ground state charge radii: An update*, Atomic Data and Nuclear Data Tables 99, 69–95 | Measured rms charge radius, converted to a uniform-sphere radius `sqrt(5/3) Rrms`. |
| Ti I (3d^24s^2) energies | [NIST Handbook: Energy Levels of Neutral Titanium](https://physics.nist.gov/PhysRefData/Handbook/Tables/titaniumtable5.htm) | Experimental compiled levels; abbreviated handbook lists eight `d²` levels, so no value is invented for `^1S_0`. |
| Atomic-units conversion | Hartree (=219474.63137~\mathrm{cm^{-1}}), standard CODATA conversion | Used to turn the `Ti ^1D_2` excitation into `0.0330578 E_h`. |
| Na I spectroscopic energies | [NIST Handbook: Energy Levels of Neutral Sodium](https://physics.nist.gov/PhysRefData/Handbook/Tables/sodiumtable5.htm) | Measured level energies used to check model level order and rough scale. |
| Na theoretical lifetimes | Froese Fischer *et al.* (2006), *Atomic Data and Nuclear Data Tables* **92**, 607–812, [NIST-hosted PDF](https://nlte.nist.gov/MCHF/all/p291.pdf), table for Na-like sequence at Z=11 | Theoretical values approx 3p 16.48 ns; 4s 38.25 ns; 3d 19.67 ns. **Not direct measured values.** |
| Na I 3p experimental lifetime | [*Atomic-Lifetime Measurements for Neutral and Ionized Sodium and Potassium*, JOSA 60 (1970) 1199](https://opg.optica.org/josa/abstract.cfm?uri=josa-60-9-1199) | Reports `17.3 ± 1.0 ns`, measurement of unresolved neutral Na I 3p doublet. |
| Coulomb direct/exchange closed-shell sums | Walter R. Johnson, *Atomic Structure Theory* (2007), Chapter 3, Eqs. 3.64 and 3.66, [publisher](https://doi.org/10.1007/978-3-540-68013-0) | Explicitly derive the shell-summed formulas, including spin and magnetic sums and Wigner–Eckart angular factors. |

## Numerical methods and caveats

**Assignment 3 Q1:** The table uses *first-order perturbation theory with point-nucleus nonrelativistic wavefunctions*. The comparison to Dirac energy shifts uses *point-nucleus* relativistic energies. A heavy (Z=83) ion has (Z\alpha \approx0.606), so relativistic finite-nuclear-size calculations require Dirac wavefunctions and should not be confused with the nonrelativistic table. The printed analytic leading formula is reproduced.

**Assignment 3 Q2:** Pauli antisymmetry gives exactly 45 (nd^2) microstates and nine (LSJ) levels. Ti I is chosen because it has the required neutral (3d^24s^2) ground configuration. NIST's abbreviated Ti handbook does not display a measured `^1S_0` value; no numerical energy is assigned to it.

**Assignment 3 Q3:** The closure approximation replaces *all* excited-state denominators with `E2-E1`, giving `16/(3Z^4)` rather than the exact hydrogen ground-state `4.5 a0³`. Polarizabilities in `cm³` are polarizability **volumes**.

**Assignment 3 Q4:** The nuclear magnetic-moment term is omitted by request. `F=0` cannot be assigned a standard electronic `g_F` through the expression with denominator `F(F+1)`; it has no first-order Zeeman splitting.

**Assignment 4 Q1:** The final Johnson equations require a sum over `m_b` and `mu_b` for a fully occupied `b` shell. The direct factor `2(2l_b+1)` differs from the exchange factor `1/(2l_a+1)`.

**Assignment 4 Q2:** Read the original figure on the second PDF page; the b–e plot geometries were inspected visually, not reconstructed from OCR. A field that reaches zero does not by itself ensure atoms remain in resonance. Even a linear resonant-velocity profile approaches zero only asymptotically in time.

**Assignment 4 Q3:** Nonrelativistic effective-potential model `Z=11, xi=1, b=0.4072`; use three radial orbital dipoles, angular weights `1/3`, `1`, `2/5`; no spin–orbit resolution. The reference comparison includes *theoretical* 4s/3d values rather than inventing missing directly measured lifetimes. The script prints a grid-refinement test.

## Scope completeness

Every subpart of every source assignment question is included. Numerical results are independently reproducible; official assessment solutions are available only for Assignments 1 and 2.
