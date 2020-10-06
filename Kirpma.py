import cv2
import numpy as np
im = cv2.imread('cameraman.jpg')
x=int(input("Satir: "))
y=int(input("Sutun: "))

#boylarını alma
h = im.shape[0]
w = im.shape[1]
c = im.shape[2]

i=1
j=1

yeniresim=np.zeros((h,w,3), np.uint8)
for i in range (90):
    for j in range(90):
        yeniresim[i,j]=im[x+i,y+j]


cv2.imshow('Original image',im)
cv2.imshow('Yeni Resim',yeniresim)
cv2.waitKey(0)
cv2.destroyAllWindows()