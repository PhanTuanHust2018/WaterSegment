import cv2
import numpy as np

path1 = "basic/HoThienQuang.jpg"
path2 = "basic/deSong2.jpg"
img_origin = cv2.imread(path1)

img = img_origin #cv2.cvtColor(img_origin,cv2.COLOR_BGR2BGR)
vectorized = img.reshape((-1,3))
vectorized = np.float32(vectorized)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

K = 10
attempts = 20
ret,label,center = cv2.kmeans(vectorized,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)

center = np.uint8(center)

res = center[label.flatten()]
result_image=res.reshape((img.shape))

#
imgHSV = cv2.cvtColor(result_image,cv2.COLOR_RGB2HSV)
h_min = 27
h_max = 94
s_min = 0
s_max = 112
v_min = 98
v_max = 255
lower = np.array([h_min,s_min,v_min])
upper = np.array([h_max,s_max,v_max])
mask = cv2.inRange(imgHSV,lower,upper)

#
#img_mask_gray = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)

#extract edges
image_edges_mask = cv2.adaptiveThreshold(mask,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,blockSize=5,C=2) 


#reduce mask noise
#mask_blur =cv2.GaussianBlur(mask,(3,3),1)   
mask_blur = mask
#
kernel = np.ones((11,11),np.uint8)
thresh1 = cv2.morphologyEx(mask_blur,cv2.MORPH_OPEN,kernel)
thresh = cv2.morphologyEx(thresh1,cv2.MORPH_CLOSE,kernel)
thresh = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
cv2.drawContours(img_origin,contours, -1,(0,255,0),2)

imgResult = cv2.bitwise_and(img,img,mask = thresh)
cv2.imshow("image_edges_rmask",image_edges_mask)
cv2.imshow("bitwise",imgResult)
cv2.imshow("mask",mask)
cv2.imshow("mask blur",mask_blur)
cv2.imshow("origin img",img_origin)
cv2.imshow("morph",thresh)
cv2.waitKey(0)