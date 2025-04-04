# benchmarks/entropy_diversity.py
import numpy as np
from scipy.stats import entropy

def compute_entropy(series):
    counts = series.value_counts(normalize=True)
    return entropy(counts)

def compute_diversity(series):
    return series.nunique()
