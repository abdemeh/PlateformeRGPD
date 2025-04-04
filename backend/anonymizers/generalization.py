import pandas as pd

def apply_generalization(df, column, generalization_map=None):
    if generalization_map:
        # Manuel : dictionnaire fourni par le frontend
        def generalize(value):
            return generalization_map.get(str(value), value)
        df[column] = df[column].apply(generalize)
        return df

    # Automatique
    col_lower = column.lower()

    if col_lower == "city" and "country" in df.columns:
        df[column] = df["country"]
        return df

    if "date" in col_lower:
        # Extraire l'année uniquement
        def extract_year(val):
            try:
                return pd.to_datetime(val).year
            except:
                return val
        df[column] = df[column].apply(extract_year)
        return df

    if col_lower == "age":
        def age_group(val):
            try:
                age = int(val)
                start = (age // 10) * 10
                return f"{start}-{start+9}"
            except:
                return val
        df[column] = df[column].apply(age_group)
        return df

    if col_lower in ["revenue", "income", "salaire"]:
        def adaptive_range(val):
            try:
                num = float(val)
                if num < 100:
                    size = 10
                elif num < 1000:
                    size = 100
                elif num < 10000:
                    size = 1000
                else:
                    size = 10000
                low = int(num // size * size)
                high = low + size - 1
                return f"{low}-{high}"
            except:
                return val
        df[column] = df[column].apply(adaptive_range)
        return df

    # Par défaut : inchangé
    return df
