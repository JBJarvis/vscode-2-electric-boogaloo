import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import date
from nsepy import get_history as gh

##LFG

##Define Stock Symbols and Date Range

stocksymbols = ['CLSK', 'MLGO', 'MSTR', 'RIOT']
startdate = date(2023, 1, 5)
end_date = date.today()

print(f"You have {len(stocksymbols)} assets in your portfolio.")

##Fetch data for each stock
df = pd.DataFrame()
for symbol in stocksymbols:
    data = gh(symbol=symbol, start=startdate, end=end_date)[['Symbol', 'Close']]
    data.rename(columns={'Close': symbol}, inplace=True)
    df = pd.concat([df, data[symbol]], axis=1)

##Calculate daily simple returns
returns = df.pct_change().dropna()

##Calculate mean daily returns and std. dev.
mean_returns = returns.mean()
risk = returns.std()

##Create a correlation matrix
correlation_matrix = returns.corr()

##Visualize daily returns and risk
plt.figure(figsize=(10, 6))
sb.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title("Correlation Matrix")
plt.show()

##Add here if I want to add more performance metrics and allat

##Save dis to a csv??
df.to_csv("portanalysis.csv", index=False)
