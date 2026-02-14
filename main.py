from data import load_data
from indicators import moving_average

data = load_data()

data["MA_20"] = moving_average(data["Close"], 20)

print(data.head(30))
