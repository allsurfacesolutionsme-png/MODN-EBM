import numpy as np

# -------------------------
# PARAMETERS
# -------------------------
N = 100
steps = 400
dt = 0.05

alpha = 0.6
gamma = 0.05
D = 0.8
mu = 0.2

# -------------------------
# STATE
# -------------------------
Phi = np.zeros((N, N))
M = np.zeros((N, N))

# seed structures
Phi[30, 30] = 2.0
Phi[70, 70] = -1.5


# -------------------------
# OPERATORS
# -------------------------
def laplacian(X):
    return (
        np.roll(X, 1, 0) +
        np.roll(X, -1, 0) +
        np.roll(X, 1, 1) +
        np.roll(X, -1, 1) -
        4 * X
    )


def grad_mag(X):
    gx = np.roll(X, -1, 0) - X
    gy = np.roll(X, -1, 1) - X
    return gx**2 + gy**2


# -------------------------
# ENERGY DERIVATIVE
# -------------------------
def dE_dPhi(Phi, M):
    return -D * laplacian(Phi) + mu * Phi + alpha * (Phi - M)


# -------------------------
# SIMULATION LOOP
# -------------------------
for t in range(steps):

    F = np.random.normal(0, 0.02, (N, N))

    Phi += dt * (-dE_dPhi(Phi, M) + F)
    M += dt * gamma * (Phi - M)

    if t % 50 == 0:
        print("step", t, "max", np.max(Phi))
