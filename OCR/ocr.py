import cv2
import pytesseract

cnh = cv2.imread('cnh.jpg')


cnh_gray = cv2.cvtColor(cnh, cv2.COLOR_BGR2GRAY)
cnh_thresh = cv2.threshold(cnh_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

cnh_text = pytesseract.image_to_string(cnh_thresh, lang='por')
print(cnh_text)