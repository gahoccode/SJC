"""
visualization.py
Helpers for Streamlit and Plotly visualizations.
"""
import streamlit as st
import plotly.graph_objs as go
import pandas as pd

def plot_gold_spread(df: pd.DataFrame, spread: pd.Series, volatility: pd.Series):
    """
    Plot gold buy/sell prices, spread, and volatility using Plotly.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['buy'], mode='lines', name='Buy Price'))
    fig.add_trace(go.Scatter(x=df.index, y=df['sell'], mode='lines', name='Sell Price'))
    fig.add_trace(go.Scatter(x=df.index, y=spread, mode='lines', name='Spread', fill='tozeroy'))
    fig.add_trace(go.Scatter(x=df.index, y=volatility, mode='lines', name='Volatility'))
    st.plotly_chart(fig, use_container_width=True)
