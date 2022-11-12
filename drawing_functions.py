import cv2 
import numpy as np

canvas = np.zeros((512,512,3),dtype=np.uint8) + 255 #Add 255 and the screen turns white. The numbers written in zeros create the black dimension of the canvas
#The reason for the 3 in parentheses is to be able to make colored drawings.512*512 pixels screen make with zeros() function

cv2.line(canvas, (0,0), (512,512), (255,51,95) , thickness=10)
#line(canvas_name,text_start_point,text_end_point,text_color(BGR),text_thickness)

cv2.line(canvas, (462,462), (100,100), (250,0,250) , thickness=30)

cv2.rectangle(canvas,(20,20),(50,50),(0,0,255),thickness=10)#If we make thickness=-1, it makes a solid rectangle; (right edge), (left edge)

cv2.circle(canvas,(250,250),100,(255,0,0),thickness=-1)#circle(....,center,radius,color,thickness)

#drawing a triangle(By creating 3 different points)
p1=(100,200)
p2=(50,50)
p3=(150,150)
cv2.line(canvas,p1,p2,(0,0,0),4)
cv2.line(canvas,p1,p3,(0,0,0),4)
cv2.line(canvas,p2,p3,(0,0,0),4)
cv2.ellipse(canvas,(250,250),(250,20),0,45,351,(50,0,15),-1) #center coordinate,width,length,angle with horizontal axis,start pain,end pain,color,thickness
points=np.array([[[0, 0], [50, 50], [100, 100], [220, 250]]] , np.int32)#to draw the polygon we want. The reason we say "true" is to create a closed shape.
cv2.polylines(canvas,[points],True,(255,0,150),5)

cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
