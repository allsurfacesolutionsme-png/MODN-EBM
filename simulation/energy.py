import numpy as np

def energy(Phi, M, alpha=0.6, mu=0.2):

    grad_x = np.roll(Phi, 1, 0) - Phi
    grad_y = np.roll(Phi, 1, 1) - Phi

    grad = np.sum(grad_x**2 + grad_y**2)
    stability = np.sum(Phi**2)
    memory = np.sum((Phi - M)**2)

    return grad + stability + alpha * memory + mu * stability
