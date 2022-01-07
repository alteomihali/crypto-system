import datetime as dt

import matplotlib.pyplot as plt
import pandas_datareader as web
import seaborn as sns

currency = "USD"
metric = "Close"

start = dt.datetime(2019, 7, 15)
end = dt.datetime.now()

crypto = ['BTC', 'ETH', 'LTC', 'DASH', 'SC']
colnames = []

first = True

for ticker in crypto:
    data = web.DataReader(f"{ticker}-{currency}", "google", start, end)
    if first:
        combined = data[[metric]].copy()
        colnames.append(ticker)
        combined.columns = colnames
        first = False
    else:
        combined = combined.join(data[metric])
        colnames.append(ticker)
        combined.columns = colnames

plt.yscale('log') # first show linear

for ticker in crypto:
    plt.plot(combined[ticker], label=ticker)

plt.legend(loc="upper right")

plt.show()

# # Correlation Heat Map

print(combined)

combined = combined.pct_change().corr(method='pearson')

sns.heatmap(combined, annot=True, cmap="coolwarm")
plt.show()
