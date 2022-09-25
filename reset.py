rawCopy = (r'C:\Users\cooli\Desktop\Screenshots\RawCopy')
raw = (r'C:\Users\cooli\Desktop\Screenshots\Raw')
crop = (r'C:\Users\cooli\Desktop\Screenshots\Cropped')
resize = (r'C:\Users\cooli\Desktop\Screenshots\Resized')
process = (r'C:\Users\cooli\Desktop\Screenshots\Processed')

import os
import shutil

shutil.rmtree(raw, ignore_errors=True)
shutil.rmtree(crop, ignore_errors=True)
os.mkdir(crop)
shutil.rmtree(resize, ignore_errors=True)
os.mkdir(resize)
shutil.rmtree(process, ignore_errors=True)
os.mkdir(process)
for filename in os.listdir(rawCopy):
    shutil.copytree(rawCopy,raw)
print("Reset completed!")