import yfinance as yf

def load_data(symbol="AAPL", start="2020-01-01", end="2024-01-01"):
    data = yf.download(symbol, start=start, end=end)
    data = data[['Close']]
    data.dropna(inplace=True)
    return data
