import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

# Read in the data into a DataFrame
raw_data = pd.read_csv(sys.argv[1])

# smoothen the DataFrame
smooth_data = raw_data.ewm(span=float(sys.argv[2])).mean()


# copy the time Series over to the smooth_data
smooth_data['time'] = raw_data['time']

# Switch on XKCD style, because it's glorious...
plt.xkcd()

# Make the axes an stuff
fig, axs = plt.subplots(2, 1, sharex=True)

# plot both Dataframes
raw_data.plot(kind='line', x='time', y='temp', ax=axs[0], label="ROHDATEN")
smooth_data.plot(kind='line', x='time', y='temp',
                 ax=axs[0], label='GEGLAETTET')
raw_data.plot(kind='line', x='time', y='hum', ax=axs[1], label="ROHDATEN")
smooth_data.plot(kind='line', x='time', y='hum', ax=axs[1], label='GEGLAETTET')


# setting title and axes label
axs[0].set_title("TEMPERATUR")
axs[0].set_ylabel("[°C]")
axs[1].set_xlabel("ZEIT")

axs[1].set_title("RELATIVE FEUCHTIGKEIT")
axs[1].set_ylabel("[%]")


# add and make the grid visible
axs[0].xaxis.grid(linewidth=1.0)
axs[0].yaxis.grid(linewidth=1.0)
axs[1].xaxis.grid(linewidth=1.0)
axs[1].yaxis.grid(linewidth=1.0)

plt.grid(True)

# show the whole thing
plt.show()
