import cv2
import numpy as np
im = cv2.imread('cameraman.jpg')

#boylarını alma
h = im.shape[0]
w = im.shape[1]
c = im.shape[2]

a1=0.5
a2=1.75
i=1
j=1
yeniresim1=np.zeros((h,w,3), np.uint8) #yeni imgeyi oluşturma yeniresim1 için(Boş bir resim oluşturur)
yeniresim2=np.zeros((h,w,3), np.uint8) #yeni imgeyi oluşturma açık için
for i in range (h):
    for j in range(w):
        if (im[i,j]*a2)[0]>255:
            yeniresim2[i,j]=255
        else:
            yeniresim2[i,j]=im[i,j]*a2
        
        yeniresim1[i,j]=im[i,j]*a1
        
cv2.imshow('Original image',im)
cv2.imshow('Yeni Resim 1',yeniresim1)
cv2.imshow('Yeni Resim 2',yeniresim2)
cv2.waitKey(0)
cv2.destroyAllWindows()