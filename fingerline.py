import cv2
import numpy as np 
from math import sin,cos,radians



img=cv2.imread('mini1.jpg')
height, width, channels = img.shape
x1=446
y1=337
angle = -5150;
length = height;



x2 = int(round(x1 + length * cos(radians(angle * 3.14 / 180.0))))
y2 = int(round(y1 + length * sin(radians(angle * 3.14 / 180.0))))
cv2.line(img,(x1,y1), (x2,y2), (255,255,0), 2)

cv2.imshow('res',img)
cv2.waitKey(0)