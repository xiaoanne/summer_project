from PIL import Image
import os


print(os.getcwd())
path = '../photo/20200212_115712[1][1].jpg'
image = Image.open(path)
print(image)



from PIL import Image
def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

exif = get_exif(path)
print(exif)


from PIL.ExifTags import TAGS
def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled

exif = get_exif(path)
labeled = get_labeled_exif(exif)
print(labeled)