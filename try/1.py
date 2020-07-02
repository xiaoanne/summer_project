from os import walk
import os
from sklearn.model_selection import train_test_split

d = os.getcwd() + '\yolov3\images'

f = []
for (dirpath, dirnames, filenames) in walk(d):
    f.extend(filenames)
    break


train, test = train_test_split(f,test_size=0.2)
print(train)
print(test)
import os

a = open("train.txt", "w")
for path, subdirs, files in os.walk(d):
   for filename in train:
     f = os.path.join(path, filename)
     a.write(str(f) + '\n')