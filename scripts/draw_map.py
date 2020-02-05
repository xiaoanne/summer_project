import os
import gmplot
import pandas as pd

df = pd.read_csv('./info.csv')
latitude_list = df['Latitude']
longitude_list = df['Longitude']

# Scatter points on the google map with the map center in christchurch central
gmap3 = gmplot.GoogleMapPlotter(-43.5310, 172.6365, 13)
gmap3.scatter(latitude_list, longitude_list, '# FF0000', size=40, marker=False)

# Plot method Draw a line in between given coordinates
gmap3.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width=2.5)
gmap3.draw("map/point.html")

# Delete the CSV file
os.remove("./info.csv")