import cv2
 
kamera = cv2.VideoCapture(0,cv2.CAP_DSHOW) #kaydedilen vido için: kamera = cv2.VideoCapture("KOLAY ŞEKİLLER.mp4") yazılır
 
while (kamera.isOpened()):
    ret, videoGoruntu = kamera.read()
    cv2.imshow("Bilgisayar Kamerasi", videoGoruntu)

    if cv2.waitKey(1) & 0xFF == ord('x'):#x e basınca video durcak.waitkey e kaç girersek o ms kadar bekleyip kare
        break
 
kamera.release()
cv2.destroyAllWindows()