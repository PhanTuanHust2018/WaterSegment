import cv2
import numpy as np
import matplotlib.pyplot as plt

path1 = "basic/HoThienQuang.jpg"
path2 = "basic/deSong2.jpg"
path3 = "basic/Song_Lo.jpg"
path4 = "basic/NuocLu2.jpec"
img_origin = cv2.imread(path3)

# img = img_origin #cv2.cvtColor(img_origin,cv2.COLOR_BGR2BGR)
# vectorized = img.reshape((-1,3))
# vectorized = np.float32(vectorized)
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# K = 7
# attempts = 20
# ret,label,center = cv2.kmeans(vectorized,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)

# center = np.uint8(center)

# res = center[label.flatten()]
# result_image=res.reshape((img.shape))

# figure_size = 15
# plt.figure(figsize=(figure_size,figure_size))
# plt.subplot(1,2,1),plt.imshow(img)
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(1,2,2),plt.imshow(result_image)
# plt.title('Segmented Image when K = %i' % K), plt.xticks([]), plt.yticks([])
# plt.show()
result_image =img = img_origin
def empty(a):
    pass

cv2.namedWindow("1")
cv2.createTrackbar("HueMin","1",32,179,empty)
cv2.createTrackbar("HueMax","1",97,179,empty)
cv2.createTrackbar("SatMin","1",0,255,empty)
cv2.createTrackbar("SatMax","1",98,255,empty)
cv2.createTrackbar("ValMin","1",82,255,empty)
cv2.createTrackbar("ValMax","1",180,255,empty)

while True:
    #img = cv2.imread(path2)
    imgHSV = cv2.cvtColor(result_image,cv2.COLOR_RGB2HSV)

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

    cv2.imshow("original",img_origin)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgResult)
    cv2.waitKey(3)
#

# cv2.imshow("img_HSV",imgHSV)
# cv2.imshow("result_image",result_image)
# cv2.waitKey(0)
#0,113,0,65,194,187