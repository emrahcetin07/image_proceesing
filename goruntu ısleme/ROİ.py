#resimdeki ilgilendiğimiz alanların çıkarımı 


import cv2
img = cv2.imread("resim1.jpg")
cv2.imshow("resim",img)

print(img.shape[:2])# resim boutları x=0-302,y=0-167

roi=img[0:167,50:150] #y ekseni, ekseni çıkarmak istediğimiz yerler
cv2.imshow("roi",roi)
cv2.imshow("resim",img)



cv2.waitKey(0)
cv2.destroyAllWindows()

