# MODN-EBM EQUATIONS

## 1. State Variables

Φ(i, j, t) ∈ ℝ  
M(i, j, t) ∈ ℝ  

---

## 2. Energy Functional

E[Φ, M] =
Σ(i,j) [
|∇Φ(i,j)|²
+ Φ(i,j)²
+ α (Φ(i,j) - M(i,j))²
+ β H(Φ)
]

---

## 3. Evolution Equations

### Main field evolution:

∂t Φ(i,j) = -δE/δΦ(i,j) + F(i,j,t)

---

### Memory evolution:

∂t M(i,j) = γ (Φ(i,j) - M(i,j))

---

## 4. Derived Quantities

### Collision field:

C(i,j) = |∇Φ(i,j)|²

---

### Gradient definition:

∇Φ(i,j) ≈
(Φ(i+1,j) - Φ(i,j),
 Φ(i,j+1) - Φ(i,j))

---

## 5. Emergent Modes

C^(k)(i,j,t) represent persistent structural patterns satisfying:

|∇Φ|² > θ

These are not explicitly defined but emerge from system dynamics.

---

## 6. Parameters

α → memory coupling strength  
β → structural regularization strength  
γ → memory update rate  
F → external forcing function  
