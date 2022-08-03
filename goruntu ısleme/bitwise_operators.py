import cv2
import numpy as np
#have same pixel number each image
#black=0 , white= 1,oher color=1 and 0
circle=np.zeros((512,512,3),np.uint8)+255 #512*512 pixels
cv2.circle(circle,(256,256),60,(255,12,25),-1)#(2550=b,0=g,0=r)==BGR 

rectangle=np.zeros((512,512,3),np.uint8)+255 #512*512 pixels
cv2.rectangle(rectangle,(100,200),(250,316),(87,12,255),-1)

bit_and=cv2.bitwise_and(circle,rectangle)
bit_or=cv2.bitwise_or(circle,rectangle)
bit_xor=cv2.bitwise_xor(circle,rectangle)
bit_not=cv2.bitwise_not(circle)
bit_not1=cv2.bitwise_not(rectangle)

cv2.imshow("original_circle",circle)
cv2.imshow("original_rectangle",rectangle)
cv2.imshow("bit_and",bit_and)
cv2.imshow("bit_or",bit_or)
cv2.imshow("bit_xor",bit_xor)
cv2.imshow("bit_not",bit_not)
cv2.imshow("bit_not1",bit_not1)

cv2.waitKey(0)
cv2.destroyAllWindows()