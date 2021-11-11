import cv2
import numpy as np

path1 = "basic/HoThienQuang.jpg"
path2 = "basic/deSong2.jpg"
path3 = "basic/Song_Lo.jpg"
path4 = "basic/NuocLu2.jpec"
img_origin = cv2.imread(path3)
img_origin =cv2.resize(img_origin,(500,500))
img_gray = cv2.cvtColor(img_origin,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img_gray,(3,3),0)
imgCanny = cv2.Canny(imgBlur,100,150)
imgCanny_reverse = cv2.bitwise_not(imgCanny)
#path2
def path2():
    imgHSV = cv2.cvtColor(img_origin,cv2.COLOR_RGB2HSV)
    h_min = 7
    h_max = 106
    s_min = 0
    s_max = 138
    v_min = 70
    v_max = 191
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    kernel = np.ones((15,15),np.uint8)
    return mask,kernel
#path1
def path1():
    imgHSV = cv2.cvtColor(img_origin,cv2.COLOR_RGB2HSV)
    h_min = 0
    h_max = 41
    s_min = 21
    s_max = 255
    v_min = 0
    v_max = 181
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    kernel = np.ones((15,15),np.uint8)
    return mask,kernel
#path3
def path3():
    imgHSV = cv2.cvtColor(img_origin,cv2.COLOR_RGB2HSV)
    h_min = 0
    h_max = 179
    s_min = 0
    s_max = 255
    v_min = 90
    v_max = 255
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    kernel = np.ones((15,15),np.uint8)
    return mask,kernel
#

#reduce mask noise
#mask,kernel = path1()
mask,kernel = path2() 
#mask,kernel = path3() 

#path2
# thresh1 = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
# thresh = cv2.morphologyEx(thresh1,cv2.MORPH_CLOSE,kernel)

thresh = cv2.bitwise_or(mask,mask,mask= imgCanny_reverse)
thresh = cv2.erode(thresh,(7,7),iterations= 2)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
max=0
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > max:
        max=area
        cnt_max = cnt
print("Number of contours = " + str(len(contours)))
cv2.drawContours(img_origin,cnt_max, -1,(0,255,0),2)

imgResult = cv2.bitwise_and(img_origin,img_origin,mask = thresh)
#cv2.imshow("image_edges_rmask",image_edges_mask)
cv2.imshow("origin img",img_origin)
cv2.imshow("morph",thresh)
cv2.imshow("Canny_reverse",imgCanny_reverse)
cv2.waitKey(0)