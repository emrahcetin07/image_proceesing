import cv2 
import numpy as np

screen = np.zeros((512,512,3),dtype=np.uint8) +255 #When you add 255,the screen becomes white.


cv2.imshow("white screen",screen)

cv2.waitKey(0)
cv2.destroyAllWindows()