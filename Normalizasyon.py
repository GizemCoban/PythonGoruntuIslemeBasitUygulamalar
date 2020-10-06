# -*- coding: utf-8 -*-
"""
Created on Wed May 13 02:15:00 2020

@author: Gizem Çoban-Normalizasyon
"""
import cv2
import numpy as np
im = cv2.imread('peppers.png')
#Gri dönüştürme işlemi
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
yeniresim2=np.zeros((h,w,3), np.uint8)
for i in range (h):
    for j in range(w):
        yeniresim[i,j]=R[i,j]*0.299+G[i,j]*0.587+B[i,j]*0.114
        
yeniresim2=yeniresim.copy()
yeniMin=0
yeniMax=100
Minimum=np.amin(yeniresim)
Maksimum=np.amax(yeniresim)
for i in range (1,h-1):
    for j in range(1,w-1):
        I=yeniresim2[i,j]
        Inew=(I-Minimum)*((yeniMax-yeniMin)/(Maksimum-Minimum))+yeniMin
        yeniresim2[i,j]=Inew
cv2.imshow('Gri',yeniresim)
cv2.imshow('Normalizasyon',yeniresim2)
cv2.imshow('orijinal resim',im)
cv2.waitKey(0)
cv2.destroyAllWindows()