import cv2
import numpy as np
'''
img=cv2.imread("resim1.jpg")
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
add=cv2.add(img1,img2)
cv2.imshow("resim bgr",img)
cv2.imshow("resim HSV ",img2)
cv2.imshow("resim GRAY",img3)
cv2.imshow("add",add)
'''
#VİDEONUN RENK UZAYINI DEĞİŞTİRME
cap=cv2.VideoCapture("KOLAY ŞEKİLLER.mp4")

while True:
     ret, frame=cap.read()
     frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)
     if ret==False:
         break

     cv2.imshow("video",frame)
     if cv2.waitKey(2) & 0xFF==ord("q"):
         break


