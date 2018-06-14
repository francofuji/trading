from mpl_finance  import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime as datetime
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

df = pd.read_csv('D:\\proyectos\\trading\\vtrading\\src\\trading\\EURUSD5OK.csv', header=0, index_col='Date', parse_dates=True)

#Reset the index to remove Date column from index
df = df.reset_index()
#Naming columns
df.columns = ["Date","Open","High",'Low',"Close"]
#Converting dates column to float values
df['Date'] = df['Date'].map(mdates.date2num)

fig, ax = plt.subplots()

plt.plot()

plt.show()