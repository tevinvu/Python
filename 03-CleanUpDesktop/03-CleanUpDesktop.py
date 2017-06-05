#!/usr/bin/python3
#This is show you how to clean up your desktop asap
import os
import glob
import shutil
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Move all the pdf files on my destop into 1 folder PDf
for f in glob.glob(desktop + '/*.pdf'):
    shutil.move(f, desktop + '/Pdf')

#Move all the pictures files with extension .jpg into a folder Pictures
for f in glob.glob(desktop + '/*.jpg'):
    shutil.move(f, desktop + '/Pictures')

#Move all the powerpoints Files into the folder PowerPoints
for f in glob.glob(desktop + '/*.pptx'):
    shutil.move(f, desktop + '/PowerPoints')

#Move all the mp3 files into the folder mp3
for f in glob.glob(desktop + '/*.mp3'):
    shutil.move(f, desktop + '/mp3')