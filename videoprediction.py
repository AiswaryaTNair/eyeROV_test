import cv2
import sys

vidcap = cv2.VideoCapture(sys.argv[1])
print(sys.argv[1])
while(vidcap.isOpened()):
    success,image = vidcap.read()
    if success:
        cv2.imshow("image",image)
    else:
        break
vidcap.release()
cv2.destroyAllWindows()

