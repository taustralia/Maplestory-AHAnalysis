#Loading required libraries
from cgi import print_exception
import numpy as np
import cv2
import pytesseract
from PIL import Image
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/cooli/AppData/Local/Tesseract-OCR/tesseract.exe'

#Store raw data image into memory
img = cv2.imread('test.jpg')

#Crop fullscreen shot into required section
crop = img[147:671,272:1004]
cv2.imwrite("Cropped-Test.jpg", crop)
cv2.waitKey(0)

#Convert cropped data into text output
img = Image.open("Cropped-Test.jpg")
text = pytesseract.image_to_string(img)
#print(text)

price = text.find("Price")
time = text.find("Time")

#Convert output into csv???
itemName = text[:int(price)]
itemPrice = text[:int(time)]
date = text[int(time):]

print(date)