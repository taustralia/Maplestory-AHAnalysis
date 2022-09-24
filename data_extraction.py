#Loading required libraries
from ast import If
from cgi import print_exception
from concurrent.futures import process
from doctest import DocFileSuite
import numpy as np
import cv2
import pytesseract
from PIL import Image
import pandas as pd
import os
import shutil
pytesseract.pytesseract.tesseract_cmd = 'C:/Users/cooli/AppData/Local/Tesseract-OCR/tesseract.exe'

rawDir = (r'C:\Users\cooli\Desktop\Screenshots\Raw')
cropDir = (r'C:\Users\cooli\Desktop\Screenshots\Cropped')
processDir = (r'C:\Users\cooli\Desktop\Screenshots\Processed')
ssDir = (r'C:\Users\cooli\Desktop\Screenshots')

os.chdir(rawDir)
for filename in os.listdir(rawDir):
    if filename.endswith('Cropped.jpg'):
        shutil.move(rawDir,cropDir)
    elif filename.endswith('.jpg'):
    #Store raw data image into memory
        img = cv2.imread(filename) 
        #Crop fullscreen shot into required section
        crop = img[147:671,272:1004]
        cv2.imwrite(filename + "Cropped.jpg", crop)
    else:
        os.remove(filename)
os.chdir(cropDir)
#Resize cropped image
for filename in os.listdir(cropDir):
    if filename.find('Resized') and filename.find('Cropped'):
        shutil.move(rawDir,processDir)
    elif filename.find('Cropped'):
        resized = cv2.resize(crop, (2559, 1834))
        cv2.imwrite(filename + "Resized.jpg", resized)
    elif filename.endswith('Cropped.jpg') == False:
        os.remove(filename)
#Show resized image
#cv2.imshow("Resized image", resized)
#cv2.waitKey(0)

#Convert resized, cropped data into text output -- converts to b&w, adds threshold
for filename in os.listdir(processDir):
    if filename.find('Resized'):
        img = Image.open(filename)
        text = pytesseract.image_to_string(img)
        resized = cv2.imread(filename, 0)
        thresh = cv2.threshold(resized, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        cv2.imwrite(filename + "Processed.jpg", thresh)
    
#Shows b&w resized img
#cv2.imshow('Thresh', thresh)
#cv2.waitKey(0)

#Variable Indexing
    price = text.find("Price")
    unit_price = text.find("Unit Price")
    time = text.find("Time")

#Convert output into csv???
    itemName = text[:int(price)]
    itemPrice = text[int(price):int(unit_price)].replace(",", "")
    unitPrice = text[int(unit_price):int(time)].replace(",", "")
    date = text[int(time):]

#Delete values in parantheses for Price & Unit Price & delete unwanted words
import re
itemPrice = re.sub("\(.*?\)|\.*?\)|\(.*?", "", itemPrice)
unitPrice = re.sub("\(.*?\)|\.*?\)|\(.*?", "", unitPrice)
itemName = itemName.replace("Item Name", "")
date = date.replace("Time", "").replace("Completed", "")
itemPrice = itemPrice.replace("Price", "").replace("\n\n", "\n")
unitPrice = unitPrice.replace("Unit Price", "").replace("\n\n", "\n")

#Combine data into table & csv export
from tabulate import tabulate
columns = ["Item", "Price", "Unit Price", "Time"]
mergedData = [[itemName, itemPrice, unitPrice, date]]
#print(tabulate(mergedData, headers=columns))

os.chdir(ssDir)
with open(filename + '.csv', 'w') as out:
    out.write(tabulate(mergedData, headers=columns))

        

