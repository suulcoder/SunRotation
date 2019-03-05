from __future__ import print_function
import sys
from PIL import Image
import PIL.Image
from module import *
import numpy as np
import matplotlib.pyplot as plt

try:
    #Get the image file into our 'original' variable
    orignal = Image.open("sunspots.jpg")
    #Get what we want
    width, height = orignial.size
    #Print data
    print("The sie of the image is: ")
    print(original.format, original.size, original.mode)

    #Convert to greyscale
    mod = original.convert('L')
    #Save in new file to compare
    mod.save('sunspotsBW.jpg') 

    #Create an array with the float32 values of the pixels of the image
    array = np.asarray(mod, dtype=np.float32) 

    #Fragment of the image
    b = array[360:375, 360:375]

    #Save the fragment to compare
    #First, the array is converted into unit8 and then into an Image file
    Image.fromarray(b.astype(np.uint8)).save("fragment.jpg")

    #Just to be sure
    print(b)
        
except:
    print("Unable to open file...")
