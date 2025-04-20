"""
app.py
Main Streamlit app for Vietnamese Financial Markets Analysis.
"""
import streamlit as st
import pandas as pd

from spread_analysis import calculate_spread, moving_average, rolling_volatility
from visualization import plot_gold_spread
from rate_limiter import RateLimiter

def main():
    st.set_page_config(page_title="Vietnamese Gold Market Analysis", layout="wide")
    st.title("Vietnamese Financial Markets Analysis")
    st.markdown("Analyze SJC gold price spreads, volatility, and trends.")

    # API-based data loading controls
    st.sidebar.header("Gold Price Data Loader (API)")
    today = pd.Timestamp.today().date()
    default_start = today.replace(day=1)
    start_date = st.sidebar.date_input("Start Date", default_start)
    end_date = st.sidebar.date_input("End Date", today)
    interval_days = st.sidebar.slider("Interval Days", 1, 30, 7)
    delay_seconds = st.sidebar.slider("Delay (seconds)", 1, 10, 1)
    fetch_data = st.sidebar.button("Fetch Gold Prices from API")

    df = None
    if fetch_data:
        with st.spinner("Fetching gold prices from API..."):
            from gold_data import get_gold_prices_for_date_range, calculate_price_spread
            df = get_gold_prices_for_date_range(str(start_date), str(end_date), interval_days, delay_seconds)
            if not df.empty:
                df = calculate_price_spread(df)
                st.success(f"Fetched {len(df)} gold price records.")
            else:
                st.warning("No data fetched for the selected period.")

    if df is not None:
        st.write("Fetched DataFrame preview:")
        st.write(df.head())
        st.write("Columns:", df.columns.tolist())
    if df is not None and not df.empty:
        # Ensure price_spread exists
        if 'price_spread' not in df.columns:
            df = calculate_price_spread(df)
        if 'price_spread' in df.columns:
            spread = df['price_spread']
            ma7 = moving_average(spread, 7)
            ma30 = moving_average(spread, 30)
            ma90 = moving_average(spread, 90)
            volatility = rolling_volatility(spread, 7)

            # Ensure 'date' is set as index for time series charts
            if 'date' in df.columns:
                df = df.copy()
                df['date'] = pd.to_datetime(df['date'])
                df = df.set_index('date')

            # Visualization
            st.subheader("Gold Price Spread & Volatility")
            plot_gold_spread(df, spread, volatility)

            # New: Spread Chart
            st.subheader("Gold Price Spread Over Time")
            st.line_chart(df[['price_spread']])

            st.subheader("Moving Averages of Price Spread")
            ma_df = pd.DataFrame({"MA7": ma7, "MA30": ma30, "MA90": ma90}, index=df.index)
            st.line_chart(ma_df)

            # Buy/Sell Prices Chart
            if 'buy' in df.columns and 'sell' in df.columns:
                st.subheader("Gold Buy and Sell Prices Over Time")
                st.line_chart(df[['buy', 'sell']])

                # Bar Chart: Sell and Buy Price by Branch
                if 'branch' in df.columns:
                    import plotly.express as px
                    branch_avg = df.groupby('branch')[['buy', 'sell']].mean().reset_index()
                    fig = px.bar(
                        branch_avg,
                        x='branch',
                        y=['buy', 'sell'],
                        barmode='group',
                        title='Average Buy and Sell Price by Branch',
                        labels={'value': 'Price', 'branch': 'Branch', 'variable': 'Price Type'}
                    )
                    st.subheader('Average Buy and Sell Price by Branch')
                    st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Price spread could not be calculated from the data.")
    else:
        st.info("Use the sidebar to fetch gold price data via API.")

    # Rate Limiter UI
    st.sidebar.header("API Rate Limiting")
    delay = st.sidebar.slider("Delay between API calls (seconds)", 1, 10, 1)
    batch_size = st.sidebar.number_input("Batch size", 1, 100, 1)
    enabled = st.sidebar.checkbox("Enable Rate Limiter", True)
    rate_limiter = RateLimiter(delay, batch_size, enabled)
    if st.sidebar.button("Simulate API Calls"):
        for _ in range(10):
            rate_limiter.request()
            rate_limiter.monitor()
    st.sidebar.write("Historical usage analytics coming soon.")

if __name__ == "__main__":
    main()
