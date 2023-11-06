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
# rep = 0
# vol = 0
# cos = 0
# restriccion = 999
# costoSum = 0
# volumSum = 0
# i = 0
# valores_seleccionados = [0 for i in range(len(matriz[0]))]


# valores_resultado = [0 for i in range(len(matriz[0]))]
# print(valores_seleccionados)

# v = vol
# if v > restriccion:
#     v = 0
# print(vol) 
# while rep < 300:
    
#     r = random.randint(0, len(matriz[0])-1)
    
#     print("Rand:", r)
#     print("costo: ", matriz[0][r])
#     print("vol: ", matriz[1][r])

#     if valores_seleccionados[r] == 0:
        
#         if vol < restriccion:    
#             cos = cos + matriz[0][r]
#             vol = vol + matriz[1][r]
#             valores_seleccionados[r] = 1
#             print(valores_seleccionados)
#             print("Sumando-Costo-volumen: ",cos, vol)    
#     else:
#         if vol > restriccion:
#             cos = cos - matriz[0][r]
#             vol = vol - matriz[1][r]
#             valores_seleccionados[r] = 0
#             print(valores_seleccionados)
#             print("Restando-Costo-volumen: ",cos, vol) 

#     if vol > v and vol < restriccion:
#         resultado = "Costo: " + str(cos) +" Volumen: " +str(vol)  #Guardamos los valores
#         for i in range(len(valores_resultado)):
#             valores_resultado[i] = valores_seleccionados[i]
        
#         v = vol
#         print("mejoro:", vol)
    
#     rep = rep + 1



rep = 0
vol = 0
cos = 0
restriccion = 999
valores_seleccionados = [0 for _ in range(len(matriz[0]))]

mejor_costo = 0
mejor_volumen = 0
mejores_valores = [0 for _ in range(len(matriz[0]))]

print(valores_seleccionados)

v = vol
if v > restriccion:
    v = 0
print(vol) 
while rep < 3000:
    r = random.randint(0, len(matriz[0])-1)
    
    print("Rand:", r)
    print("costo: ", matriz[0][r])
    print("vol: ", matriz[1][r])

    if valores_seleccionados[r] == 0:
        if vol < restriccion:    
            cos += matriz[0][r]
            vol += matriz[1][r]
            valores_seleccionados[r] = 1
            print(valores_seleccionados)
            print("Sumando-Costo-volumen: ", cos, vol)    
    else:
        if vol > restriccion:
            cos -= matriz[0][r]
            vol -= matriz[1][r]
            valores_seleccionados[r] = 0
            print(valores_seleccionados)
            print("Restando-Costo-volumen: ", cos, vol) 

    if vol > v and vol < restriccion:
        resultado = "Costo: " + str(cos) + " Volumen: " + str(vol)  # Guardamos los valores
        mejores_valores = valores_seleccionados.copy()
        v = vol
        print("mejoro:", vol)
    
    rep += 1

anclado = zip(matriz[0],matriz[1],mejores_valores)
valores_ordenados = sorted(anclado, key = lambda x:x[2]  )
#Imprimimos los valores 
for i in valores_ordenados:
    print(i)

print("mejor valor:", v)
print(mejores_valores, resultado)
print("costo: ",cos)
print("volumen: ",vol)