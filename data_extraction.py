#Loading required libraries
from cgi import print_exception
from doctest import DocFileSuite
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

#Resize cropped image
resized = cv2.resize(crop, (2559, 1834))
cv2.imwrite("Resized-Test.jpg", resized)

#Show resized image
#cv2.imshow("Resized image", resized)
#cv2.waitKey(0)

#Convert resized, cropped data into text output -- converts to b&w, adds threshold
img = Image.open("Resized-Test.jpg")
text = pytesseract.image_to_string(img)
resized = cv2.imread('Resized-Test.jpg', 0)
thresh = cv2.threshold(resized, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#Shows b&w resized img
cv2.imshow('Thresh', thresh)
cv2.waitKey()

#Variable Indexing
price = text.find("Price")
unit_price = text.find("Unit Price")
time = text.find("Time")

#Convert output into csv???
itemName = text[:int(price)]
itemPrice = text[int(price):int(unit_price)].replace(",", "")
unitPrice = text[int(unit_price):int(time)].replace(",", "")
date = text[int(time):]

#Delete values in parantheses for Price & Unit Price
import re
itemPrice = re.sub("\(.*?\)", "", itemPrice)
itemPrice = re.sub("\.*?\)", "", itemPrice)

x = itemPrice.split()
print(" ".join(sorted(set(x), key=x.index)))

unitPrice = re.sub("\(.*?\)", "", unitPrice)
unitPrice = re.sub("\.*?\)", "", unitPrice)

y = unitPrice.split()
print(" ".join(sorted(set(y), key=y.index)))