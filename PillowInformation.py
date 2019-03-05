from __future__ import print_function
import sys
from PIL import Image
import PIL.Image
from module import *
import numpy as np

#To open a document you must do the following:
try:
    original = Image.open("more.png")#Name of the document, in a specific format, in the same path of the document. 
except:
    print("Unable to load image")
print("The size of the Image is: ")
print(original.format, original.size, original.mode)

#The next Stuff cast the image into an data array, but it doesn´t work like we want, i mean it
#doesn´t make the matrix work in binary. 
pix = numpy.array(original)
img = Image.open('more.png').convert('L')
np_img = np.array(img)
np_img = ~np_img  # invert B&W
np_img[np_img > 0] = 1
print(np_img)
