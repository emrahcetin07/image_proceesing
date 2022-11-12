import cv2

import numpy as np

#colorful picture for each pixel bright with RGB
"""
img=np.zeros((10,10,3),np.uint8)
img[0,0]=(255,255,255)
img[0,1]=(200,255,255)
img[0,2]=(150,255,255)
img[0,3]=(100,255,255)
img[0,4]=(50,255,255)
"""
#TO CREATE A GRAY PICTURE:
img=np.zeros((10,10),np.uint8)
img[0,0]=255
img[0,1]=254
img[0,2]=253
img[0,3]=50
img[0,4]=0



img = cv2.resize(img,(1000,1000),interpolation=cv2.INTER_AREA)#Specifies the size of the canvas with the "resize()"" function

cv2.imshow("canvas",img)
cv2.waitKey(0)
cv2.destroyAllWindows()