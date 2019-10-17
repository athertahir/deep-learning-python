# example of loading the vgg16 model
from keras.applications.vgg16 import VGG16
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# load model
model = VGG16()
# summarize the model
model.summary()