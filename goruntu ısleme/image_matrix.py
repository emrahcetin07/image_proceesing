
from turtle import shape
import cv2
import numpy as np

img=cv2.imread("three.jpg",0)

row,col=img.shape#satır ve sütün sayılarını öğrendik


print(row)
print(col)
'''
#M=[1 0 t][0,1,t] ,öteleme işlemi
M = np.float32([1,0,13],[0,1,10]) #transformation matrix
#13 piksel  x düzleminde sağa,100 piksel y düzleminde kaydırır ve resmin kenarlarında bu pikseller kadar boşluk kalır
dst=cv2.warpAffine(img, M, (row,col))
cv2.imshow("dst",dst)
'''

M_1=cv2.getRotationMatrix2D((col/4,row/4),90,1)#90 derece döndürme ve 3 kat yakınlaştırma
dst_1=cv2.warpAffine(img,M_1,(col,row))
cv2.imshow("dst_1",dst_1)


cv2.waitKey(0)
cv2.destroyAllWindows()