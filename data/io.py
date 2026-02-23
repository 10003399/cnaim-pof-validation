import pandas as pd

def load_assets(path):
    return pd.read_csv(path)

def load_failures(path):
    return pd.read_csv(path)