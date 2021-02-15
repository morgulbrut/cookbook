import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

# Read in the data into a DataFrame
raw_data = pd.read_csv(sys.argv[1])

# smoothen the DataFrame
smooth_data = raw_data.ewm(span=float(sys.argv[2])).mean()
smooth_data_com = raw_data.ewm(com=float(sys.argv[2])).mean()

# copy the time Series over to the smooth_data
smooth_data['time'] = raw_data['time']
smooth_data_com['time'] = raw_data['time']

# Switch on XKCD style, because it's glorious...
plt.xkcd()

# get the current axes from the plt. because the are used later
ax = plt.gca()

# plot both Dataframes
raw_data.plot(kind='line', x='time', y=sys.argv[3], ax=ax, label="RAW DATA")
smooth_data.plot(kind='line', x='time',
                 y=sys.argv[3], ax=ax, label=('SMOOTHEN (span={})'.format(sys.argv[2])))
smooth_data_com.plot(kind='line', x='time',
                     y=sys.argv[3], ax=ax, label=('SMOOTHEN (com={})'.format(sys.argv[2])))

plt.ylabel(sys.argv[3].upper())
plt.xlabel("TIME")


# add and make the grid visible
ax.xaxis.grid(linewidth=1.0)
ax.yaxis.grid(linewidth=1.0)
plt.grid(True)

# show the whole thing
plt.show()
