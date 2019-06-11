from __future__ import print_function
import sys
import os
from PIL import Image
import PIL.Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
from sklearn.linear_model import LinearRegression
import csv
# best_fit calculates the ecuation of best fit of the given data. Useful later
#This function was obtained from the stackOverflow answer posted by Aziz Alto on this page: https://stackoverflow.com/questions/22239691/code-for-best-fit-straight-line-of-a-scatter-plot-in-python
# So credit to Aziz Alto on this function: best_fit
def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    bestFit =r'$\theta$ = {:.2f} + {:.2f}t'.format(a, b)

    return a, b , bestFit
"""
Saul Contreras
Marco Fuentes
Maria Jose Castro

The function of the following program is to convert a serie of images, of the SOHO (solar and helioscopic observatory)
from NASA, and convert them in a Matrix where 0 are the pixeles wich color were black, and 1 for pixels with other colors.
The program will return in a csv the information with the angle where the sunspot was found. 
"""
time = np.array([])
h = np.array([])
class Matrix(object):
	"""This class is a matrix that contains an previus image where:
		 black pixeles were converted into 0s 
		 and white pixels were converted into 1s"""
	def __init__(self, arg):
		self.arg = arg
		
	def getZero(self):#This method returns the coordenates i,j of an entry wich value is 0 and where their neighbors are 1s
		counter_y=0
		for line in self.arg:
			counter_x=0
			for pixel in line:
				if pixel==0:
					try:
						if(line[counter_x-1]==1 and line[counter_x+1]==1 and self.arg[counter_y-1][counter_x]==1 and self.arg[counter_y+1][counter_x]==1):
							toreturn = [counter_x,counter_y]
							return toreturn		
					except Exception as e:
						return [0,0]
				counter_x=counter_x+1
			counter_y=counter_y+1
		return [0,0]

	def getSunRadio(self): #It obtain sun radius base on the number of pixels of the matrix
		counter_y=0
		start = 0
		end = 0
		found = False
		for line in self.arg:
			counter_x=0
			for pixel in line:
				if(pixel==1):
					end=counter_y
				try:
					if(pixel==1 and found==False):
						found=True
						start = counter_y		
				except Exception as e:
					found = True
				counter_x=counter_x+1
			counter_y=counter_y+1
		return (end-start)/2		
		
#---------------------------------------------------------------------------------------------------------
size = 20#Change to get more data


#read data
fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(fileDir, 'sample22009/')#You must change the number with the number of your folder
#read dates
with open("sample12006.txt") as f:
    dates = f.readlines()
#take each image
rango = 6
for image in range(1,rango):#You must change the range, it must have the number of pictures that your serie has 
	original = Image.open(filename+'/'+str(image)+'.jpg')
	#We convert the image in a gray-scale picture
	mod = original.convert('L')
	array = np.asarray(mod.resize((size,size)), dtype=np.float32)
	answer = []
	b = array
	#Convert to binary
	for i in b:
	    listOne= []
	    for pixel in i:
	        if(pixel<50):
	            listOne.append(0)
	        elif(pixel>50):
	            listOne.append(1)
	    answer.append(listOne)
	matrix = Matrix(answer)
	answer = matrix.getZero()#Get angle
	sunRadius = matrix.getSunRadio()#Get radius
	print(sunRadius)#Print radius
	with open('ejemplo.csv',mode='a') as document:#Write data
		document = csv.writer(document,delimiter=',',quoting=csv.QUOTE_ALL)
		date = dates[image-1]
		date = date.replace("\n"," ")
		date = date.replace("\t"," ")
		vertical = str(np.arcsin((answer[1]-(size/2))/sunRadius))
		horizontal = str(np.arcsin((answer[0]-(size/2))/sunRadius))
		document.writerow([date,horizontal,vertical])
		#we store the data that can be recorded
		if (horizontal != "nan"):
			time = np.append(time,image)#agrego contador de tiempo
			h = np.append(h,np.arcsin((answer[0]-(size/2))/sunRadius))	

a,b,ecuacion = best_fit(time,h)
#posfit is a numpy array that contains the function of best fit of the data.
posfit = [a + b*ti for ti in time]
plt.plot(time,posfit)

#here we calculate the r² coefficient
reg = LinearRegression()
reg.fit(time.reshape(-1,1),posfit)
r2 = reg.score(time.reshape(-1,1),h)
print("Valor de r2 es: "+str(r2))

#plot the data as scatter points
plt.scatter(time, h)
plt.ylabel('Posicion angular horizontal')
plt.xlabel('Tiempo en dias')
plt.title('Posicion angular del sunspot')
print(ecuacion)
#Show the ecuation and the coefficient
plt.text(1,0.5,ecuacion)
plt.text(1,0.45,'r²='+str(r2))
#Show the graph
plt.show()
