import cv2;
import numpy as np
import matplotlib.pyplot as plt
im = cv2.imread('peppers.png') #resmi dahil etme
#boylarını alma
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

hist=np.zeros((256,1), np.uint8)
for i in range (h):
    for j in range(w):
        hist[yeniresim[i,j]+1]=hist[yeniresim[i,j]+1]+1

cv2.imshow('Original image',im) #resmi ekranda gösterme
cv2.imshow('Yeniimage',yeniresim)
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()