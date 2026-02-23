import pandas as pd
from src.exposure import build_asset_years


def test_asset_year_generation():
    assets = pd.DataFrame({
        "asset_id": [1],
        "asset_type": ["cable"],
        "installation_year": [2020],
        "cnaim_pof": [0.02],
    })

    failures = pd.DataFrame({
        "failure_id": [10],
        "asset_id": [1],
        "failure_date": ["2022-01-01"],
    })

    result = build_asset_years(assets, failures, end_year=2023)

    assert len(result) == 4
    assert result["failures_in_year"].sum() == 1