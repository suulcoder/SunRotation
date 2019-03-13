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
"""
Saul Contreras
Marco Fuentes
Maria Jose Castro

Proyecto 1 - Fisica 2:

El siguiente proyecto consiste en un simulador, el objetivo de este programa es tomar fotos proporcionadas
por el SOHO, solar and helioscopic observatory de la NASA, convirtiendolas en una estructura de datos, donde
se realizaran ciertos calculos para calcular el angulo en que se posiciona un sunsput en el sol. Para luego
devolver una grafica de angulo vs tiempo, para calcular la velocidad angular de dicho angulo
"""

class Matrix(object):
	"""Nos permite obtener el susnsput
	ubicado en una matrix, el parametro arg
	es un array de arrays, donde se encuentran
	digitos binarios."""
	def __init__(self, arg):
		self.arg = arg
		
	def getZero(self):
		contadory=0
		for linea in self.arg:
			contadorx=0
			for pixel in linea:
				if pixel==0:
					try:
						if(linea[contadorx-1]==1 and linea[contadorx+1]==1 and self.arg[contadory-1][contadorx]==1 and self.arg[contadory+1][contadorx]==1):
							retorno = [contadorx,contadory]
							return retorno		
					except Exception as e:
						return [0,0]
				contadorx=contadorx+1
			contadory=contadory+1
		return [0,0]
		

#Tomamos los datos
fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(fileDir, 'imagenes/')
#A continuacion se toman las fechas
with open("fechas.txt") as f:
    fechas = f.readlines()
#A continuacion se toman las imagenes
for image in range(1,5):
	original = Image.open(filename+'/'+str(image)+'.jpg')
	#Convertimos a escala de grises
	mod = original.convert('L')
	array = np.asarray(mod.resize((130,130)), dtype=np.float32)
	respuesta = []
	b = array
	#Convertimos a bianrio
	for i in b:
	    lista= []
	    for pixel in i:
	        if(pixel<50):
	            lista.append(0)
	        elif(pixel>50):
	            lista.append(1)
	    respuesta.append(lista)
	matrix = Matrix(respuesta)
	respuesta = matrix.getZero()
	print(fechas[0])
	with open('data.csv',mode='a') as document:
		document = csv.writer(document,delimiter=',',quoting=csv.QUOTE_ALL)
		fecha = fechas[image-1]
		fecha = fecha.replace("\n"," ")
		fecha = fecha.replace("\t"," ")
		vertical = str(respuesta[1])
		document.writerow([fecha,str(respuesta[0]),vertical])
df = pd.read_csv('data.csv')
print(df)
npMatrix = np.matrix(df)
x, y = npMatrix[:0],npMatrix[:1]
x, y = x.reshape(-1,1), y.reshape(-1, 1)
lin_regression = LinearRegression()
lin_regression.fit(x,y)
m = lin_regression.coef_(0)
b = lin_regression.intercept_
print('formula: y = {0}x + {1}'.format(m,b))
plt.scatter(X,Y,color='blue')
plt.pyplot([0,100],[b.m*100+b],'r')
plt.tittle('Linear Regression',fontsize=20)
plt.xlabel('X',fontsize=15)
plt.ylabel('Y',fontsize=15)


