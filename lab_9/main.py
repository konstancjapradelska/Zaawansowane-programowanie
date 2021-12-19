import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


img_1 = cv2.imread('1.jpg')
img_2 = cv2.imread('2.jpg')
img_3 = cv2.imread('3.jpg')
img_4 = cv2.imread('4.jpg')
img_5 = cv2.imread('5.jpg')


print(type(img_1))
print(img_1.shape)

cv2.imshow('image', img_1)
x = pytesseract.image_to_string(cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB))

print(x)
