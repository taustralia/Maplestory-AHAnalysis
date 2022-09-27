#Loading required libraries
from contextlib import closing
import cv2
import pytesseract
from PIL import Image
import os
import shutil
import time
import numpy as np
import pandas as pd
from textblob import TextBlob

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/cooli/AppData/Local/Tesseract-OCR/tesseract.exe'
xconfig = ' --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-.,()%'
yconfig = ' --oem 3 preserve_interword_spaces=1 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-.,()%'
rawDir = (r'C:\Users\cooli\Desktop\Screenshots\Raw')
cropDir = (r'C:\Users\cooli\Desktop\Screenshots\Cropped')
processDir = (r'C:\Users\cooli\Desktop\Screenshots\Processed')
resizeDir = (r'C:\Users\cooli\Desktop\Screenshots\Resized')
csvDir = (r'C:\Users\cooli\Desktop\Screenshots\CSV')

def imageOCR():
    os.chdir(rawDir)
    for filename in os.listdir(rawDir):
            img = cv2.imread(filename) 
            #Crop fullscreen shot into required section
            crop = img[147:671,272:1004]
            cv2.imwrite(filename + "Cropped.jpg", crop)
            time.sleep(1)
            os.remove(filename)
            croppedFiles = [filename for filename in os.listdir(rawDir) if filename.endswith('Cropped.jpg')]
            for filename in croppedFiles:
                shutil.move(os.path.join(rawDir, filename), cropDir) 
#Resizes image & performs morphological transformations to allow for accurate text output
    os.chdir(cropDir)
    for filename in os.listdir(cropDir):
        img = cv2.imread(filename)
        crop = np.array(Image.open(filename))
        resized = cv2.resize(crop, (1600, 1146), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(filename + "Resized.jpg", resized)
        time.sleep(1)
        os.remove(filename)
        resizedFiles = [filename for filename in os.listdir(cropDir) if filename.endswith('Resized.jpg')]
        for filename in resizedFiles:
            shutil.move(os.path.join(cropDir, filename), resizeDir)

    os.chdir(resizeDir)
    for filename in os.listdir(resizeDir):
        img = cv2.imread(filename)
        resized = cv2.imread(filename, 0)
        blur = cv2.GaussianBlur(resized, (3,3), 0)
        erosion = cv2.erode(blur, kernel = np.ones((2,1), 'uint8'))
        dilation = cv2.dilate(erosion, kernel = np.ones((2,1), 'uint8'), iterations=2)
        blurv2 = cv2.GaussianBlur(dilation, (3,3), 0)
        opening = cv2.morphologyEx(blurv2, cv2.MORPH_OPEN, kernel = np.ones((2,1), 'uint8'))
        thresh = cv2.threshold(opening, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        cv2.imwrite(filename + "Processed.jpg", thresh)
        time.sleep(3)
        os.remove(filename)
        processedFiles = [filename for filename in os.listdir(resizeDir) if filename.endswith('Processed.jpg')]
        for filename in processedFiles:
            shutil.move(os.path.join(resizeDir, filename), processDir)
#Extracts required information into distinct variables to set up dataframe    
def dataCleanup():
    os.chdir(processDir)
    for filename in os.listdir(processDir):
        if filename.endswith('.jpg'):
            img = Image.open(filename)
            text = pytesseract.image_to_string(img, config=xconfig)
            itemName = text[text.find("Name"):(text.find("Price"))]
            itemPrice = text[(text.find("Price")):(text.find("UnitPrice"))].replace(",", "")
            unitPrice = text[(text.find("UnitPrice")):(text.find("2022"))].replace(",", "")
            date = text[(text.find("2022")):]
            
            #Remove unwanted symbols, words & prep columns for export
            import re
            itemPrice = re.sub("\(.*?\)|\.*?\)|.*?\)|^, |, \Z|[^0-9\n\.]|Price|\n\n", "", itemPrice)
            unitPrice = re.sub("\(.*?\)|\.*?\)|.*?\)|[^0-9\n\.]|UnitPrice|\n\n|,\Z", "", unitPrice)
            itemName = itemName.replace("\n\n", "", 1).replace("\n\n", "\n").replace("Name", "")
            date = date.replace("\n\n", "\n")
            #print([unitPrice.splitlines()])
            data = {'Item': (itemName.splitlines()), 'Price': (itemPrice.splitlines()), 'Date': (date.splitlines())}
            df = pd.DataFrame(data)
            df.to_csv('mergedData' + filename + '.csv')

            #Separating Unit Price into it's own CSV due to the fact that pytesseract can't detect single hyphens
            unitpriceData = {'Unit Price': (unitPrice.splitlines())}
            df2 = pd.DataFrame(unitpriceData)    
            df2.to_csv('unitPrice' + filename + '.csv')
            os.remove(filename)
            finalCSV = [filename for filename in os.listdir(processDir) if filename.endswith('.csv')]
            for filename in finalCSV:
                shutil.move(os.path.join(processDir, filename), csvDir)
def renameCSV():
    os.chdir(csvDir)
    folder = r"C:\Users\cooli\Desktop\Screenshots\CSV"
    for filename in os.listdir(csvDir):
        beginning = filename[filename.find(".jpgCropped"):filename.find(".csv")]
        if str(beginning) in filename:
            oldName = filename
            newName = filename.replace(str(beginning),"")
            os.rename (oldName, newName)
        #oldFilename = r'C:\Users\cooli\Desktop\Screenshots\CSV\\' + filename
        #print(oldFilename)
        #newFilename = folder + filename.split('.jpgCropped', 1)[0] + ".csv"
        #print(newFilename)
        #os.renames(filename, newFilename)
            
#imageOCR()
#dataCleanup()
renameCSV()
#os.chdir(ssDir)
#for filename in os.listdir(processDir):
  #  with open(filename + '.csv', 'w') as out:
     #   out.write(tabulate(mergedData, headers=columns))