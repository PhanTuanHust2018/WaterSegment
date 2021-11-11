import cv2
import numpy as np

path1 = "basic/NuocLu2.jpeg"
path2 = "basic/HoThienQuang.jpg"
path3 = "basic/deSong2.jpg"
path4 = "basic/Song_Lo.jpg"
original_image = cv2.imread(path4)
original_image = cv2.resize(original_image,(500,500))
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

canny = cv2.Canny(blur,100,100)
canny_reverse = cv2.bitwise_not(canny)

#loc nguong otsu
imgGray = cv2.cvtColor(result_image,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(3,3),0)
kernel = np.ones((4, 4), np.uint8)
imgBlur = cv2.erode(imgBlur, kernel, iterations=1)
a,otsu = cv2.threshold(imgBlur,0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
otsu = cv2.bitwise_or(otsu,otsu, mask=canny_reverse)
#otsu = cv2.bitwise_not(otsu)

#
def getContours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    max=0
    max1=0
    print(len(contours))
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max:
            max=area
            cnt_max = cnt
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max1 and area < max:
            max1=area
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area == max1:
            cv2.drawContours(original_image,cnt,-1,(0,255,0),2)
    #cv2.drawContours(original_image,cnt_max,-1,(0,250,0),2) 
    return contours
#
otsu = cv2.morphologyEx(otsu,cv2.MORPH_OPEN,(3,3))
contours =  getContours(otsu)
# cnt,cX,cY =  find_contour_in_center_of_img(contours)

cv2.imshow("ori",original_image)
cv2.imshow("otsu",otsu)
cv2.imshow("canny_reverse",canny_reverse)
cv2.waitKey(0)