import os
import shutil
import glob

desktop = (r'C:\Users\cooli\Desktop')
tempDir = (r'C:\Users\cooli\Screenshots\Temp')

os.chdir(desktop)
pattern = desktop + "\Maple_*"
screenshots = glob.glob(desktop + pattern)

for filename in glob.iglob(pattern, recursive=True):
    filename = os.path.basename(filename)
    shutil.move(filename, tempDir + filename)
    print('Moved:', filename)
