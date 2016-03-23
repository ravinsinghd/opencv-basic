import cv2
from PIL import Image

img = cv2.imread('text.png',0)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imwrite('adoThres.png',th3);
#pil_im = Image.fromarray(th3)
#print(pil_im.info['dpi'])
#pil_im.save("adoThres.png" )
