import cv2
import numpy as np
cv2.namedWindow('gosteri',cv2.WINDOW_NORMAL)#resmi boyutlandırmak için
resim=cv2.imread("resim1.jpg",0) #resmi siyah beyaz yapmak için 0 yazdık
resim=cv2.resize(resim,(24,2))
#resim=cv2.imread("resim1.jpg")
cv2.imshow("gosteri",resim) #resmi göstermek için kullandık
#print(resim)
#cv2.imwrite("resim4.jpg",resim) #2. bir resim yapmak için kullanırız
cv2.waitKey(0)#resim istenildiği kadar tutmak için
cv2.destroyAllWindows()