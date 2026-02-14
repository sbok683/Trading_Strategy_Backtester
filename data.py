import yfinance as yf
import pandas as pd

def load_data(symbol="AAPL", start="2020-01-01", end="2024-01-01"):
    # Download data
    data = yf.download(symbol, start=start, end=end)

    # Flatten multi-index columns if they exist
    if isinstance(data.columns, pd.MultiIndex):
        # e.g., ('Close', 'AAPL') → 'Close'
        data.columns = [col[0] for col in data.columns]

    # Keep only the 'Close' column
    if 'Close' not in data.columns:
        raise ValueError(f"'Close' column not found in data.columns: {data.columns}")

    data = data[['Close']].copy()

    # Drop any missing values
    data.dropna(inplace=True)

    return data
