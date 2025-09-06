# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Vietnamese Financial Markets Analysis application built with Streamlit that provides comprehensive analytics for the Vietnamese gold market, specifically focusing on SJC gold price data. The application fetches gold prices via API, calculates spreads, moving averages, and volatility, and provides interactive visualizations.

## Development Commands

**Setup and Installation:**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
# Or using uv:
uv sync
```

**Running the Application:**
```bash
streamlit run app/app.py
```

**Testing:**
```bash
pytest tests
# Run specific test file:
pytest tests/test_gold_data.py
# Run with verbose output:
pytest -v tests
```

## Architecture and Code Structure

**Core Module Architecture:**
- `app/app.py`: Main Streamlit application entry point that orchestrates data fetching, analysis, and visualization
- `app/gold_data.py`: Data layer responsible for fetching SJC gold prices via vnstock API with rate limiting
- `app/spread_analysis.py`: Analytics engine that calculates spreads, moving averages (7/30/90 days), and rolling volatility
- `app/visualization.py`: Plotly-based chart generation for interactive gold price visualizations
- `app/rate_limiter.py`: API rate limiting controls with configurable delays and batch sizes

**Key Integration Points:**
- Data flows from vnstock API → gold_data.py → spread_analysis.py → visualization.py → Streamlit app.py
- All date/date range handling uses pandas.Timestamp and datetime for consistent time series processing
- Spread calculations require both 'buy' and 'sell' columns in DataFrame format
- Visualizations use Plotly for interactive charts integrated with Streamlit

**Data Requirements:**
- CSV data must contain columns: `date`, `buy`, `sell`
- Date column must be parseable as datetime
- API-based data fetching includes configurable intervals and rate limiting (delay_seconds parameter)

**Testing Strategy:**
- Unit tests cover core analytics functions in tests/
- Tests validate data loading, spread calculations, and rate limiting behavior
- All requirements in prd.md are traceable to tests in tests.md