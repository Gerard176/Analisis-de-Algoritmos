
# importing libraries
import numpy as np
import pandas as pd

# div-ordeno-sumo
# ordeno-div-sumo

# Recoleccion de datos
datasheet = pd.read_csv("matriz.csv",sep=';',header=None) #Leemos los valores
print(datasheet)
matriz = datasheet.to_numpy().tolist() #Convertimos el dataframe a una matriz de python

print(matriz)
valores_seleccionados = [0 for i in range(len(matriz[0]))] #Creamos el vector de resultados inicializado en cero

# Declaramos variables
restriccion = 26
costoSum = 0
volumSum = 0
i = 0
#Realizamos la suma acumulativa
while volumSum < restriccion:
        resultado = "Costo: " + str(costoSum) +" Volumen: " +str(volumSum) #Guardamos los valores   
        costoSum  += matriz[0][i]
        volumSum += matriz[1][i]
        #Si la suma de volumen es menor a 26, los valores cero de valores_seleccionados se iran cambiando por uno
        if volumSum < restriccion: 
                valores_seleccionados[i] = 1
        i += 1 
        print(volumSum)
matriz.append(valores_seleccionados) 
      
print(matriz[0])
print(matriz[1])
print(matriz[2])      
print(resultado)