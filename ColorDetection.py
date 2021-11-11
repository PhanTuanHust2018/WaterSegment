import cv2
import numpy as np

def empty(a):
    pass

path = "basic/HoThienQuang.jpg"
cv2.namedWindow("1")
cv2.createTrackbar("HueMin","1",0,179,empty)
cv2.createTrackbar("HueMax","1",91,179,empty)
cv2.createTrackbar("SatMin","1",0,255,empty)
cv2.createTrackbar("SatMax","1",255,255,empty)
cv2.createTrackbar("ValMin","1",0,255,empty)
cv2.createTrackbar("ValMax","1",255,255,empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HueMin","1")
    h_max = cv2.getTrackbarPos("HueMax","1")
    s_min = cv2.getTrackbarPos("SatMin","1")
    s_max = cv2.getTrackbarPos("SatMax","1")
    v_min = cv2.getTrackbarPos("ValMin","1")
    v_max = cv2.getTrackbarPos("ValMax","1")

    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask = mask)

    cv2.imshow("original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgResult)
    cv2.waitKey(3)