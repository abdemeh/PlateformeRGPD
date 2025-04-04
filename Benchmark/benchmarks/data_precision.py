# benchmarks/data_precision.py
import numpy as np
import pandas as pd

def compute_data_precision(original_series, anonymized_series):
    """
    Calcule la précision des données :
    - Si données numériques : retourne la corrélation (absolue) * 100
    - Sinon : retourne le taux de valeurs identiques (%)
    """
    is_numeric = (
        pd.api.types.is_numeric_dtype(original_series) and
        pd.api.types.is_numeric_dtype(anonymized_series)
    )

    if is_numeric:
        try:
            correlation = np.corrcoef(original_series, anonymized_series)[0, 1]
            return abs(correlation)
        except Exception as e:
            print(f"Erreur de corrélation : {e}")
            return 0.0
    else:
        exact_matches = (original_series == anonymized_series).sum()
        total = len(original_series)
        return (exact_matches / total)
