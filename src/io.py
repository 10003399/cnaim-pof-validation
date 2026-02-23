import pandas as pd

def load_assets(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    if "asset_id" not in df.columns:
        raise ValueError("assets saknar kolumnen 'asset_id'")
    return df

def load_failures(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    if "asset_id" not in df.columns:
        raise ValueError("failures saknar kolumnen 'asset_id'")
    return df