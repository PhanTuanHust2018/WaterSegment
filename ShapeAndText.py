import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# # : co nghia la la toan bo anh se co mau xanh 
# img[:] = 255,0,0

#img.shape[1] is the height, img.shape[0] is the wight of picture
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(400,80),60,(255,250,0),5)
#put text on image
cv2.putText(img," OPENCV ",(200,200),cv2.FONT_HERSHEY_COMPLEX,2,(0,150,0),2)


cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
