This project is for my summer intern project. 

Use "python scripts/open_file.py" and "python scripts/draw_map.py" to run the script.

To run the script, ensure you have these dependencies installed(--user maybe not required):
pip install exifread --user
pip install piexif --user
pip install Pillow --user
pip install GPSPhoto
pip install gmplot --user
pip install pandas --user

To understand the structure, there are a few components:
1. Open file and extract the photo's information with open_file.py, available attributes contains GPS info such as 
    longtitude and latitude, photo's name and timestamp;
2. Given the geo coordinates, draw_map.py can plot the points on google map;
    


