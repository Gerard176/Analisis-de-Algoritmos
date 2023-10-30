import numpy as np
import pandas as pd
import random

# Recoleccion de datos
datasheet = pd.read_csv("text1.csv",header=None)
print(datasheet)
matriz = datasheet.to_numpy().tolist()
print(matriz)


#Declaramos variables
rango = len(matriz[0]) # Largo de la matriz
relacion = []
normalizacion = []
indice = []
#Creamos el indice dividiendo costo sobre volumen
for i in range(rango): 
    relacion.append(matriz[0][i] / matriz[1][i]) #Creamos un array para guardar el indice de relacion
    indice.append(i) #Creamos un array de indices del 0 al 9
for i in range(rango):
      mayorRelacion = max(relacion)
      normalizacion.append(relacion[i]/mayorRelacion)


# Agregamos estos arrays a la matriz
matriz.append(relacion)
matriz.append(indice) 
matriz.append(normalizacion)
print(matriz)

anclado = zip(matriz[3],matriz[0],matriz[1],matriz[4], matriz[2]) #Asociamos los cuatro arrays que se encuentran en este momento dentro de la matriz
valores_ordenados = sorted(anclado, key = lambda x:x[-1], reverse=True) #Le decimos a python que los ordene de mayor a menor con base al ultimo de los arrays    
matriz_ordenada = matriz # Creamos una matriz parecida a la original para reemplazar los valores nuevos en ella
#Reemplazamos los valores de la matriz original por los nuevos ordenados


for i in range(rango):
    matriz_ordenada[0][i] = valores_ordenados[i][0]
    matriz_ordenada[1][i] = valores_ordenados[i][1]
    matriz_ordenada[2][i] = valores_ordenados[i][2]
    matriz_ordenada[3][i] = valores_ordenados[i][3]
    matriz_ordenada[4][i] = valores_ordenados[i][4]
        
print(matriz_ordenada[0])
print(matriz_ordenada[1])
print(matriz_ordenada[2])
print(matriz_ordenada[3])
print(matriz_ordenada[4])


#Elegimos los valores que cumplen con la condicion para la normalizacion


valores_seleccionados = [0 for i in range(len(matriz_ordenada[0]))]
valores_resultado = [0 for i in range(len(matriz_ordenada[0]))]
print(valores_seleccionados)
rep = 0
vol = 0 
cos = 0
v = vol

if v > 26:
    v = 0
print(vol)
while rep < 40:

    r = random.randint(0, 9)
       
    print("Rand:", r)
    print("costo: ", matriz_ordenada[1][r])
    print("vol: ", matriz_ordenada[2][r])
    print("Normalizacion: ",matriz_ordenada[3][r])
    if vol < 26 and matriz_ordenada[3][r] > 0.2 and matriz_ordenada[3][r]< 0.8:

        if valores_seleccionados[r] == 0 :
            cos = cos + matriz_ordenada[1][r]  
            vol = vol + matriz_ordenada[2][r]
            # if vol < 26:
            valores_seleccionados[r] = 1
            print(valores_seleccionados)
            print("Sumando: ", vol)    
    else:
        if valores_seleccionados[r] == 1:
            cos = cos - matriz_ordenada[1][r]
            vol = vol - matriz_ordenada[2][r]
            valores_seleccionados[r] = 0
            print(valores_seleccionados)
            print("restando:", vol)

    if vol > v and vol < 26:
        resultado = "Costo: " + str(cos) +" Volumen: " +str(vol)  #Guardamos los valores
        for i in range(len(valores_resultado)):
            valores_resultado[i] = valores_seleccionados[i]
        v = vol
        print("mejoró:", vol)
    
    rep = rep + 1


print('     '.join(map(str, matriz_ordenada[1])))
print('     '.join(map(str, matriz_ordenada[2])))
print(' '.join(map(str, matriz_ordenada[3])))  
print('     '.join(map(str, valores_seleccionados)))
print("mejor valor:", v)
print(resultado)
print("costo: ",cos)
print("volumen: ",vol)



#Regresamos los valores a sus posiciones originales    
anclado = zip(matriz_ordenada[0],matriz_ordenada[1],matriz_ordenada[2], matriz_ordenada[3],matriz_ordenada[4], valores_resultado) #Asociamos todos los arrays de la matriz
valores_ordenados = sorted(anclado, key = lambda x:x[0])#Los ordenamos con respecto al primer array que en este caso es el array de indices iniciales
matriz_ordenada.append(valores_seleccionados)
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
    matriz_ordenada[5][i] = valores_ordenados[i][5]
print("Display horizontal: indice original|costo|volumen|indice relacion|productos seleccionados")
print(matriz_ordenada[0])
print(matriz_ordenada[1])
print(matriz_ordenada[2])
print(matriz_ordenada[3])    
print(matriz_ordenada[4])   
print(matriz_ordenada[5])   
print(resultado)
