from data import load_data
from strategy import ma_crossover_strategy
from backtester import run_backtest
from metrics import sharpe_ratio, max_drawdown
from monte_carlo import monte_carlo_simulation
import matplotlib.pyplot as plt

# ------------------------------
# 1. Load historical price data
# ------------------------------
data = load_data("QQQ")  # You can change ticker here

# ------------------------------
# 2. Run MA crossover strategy
# ------------------------------
data = ma_crossover_strategy(data)

# ------------------------------
# 3. Backtest strategy
# ------------------------------
data = run_backtest(data)

# ------------------------------
# 4. Show latest portfolio info
# ------------------------------
print(data[["Close", "ma_short", "ma_long", "position", "portfolio_value"]].tail(20))

# ------------------------------
# 5. Plot portfolio value over time
# ------------------------------
plt.figure(figsize=(12,6))
data["portfolio_value"].plot(title="Portfolio Value Over Time")
plt.xlabel("Date")
plt.ylabel("Portfolio Value ($)")
plt.grid(True)
plt.show()

# ------------------------------
# 6. Profit and percent return
# ------------------------------
start_value = data["portfolio_value"].iloc[0]
end_value = data["portfolio_value"].iloc[-1]
profit = end_value - start_value
percent_return = (profit / start_value) * 100

print(f"Start Portfolio Value: ${start_value:.2f}")
print(f"End Portfolio Value:   ${end_value:.2f}")
print(f"Profit:               ${profit:.2f}")
print(f"Percent Return:       {percent_return:.2f}%")

# ------------------------------
# 7. Performance Metrics
# ------------------------------
sharpe = sharpe_ratio(data["returns"].dropna())
drawdown = max_drawdown(data["portfolio_value"])

print(f"Sharpe Ratio: {sharpe:.2f}")
print(f"Max Drawdown: {drawdown:.2%}")

# ------------------------------
# 8. Monte Carlo Simulation
# ------------------------------
mc_results = monte_carlo_simulation(data["returns"].dropna())
print("Monte Carlo Final Values (first 5):", mc_results[:5])

# Optional: plot Monte Carlo histogram
plt.figure(figsize=(10,5))
plt.hist(mc_results, bins=50, color="skyblue", edgecolor="black")
plt.title("Monte Carlo Simulation of Portfolio Value")
plt.xlabel("Portfolio Value ($)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
