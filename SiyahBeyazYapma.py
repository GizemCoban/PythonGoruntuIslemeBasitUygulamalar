import cv2
import numpy as np
im = cv2.imread('meyve.jpg')

esik=50
#boylarını alma
h = im.shape[0]
w = im.shape[1]
c = im.shape[2]
R=im[:,:,0];
G=im[:,:,1];
B=im[:,:,2];
i=0
j=0
yeniresim=np.zeros((h,w,3), np.uint8)
yeniresim2=np.zeros((h,w,3), np.uint8)
for i in range (h):
    for j in range(w):
        yeniresim[i,j]=(R[i,j]+G[i,j]+B[i,j])/3
        if yeniresim[i,j,0]>esik:
            yeniresim2[i,j]=255
        else:
            yeniresim2[i,j]=0
               
cv2.imshow('Original image',im)
cv2.imshow('Yeni image',yeniresim2)
cv2.waitKey(0)
cv2.destroyAllWindows()