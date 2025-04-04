# methods/aggregation.py
import pandas as pd

def aggregate_numeric(series, bins=5):
    # Group numeric data into bins
    return pd.cut(series, bins=bins, labels=False)
