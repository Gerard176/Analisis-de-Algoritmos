import numpy as np
import pandas as pd



# Recoleccion de datos
datasheet = pd.read_csv("matriz.csv",sep=';',header=None)
print(datasheet)
matriz = datasheet.to_numpy().tolist()
print(matriz)

#Declaramos variables
rango = len(matriz[0]) # Largo de la matriz
relacion = []
indice = []
#Creamos el indice dividiendo costo sobre volumen
for i in range(rango): 
    relacion.append(matriz[0][i] / matriz[1][i]) #Creamos un array para guardar el indice de relacion
    indice.append(i) #Creamos un array de indices del 0 al 9
# Agregamos estos arrays a la matriz
matriz.append(relacion) 
matriz.append(indice) 

anclado = zip(matriz[3],matriz[0],matriz[1], matriz[2]) #Asociamos los cuatro arrays que se encuentran en este momento dentro de la matriz
valores_ordenados = sorted(anclado, key = lambda x:x[-1], reverse=True) #Le decimos a python que los ordene de mayor a menor con base al ultimo de los arrays    
matriz_ordenada = matriz # Creamos una matriz parecida a la original para reemplazar los valores nuevos en ella
#Reemplazamos los valores de la matriz original por los nuevos ordenados
for i in range(rango):
    matriz_ordenada[0][i] = valores_ordenados[i][0]
    matriz_ordenada[1][i] = valores_ordenados[i][1]
    matriz_ordenada[2][i] = valores_ordenados[i][2]
    matriz_ordenada[3][i] = valores_ordenados[i][3]

print(matriz_ordenada)

valores_seleccionados = [0 for i in range(len(matriz[0]))] #Creamos el vector de resultados inicializado en cero
# Declaramos variables
restriccion = 26
costoSum = 0
volumSum = 0
i = 0
#Realizamos la suma usando matriz_ordenada
while volumSum < restriccion:
        resultado = "Costo: " + str(costoSum) +" Volumen: " +str(volumSum)  #Guardamos los valores
        costoSum  += matriz_ordenada[1][i] 
        volumSum += matriz_ordenada[2][i]
        # print(costoSum)
        print(volumSum)
        if volumSum < restriccion:
                valores_seleccionados[i] = 1
        i += 1 
matriz_ordenada.append(valores_seleccionados) 


#Regresamos los valores a sus posiciones originales    
anclado = zip(matriz_ordenada[0],matriz_ordenada[1],matriz_ordenada[2], matriz_ordenada[3],matriz_ordenada[4]) #Asociamos todos los arrays de la matriz
valores_ordenados = sorted(anclado, key = lambda x:x[0])#Los ordenamos con respecto al primer array que en este caso es el array de indices iniciales
matriz_ordenada = matriz
print("Display vertical: indice original|costo|volumen|indice relacion|productos seleccionados")
for i in valores_ordenados:
      print(i)
#realizamos la reescritura de los valores de la matriz
for i in range(rango):
    matriz_ordenada[0][i] = valores_ordenados[i][0]
    matriz_ordenada[1][i] = valores_ordenados[i][1]
    matriz_ordenada[2][i] = valores_ordenados[i][2]
    matriz_ordenada[3][i] = valores_ordenados[i][3]
    matriz_ordenada[4][i] = valores_ordenados[i][4]
print("Display horizontal: indice original|costo|volumen|indice relacion|productos seleccionados")
print(matriz_ordenada[0])
print(matriz_ordenada[1])
print(matriz_ordenada[2])
print(matriz_ordenada[3])    
print(matriz_ordenada[4])   
print(resultado)