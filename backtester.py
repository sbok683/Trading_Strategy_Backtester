def run_backtest(data, initial_cash=10000):
    data = data.copy()
    cash = initial_cash
    shares = 0
    portfolio_value = []

    # Fill forward the position so it’s continuous
    data["position"] = data["position"].fillna(0)
    current_position = 0  # 0 = no shares, 1 = long

    for i in range(len(data)):
        price = data["Close"].iloc[i]
        signal = data["position"].iloc[i]

        # Update current position if signal changes
        if signal == 1 and current_position == 0:
            # BUY
            shares = cash // price
            cash -= shares * price
            current_position = 1
        elif signal == -1 and current_position == 1:
            # SELL
            cash += shares * price
            shares = 0
            current_position = 0

        # portfolio value
        total_value = cash + shares * price
        portfolio_value.append(total_value)

    data["portfolio_value"] = portfolio_value
    data["returns"] = data["portfolio_value"].pct_change()
    return data
