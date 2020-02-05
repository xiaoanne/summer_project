# -*- coding: utf-8 -*-
from GPSPhoto import gpsphoto
from PIL import Image
import os
import csv


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