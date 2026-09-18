import plotly.express as px
from data_fetcher import fetch_data
from preprocessor import clean_data

def plot_price_history(df):
    """
    Generates an interactive line chart of stock prices.
    """
    print("Generating interactive chart in your browser...")
    
    # Create a line chart using Plotly Express
    fig = px.line(
        df, 
        title='QuantFolio: Asset Price History',
        labels={'value': 'Price (USD)', 'Date': 'Date', 'variable': 'Ticker'},
        template='plotly_dark' # Gives it a sleek, professional dark mode look
    )
    
    # This command physically opens a new tab in your default web browser
    fig.show()

if __name__ == "__main__":
    # 1. Fetch the data
    tickers = ["AAPL", "MSFT"]
    raw_data = fetch_data(tickers, "2023-01-01", "2024-01-01")
    
    # 2. Clean it
    cleaned_data = clean_data(raw_data)
    
    # 3. Plot it!
    plot_price_history(cleaned_data)