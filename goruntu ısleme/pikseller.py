import cv2 
import numpy as np

img=cv2.imread("resim1.jpg")
dimension=img.shape#resimin boyutu
print(dimension)
color= img[100,150] #yazılan pikseldeki rengi bgr olarak tanımı
print(color)



blue=img[0,0,0] #o pikseldeki mavii değerini  görmek
print("blue",blue)

blue1=img.item(150,200,0)
img.itemset((150,200,0),172)#yazılan piksel değeri ile 172. piksel ile değişdi

print("new blue1:",img[150,200,0])



cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()