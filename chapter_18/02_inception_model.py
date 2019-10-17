# example of loading the inception v3 model
from keras.applications.inception_v3 import InceptionV3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# load model
model = InceptionV3()
# summarize the model
model.summary()