import pandas as pd
import numpy as np
import random

restriccion=999


df = pd.read_csv("data.csv", header=None)
data = df.values
n = len(data[0])
m = len(data)
for i in range(3):
    fila=np.zeros(n)
    data = np.vstack((data,fila))

#MEJOR SOLUCION
#indice de sensibilidad
for i in range(len(data[0])):
    data[2][i] = round(data[0][i]/data[1][i],1)
    data[3][i] = i+1.0

matriz = np.array(data)

matriz_ordenada = sorted(zip(data[2], *data), reverse=True) #ordenamos matriz tomando como referencia el costo
matriz = [list(x) for x in zip(*matriz_ordenada)]
print(matriz)
del matriz[0]#se eliminar la primera fila para que la matriz quede normal

#calculamos costo y volumen
costo=0
volumen=0
fila=0
while volumen<=restriccion and fila<len(data[0]):
    if(volumen+matriz[1][fila])<=restriccion:
        costo=costo+matriz[0][fila]
        volumen=volumen+matriz[1][fila]
        matriz[4][fila]=1.0
    fila=fila+1

matriz_ordenada = sorted(zip(matriz[3], *matriz)) #ordenamos matriz tomando como referencia el costo
matriz = [list(x) for x in zip(*matriz_ordenada)]
del matriz[0]#se eliminar la primera fila para que la matriz quede normal

print(f"\n**MEJOR SOLUCION**")
for i in range(len(matriz[0])):
    print(int(matriz[4][i]), end=" | ")
print(f"\nCosto={costo}\nVolumen={volumen}")

#mejoramos la solucion
iteraciones=0
costo_n=0
volumen_n=0

while iteraciones<1000:
    i=random.randint(0,len(matriz[0]))
    j=i+1
    if i!=len(matriz[0]):       
        if matriz[4][i]==0:
            if j<len(matriz[0]):
                volumen_n=volumen+matriz[1][j]
                costo_n=costo_n+matriz[0][j]
                if volumen_n<restriccion:
                    volumen=volumen_n
                    costo=costo_n
                    matriz[4][j]=1
        if matriz[4][i]==1:
            volumen_n=volumen-matriz[1][i]
            costo_n=costo-matriz[0][i]
            if j<len(matriz[0]):
                volumen_n=volumen+matriz[1][j]
                costo_n=costo+matriz[0][j]
                if volumen_n<restriccion:
                    volumen=volumen_n
                    costo=costo_n
                    matriz[4][j]=1
                    matriz[4][i]=0
    iteraciones+=1

#presentamos la solucion mejorada
print("\n**SOLUCION MEJORADA**")
for i in range(n):
    print(int(matriz[4][i]), end=" | ")
print(f"\nCosto: {costo}\nVolumen: {volumen}")