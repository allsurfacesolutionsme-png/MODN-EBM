# System Definition

MODN-EBM is defined on a discrete grid (i, j) where all state variables evolve over time t.

---

## State Variables

Φ(i, j, t): primary field  
M(i, j, t): memory field  
F(i, j, t): external input  

---

## System Evolution

The system evolves according to:

∂t Φ = -δE/δΦ + F(i,j,t)

∂t M = γ(Φ - M)

---

## Interpretation

- Φ: active system state
- M: slow memory trace
- F: external forcing or noise

---

## Principle

All structure emerges from energy minimization rather than explicit interaction rules.
