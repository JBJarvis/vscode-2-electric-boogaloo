## Portforlio Optimization - Prolly Yfinance Portfolio for some arbitraty reason

from scipy.optimize import minimize
import numpy as np

# Define expected returns and covariance matrix
expected_returns = np.array([.1, .15, .12])
covariance_matrix = np.array([[.04, .02, .01],
                              [.02, .05, .03],
                              [.01, .03, .06]])

# Optimize portfolio weights
def objective(weights):
    return -np.dot(weights, expected_returns)

constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1})
bounds = [(0,1)] * len(expected_returns)
result = minimize(objective, x0=np.ones(len(expected_returns)) / len(expected_returns),
                  bounds=bounds, constraints=constraints)
optimal_weights = result.x

print(result.x)