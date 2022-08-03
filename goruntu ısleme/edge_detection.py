import cv2
 
kamera = cv2.VideoCapture(0,cv2.CAP_DSHOW) #kaydedilen vido için: kamera = cv2.VideoCapture("KOLAY ŞEKİLLER.mp4") yazılır
 
while (kamera.isOpened()):
    ret, videoGoruntu = kamera.read()
    videoGoruntu=cv2.flip(videoGoruntu,1)# y eksenine göre alır
    edges=cv2.Canny(videoGoruntu,100,200)
    cv2.imshow("Bilgisayar Kamerasi", videoGoruntu)
    cv2.imshow("Kenarlar",edges)
    if cv2.waitKey(1) & 0xFF == ord('x'):#x e basınca video durcak.waitkey e kaç girersek o ms kadar bekleyip kare
        break
 
kamera.release()
cv2.destroyAllWindows()