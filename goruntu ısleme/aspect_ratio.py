#enboy oranı
import cv2
from cv2 import destroyAllWindows
def resizewithaspectratio(img, width = None, height = None, inter = cv2.INTER_AREA):
    dimension = None
    (h,w) =img.shape[:2]

    if width is None and height is None:
        return img
    
    if width is None:
            r=height / float(w)
            dimension = (int(w*r),height)

    else: 
            r = width / float(w)
            dimension = (width, int(h*r))
    return cv2.resize(img, dimension, interpolation = inter)

img=cv2.imread("resim1.jpg")
img1=resizewithaspectratio(img, width = None, height = 200, inter = cv2.INTER_AREA)
cv2.imshow("orginal",img)
cv2.imshow("resized",img1)
cv2.imwrite("resizedpicture.jpg",img1)
cv2.waitKey(0)
destroyAllWindows()

