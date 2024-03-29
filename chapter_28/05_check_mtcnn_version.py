# %%
'''
## Face Detection With Deep Learning
A number of deep learning methods have been developed and demonstrated for face detection.
Perhaps one of the more popular approaches is called the Multi-Task Cascaded Convolutional
Neural Network, or MTCNN for short, described by Kaipeng Zhang, et al. in the 2016 paper
titled Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks.
The MTCNN is popular because it achieved then state-of-the-art results on a range of benchmark
datasets, and because it is capable of also recognizing other facial features such as eyes and
mouth, called landmark detection.
The network uses a cascade structure with three networks; first the image is rescaled to a
range of different sizes (called an image pyramid), then the first model (Proposal Network or
P-Net) proposes candidate facial regions, the second model (Refine Network or R-Net) filters the
bounding boxes, and the third model (Output Network or O-Net) proposes facial landmarks.
'''

# %%
'''
The MTCNN project, which we will refer to as ipazc/MTCNN to differentiate it from the
name of the network, provides an implementation of the MTCNN architecture using TensorFlow
and OpenCV. There are two main benefits to this project; first, it provides a top-performing
pre-trained model and the second is that it can be installed as a library ready for use in your
own code. The library can be installed via pip; for example:

sudo pip install mtcnn
'''

# %%
# confirm mtcnn was installed correctly
import mtcnn
# print version
print(mtcnn.__version__)


# %%
'''
Running the example will load the library, confirming it was installed correctly; and print
the version.
'''