rawCopy = (r'C:\Users\cooli\Desktop\Screenshots\RawCopy')
raw = (r'C:\Users\cooli\Desktop\Screenshots\Raw')
crop = (r'C:\Users\cooli\Desktop\Screenshots\Cropped')
resize = (r'C:\Users\cooli\Desktop\Screenshots\Resized')
process = (r'C:\Users\cooli\Desktop\Screenshots\Processed')
tempDir = (r'C:\Users\cooli\Screenshots\Temp')
csvDir = (r'C:\Users\cooli\Screenshots\CSV')

import os
import shutil

def reset(directory):
    shutil.rmtree(directory, ignore_errors=True)
    os.mkdir(directory)
    print("Reset of folder: " + directory + "has been completed!")

def copy(source, destination):
    shutil.rmtree(destination, ignore_errors=True)
    for filename in os.list(source):
        shutil.copytree(destination)
    print("Successful copy of folder: " + source + "to folder: " + destination " !")