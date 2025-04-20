# Test Requirements for Vietnamese Financial Markets Analysis Application

This document outlines the test requirements derived from the [Product Requirements Document (prd.md)](prd.md). Each requirement is traceable to a specific functional or technical specification in the PRD.

---

## 1. Gold Price Spread Analysis

### 1.1 Buy/Sell Spread Trends
- [ ] TR-1.1.1: Correct calculation of daily spread between SJC gold buy and sell prices.
- [ ] TR-1.1.2: Accurate generation of time series visualizations of spread trends.
- [ ] TR-1.1.3: Identification and display of long-term patterns in spread behavior.
- [ ] TR-1.1.4: Calculation and display of moving averages of spreads for 7-day, 30-day, and 90-day windows.

### 1.2 Spread Volatility as Market Stress Indicator
- [ ] TR-1.2.1: Calculation of spread volatility using rolling standard deviation.
- [ ] TR-1.2.2: Establishment and documentation of thresholds for normal vs. stressed market conditions.
- [ ] TR-1.2.3: Alert generation when spread volatility exceeds defined thresholds.
- [ ] TR-1.2.4: Visual or textual comparison of spread volatility with known market events.

### 1.3 Temporal Variations in Spread Patterns
- [ ] TR-1.3.1: Application of a 7-day moving average to smooth daily spread data.
- [ ] TR-1.3.2: Implementation of seasonality decomposition as specified (monthly averages, indices, deseasonalization, reseasonalization).
- [ ] TR-1.3.3: Analysis and visualization of deseasonalized data for trends and patterns. _(Planned: Not yet implemented)_
- [ ] TR-1.3.4: Correct reseasonalization of projections using trend forecasts and seasonal indices. _(Planned: Not yet implemented)_

---

## 2. Data Processing

- [ ] TR-2.1: Daily ingestion of SJC data and proper handling of missing values (sort by date, drop missing, consistent datetime index, set index to date).
- [ ] TR-2.2: Consistent alignment and formatting of all time series data.

---

## 3. Streamlit Visualization

- [ ] TR-3.1: Generation of time series visualizations using Streamlit components (st.line_chart, st.bar_chart, st.plotly_chart).
- [ ] TR-3.2: Gold price spread visualization includes:
  - Gold buy price (primary line)
  - Gold sell price (secondary line)
  - Shaded spread area
  - Overlay of rolling volatility
- [ ] TR-3.3: Dashboard supports interactive features (tabs, sidebars).

---

## 4. API Rate Limiting

- [ ] TR-4.1: Option to enable/disable API rate limiters.
- [ ] TR-4.2: Configurable delay between API calls (1–10 seconds).
- [ ] TR-4.3: Configurable batch size for requests.
- [ ] TR-4.4: Implementation of retry logic for failed requests. _(Planned: Not yet implemented)_
- [x] TR-4.5: Compliance with SJC Gold API’s default delay and interval. _(Implemented: User can set delay and interval in UI, enforced in API loader)_
- [ ] TR-4.6: Real-time API call rate display using st.progress(). _(Planned: Not yet implemented)_
- [ ] TR-4.7: Warning when approaching rate limits and logging of rate limit events. _(Planned: Not yet implemented)_
- [ ] TR-4.8: Visualization of historical API usage analytics.

---

## 5. Technical & Non-Functional

- [ ] TR-5.1: Optimization for large datasets using @st.cache_data.
- [ ] TR-5.2: Performance and aesthetic enhancements (custom CSS, Streamlit best practices).
- [ ] TR-5.3: Accuracy and traceability of all calculations to underlying data.

---

## 6. Success Metrics

- [ ] TR-6.1: Accurate identification and reporting of market stress periods.
- [ ] TR-6.2: Tracking and reporting of user engagement with visualizations and insights.

---

## Traceability Notes

- Each requirement (TR-x.x.x) is mapped to a specific section in the PRD for audit and validation purposes.
- This document is to be updated in parallel with any changes in `prd.md`.
