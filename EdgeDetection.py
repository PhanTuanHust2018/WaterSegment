import cv2
import numpy as np
import matplotlib.pyplot as plt

#def getContours(img):
#   contours,hierarchy = cv2.findContours(img,cv2.)
kernel = np.ones((3,3),np.uint8)

path = "basic/HoThienQuang.jpg"
img = cv2.imread(path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
imgCanny = cv2.Canny(imgBlur,150,200)

imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Canny",imgCanny)
cv2.imshow("Eroded",imgEroded)
cv2.imshow("Dialation",imgEroded)
cv2.waitKey(0)
