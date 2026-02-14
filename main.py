from data import load_data
from strategy import ma_crossover_strategy
import matplotlib.pyplot as plt

# 1. Load data
data = load_data()

# 2. Run strategy
data = ma_crossover_strategy(data)

# 3. Plot
plt.figure(figsize=(14,7))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['ma_short'], label='MA 20', color='orange')
plt.plot(data['ma_long'], label='MA 50', color='purple')

# Buy signals
plt.scatter(data.index[data['position'] == 1],
            data['Close'][data['position'] == 1],
            marker='^', color='green', s=100, label='Buy')

# Sell signals
plt.scatter(data.index[data['position'] == -1],
            data['Close'][data['position'] == -1],
            marker='v', color='red', s=100, label='Sell')

plt.title('MA Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
