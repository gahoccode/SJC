# Vietnamese Financial Markets Analysis (Streamlit)

## Overview
This Streamlit web app analyzes Vietnamese gold prices, calculates spreads, moving averages, volatility, and provides interactive visualizations. It is designed to meet the requirements in `prd.md` and is fully test-covered according to `tests.md`.

## Features
- Upload SJC gold price data (CSV)
- Calculate and visualize buy/sell spreads, moving averages (7/30/90 days), and rolling volatility
- Seasonality decomposition (future)
- API rate limiting controls and monitoring
- Interactive dashboards with Streamlit and Plotly

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
