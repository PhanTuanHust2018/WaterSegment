import cv2
import numpy as np

img = cv2.imread("basic/Lena.png")
print(img.shape)
#resize an image -> (witdh, height)
imgResize = cv2.resize(img,(300,200))

#crop an image (height, witdh)
imgCropped = img[0:200, 200:500]
#cv2.imshow("img",img)
cv2.imshow("the crop",imgCropped)

cv2.waitKey(0)
cv2.destroyAllWindows()