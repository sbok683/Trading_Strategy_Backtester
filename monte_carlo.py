import numpy as np

def monte_carlo_simulation(returns, days=252, simulations=1000):
    """
    Simulates future portfolio values based on historical returns.
    
    returns: pd.Series of daily returns
    days: number of days to simulate (default 252 trading days ~ 1 year)
    simulations: number of Monte Carlo simulations
    """
    mean = returns.mean()
    std = returns.std()
    results = []

    for _ in range(simulations):
        sim_returns = np.random.normal(mean, std, days)
        price = 100 * np.cumprod(1 + sim_returns)  # start at 100 for scaling
        results.append(price[-1])

    return results
