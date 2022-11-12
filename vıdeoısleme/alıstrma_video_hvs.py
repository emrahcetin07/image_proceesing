import cv2
import numpy as np

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

def nothing(x):
    pass
cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar",500,500)


cv2.createTrackbar("lower-H","trackbar",0,180,nothing)
cv2.createTrackbar("lower-S","trackbar",0,255,nothing)
cv2.createTrackbar("lower-V","trackbar",0,255,nothing)

cv2.createTrackbar("upper-H","trackbar",0,180,nothing)
cv2.createTrackbar("upper-S","trackbar",0,255,nothing)
cv2.createTrackbar("upper-V","trackbar",0,255,nothing)

cv2.setTrackbarPos("upper-H","trackbar",180)
cv2.setTrackbarPos("upper-S","trackbar",255)
cv2.setTrackbarPos("upper-V","trackbar",255)

while True:
    ret,frame= cap.read()
    frame=cv2.flip(frame,1)

    frame_hsv=cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
    
    lower_h=cv2.getTrackbarPos("lower-H","trackbar")
    lower_s=cv2.getTrackbarPos("lower-S","trackbar")
    lower_v=cv2.getTrackbarPos("lower-V","trackbar")

    upper_h=cv2.getTrackbarPos("upper-H","trackbar")
    upper_s=cv2.getTrackbarPos("upper-S","trackbar")
    upper_v=cv2.getTrackbarPos("upper-V","trackbar")
    
    lower_color=np.array([lower_h,lower_s,lower_v])
    upper_color=np.array([upper_h,upper_s,upper_v])
    
    mask= cv2.inRange(frame_hsv,lower_color,upper_color)

    cv2.imshow("orginal",frame)
    cv2.imshow("mask",mask)
    if cv2.waitKey(50) & 0xFF == ord("q"):
     break
    



cv2.release()
cv2.destroyAllWindows()