import cv2
import numpy as np 
import imutils

image = cv2.imread('fr.jpg')
hsv= cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")
mask = cv2.inRange(hsv, lower, upper)
cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
c = max(cnts, key=cv2.contourArea)

extTop = tuple(c[c[:, :, 1].argmin()][0])
print extTop
cv2.imshow('mask',mask)
cv2.imshow('hsv',hsv)
cv2.waitKey(0)
