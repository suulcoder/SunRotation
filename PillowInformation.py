from __future__ import print_function
import sys
from PIL import Image
import PIL.Image
from module import *

#To open a document you must do the following:
try:
    original = Image.open("more.png")#Name of the document, in a specific format, in the same path of the document. 
except:
    print("Unable to load image")
print("The size of the Image is: ")
print(original.format, original.size, original.mode)
pix = numpy.array(original)