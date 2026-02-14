import pandas as pd

def run_backtest(data, initial_cash=10000):
    data = data.copy()
    data["position"] = pd.to_numeric(data["position"])  # ensure numeric
    
    cash = initial_cash
    shares = 0
    portfolio_value = []

    for i in range(len(data)):
        price = data["Close"].iloc[i]
        signal = data["position"].iloc[i]

        # BUY
        if signal == 1:
            shares = cash // price
            cash -= shares * price

        # SELL
        elif signal == -1:
            cash += shares * price
            shares = 0

        # portfolio value
        total_value = cash + shares * price
        portfolio_value.append(total_value)

    data["portfolio_value"] = portfolio_value
    data["returns"] = data["portfolio_value"].pct_change()
    return data
