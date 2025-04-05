# methods/generalisation.py
import pandas as pd

def generalize_birth_date(series):
    # For example, group birth dates into decades (e.g., "1980s")
    return series.apply(lambda x: str(x)[:3] + "0s" if pd.notnull(x) else x)
