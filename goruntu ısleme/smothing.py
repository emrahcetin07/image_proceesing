import cv2
import numpy as np


img_filter=cv2.imread("noise.jpg")
img_median=cv2.imread("resim1.jpg")
img_bilateral=cv2.imread("resim2.jpg")

blur_1=cv2.blur(img_filter,(501,501))#it will only be a positive odd number, the more it gets the longer it gets.
blur_2=cv2.GaussianBlur(img_filter,(5,5), cv2.BORDER_DEFAULT)
median_blur=cv2.medianBlur(img_filter,9)#noise is decrease,parameter is always odd number
bilateral_blur=cv2.bilateralFilter(img_filter,9,41,41)

cv2.imshow("original image",img_filter)
cv2.imshow("blur image",blur_1)
cv2.imshow(" gaussian blur image",blur_2)
cv2.imshow("median blur image",median_blur)
cv2.imshow("bilateral blur image",bilateral_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()