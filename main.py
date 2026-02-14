from data import load_data
from strategy import ma_crossover_strategy
from backtester import run_backtest
import matplotlib.pyplot as plt

# Load data
data = load_data("AAPL")

# Run strategy
data = ma_crossover_strategy(data)

# Run backtest
data = run_backtest(data)

# Print latest portfolio value
print(data[["Close","ma_short","ma_long","position","portfolio_value"]].tail(20))

# Plot portfolio value
data["portfolio_value"].plot(title="Portfolio Value Over Time", figsize=(12,6))
plt.xlabel("Date")
plt.ylabel("Portfolio Value")
plt.show()
start_value = data["portfolio_value"].iloc[0]
end_value = data["portfolio_value"].iloc[-1]
profit = end_value - start_value
percent_return = (profit / start_value) * 100

print(f"Start Portfolio Value: ${start_value:.2f}")
print(f"End Portfolio Value:   ${end_value:.2f}")
print(f"Profit:               ${profit:.2f}")
print(f"Percent Return:       {percent_return:.2f}%")

