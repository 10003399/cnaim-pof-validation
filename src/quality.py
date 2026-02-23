def validate_assets(df):
    assert df["asset_id"].is_unique
    assert (df["installation_year"] > 1900).all()

def validate_failures(df):
    assert "asset_id" in df.columns