from __future__ import print_function
import sys
from PIL import Image
import PIL.Image

#To open a document you must do the following:
try:
    original = Image.open("LogoApp.png")#Name of the document, in a specific format, in the same path of the document. 
except:
    print("Unable to load image")
print("The size of the Image is: ")
print(original.format, original.size, original.mode)

red="\xff\x00\x00\xff"
green="\x00\xff\x00\xff"
blue="\x00\x00\xff\xff"
im = PIL.Image.frombytes("RGBA", (64,64), (red*64 + green*64 + blue*64 + red*64) * 16)
im.save("test.png")