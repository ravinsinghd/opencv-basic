import cv2
img = cv2.imread('download.png',0)
resized_image = cv2.resize(img,None,fx=4, fy=4, interpolation = cv2.INTER_CUBIC)
cv2.imwrite('extrabigresized.png',resized_image);