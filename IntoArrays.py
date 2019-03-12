from __future__ import print_function
import sys
from PIL import Image
import PIL.Image
from module import *
import numpy as np
import matplotlib.pyplot as plt
import cv2

#NEED TO install matplotlib and CV to work

#try:
#Get the image file into our 'original' variable
original = Image.open('sunspots.jpg')
#Get what we want
width, height = original.size
original.resize((200, 200))
#Print data
print("The sie of the image is: ")
print(original.format, original.size, original.mode)

#Convert to greyscale
mod = original.convert('L')
#Save in new file to compare
#mod.save('sunspotsBW.jpg') 

#Create an array with the float32 values of the pixels of the image
array = np.asarray(mod.resize((50,50)), dtype=np.float32)
#Fragment of the image
respuesta = []
print(array)
b = array#[0:200, 0:200]
for i in b:
    lista= []
    for pixel in i:
        if(pixel<50):
            lista.append(0)
        elif(pixel>50):
            lista.append(1)
    respuesta.append(lista)
#Save the fragment to compare
#First, the array is converted into unit8 and then into an Image file
Image.fromarray(b.astype(np.uint8)).save('fragment.jpg')

for i in respuesta:
    print(i)

#Just to be sure

#Use Canny Edge Detection to identify the sun
#edged = cv2.Canny(original, 100, 100)
#edged.save('CannySun.jpg')
#except:
 #   print("Unable to open file...")


