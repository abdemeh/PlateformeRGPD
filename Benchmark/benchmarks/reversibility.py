# benchmarks/reversibility.py

def compute_reversibility(original_series, anonymized_series):
    """
    Simule une attaque simple pour estimer la réversibilité.
    Retourne le pourcentage de lignes où la valeur anonymisée
    contient ou est contenue dans la valeur originale.
    """
    count_reversible = 0
    total = len(original_series)
    for o, a in zip(original_series, anonymized_series):
        o_str, a_str = str(o), str(a)
        if o_str in a_str or a_str in o_str:
            count_reversible += 1
    return (count_reversible / total) * 100
