import sqlite3
import pandas as pd
from pathlib import Path

def get_conn(db_path: str = "../data/processed/cnaim.db"):
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(db_path)

def load_csv_to_sqlite(csv_path: str, table: str, conn):
    df = pd.read_csv(csv_path)
    df.to_sql(table, conn, if_exists="replace", index=False)
    return df