import cv2;
import numpy as np
import matplotlib.pyplot as plt
im = cv2.imread('cameraman.jpg') #resmi dahil etme

#boylarını alma
h = im.shape[0]
w = im.shape[1]
c = im.shape[2]

hist=np.zeros((256,1), np.uint8)
for i in range (h):
    for j in range(w):
        hist[im[i,j]+1]=hist[im[i,j]+1]+1


cv2.imshow('Original image',im) #resmi ekranda gösterme
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()