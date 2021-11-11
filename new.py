import cv2
import numpy as np
path = "basic/Lena.png"
img = cv2.imread(path)

kernel = np.ones((3,3),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
#dilate increase the thickness of white area of canny picture
#iterations define how much thickness do we want
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)


cv2.imshow("Canny img",imgCanny)
cv2.imshow("Dilation img",imgDialation)
cv2.imshow("Eroded img",imgEroded)
cv2.waitKey(0)
cv2.destroyAllWindows()