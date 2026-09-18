# src/data_fetcher.py
import yfinance as yf
import pandas as pd

def fetch_data(tickers, start_date: str, end_date: str) -> pd.DataFrame:
    """Fetches full market data and handles multi-index columns."""
    df = yf.download(tickers, start=start_date, end=end_date)
    
    # If yfinance returns a MultiIndex (e.g., 'Adj Close' -> 'AAPL'), flatten it
    if isinstance(df.columns, pd.MultiIndex):
        # Drop the ticker name layer so columns are just 'Open', 'Close', etc.
        df.columns = df.columns.droplevel(1)
            
    df.dropna(inplace=True)
    return df