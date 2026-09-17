import pandas as pd
# We can import the function we built yesterday!
from data_fetcher import fetch_data

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handles missing values by forward-filling (using yesterday's price for today), 
    then backward-filling (just in case the first row is missing).
    """
    print("Cleaning data and handling missing values...")
    # .ffill() = forward fill, .bfill() = backward fill
    cleaned_df = df.ffill().bfill()
    return cleaned_df

def calculate_daily_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the daily percentage change of the stock prices.
    """
    print("Calculating daily percentage returns...")
    # .pct_change() does the math automatically!
    returns = df.pct_change()
    # The first day will always be NaN because there is no "yesterday" to compare to, so we drop it.
    returns.dropna(inplace=True)
    return returns

# A quick test block
if __name__ == "__main__":
    # 1. Fetch the data using yesterday's code
    tickers = ["AAPL", "MSFT"]
    raw_data = fetch_data(tickers, "2023-01-01", "2024-01-01")
    
    # 2. Clean it
    cleaned_data = clean_data(raw_data)
    
    # 3. Calculate returns
    returns = calculate_daily_returns(cleaned_data)
    
    print("\n--- Daily Returns (Percentage) ---")
    print(returns.head())