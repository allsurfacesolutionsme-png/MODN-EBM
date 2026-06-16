Author: Justin Paul Cline

# MODN-EBM

MODN-EBM is a matrix-based energy-driven dynamical system where structured patterns, memory effects, and emergent modes arise from gradient descent on a coupled energy functional.

---

## Core Equations

Φ evolution:
∂t Φ = -δE/δΦ + F

Memory:
∂t M = γ(Φ - M)

Collision:
C = |∇Φ|²

---

## Features

- Energy-based field evolution
- Memory-coupled dynamics
- Emergent structure formation
- Matrix-based simulation
- Collision emerges from gradients

---

## Run

```bash
python simulation/modn_matrix.py
