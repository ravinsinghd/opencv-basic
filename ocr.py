import cv2
import subprocess
img = cv2.imread('download (8).png',0)
threshimage = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
resized_image = cv2.resize(threshimage,None,fx=7, fy=7, interpolation = cv2.INTER_CUBIC)
cv2.imwrite('preprocessed.png',resized_image);
print('doing OCR in image')
test = subprocess.Popen(["tesseract","preprocessed.png","out"], stdout=subprocess.PIPE)
test.communicate()[0]
f = open("out.txt")
print(f.read().strip())