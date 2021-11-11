import cv2

def empty(a):
    pass
cv2.namedWindow("1",cv2.WINDOW_NORMAL)
#cv2.resizeWindow("TrackBars",640,500)
cv2.createTrackbar("Tuan","1",0,179,empty)
cv2.createTrackbar("Tuan2","1",0,179,empty)
cv2.waitKey(0)