import what3words
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import folium
from folium.plugins import MarkerCluster
import pandas as pd
from pprint import pprint

import io
from PIL import Image

name = 'error.error.error'

geocoder = what3words.Geocoder("8ALQVNE8")
res = geocoder.convert_to_coordinates(name)
pprint(res)

startcords = [res['coordinates']['lat'], res['coordinates']['lng']]

# Create the map
m = folium.Map(location=startcords, zoom_start=13, tiles='Stamen Toner')
folium.Marker(startcords, popup=name).add_to(m)

m

# Display the map
img_data = m._to_png(5)
img = Image.open(io.BytesIO(img_data))
img.save('image.png')
