import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import os

CHECK_IF_EXISTS = True


def safe_file(plt, image_path):
    print("writing png")
    fig = plt.gcf()
    fig.set_size_inches(16.5, 23.4)
    fig.savefig(image_path, dpi=100)


def plot_image(file, span):
    # Read in the data into a DataFrame
    raw_data = pd.read_csv(file)

    raw_data_interpolated = raw_data.interpolate()
    # smoothen the DataFrame
    smooth_data = raw_data_interpolated.ewm(span=span).mean()

    # copy the time Series over to the smooth_data
    smooth_data['time'] = raw_data['time']

    # Switch on XKCD style, because it's glorious...
    plt.xkcd()

    # Make the axes an stuff
    fig, axs = plt.subplots(3, 1, sharex=True)

    plot_value(axs, 0, 'temp', 'TEMPERATUR', "ZEIT", "[°C]", [
               "ROHDATEN", 'GEGLAETTET'], [raw_data, smooth_data])
    plot_value(axs, 1, 'hum', 'RELATIVE FEUCHTIGKEIT',  "ZEIT", "[%]", [
               "ROHDATEN", 'GEGLAETTET'], [raw_data, smooth_data])
    plot_value(axs, 2, 'tvoc', 'TVOC',  "ZEIT", "[ppb]", [
               "ROHDATEN", 'GEGLAETTET'], [raw_data, smooth_data])

    plt.grid(True)

    filename, file_extension = os.path.splitext(file)

    image_path = filename + ".png"
    if CHECK_IF_EXISTS:
        if not os.path.exists(image_path):
            safe_file(plt, image_path)
    else:
        safe_file(plt, image_path)


def plot_value(ax, indx, name, title, xaxis_title, yaxis_title, labels, dfs):
    for i in range(len(dfs)):
        dfs[i].plot(kind='line', x='time', y=name,
                    ax=ax[indx], label=labels[i])
    ax[indx].set_title(title)
    ax[indx].set_ylabel(yaxis_title)
    ax[indx].set_xlabel(xaxis_title)
    ax[indx].xaxis.grid(linewidth=1.0)
    ax[indx].yaxis.grid(linewidth=1.0)


if __name__ == "__main__":
    CHECK_IF_EXISTS = False
    plot_image(sys.argv[1], float(sys.argv[2]))
