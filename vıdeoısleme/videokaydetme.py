#alınan videoyu kaydetme
import cv2
 
kamera = cv2.VideoCapture(0,cv2.CAP_DSHOW) #kaydedilen vido için: kamera = cv2.VideoCapture("KOLAY ŞEKİLLER.mp4") yazılır
 
filename = "C:\Program Files (x86)\görüntü isleme\webcam.avi"
codec = cv2.VideoWriter_fourcc('W','M','V','2')
frameRate = 30
resolution = (640,480)
 
videofileOutput = cv2.VideoWriter(filename, codec, frameRate, resolution)

while True :
    ret, videoGoruntu = kamera.read()
    videoGoruntu=cv2.flip(videoGoruntu,1) #video y eksenine göre yansır
    videofileOutput.write(videoGoruntu)
    cv2.imshow("Bilgisayar Kamerasi", videoGoruntu)

    if cv2.waitKey(1) & 0xFF == ord('a'):#a e basınca video durcak.waitkey e kaç girersek o ms kadar bekleyip kare
        break
 
videofileOutput.release()
kamera.release()
cv2.destroyAllWindows()