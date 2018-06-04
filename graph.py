from mpl_finance  import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime as datetime
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

df_ohlc = pd.read_csv('C:\\proyectos\\vtrading\\src\\EURUSD5OK.csv', header=0, index_col='Date', parse_dates=True)

#Reset the index to remove Date column from index
df_ohlc = df_ohlc.reset_index()
#Naming columns
df_ohlc.columns = ["Date","Open","High",'Low',"Close"]
#Converting dates column to float values
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

fig, ax = plt.subplots()
candlestick_ohlc(ax,df_ohlc.head().values, width=0.6)


ax.xaxis.set_major_locator(ticker.MaxNLocator(6))


fig.autofmt_xdate()
fig.tight_layout()

plt.show()