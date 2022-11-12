import cv2 
import numpy as np

font1=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
font2=cv2.FONT_HERSHEY_PLAIN
font3=cv2.FONT_HERSHEY_SCRIPT_COMPLEX

canvas = np.zeros((512,512,3),dtype=np.uint8)+255 

cv2.putText(canvas,"BERK ",(100,100),font3,4,(255,0,0),cv2.LINE_AA)#screen name,words,word lower left corner,font,size,color,static argument

cv2.putText(canvas,"EMRAH",(30,220),font3,4,(255,0,0),cv2.LINE_AA)

cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()