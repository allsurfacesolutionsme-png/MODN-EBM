import numpy as np

class MemoryField:
    def __init__(self, shape, gamma=0.05):
        self.M = np.zeros(shape)
        self.gamma = gamma

    def update(self, Phi, dt):
        self.M += dt * self.gamma * (Phi - self.M)
        return self.M
