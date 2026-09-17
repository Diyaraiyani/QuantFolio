import yfinance as yf
import pandas as pd

def fetch_data(tickers: list, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetches adjusted close prices for multiple tickers from Yahoo Finance.
    """
    print(f"Downloading market data for: {tickers}...")
    
    # Download the data
    df = yf.download(tickers, start=start_date, end=end_date)['Close']
    
    # Clean the data by dropping any rows that have missing values
    df.dropna(inplace=True)
    
    print("Download complete! Here is a sneak peek:")
    return df

# A quick test block so we can run this file directly and see it work
if __name__ == "__main__":
    # Let's test it by pulling Apple and Microsoft data for 2023
    test_tickers = ["AAPL", "MSFT"]
    data = fetch_data(test_tickers, "2023-01-01", "2024-01-01")
    
    # Print the first 5 rows to the terminal
    print(data.head())