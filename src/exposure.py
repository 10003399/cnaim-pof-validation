import pandas as pd

def calculate_asset_years(df, current_year):
    df["asset_years"] = current_year - df["installation_year"]
    return df