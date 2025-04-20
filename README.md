# Vietnamese Financial Markets Analysis (Streamlit)

## Overview
This Streamlit web app provides comprehensive analytics for the Vietnamese gold market, focusing on SJC gold price data. It enables users to fetch and analyze gold prices, calculate spreads, moving averages, and volatility, and visualize results interactively. The app is designed to meet requirements in `prd.md` and is fully test-covered according to `tests.md`.

## Features
- **SJC Gold Price Analysis:**
  - Fetches SJC gold price data via API (vnstock) for customizable date ranges and intervals
  - **Spread & Volatility Analytics:**
  - Calculates and visualizes buy/sell spreads, moving averages (7/30/90 days), and rolling volatility
  - Interactive dashboards using Streamlit and Plotly
- **API Rate Limiting & Monitoring:**
  - Built-in controls for API call frequency and batch size
  - Visual feedback and warnings for rate limit status
- **Data Visualization:**
  - Interactive charts for gold price trends, spreads, and volatility
- **Testing & Requirements Traceability:**
  - All core analytics are covered by unit tests
  - Requirements in `prd.md` are mapped to tests in `tests.md`
- **Planned/Experimental:**
  - Seasonality decomposition (future)
  - Historical API usage analytics (coming soon)

## Setup Instructions

### 1. Create and Activate Virtual Environment (Windows)
```
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

Or using [uv](https://github.com/astral-sh/uv):
```
uv sync
```

### 3. Run the App
```
streamlit run app/app.py
```

### 4. Run Tests
```
pytest tests
```

## Project Structure
```
app/
  __init__.py
  app.py
  gold_data.py
  spread_analysis.py
  rate_limiter.py
  visualization.py
tests/
  test_gold_data.py
  test_spread_analysis.py
  test_rate_limiter.py
  test_visualization.py
prd.md
tests.md
requirements.txt
pyproject.toml
README.md
```

## Data Format
CSV must have columns: `date`, `buy`, `sell`

## Requirements Traceability
- All requirements in `prd.md` are mapped to tests in `tests.md` and implemented in the codebase.

## License
MIT
