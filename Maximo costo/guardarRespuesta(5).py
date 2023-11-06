# importing libraries
import numpy as np
import pandas as pd
import random

# Recoleccion de datos
datasheet = pd.read_csv("text1.csv",header=None)
print(datasheet)
matriz = datasheet.to_numpy().tolist()
print(matriz)


valores_seleccionados = [0 for i in range(len(matriz[0]))]
valores_resultado = [0 for i in range(len(matriz[0]))]
print(valores_seleccionados)
rep = 0
vol = 0 
cos = 0
v = vol

if v > 26:
    v = 0
print(vol)
while rep < 60:
    
    r = random.randint(0, 9)
    # while rguard == r:
    #     print("El numero es igual", r)
    #     r = random.randint(0, 9)
    
    # print("guardado ",rguard)
    # rguard = r   
    
    print("Rand:", r)
    print("costo: ", matriz[0][r])
    print("vol: ", matriz[1][r])

    if vol < 26:
        
        if valores_seleccionados[r] == 0 :    
            vol = vol + matriz[1][r]
            cos = cos + matriz[0][r]
            valores_seleccionados[r] = 1
            print(valores_seleccionados)
            print("Sumando: ", vol)    
    else:
        if valores_seleccionados[r] == 1:
            cos = cos - matriz[0][r]
            vol = vol - matriz[1][r]
            valores_seleccionados[r] = 0
            print(valores_seleccionados)
            print("restando:", vol)

    if vol > v and vol < 26:
        resultado = "Costo: " + str(cos) +" Volumen: " +str(vol)  #Guardamos los valores
        
        for i in range(len(valores_resultado)):
            valores_resultado[i] = valores_seleccionados[i]
        
        v = vol
        print("mejoro:", vol)
    
    rep = rep + 1


print(matriz[0])
print(matriz[1])    
print(valores_resultado)
print("mejor valor:", v)
print(resultado)
print("costo: ",cos)
print("volumen: ",vol)