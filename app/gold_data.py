"""
gold_data.py
Module for loading and preprocessing SJC gold price data using vnstock API.
"""
import pandas as pd
import numpy as np
import time
import streamlit as st
from datetime import datetime, timedelta
from vnstock.explorer.misc import sjc_gold_price

def get_gold_prices_for_date_range(start_date_str, end_date_str, interval_days=7, delay_seconds=2):
    """
    Fetch gold prices for a range of dates with rate limiting.
    Args:
        start_date_str (str): Start date in 'YYYY-MM-DD' format
        end_date_str (str): End date in 'YYYY-MM-DD' format
        interval_days (int): Number of days between each data point
        delay_seconds (int): Number of seconds to wait between API calls
    Returns:
        pd.DataFrame: Combined DataFrame with gold prices for the date range
    """
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    all_prices = []
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        try:
            prices = sjc_gold_price(date=date_str)
            if not prices.empty:
                all_prices.append(prices)
        except Exception as e:
            print(f"Error fetching data for {date_str}: {e}")
        current_date += timedelta(days=interval_days)
        if current_date <= end_date:
            time.sleep(delay_seconds)
    if all_prices:
        gold_prices = pd.concat(all_prices, ignore_index=True)
        # Standardize column names for downstream compatibility
        gold_prices = gold_prices.rename(columns={'buy_price': 'buy', 'sell_price': 'sell'})
        return gold_prices
    else:
        return pd.DataFrame()

def calculate_price_spread(df):
    """
    Calculate the spread between sell price and buy price.
    Args:
        df (pd.DataFrame): DataFrame containing 'buy' and 'sell' columns
    Returns:
        pd.DataFrame: DataFrame with additional 'price_spread' column
    """
    if 'buy' in df.columns and 'sell' in df.columns:
        result_df = df.copy()
        result_df['buy'] = pd.to_numeric(result_df['buy'], errors='coerce')
        result_df['sell'] = pd.to_numeric(result_df['sell'], errors='coerce')
        result_df['price_spread'] = result_df['sell'] - result_df['buy']
        return result_df
    else:
        return df
