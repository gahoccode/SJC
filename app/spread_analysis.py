"""
spread_analysis.py
Core analytics for spread, moving averages, volatility, and seasonality.
"""
import pandas as pd

def calculate_spread(df: pd.DataFrame) -> pd.Series:
    """
    Calculate daily spread between buy and sell prices.
    Args:
        df (pd.DataFrame): Gold price data with 'buy' and 'sell' columns.
    Returns:
        pd.Series: Daily spread.
    """
    return df['sell'] - df['buy']

def moving_average(series: pd.Series, window: int) -> pd.Series:
    """
    Calculate moving average for a given window.
    Args:
        series (pd.Series): Input data.
        window (int): Window size.
    Returns:
        pd.Series: Moving average series.
    """
    return series.rolling(window=window).mean()

def rolling_volatility(series: pd.Series, window: int) -> pd.Series:
    """
    Calculate rolling volatility (standard deviation).
    Args:
        series (pd.Series): Input data.
        window (int): Window size.
    Returns:
        pd.Series: Rolling volatility.
    """
    return series.rolling(window=window).std()
