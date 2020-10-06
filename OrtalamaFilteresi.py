# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:02:26 2020

@author: Gizem Çoban-Ortalama Filtresi
"""
import cv2
import numpy as np
im = cv2.imread('cameraman.jpg')
#boylarını alma
h = im.shape[0]
w = im.shape[1]
c = im.shape[2]
yeniresim=np.zeros((h,w,3), np.uint8)
for i in range (0,h-1):
    for j in range(0,w-1):
        if ((i==0) or (j==0)or(i==h-1)or (j==w-1)):
            yeniresim[i,j]=im[i,j]
            continue
        toplam=int((im[i-1,j-1,0]))+int((im[i-1,j,0]))+int((im[i-1,j+1,0]))+int((im[i,j-1,0]))+ int((im[i,j,0]))+int((im[i,j,0]))+int((im[i+1,j-1,0]))+int((im[i+1,j,0]))+int((im[i+1,j+1,0]))
        ortalama=toplam/9
        yeniresim[i,j]=ortalama
cv2.imshow(' resim',yeniresim)
cv2.imshow('orijinal resim',im)
cv2.waitKey(0)
cv2.destroyAllWindows()