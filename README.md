# eyeROV_test
## Task 1: Check points contains a circular region in image.
### libraries used

 * Numpy
 * cv2-opencv python
 * sys-To communicate with interpreter.For eg: taking argument list as input using sys module.
 * matplotlib.patches-to draw a circle and check coordinates are inside or outside the circle.

### Problem statement

Given an image find whether the image has a circular region and if so evaluate the given
pixel is inside that circular region.

### Solution
There are 3 arguments and they are python file name, path of image and coordinate to search.
check if length of argument is not equal to 3 the print input format is not correct.Please enter image file name and coordinate and exit.
first consider argument 1,The function imread loads an image as 3 channel BGR color image of the given file.
As grayscale images simplifying the algorithms and computational requirements, we convert the colored images to gtayscale images.
Using cv2.cv.HOUGH_GRADIENT algorithm of cv2.HoughCircles function in opencv for circle detection.
After that using matplotlib.patches I found the coordinates are inside Or outside the circle.



## Task 2: Predict probability of circles in a video 
### libraries used
 * Numpy
 * cv2-opencv python
 * keras rcnn
 
### Problem statement
Using any Deep-learning framework(Tensorflow, PyTorch, Keras etc), a classifier
or detector using imagenet pretrained weights to process video instead of images has to be created. Also
want to show the prediction probability of circles(green in color if it’s above 80 otherwise red) any where in the video.


### Design

### First step:Create a model

let choose keras deep learning framework for implementing the model. First we do preproceing on keras dataset and then split keras dataset into train and test data.
Using train dataset we train keras rcnn model and test the keras rcnn model. 
### Second step:Find Prediction probability.

Take a video as input.
Opening videos using opencv function cv2.VideoCapture. Then extract frame by frame from the loaded video.
Load implemented keras rcnn model.Iterate through frame and predict probabily of circles in the extracted frame using loaded keras rcnn model.




