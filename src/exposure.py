from __future__ import annotations
import pandas as pd

def build_asset_years(assets: pd.DataFrame, failures: pd.DataFrame, end_year: int) -> pd.DataFrame:
    """
    One row per (asset_id, year).
    Phase 1 assumption: exposure_years = 1.0 for each full year from installation_year..end_year.
    failures_in_year = count of failures whose failure_date falls in that year.
    """
    a = assets.copy()
    f = failures.copy()

    # Types
    a["installation_year"] = pd.to_numeric(a["installation_year"], errors="coerce")
    if a["installation_year"].isna().any():
        raise ValueError("installation_year contains non-numeric values")

    f["failure_date"] = pd.to_datetime(f["failure_date"], errors="coerce")
    f = f.dropna(subset=["failure_date"])
    f["year"] = f["failure_date"].dt.year.astype(int)

    # Generate (asset_id, year)
    rows = []
    for _, row in a.iterrows():
        start = int(row["installation_year"])
        if start > end_year:
            continue
        for y in range(start, end_year + 1):
            rows.append({"asset_id": row["asset_id"], "year": y})
    ay = pd.DataFrame(rows)

    # Merge features
    keep = [c for c in ["asset_id", "asset_type", "installation_year", "cnaim_pof"] if c in a.columns]
    ay = ay.merge(a[keep], on="asset_id", how="left", validate="many_to_one")
    ay["age"] = ay["year"] - ay["installation_year"]

    # Failure counts per year
    fail_counts = (
        f.groupby(["asset_id", "year"])
         .size()
         .reset_index(name="failures_in_year")
    )
    ay = ay.merge(fail_counts, on=["asset_id", "year"], how="left")
    ay["failures_in_year"] = ay["failures_in_year"].fillna(0).astype(int)

    # Exposure (Phase 1 MVP)
    ay["exposure_years"] = 1.0

    return ay