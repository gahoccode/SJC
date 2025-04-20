"""
test_visualization.py
Smoke test for visualization.py
"""
import pandas as pd
from app.visualization import plot_gold_spread

def test_plot_gold_spread():
    df = pd.DataFrame({
        "buy": [6800000, 6810000, 6820000],
        "sell": [6850000, 6860000, 6870000]
    }, index=pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-03"]))
    spread = df['sell'] - df['buy']
    volatility = spread.rolling(window=2).std()
    # Should not raise
    plot_gold_spread(df, spread, volatility)
