import cv2
import numpy as np
import os

original_image = cv2.imread("/home/quangtuan/Documents/python_project/basic/hoTien1.jpg")
# original_image = cv2.resize(original_image,(800,800))
# cv2.imwrite("hoTien1.jpg",original_image)

img = cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB)
pixel_values = img.reshape((-1, 3))
# convert to float
pixel_values = np.float32(pixel_values)
# define stopping criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
# number of clusters (K)
k = 6
_, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# convert back to 8 bit values
centers = np.uint8(centers)
# print(centers)

# flatten the labels array
labels = labels.flatten()
# convert all pixels to the color of the centroids
segmented_image = centers[labels.flatten()]
# reshape back to the original image dimension
segmented_image = segmented_image.reshape(img.shape)
# disable only the cluster number 2 (turn the pixel into black)
masked_image = np.zeros((img.shape[0],img.shape[1]), np.uint8)
# convert to the shape of a vector of pixel values
masked_image = masked_image.flatten()
# color (i.e cluster) to disable
min = 255
cluster = 0
for i in range(len(centers)):
    bright = centers[i][0]*0.2989 + centers[i][1]*0.587 + centers[i][2]*0.114
    if bright < min:
        min = bright
        cluster = i

masked_image[labels == cluster] = 255
# convert back to original shape
masked_image = masked_image.reshape(img.shape[0],img.shape[1])
# canny = cv2.Canny(masked_image,10,10)
# canny = cv2.dilate(canny, kernel, iterations=1)
def getContours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    max=0
    points = np.zeros((2,2),np.int)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max:
            max=area
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area == max:
            cv2.drawContours(original_image,cnt,-1,(0,0,255),2) 
            # cv2.fillPoly(original_image, cnt, color=(0,255,0))
            i=0
            for a in cnt:
                if a[0][0] == 400:
                    cv2.circle(original_image,(a[0][0],a[0][1]),2,(255,0,0),3) 
                    points[i] = a[0] 
                    i+=1
    distance = abs(points[0][1]-points[1][1])
    cv2.putText(original_image,f'{round(distance/20,2)} m',(points[0][0]+3,int((points[0][1]+points[1][1])/2)),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0))
    return distance
# getContours(canny_seg)
d = getContours(masked_image)
print(d)
cv2.imshow("test",segmented_image)
cv2.imshow("ori",original_image)
cv2.imshow("mask",masked_image)
cv2.waitKey(0)