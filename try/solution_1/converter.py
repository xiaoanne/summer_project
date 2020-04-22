from tensorflow.contrib import lite
from keras.models import load_model
base_model=load_model('mask_rcnn_cracking_0034.h5')

converter = lite.TFLiteConverter.from_keras_model_file(base_model)
tfmodel = converter.convert()
# open("model.tflite", "wb").write(tfmodel)
with open("model.tflite", "wb") as f:
    f.write(tfmodel)