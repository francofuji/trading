from mpl_finance  import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime as datetime
import numpy as np
import pandas as pd

quotes = pd.read_csv('C:\\proyectos\\vtrading\\EURUSD5OK.csv', header=0, index_col='Date', parse_dates=True)

fig, ax = plt.subplots()
candlestick_ohlc(ax,quotes.values, width=0.6)


ax.xaxis.set_major_locator(ticker.MaxNLocator(6))


fig.autofmt_xdate()
fig.tight_layout()

plt.show()