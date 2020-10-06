import cv2
img=cv2.imread('meyve.jpg')
cv2.imshow('resim',img)
R=img[:,:,0];
G=img[:,:,1];
B=img[:,:,2];
cv2.imshow('Red',R);
cv2.imshow('Green',G);
cv2.imshow('Blue',B);
cv2.waitKey(0)
cv2.destroyAllWindows()
