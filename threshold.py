import cv2
import numpy as np

path1 = "basic/HoThienQuang.jpg"
path2 = "basic/deSong2.jpg"
path3 = "basic/NuocLu2.jpeg"
img_origin = cv2.imread(path3)
img_origin = cv2.resize(img_origin,(500,500))
img_gray = cv2.cvtColor(img_origin,cv2.COLOR_BGR2GRAY)
ret,image_threshold_Bi_OISU = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
img_canny = cv2.Canny(img_gray,100,200)
#
def getContours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    max=0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max:
            max=area
            cnt_max = cnt
    cv2.drawContours(img_origin,cnt_max,-1,(0,0,255),2)
getContours(image_threshold_Bi_OISU)
cv2.imshow("gray",img_gray)
cv2.imshow("threshold_bi_oisu",image_threshold_Bi_OISU)
cv2.imshow("origin img",img_origin)
cv2.waitKey(0)