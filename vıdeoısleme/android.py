import cv2
import numpy as np

import requests


while True:

     img_resp= requests.get("https://192.168.1.34:8080//shot.jpg")

     img_arr = np.array(bytearray(img_resp.content),dtype=np.uint8)
     img=cv2.imdecode(img_arr,cv2.IMREAD_COLOR)

     img=cv2.resize(img,(640,480))

     cv2.imshow("android",img)


cv2.waitKey(1) 
    
    

    
cv2.destroyAllWindows()


