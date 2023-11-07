# importing libraries
import numpy as np
import pandas as pd
import random

# Recoleccion de datos
datasheet = pd.read_csv("data.csv",header=None)
print(datasheet)
matriz = datasheet.to_numpy().tolist()
print(matriz)
# vol = 100422
# cos = 120422

#Declaramos variables
rep = 0
vol = 0
cos = 0
restriccion = 999
costoSum = 0
volumSum = 0
i = 0
valores_seleccionados = [0 for i in range(len(matriz[0]))] #Valores iniciales
valores_resultado = [0 for i in range(len(matriz[0]))] #Valores reslutado final

v = vol
if v > restriccion:
    v = 0

#Iniciamos la mejora
while rep < 3000:
    #Creamos el numero random
    r = random.randint(0, len(matriz[0])-1)
    
    print("Rand:", r)
    print("costo: ", matriz[0][r])
    print("vol: ", matriz[1][r])
    #Miramos si la posicion en la que aparecio el random esta el valor seleccionado o no
    if valores_seleccionados[r] == 0:
        #Miramos que la suma del volumen no haya sobrepasado la restriccion 
        if vol < restriccion:    
            #Realizamos la suma
            cos = cos + matriz[0][r] 
            vol = vol + matriz[1][r]
            #Cambiamos el valor de cero a uno
            valores_seleccionados[r] = 1
            print(valores_seleccionados)
            print("Sumando-Costo-volumen: ",cos, vol)     
    else:
        #En este caso miramos que si se ha sobrepasado el limite se haga una resta
        # if vol > restriccion:
            cos = cos - matriz[0][r]
            vol = vol - matriz[1][r]
            # al restar, cambiamos el valor de un uno a un cero
            valores_seleccionados[r] = 0
            print(valores_seleccionados)
            print("Restando-Costo-volumen: ",cos, vol) 

    if vol > v and vol < restriccion:
        resultado = "Costo: " + str(cos) +" Volumen: " +str(vol)  #Guardamos los valores
        for i in range(len(valores_resultado)):
            valores_resultado[i] = valores_seleccionados[i]
        
        v = vol
        print("mejoro:", vol)
    
    rep = rep + 1





anclado = zip(matriz[0],matriz[1],valores_resultado)
valores_ordenados = sorted(anclado, key = lambda x:x[2]  )
#Imprimimos los valores 
for i in valores_ordenados:
    print(i)

print("mejor valor:", v)
print(valores_resultado, resultado)
print("costo: ",cos)
print("volumen: ",vol)