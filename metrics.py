import numpy as np

def sharpe_ratio(returns, risk_free=0.0):
    """Annualized Sharpe Ratio"""
    excess = returns - risk_free
    return np.sqrt(252) * excess.mean() / excess.std()

def max_drawdown(portfolio_values):
    """Maximum drawdown from peak"""
    cumulative_max = portfolio_values.cummax()
    drawdown = (portfolio_values - cumulative_max) / cumulative_max
    return drawdown.min()
