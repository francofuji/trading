import matplotlib.pyplot as plt
import datetime
from numpy import sin, arange
from math import pi

starttime = datetime.datetime(2015, 12, 8, 8, 37, 0)
delta = datetime.timedelta(minutes=1)

# Create label locations and strings
sample_times = [starttime + i * delta for i in range(60)]
label_locations = [d for d in sample_times if d.minute % 5 == 0]
labels = [d.strftime('%Y-%m-%d %H:%M:%S') for d in label_locations]

# Create some y data to plot
x = arange(60)
y = sin(x * 2 * pi / 60.0)

# Do the plotting. You'll probably want to make adjustments to accommodate the size 
# of the labels.
plt.plot(sample_times, y)
plt.xticks(label_locations, labels, rotation=90)
plt.show()