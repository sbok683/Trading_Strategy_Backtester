from indicators import moving_average

def ma_crossover_strategy(data, short=20, long=50):
    data = data.copy()

    # Calculate moving averages
    data["ma_short"] = moving_average(data["Close"], short)
    data["ma_long"] = moving_average(data["Close"], long)

    # Generate signals: 1 = holding, 0 = not holding
    data["signal"] = 0
    data.loc[data["ma_short"] > data["ma_long"], "signal"] = 1

    # Detect changes: +1 = buy, -1 = sell
    data["position"] = data["signal"].diff()

    return data
