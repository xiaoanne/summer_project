# -*- coding: utf-8 -*-
from GPSPhoto import gpsphoto
from PIL import Image
import os
import csv
import gmplot
import pandas as pd


def get_date_taken(p):
    return Image.open(p)._getexif()[36867]


filename = os.listdir("photo")
with open('info.csv', mode='a') as csv_file:
    fieldnames = ['filename', 'date', 'Latitude', 'Longitude']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(1, len(filename)):
        path = 'photo/' + filename[i]
        name = filename[i]
        date = get_date_taken(path)
        latitude = gpsphoto.getGPSData(path)['Latitude']
        longitude = gpsphoto.getGPSData(path)['Longitude']
        # print(filename[i])
        # print(get_date_taken(path))
        # print('Latitude', gpsphoto.getGPSData(path)['Latitude'])
        # print('Longitude', gpsphoto.getGPSData(path)['Longitude'])
        writer.writerow({'filename': name, 'date': date, 'Latitude': latitude, 'Longitude': longitude})


df = pd.read_csv('info.csv')
latitude_list = df['Latitude']
longitude_list = df['Longitude']

# Scatter points on the google map with the map center in christchurch central
gmap3 = gmplot.GoogleMapPlotter(-43.5310, 172.6365, 13)
gmap3.scatter(latitude_list, longitude_list, '# FF0000', size=40, marker=False)

# Plot method Draw a line in between given coordinates
gmap3.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width=2.5)
gmap3.draw("map/point.html")

# Delete the CSV file
os.remove("info.csv")