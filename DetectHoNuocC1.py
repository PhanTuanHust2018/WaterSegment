import cv2
import numpy as np
import math

#read image
path1 = "basic/NuocLu2.jpeg"
path2 = "basic/HoThienQuang.jpg"
path3 = "basic/deSong2.jpg"
path4 = "basic/HoNuocC1_1.png"
path5 = "basic/Song_Lo.jpg"

original_image = cv2.imread(path4)
original_image = cv2.resize(original_image,(500,500))
img_ori = cv2.imread(path4)
img_ori = cv2.resize(original_image,(500,500))
img=cv2.cvtColor(original_image,cv2.COLOR_BGR2LAB)

#k-means
vectorized = img.reshape((-1,3))
vectorized = np.float32(vectorized)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 1.0)
K = 5
attempts=10
ret,label,center=cv2.kmeans(vectorized,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
result_image = res.reshape((img.shape))
#canny
gray = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

canny = cv2.Canny(blur,150,150)
canny_reverse = cv2.bitwise_not(canny)

#loc nguong otsu
imgGray = cv2.cvtColor(result_image,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(3,3),0)
kernel = np.ones((4, 4), np.uint8)
imgBlur = cv2.erode(imgBlur, kernel, iterations=1)
a,otsu = cv2.threshold(imgBlur,0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
otsu = cv2.bitwise_or(otsu,otsu, mask=canny_reverse)
otsu = cv2.bitwise_not(otsu)

#
def getContours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    max=0
    # print("Number of contours = " + str(len(contours)))
    # for cnt in contours:
    #     area = cv2.contourArea(cnt)
    #     if area > max:
    #         max=area
    #         cnt_max = cnt
    #cv2.drawContours(original_image,contours,-1,(0,0,255),2) 
    return contours
#
#center of contours
def find_contour_in_center_of_img(contours):
    count = 0;
    for cnt in contours:
        M = cv2.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        if cX in range(220,280) and cY in range (220,320):
            return cnt,cX,cY
    return 0



def draw_center_radius(c,cX,cY):
    count = 0;
    cv2.circle(original_image,(cX,cY),7,(0,0,255),-1)
    cv2.drawContours(original_image,c,-1,(0,255,0),2)
    cv2.putText(original_image,"center",(cX - 10,cY - 10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
    count += 1
    print("number of center Contours: "+str(count))
    max_X = 0
    max_Y = 0
    for m in c:
        if m[0][0] > max_X: 
            max_X = m[0][0]
            max_Y = m[0][1]
    cv2.line(original_image,(cX,cY),(max_X,max_Y),(255,0,0),2)
    dist = math.sqrt((cX - max_X)**2 + (cY - max_Y)**2)
    dist = int(dist)
    p = int((cX+max_X) / 2)
    q = int((cY+max_Y) / 2)
    cv2.putText(original_image,"R = "+str(dist),(p,q-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)

#
kernel = np.ones((3,3),np.uint8)
#giam bot cac dom mau trang/reduce the white noise =>> reduce the number of contours
otsu = cv2.erode(otsu,kernel,iterations= 2)
otsu = cv2.dilate(otsu,kernel,iterations= 2)
ostu = cv2.bitwise_or(otsu,otsu,mask= canny_reverse)
#
cnts =  getContours(otsu)
c,cX,cY = find_contour_in_center_of_img(cnts)
draw_center_radius(c,cX,cY)
cv2.imshow("img_origin",original_image)
hor = np.hstack((canny_reverse,otsu))
cv2.imshow("result",hor)
cv2.imshow("img_ori",img_ori)
cv2.waitKey(0)