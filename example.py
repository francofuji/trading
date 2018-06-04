import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import datetime as dt

df_ohlc = pd.read_csv('C:\\proyectos\\vtrading\\src\\EURUSD5OK.csv', header=0, index_col='Date', parse_dates=True)

#Reset the index to remove Date column from index
df_ohlc = df_ohlc.reset_index()
#Naming columns
df_ohlc.columns = ["Date","Open","High",'Low',"Close", "Volume"]
#Converting dates column to float values
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

#Making plot
fig = plt.figure()
fig.autofmt_xdate()
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=6, colspan=1)

#Converts raw mdate numbers to dates
ax1.xaxis_date()
plt.xlabel("Date")
print(df_ohlc)

#Making candlestick plot
candlestick_ohlc(ax1,df_ohlc.values,width=1, colorup='g', colordown='k',alpha=0.75)
plt.ylabel("Price")
plt.legend()

plt.show()