import cv2
import numpy as np
from  matplotlib import pyplot as plt
img=cv2.imread("resim1.jpg")
#img=np.zeros((500,500),np.uint8)
#cv2.circle(img,(250,250),100,(22,255,53),thickness=11)#circle(....,center,radius,color,thickness)
b,g,r=cv2.split(img)

cv2.imshow('img',img)
plt.hist(b.ravel(), 256, [0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(r.ravel(), 256, [0,256])
#plt.hist(img.ravel(), 256, [0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
