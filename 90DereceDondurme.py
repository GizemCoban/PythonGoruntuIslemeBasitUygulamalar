import cv2
import numpy as np
im = cv2.imread('kedi.jpg')
#boylarını alma
h = im.shape[0]
w = im.shape[1]
c = im.shape[2]
resimtranspoz=np.transpose(im)
i=0
j=0
yeniresim=np.zeros((3,w,h), np.uint8)
for i in range (resimtranspoz.shape[0]):
    for j in range(resimtranspoz.shape[1]):
        yeniresim[i,j]=resimtranspoz[i,resimtranspoz.shape[0]-j]
test= cv2.merge(yeniresim)
cv2.imshow('Original image',test)
cv2.waitKey(0)
cv2.destroyAllWindows()