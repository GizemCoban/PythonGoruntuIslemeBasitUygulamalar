import cv2
import numpy as np
im = cv2.imread('kedi.jpg')
#boylarını alma
h = im.shape[0]
w = im.shape[1]
c = im.shape[2]
i=0
j=0
yeniresim=np.zeros((h,w,3), np.uint8)
for i in range (h):
    for j in range(w):
     
        yeniresim[i,j]=im[i,w-j-1]   
cv2.imshow('Original image',im)
cv2.imshow('Yeni image',yeniresim)
cv2.waitKey(0)
cv2.destroyAllWindows()