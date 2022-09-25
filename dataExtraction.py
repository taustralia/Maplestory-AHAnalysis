#Loading required libraries
from copy import copy
import cv2
import pytesseract
from PIL import Image
import os
import shutil
import time
import numpy as np
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/cooli/AppData/Local/Tesseract-OCR/tesseract.exe'

rawDir = (r'C:\Users\cooli\Desktop\Screenshots\Raw')
cropDir = (r'C:\Users\cooli\Desktop\Screenshots\Cropped')
processDir = (r'C:\Users\cooli\Desktop\Screenshots\Processed')
resizeDir = (r'C:\Users\cooli\Desktop\Screenshots\Resized')
excelDir = (r'C:\Users\cooli\Desktop\Screenshots')

os.chdir(rawDir)
for filename in os.listdir(rawDir):
    if len(str(filename)) == int(23):
    #Store raw data image into memory
        img = cv2.imread(filename) 
        #Crop fullscreen shot into required section
        crop = img[147:671,272:1004]
        cv2.imwrite(filename + "Cropped.jpg", crop)
        time.sleep(1)
        os.remove(filename)
        
for filename in os.listdir(rawDir):
    time.sleep(1)
    shutil.move(os.path.join(rawDir, filename), cropDir) 

os.chdir(cropDir)
for filename in os.listdir(cropDir):
    img = cv2.imread(filename)
    crop = np.array(Image.open(filename))
    resized = cv2.resize(crop, (2559, 1834))
    cv2.imwrite(filename + "Resized.jpg", resized)
    time.sleep(1)
    os.remove(filename)

for filename in os.listdir(cropDir):
    time.sleep(1)
    shutil.move(os.path.join(cropDir, filename), resizeDir)

os.chdir(resizeDir)
for filename in os.listdir(resizeDir):
    img = cv2.imread(filename)
    img = Image.open(filename)
    text = pytesseract.image_to_string(img)
    resized = cv2.imread(filename, 0)
    thresh = cv2.threshold(resized, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    cv2.imwrite(filename + "Processed.jpg", thresh)
    time.sleep(3)
    os.remove(filename)

for filename in os.listdir(resizeDir):
    time.sleep(1)
    shutil.move(os.path.join(resizeDir, filename), processDir)
os.chdir(processDir)

for filename in os.listdir(processDir):
    price = text.find("Price")
    unit_price = text.find("Unit Price")
    date = text.find("Time")
    itemName = text[:int(price)]
    itemPrice = text[int(price):int(unit_price)].replace(",", "")
    unitPrice = text[int(unit_price):int(date)].replace(",", "")
    date = text[int(date):]

    #Delete values in parantheses for Price & Unit Price & delete unwanted words
    import re
    itemPrice = re.sub("\(.*?\)|\.*?\)|\(.*?", "", itemPrice)
    unitPrice = re.sub("\(.*?\)|\.*?\)|\(.*?", "", unitPrice)
    itemName = itemName.replace("Item Name", "")
    date = date.replace("Time", "").replace("Completed", "")
    itemPrice = itemPrice.replace("Price", "").replace("\n\n", "\n")
    unitPrice = unitPrice.replace("Unit Price", "").replace("\n\n", "\n")

#Combine data into table & csv export
   # from tabulate import tabulate

    #columns = ["Item", "Price", "Unit Price", "Time"]
    #mergedData = [[itemName, itemPrice, unitPrice, date]]
#print(tabulate(mergedData, headers=columns))

#os.chdir(ssDir)
#for filename in os.listdir(processDir):
  #  with open(filename + '.csv', 'w') as out:
     #   out.write(tabulate(mergedData, headers=columns))

    item = list(itemName)
    
    columns = ["Item", "Price", "Unit Price", "Time"]
    df = pd.DataFrame(item, [itemPrice], [unitPrice],) columns = columns)
    df.to_excel(filename + '.xlsx')
