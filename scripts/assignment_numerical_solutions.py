#!/usr/bin/env python3
"""PHYS4055 reproducible numeric assignment answers (2026).

Assignment 3 Q1: hydrogenic 209Bi finite-nuclear-size shifts and point-nucleus Dirac
comparisons. Assignment 4 Q3: nonrelativistic radial effective-potential model
of neutral Na, E1 dipole amplitudes, and 3p / 4s / 3d lifetimes.

Run: python -m pip install numpy scipy
     python scripts/assignment_numerical_solutions.py
All energies and radial distances are in atomic units unless stated.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal
from scipy.special import eval_genlaguerre

ALPHA = 1 / 137.035999084
TAU_AU_S = 2.4188843265857e-17
BOHR_FM = 52917.7210903
EV_PER_HARTREE = 27.211386245988
RMS_BI209_FM = 5.5211  # Angeli & Marinova (2013), rms nuclear charge radius.


def hydrogen_radial(r: float, n: int, l: int, Z: int) -> float:
    rho = 2.0 * Z * r / n
    prefactor = (2 * Z / n)**1.5 * math.sqrt(
        math.factorial(n-l-1) / (2 * n * math.factorial(n+l))
    )
    return prefactor * math.exp(-rho/2) * rho**l * eval_genlaguerre(n-l-1, 2*l+1, rho)


def fns_deltaV(r: float, Z: int, R: float) -> float:
    if r >= R: return 0.0
    return Z*(1/r - 3/(2*R) + r*r/(2*R**3))


def hydrogenic_bi_shifts():
    Z = 83
    R = math.sqrt(5/3)*RMS_BI209_FM/BOHR_FM
    print("ASSIGNMENT 3 Q1. 209Bi nuclear-size shifts")
    print(f"Uniform nuclear radius = {R:.10g} Bohr = {R*BOHR_FM:.7f} fm")
    print("State    finite-size (Ha)    finite-size (eV)   Dirac minus Schrodinger (Ha)")
    for n,l,label,kappa in [(1,0,"1s",-1),(2,1,"2p1/2",+1),
                              (3,2,"3d3/2",+2),(3,2,"3d5/2",-3)]:
        integral,_ = quad(
            lambda x: abs(hydrogen_radial(R*x,n,l,Z))**2
                * (R*x)**2 * fns_deltaV(R*x,Z,R) * R,
            1.0e-12, 1.0, epsabs=1e-20, epsrel=1e-12, limit=200)
        mc2 = 1/ALPHA**2
        gam = math.sqrt(kappa*kappa-(Z*ALPHA)**2)
        E_dirac = mc2*((1+(Z*ALPHA)**2/(n-abs(kappa)+gam)**2)**-0.5-1)
        E_sch = -Z**2/(2*n*n)
        print(f"{label:7} {integral:17.10e} {integral*EV_PER_HARTREE:18.10e} {E_dirac-E_sch:22.9f}")
    leading = 2*Z**4*R**2/5
    print("1s small-R leading shift:",f"{leading:.10f} Hartree")


def na_states(step=0.012, r_max=120.0):
    """Radial finite-difference solver with Dirichlet boundaries at r=0, r=rmax.

    u(r)=r R_nl(r), integral |u|² dr=1.
    Effective potential V=-Z/r+(Z-xi)(1-exp(-r/b))/r, Z=11, xi=1, b=.4072.
    Retain states labelled by n and l, using the radial node index n-l-1.
    """
    Z,xi,b = 11,1,0.4072
    r = np.arange(1,int(r_max/step)+1,dtype=float)*step
    V = -xi/r - (Z-xi)*np.exp(-r/b)/r
    wanted = {"3s":(0,2), "4s":(0,3), "3p":(1,1), "3d":(2,0)}
    states={}
    for l in [0,1,2]:
        diagonal = 1/step**2 + V + l*(l+1)/(2*r**2)
        offdiagonal = np.full(len(r)-1,-1/(2*step**2))
        energies, vectors=eigh_tridiagonal(
            diagonal,offdiagonal,select="i",select_range=(0,4))
        for label,(wanted_l,k) in wanted.items():
            if l==wanted_l:
                u=vectors[:,k]/math.sqrt(step)
                states[label] = (float(energies[k]),u)
    return r,states


def sodium_lifetimes(step=0.012, r_max=120.0):
    r,states=na_states(step,r_max)
    print("\nASSIGNMENT 4 Q3. Na effective-potential E1 lifetimes")
    print("Radius step =",step,"a0; r_max =",r_max,"a0")
    for name in ("3s","3p","4s","3d"):
        print(f"{name:4} E={states[name][0]:.9f} Ha")
    print("Transition  radial dipole(a0)  omega(Ha)    A(s^-1)       lifetime(ns)")
    for src,dst,factor in [("3p","3s",1/3),("4s","3p",1),("3d","3p",2/5)]:
        E_i,u_i=states[src];E_f,u_f=states[dst]
        radial=float(np.trapezoid(u_i*u_f*r,dx=step))
        omega=E_i-E_f
        assert omega>0, "Final state must have lower energy"
        A=(4/3)*ALPHA**3*(omega**3)*factor*radial**2/TAU_AU_S
        tau_ns=1e9/A
        print(f"{src}->{dst:2} {radial:18.7f} {omega:12.8f} {A:11.4e} {tau_ns:14.5f}")
    print("Reference theoretical lifetimes: Na 3p ~=16.48 ns, 4s ~=38.25 ns,")
    print("3d ~=19.7 ns (Froese Fischer et al., ADND Tables 92 [2006], Z=11).")
    print("Na 3p historical direct measurement: 17.3 +/- 1.0 ns")
    print("(JOSA 60, 1199 [1970]: Atomic-Lifetime Measurements for Neutral")
    print("and Ionized Sodium and Potassium; experimental Na I 3p result).")


if __name__=="__main__":
    hydrogenic_bi_shifts()
    sodium_lifetimes()
    print("\nGrid-convergence check:")
    for h in [0.024, 0.016,0.012,0.010]:
        print(f"--- h = {h} ---")
        sodium_lifetimes(h, 120.0)
