# src/features.py
import pandas as pd

def add_moving_averages(df: pd.DataFrame, short_window=20, long_window=50) -> pd.DataFrame:
    """Calculates Simple and Exponential Moving Averages."""
    df[f'SMA_{short_window}'] = df['Close'].rolling(window=short_window).mean()
    df[f'SMA_{long_window}'] = df['Close'].rolling(window=long_window).mean()
    
    df[f'EMA_{short_window}'] = df['Close'].ewm(span=short_window, adjust=False).mean()
    return df

def add_macd(df: pd.DataFrame, fast=12, slow=26, signal=9) -> pd.DataFrame:
    """Calculates the Moving Average Convergence Divergence."""
    ema_fast = df['Close'].ewm(span=fast, adjust=False).mean()
    ema_slow = df['Close'].ewm(span=slow, adjust=False).mean()
    
    df['MACD'] = ema_fast - ema_slow
    df['MACD_Signal'] = df['MACD'].ewm(span=signal, adjust=False).mean()
    df['MACD_Histogram'] = df['MACD'] - df['MACD_Signal']
    return df

if __name__ == "__main__":
    from data_fetcher import fetch_data
    
    # Test the pipeline
    print("Downloading market data...")
    raw_data = fetch_data(["AAPL"], "2023-01-01", "2024-01-01")
    
    print("Applying technical indicators...")
    df_with_ma = add_moving_averages(raw_data)
    df_with_macd = add_macd(df_with_ma)
    
    # Print the last 5 rows to verify
    print("\nSuccess! Here is a sneak peek at your new features:")
    print(df_with_macd[['Close', 'SMA_20', 'MACD', 'MACD_Signal']].tail())