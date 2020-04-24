Tutorials in:
https://towardsdatascience.com/detailed-tutorial-build-your-custom-real-time-object-detector-5ade1017fd2d


=====================================labelImg==========================================

https://github.com/tzutalin/labelImg

1. Install labelImg:
    pip install PyQt5
    pip install lxml

2. Open and Use labelImg tgo annotate images, by pip install labelImg to install, then type labelImg to open and use it;

Shortcut to use labelImg:
w	Create a rect box
d	Next image
Ctrl + s	Save

    
=========================================Download photos from Google=================================
https://google-images-download.readthedocs.io/en/latest/installation.html


=========================== Install Required Packages=================================
pip install -qq Cython contextlib2 pillow lxml matplotlib pycocotools

Error may happen when install pycocotools on windows10, to solve it:
1. install cython: pip install --upgrade cython
2. install  Microsoft Visual C++ 14.0: https://go.microsoft.com/fwlink/?LinkId=691126
3. pip install setuptools --upgrade
3. install pycocotools: pip install git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI


=============================Convert .xml to .csv====================================================
Run xml_to_csv.py under test_labels and train_labels to generate csv file from xml, then move the csv file to data folder
The converter code is in: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html

===============================Create label_map.pbtxt===================================
there is only 1 class in the lable map



==========================Download tensorflow/models from github=======================
https://github.com/tensorflow/models/releases
download the v1.13.0 version then rename the folder to models and move to object_detector folder


===============================protobuf===================================================
Download the binary file from with windows version: https://github.com/protocolbuffers/protobuf/releases
Extract the folder, find the application file in bin folder, then copy it to where your python script folder, my case is:
C:\Users\anne.wang\AppData\Local\Programs\Python\Python37\Scripts
If you don't know where your python is installed, use "where python" to find out.

then compile the proto file: protoc object_detection/protos/*.proto --python_out=.
test the builder: python object_detection/builders/model_builder_test.py


================================Failed to run model builder======================================
Error:
Traceback (most recent call last):
  File "object_detection/builders/model_builder_test.py", line 23, in <module>
    from object_detection.builders import model_builder
ModuleNotFoundError: No module named 'object_detection'

Solution:
in object_detection/builders/model_builder_test.py, after "import tensorflow as tf" add:
import sys
sys.path.append(r"C:\Anne\DATA_SCIENCE\summer_project\try\object_detector\\\models\\research\\")
sys.path.append(r"C:\Anne\DATA_SCIENCE\summer_project\try\object_detector\\models\\research\\object_detection\\utils")


==================================================ModuleNotFoundError: No module named 'nets'====================
I add this code sys.path.append("../../models/research/slim/") into /models/research/object_detection/models/faster_rcnn_inception_resnet_v2_feature_extrac
tor.py

code: 
import sys
sys.path.append("../../models/research/slim/")




=========================python object_detection/builders/model_builder_test.py now should run===========================
\object_detector\models\research>python object_detection/builders/model_builder_test.py

you should see:
  if not isinstance(wrapped_dict, collections.Mapping):
[       OK ] ModelBuilderTest.test_create_ssd_mobilenet_v2_keras_model_from_config
[ RUN      ] ModelBuilderTest.test_create_ssd_mobilenet_v2_model_from_config
[       OK ] ModelBuilderTest.test_create_ssd_mobilenet_v2_model_from_config
[ RUN      ] ModelBuilderTest.test_create_ssd_resnet_v1_fpn_model_from_config
[       OK ] ModelBuilderTest.test_create_ssd_resnet_v1_fpn_model_from_config
[ RUN      ] ModelBuilderTest.test_create_ssd_resnet_v1_ppn_model_from_config
[       OK ] ModelBuilderTest.test_create_ssd_resnet_v1_ppn_model_from_config
[ RUN      ] ModelBuilderTest.test_session
[  SKIPPED ] ModelBuilderTest.test_session
----------------------------------------------------------------------
Ran 22 tests in 0.094s

OK (skipped=1)





================Generate tf record file================================================
Create generate_tfrecord python file under model/research folder with code in: https://towardsdatascience.com/detailed-tutorial-build-your-custom-real-time-object-detector-5ade1017fd2d
Change the raw_label;
Add the python libraries;
Change base url to data_base_url = r'C:/Anne/DATA_SCIENCE/summer_project/try/object_detector/data/'

Run the file and see train_labels.record and test_label.record file generated under data folder.



============================Download the mobilessd model===================================
Can download via code 



==========================Modify ssd_inception_v2_coco config===================
Under C:\Anne\DATA_SCIENCE\summer_project\try\object_detector\models\research\object_detection\samples\configs folder:
num_classes: 1
Change train_config {} / train_input_reader {} / eval_input_reader {}


====================================Add path to computer===================================
set PYTHONPATH= C:\Anne\DATA_SCIENCE\summer_project\try\object_detector\models\research; C:\Anne\DATA_SCIENCE\summer_project\try\object_detector\models\research\slim



=============================Start training=============================================
Under folder:  C:\Anne\DATA_SCIENCE\summer_project\try\object_detector\models\research>
python object_detection/model_main.py --pipeline_config_path=C:\Anne\DATA_SCIENCE\summer_project\try\object_detector\models\research\object_detection\samples\configs --model_dir=training/