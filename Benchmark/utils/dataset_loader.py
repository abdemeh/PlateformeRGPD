# utils/dataset_loader.py
import pandas as pd
import os

def load_dataset(csv_path):
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    else:
        raise FileNotFoundError(f"Dataset not found: {csv_path}")
