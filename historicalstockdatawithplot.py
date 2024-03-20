import yfinance as yf
import plotly.graph_objects as go

def get_stock_data(stock_symbol, start_date, end_date):
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    return data[['Close']].reset_index()

def plot_stock_chart(stock_data):
    fig = go.Figure(data=go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines'))
    fig.update_layout(title=f"{stock_symbol} Stock Price Chart", xaxis_title="Date", yaxis_title="Closing Price")
    fig.show()

if __name__ == "__main__":
    stock_symbol = 'MSTR' ## Example: MicroStrategy Inc.
    start_date = '2023-01-05'
    end_date = '2024-03-11'

    stock_data = get_stock_data(stock_symbol, start_date, end_date)
    plot_stock_chart(stock_data)