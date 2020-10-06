import cv2
import numpy as np
im = cv2.imread('cameraman.jpg')
#boylarını alma
h = im.shape[0]
w = im.shape[1]
c = im.shape[2]
b1=-50
b2=50

i=1
j=1
koyu=np.zeros((h,w,3), np.uint8) #yeni imgeyi oluşturma koyu için
acik=np.zeros((h,w,3), np.uint8) #yeni imgeyi oluşturma açık için
for i in range (h):
    for j in range(w):
        if (im[i,j]+b1)[0]<0:
            koyu[i,j]=0
        else:
            koyu[i,j]=im[i,j]+b1
        acik[i,j]=im[i,j]+b2
cv2.imshow('Original image',im)
cv2.imshow('Koyu',koyu)
cv2.imshow('Acik',acik)
cv2.waitKey(0)
cv2.destroyAllWindows()