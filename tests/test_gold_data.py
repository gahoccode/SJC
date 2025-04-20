"""
test_gold_data.py
Unit tests for gold_data.py
"""
import pandas as pd
import pytest
from app.gold_data import load_gold_data

def test_load_gold_data(tmp_path):
    # Create a dummy CSV
    csv = tmp_path / "gold.csv"
    csv.write_text("date,buy,sell\n2023-01-01,6800000,6850000\n2023-01-02,6810000,6860000\n")
    df = load_gold_data(str(csv))
    assert not df.empty
    assert set(["buy", "sell"]).issubset(df.columns)
    assert pd.api.types.is_datetime64_any_dtype(df.index)
    assert df.isnull().sum().sum() == 0
