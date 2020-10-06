# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:31:51 2020

@author: Gizem ÇOBAN-Sobel Kenar Bulma Algoritması
"""
import cv2
import numpy as np
Gx=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
Gy=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
#Uygulanacak resmi ekledik
im = cv2.imread('rice.jpg')
#boylarını alma
h = im.shape[0]
w = im.shape[1]
c = im.shape[2]

yeniresim=np.zeros((h+2,w+2,3), np.uint8)

yeniresim[1:h+1,1:w+1]=im

G=np.zeros((h,w,3), np.uint8)
for i in range (1,h-1):
    for j in range(1,w-1):
        
        bir=yeniresim[i:i+1,j:j+1]*Gx
        iki=yeniresim[i:i+1,j:j+1]*Gy
        birtoplam=sum(sum(bir))
        ikitoplam=sum(sum(iki))
        G[i,j]=abs(birtoplam)+abs(ikitoplam)
        
        if(G[i,j,0]<200):
            G[i,j]=0
        else:
            G[i,j]=255
            
cv2.imshow('orijinal resim',im)      
cv2.imshow('yeniresim',G)
cv2.waitKey(0)
cv2.destroyAllWindows()