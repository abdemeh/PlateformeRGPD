# benchmarks/re_identification.py

def compute_reidentification_risk(anonymized_series):
    """
    Calcule le risque de ré-identification en évaluant le pourcentage
    de doublons dans la colonne anonymisée.
    """
    duplicates = anonymized_series.duplicated().sum()
    total = len(anonymized_series)
    return (duplicates / total) * 100
