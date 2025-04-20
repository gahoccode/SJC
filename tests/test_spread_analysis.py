"""
test_spread_analysis.py
Unit tests for spread_analysis.py
"""
import pandas as pd
import numpy as np
from app.spread_analysis import calculate_spread, moving_average, rolling_volatility

def test_calculate_spread():
    df = pd.DataFrame({"buy": [6800000, 6810000], "sell": [6850000, 6860000]},
                     index=pd.to_datetime(["2023-01-01", "2023-01-02"]))
    spread = calculate_spread(df)
    assert np.allclose(spread.values, [50000, 50000])

def test_moving_average():
    s = pd.Series([1, 2, 3, 4, 5, 6, 7])
    ma = moving_average(s, 3)
    assert np.isnan(ma.iloc[1])
    assert ma.iloc[2] == 2.0
    assert ma.iloc[-1] == 6.0

def test_rolling_volatility():
    s = pd.Series([1, 2, 3, 4, 5, 6, 7])
    vol = rolling_volatility(s, 3)
    assert np.isnan(vol.iloc[1])
    assert np.isclose(vol.iloc[2], 1.0)
    assert np.isclose(vol.iloc[-1], 1.0)
