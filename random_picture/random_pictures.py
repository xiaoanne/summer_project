# -*- coding: utf-8 -*-
import os
import random
from PIL import Image


root_dir = r"C:\Users\anne.wang\Downloads\project images\Chch-Nelson_Road_Thomas_Phone_Photos\\"
new_dir = r"C:\Anne\DATA_SCIENCE\summer_project\100\\"

filename = os.listdir(root_dir)
print(type(filename))
print(len(filename))
print(filename)


for i in range(1, 105):
    a= filename[random.randint(1, len(filename))]
    print(a)
    image = Image.open(os.path.join(root_dir + a))
    image.save(os.path.join(new_dir + a))

    # with open(os.path.join(root_dir, a), 'r') as file:
    #     print(file)

