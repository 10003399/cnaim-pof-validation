import pandas as pd

def validate_assets(df: pd.DataFrame) -> None:
    required = {"asset_id", "installation_year"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"assets saknar kolumner: {sorted(missing)}")

    if df["asset_id"].isna().any():
        raise ValueError("assets har NaN i asset_id")

    if not df["asset_id"].is_unique:
        raise ValueError("assets har duplicerade asset_id")

    years = pd.to_numeric(df["installation_year"], errors="coerce")
    if years.isna().any():
        raise ValueError("installation_year innehåller icke-numeriska värden")

def validate_failures(df: pd.DataFrame) -> None:
    required = {"failure_id", "asset_id", "failure_date"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"failures saknar kolumner: {sorted(missing)}")

    if df["asset_id"].isna().any():
        raise ValueError("failures har NaN i asset_id")