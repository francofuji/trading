import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

eurusd = pd.read_csv('C:\\proyectos\\vtrading\\src\\EURUSD5OK.csv', header=0, index_col='Date', parse_dates=True)

print(eurusd['index_col'])

# Plot the closing prices for `aapl`
#eurusd['Close'].plot(grid=True)

# Show the plot
#plt.show()



def transform_data(origin = 'C:\\proyectos\\vtrading\\EURUSD5.csv', destination = 'C:\\proyectos\\vtrading\\EURUSD5OK.csv'): 
	"""
	function to transform csv donwloaded from MT4 to pandas series
	"""
	import csv

	new_csv = list()
	with open(origin, 'rb') as csvorigen:     
		csvreader = csv.reader(csvorigen, delimiter=',')
		new_csv.append(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
		for row in csvreader:
			new_row = list()
			# append date
			new_row.append(' '.join((row[0].replace('.', '-'), row[1])))
			# open
			new_row = new_row + row[2:]

			new_csv.append(new_row)

	with open(destination, 'wb') as csvfile:
	    csvwriter = csv.writer(csvfile, delimiter=',')
	    for row in new_csv:
	    	csvwriter.writerow(row)
