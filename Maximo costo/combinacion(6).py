
# importing libraries
import numpy as np
import pandas as pd
import random 
# div-ordeno-sumo
# ordeno-div-sumo

# Recoleccion de datos
datasheet = pd.read_csv("matriz.csv",sep=';',header=None) #Leemos los valores
print(datasheet)
matriz = datasheet.to_numpy().tolist() #Convertimos el dataframe a una matriz de python

print(matriz)

#(1)

valores_seleccionados = [0 for i in range(len(matriz[0]))] #Creamos el vector de resultados inicializado en cero

# Declaramos variables
restriccion = 26
costoSum = 0
volumSum = 0
i = 0
#Realizamos la suma acumulativa
while volumSum < restriccion:
        resultado = "Costo: " + str(costoSum) +" Volumen: " +str(volumSum) #Guardamos los valores
        ultimoCos = costoSum
        ultimoVol = volumSum  
        costoSum  += matriz[0][i]
        volumSum += matriz[1][i]
        #Si la suma de volumen es menor a 26, los valores cero de valores_seleccionados se iran cambiando por uno
        if volumSum < restriccion: 
                valores_seleccionados[i] = 1
        i += 1 
matriz.append(valores_seleccionados) 
      
print(matriz[0])
print(matriz[1])
print(matriz[2])      
print(resultado)


valores_resultado = [0 for i in range(len(matriz[0]))]


#(5)

rep = 0
v = ultimoVol

if v > 26:
    v = 0
print(ultimoVol)
print(valores_seleccionados)
while rep < 1000:
    
    r = random.randint(0, 9)
    # while rguard == r:
    #     print("El numero es igual", r)
    #     r = random.randint(0, 9)
    
    # print("guardado ",rguard)
    # rguard = r   
    
    print("Rand:", r)
    print("costo: ", matriz[0][r])
    print("vol: ", matriz[1][r])
    print("volumsum: ", ultimoVol)
    if ultimoVol < 26:
        
        if valores_seleccionados[r] == 0:    
            ultimoVol = ultimoVol + matriz[1][r]
            ultimoCos = ultimoCos + matriz[0][r]
            valores_seleccionados[r] = 1
            print(valores_seleccionados)
            print("Sumando: ", ultimoVol)    
    else:
        if valores_seleccionados[r] == 1:
            ultimoCos = ultimoCos - matriz[0][r]
            ultimoVol = ultimoVol - matriz[1][r]
            valores_seleccionados[r] = 0
            print(valores_seleccionados)
            print("restando:", ultimoVol)

    if ultimoVol > v and ultimoVol < 26:
        resultado = "Costo: " + str(ultimoCos) +" Volumen: " +str(ultimoVol)  #Guardamos los valores
        for i in range(len(valores_resultado)):
            valores_resultado[i] = valores_seleccionados[i]
        v = ultimoVol
        print("mejoro:", ultimoVol)
    
    rep = rep + 1


print(matriz[0])
print(matriz[1])    
print(valores_resultado)
print("mejor valor:", v)
print(resultado)
print("costo: ",ultimoCos)
print("volumen: ",ultimoVol)