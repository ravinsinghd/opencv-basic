from PIL import Image
import pytesseract
img=Image.open(r'test.png');
print(img)
print(pytesseract.image_to_string(img))

