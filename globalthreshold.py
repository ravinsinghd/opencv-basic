import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('text.png',0)
#threshold(src,threshvalue,maxvalue,thresh type)
# replace any pixel greater than 250 to 255 all other pixel will set as 0 
ret,thresh1 = cv2.threshold(img,250,255,cv2.THRESH_BINARY)
# replace any pixel greater than 254 to 255 all other pixel will set as 0
ret,thresh2 = cv2.threshold(img,254,255,cv2.THRESH_BINARY)



titles = ['Original Image','250','255']
images = [img, thresh1, thresh2]

for i in range(3):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
