import cv2
import numpy as np
im = cv2.imread('kaplan.jpg')
oylarını alma
h = im.shape[0]
w = im.shape[1]
c = im.shape[2]
#Resmi renk katmanlarına ayırma
R=im[:,:,0];
G=im[:,:,1];
B=im[:,:,2];

i=0
j=0
yeniresim=np.zeros((h,w,3), np.uint8)
for i in range (h):
    for j in range(w):
        
        yeniresim[i,j]=R[i,j]*0.299+G[i,j]*0.587+B[i,j]*0.114

cv2.imshow('Original image',yeniresim)
cv2.waitKey(0)
cv2.destroyAllWindows()