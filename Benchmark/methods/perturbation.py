# methods/perturbation.py
import numpy as np

def perturb_numeric(series, noise_level=0.1):
    # Add Gaussian noise to numeric values
    return series + series * noise_level * np.random.randn(len(series))
