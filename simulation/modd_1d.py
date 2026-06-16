import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# PARAMETERS
# -------------------------
N = 200
steps = 300
dt = 0.05

alpha = 0.6
gamma = 0.05
D = 1.0
mu = 0.2

# -------------------------
# STATE VARIABLES
# -------------------------
Phi = np.zeros(N)
M = np.zeros(N)

# initial seed
Phi[80:120] = np.exp(-((np.arange(40)-20)**2)/50)


# -------------------------
# OPERATORS
# -------------------------
def laplacian_1d(x):
    return np.roll(x, 1) + np.roll(x, -1) - 2 * x


def gradient_1d(x):
    return np.roll(x, -1) - x


# -------------------------
# ENERGY DERIVATIVE (SIMPLIFIED)
# -------------------------
def dE_dPhi(Phi, M):
    return -D * laplacian_1d(Phi) + mu * Phi + alpha * (Phi - M)


# -------------------------
# SIMULATION
# -------------------------
for t in range(steps):

    F = np.random.normal(0, 0.02, N)

    dPhi = -dE_dPhi(Phi, M) + F
    Phi += dt * dPhi

    M += dt * gamma * (Phi - M)

    if t % 50 == 0:
        plt.plot(Phi)

plt.title("MODN-EBM 1D Evolution")
plt.show()
