import pandas as pd

def load_assets(path):
    df = pd.read_csv(path)
    assert "asset_id" in df.columns
    return df

def load_failures(path):
    df = pd.read_csv(path)
    assert "asset_id" in df.columns
    return df