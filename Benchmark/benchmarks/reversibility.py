from Levenshtein import distance as lev_distance

def compute_reversibility(original_series, anonymized_series, threshold=0.3):
    """
    Calcule la réversibilité entre les séries originales et anonymisées en utilisant la distance de Levenshtein.
    
    Pour chaque paire, on calcule un ratio de similarité normalisé (1 - distance / longueur maximale).
    Si ce ratio est supérieur ou égal au seuil (par défaut 0.3), la ligne est considérée réversible.
    
    Retourne un tuple :
        - Pourcentage de lignes réversibles.
        - Similarité moyenne (en %) sur l'ensemble des lignes.
    """
    total = len(original_series)
    count_reversible = 0
    total_ratio = 0.0

    for o, a in zip(original_series, anonymized_series):
        o_str, a_str = str(o), str(a)
        max_len = max(len(o_str), len(a_str))
        if max_len == 0:
            ratio = 1.0  # Cas où les deux chaînes sont vides
        else:
            ratio = 1 - lev_distance(o_str, a_str) / max_len
        total_ratio += ratio
        # Debug : afficher le ratio pour une vérification
        # print(f"Original: {o_str} / Anonymisé: {a_str} → Ratio: {ratio}")
        if ratio >= threshold:
            count_reversible += 1

    perc_reversible = (count_reversible / total) * 100
    avg_similarity = (total_ratio / total) * 100
    return perc_reversible, avg_similarity
