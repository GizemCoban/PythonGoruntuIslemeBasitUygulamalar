import cv2;
import numpy as np
im = cv2.imread('cameraman.jpg') #resmi dahil etme
#boylarını alma
h = im.shape[0]
w = im.shape[1]
c = im.shape[2]
=1
j=1
yeniresim=np.zeros((h,w,3), np.uint8)
for i in range (h):
    for j in range(w):
        yeniresim[i,j]=255-im[i,j]  #olumsuzlama işleminin yapıldığı yer

cv2.imshow('Original image',yeniresim) #resmi ekranda gösterme
cv2.waitKey(0)
cv2.destroyAllWindows()