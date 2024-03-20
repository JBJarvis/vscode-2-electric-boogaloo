import yfinance as yf
import pandas as pd

def get_stock_data(stock_symbol, start_date, end_date):
    """
    Retrieves historical stock data for a given stock symbol within the specified date range.
    Args:
        stock_symbol (str): Ticker symbol (e.g., 'AAPL' for Apple).
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
    Returns:
        pd.DataFrame: DataFrame containing date, ticker, and closing price.
    """
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    return data[['Close']].reset_index()

def main():
    stock_symbol = 'MSTR'  # Example: Apple Inc.
    start_date = '2023-02-14'
    end_date = '2024-03-23'

    stock_data = get_stock_data(stock_symbol, start_date, end_date)

    # Display stock data in a simple table
    print("\nStock Data for", stock_symbol)
    print("-" * 30)
    print(stock_data)

if __name__ == "__main__":
    main()
