# benchmarks/information_loss.py
import numpy as np
import pandas as pd
from Levenshtein import distance as levenshtein_distance

def compute_information_loss(original_series, anonymized_series):
    """
    Calcule la perte d'information entre deux colonnes.
    - Si les deux sont numériques, utilise RMSE normalisé.
    - Sinon, utilise la distance de Levenshtein normalisée.
    """

    is_numeric = (
        pd.api.types.is_numeric_dtype(original_series) and
        pd.api.types.is_numeric_dtype(anonymized_series)
    )

    if is_numeric:
        try:
            diff = original_series - anonymized_series
            rmse = np.sqrt(np.mean(diff**2))
            range_val = original_series.max() - original_series.min()
            return rmse / range_val if range_val != 0 else 0
        except Exception as e:
            print(f"⚠️ Erreur RMSE : {e}")
            return None

    # Sinon : calcul de distance de Levenshtein normalisée
    distances = []
    for o, a in zip(original_series, anonymized_series):
        o_str, a_str = str(o), str(a)
        if len(o_str) > 0:
            distances.append(levenshtein_distance(o_str, a_str) / len(o_str))
        else:
            distances.append(0)
    return np.mean(distances)
