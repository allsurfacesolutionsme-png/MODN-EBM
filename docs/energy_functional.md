# Energy Functional

The MODN-EBM system is governed by a global energy functional:

---

## Energy Definition

E[Φ, M] =
Σ(i,j) [
|∇Φ(i,j)|²
+ Φ(i,j)²
+ α(Φ(i,j) - M(i,j))²
+ βH(Φ)
]

---

## Term Breakdown

### 1. Gradient Energy
|∇Φ|²  
Controls spatial smoothness and interaction strength.

---

### 2. Stability Term
Φ²  
Prevents divergence of field values.

---

### 3. Memory Coupling
(Φ - M)²  
Forces system to retain past information.

---

### 4. Structural Regularization
H(Φ)  
Encourages coherent global structure formation.

---

## Behavior

Minimizing this energy produces:
- smooth field evolution
- stable attractors
- memory-dependent dynamics
- emergent structural patterns
