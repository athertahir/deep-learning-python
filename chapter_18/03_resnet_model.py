# example of loading the resnet50 model
from keras.applications.resnet50 import ResNet50
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# load model
model = ResNet50()
# summarize the model
model.summary()