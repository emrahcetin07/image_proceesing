import cv2
import numpy as np

circle=np.zeros((512,512,3),np.uint8)+255
cv2.circle(circle,(256,256),60,(255,0,0),-1)#(2550=b,0=g,0=r)==BGR VAR BURDA HEPPPPPP DİĞERERİNDEDE AYNISI
cv2.imshow("circle",circle)
rectangle=np.zeros((512,512,3),np.uint8)+255
cv2.rectangle(rectangle,(0,0),(250,316),(0,0,255),-1)
cv2.imshow("rectangle",rectangle)
'''
add=cv2.add(circle,rectangle)
print(add[256,256])
cv2.imshow("add",add)
'''
dst=cv2.addWeighted(circle,0.7, rectangle,0.3,20)
#(ilk şekil,oranı,2.şekil,oranı,eklenecek sabit sayı)
cv2.imshow("dst",dst)


cv2.waitKey(0)
cv2.destroyAllWindows()