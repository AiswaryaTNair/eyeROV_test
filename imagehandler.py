import numpy as np
import cv2
import sys
from matplotlib.patches import Circle

if len(sys.argv)!=3:
    print("input format is not correct.Please enter image file name and coordinate")
    exit()

img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
coordinate=sys.argv[2]
coordinate=coordinate.replace("(","")
coordinate=coordinate.replace(")","")
seperate=coordinate.split(",")
x_point=int(seperate[0])
y_point=int(seperate[1])
print(x_point,y_point)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT,1.2,100)
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        circ = Circle((x,y), radius = r)
        output=circ.contains_point([x_point,y_point])
        if output==True:
            print("coordinate is inside")
        else:
            print("coordinate is outside")
        
    #cv2.imshow("output",img)
    #cv2.waitKey(0)

