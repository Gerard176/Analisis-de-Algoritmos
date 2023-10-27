# importing libraries
import numpy as np
import pandas as pd

# div-ordeno-sumo
# ordeno-div-sumo

# Recoleccion de datos
datasheet = pd.read_csv("matriz.csv",sep=';',header=None)
print(datasheet)
matriz = datasheet.to_numpy().tolist()
print(matriz)

rango = len(matriz[0])
relacion = []
indice = []
#Creamos los indices de relacion y de la matriz original
for i in range(rango):
    relacion.append(matriz[0][i] / matriz[1][i])
    indice.append(i)
#los incluimos en la matriz    
matriz.append(relacion)
matriz.append(indice)
print(matriz)
anclado = zip(matriz[3],matriz[0],matriz[1], matriz[2]) #Asociamos los valores de los arrays de la matriz
valores_ordenados = sorted(anclado, key = lambda x:x[-1], reverse=True)   #Le decimos a python que los ordene por el ultimo array asociado
for i in valores_ordenados:
    print(i)
matriz_ordenada = matriz
#Reemplazamos los valores de la matriz por los nuevos
for i in range(rango):
    matriz_ordenada[0][i] = valores_ordenados[i][0]
    matriz_ordenada[1][i] = valores_ordenados[i][1]
    matriz_ordenada[2][i] = valores_ordenados[i][2]
    matriz_ordenada[3][i] = valores_ordenados[i][3]

print(matriz_ordenada)

#Inicializamos variables
largo = len(matriz[0])
print(largo)
numero_divisiones = 2 #declaramos el numero de divisiones
ListaAuxiliarCosto = []
ListaAuxiliarVolumen = []
ListaIndicesOriginales = []
ListaIndicesRelacion = []
matrizAuxiliar = []
indices = []
n = (largo//numero_divisiones) #este es el largo que debe tener cada matriz al dividirla
a = n #guardamos el largo original

#Dividimos la matriz
for indice, numero in enumerate(matriz[0]):
    # recorremos los valores de costo y volumen hasta el largo n
    if indice < n:
        #Guardamos los valores en arrays auxiliares
        ListaIndicesOriginales.append(matriz_ordenada[0][indice])
        ListaAuxiliarCosto.append(matriz_ordenada[1][indice]) 
        ListaAuxiliarVolumen.append(matriz_ordenada[2][indice])
        ListaIndicesRelacion.append(matriz_ordenada[3][indice])
        print(ListaAuxiliarCosto)
        print(n)
        #Si estamos en la ultima posicion de la primera matriz
    if indice == n-1:
        #Guardamos los arrays en una nueva matriz
        matrizAuxiliar.append(ListaIndicesOriginales)
        matrizAuxiliar.append(ListaAuxiliarCosto) 
        matrizAuxiliar.append(ListaAuxiliarVolumen)
        matrizAuxiliar.append(ListaIndicesRelacion)
        #reiniciamos los valores de cada array
        ListaIndicesOriginales = []
        ListaIndicesRelacion = []
        ListaAuxiliarCosto = []
        ListaAuxiliarVolumen = []
        j = 0
        #aumentamos n las veces que necesitamos
        while j != a:
            n = n+1
            j = j+1
            print(n, j, a)

        # print(n)
print(matrizAuxiliar)


valores_seleccionados = [0 for i in range(len(matriz[0]))]    
restriccion = 26
costoSum = 0
volumSum = 0
i = 0
c = 0
r = 0
#Realizamos la suma guardando el resultado de cada matriz
for j in range(numero_divisiones):
    #Reiniciamos i cada vez que sea igual al largo de cada matriz
    if i == a:
        i = 0 
    #Realizamos la suma acumulativa   
    while volumSum < restriccion and i != a: # si estamos en una posicion diferente al largo de cada matriz entonces entrara
            resultado = "Costo: " + str(costoSum) +" Volumen: " +str(volumSum)  
            costoSum  += matrizAuxiliar[c+1][i]
            volumSum += matrizAuxiliar[c+2][i]
            # print(costoSum)
            print(volumSum)
            if volumSum < restriccion:
                valores_seleccionados[r] = 1
            print(valores_seleccionados)    
            r += 1
            i += 1
                        
    c += 4 #aumentamos de 4 en 4
print(matrizAuxiliar)
print(resultado)
ListasUnidas = []
ListaIndicesOriginales = []
ListaIndicesRelacion = []
ListaAuxiliarCosto = []
ListaAuxiliarVolumen = []
c = 0
for i in range(numero_divisiones):
    ListaIndicesOriginales +=matrizAuxiliar[c]
    ListaAuxiliarCosto += matrizAuxiliar[c+1]
    ListaAuxiliarVolumen += matrizAuxiliar[c+2]
    ListaIndicesRelacion +=matrizAuxiliar[c+3]
    
    c += 4
ListasUnidas.append(ListaIndicesOriginales)
ListasUnidas.append(ListaAuxiliarCosto)
ListasUnidas.append(ListaAuxiliarVolumen)
ListasUnidas.append(ListaIndicesRelacion)
print(ListasUnidas)

matriz_resultante = []
#Reordenamos la matriz a sus posiciones originales
    
anclado = zip(ListasUnidas[0], ListasUnidas[1],ListasUnidas[2],ListasUnidas[3] ,valores_seleccionados)# Asociamos todos los arrays de la matriz 
valores_ordenados = sorted(anclado, key = lambda x:x[0])   #la organizamos en base al primer array que es el de indices normales
matriz_ordenada = []
matriz_ordenada.append(ListasUnidas[0])
matriz_ordenada.append(ListasUnidas[1])
matriz_ordenada.append(ListasUnidas[2])
matriz_ordenada.append(ListasUnidas[3])
matriz_ordenada.append(valores_seleccionados)
print("Display vertical: indice original|costo|volumen|indice relacion|productos seleccionados")
for i in valores_ordenados:
     print(i)
#Reemplazamos los valores de la matriz anterior por los nuevos

for j in range(rango): 
        matriz_ordenada[0][j] = valores_ordenados[j][0]
        matriz_ordenada[1][j] = valores_ordenados[j][1]
        matriz_ordenada[2][j] = valores_ordenados[j][2]
        matriz_ordenada[3][j] = valores_ordenados[j][3]
        matriz_ordenada[4][j] = valores_ordenados[j][4]
        
# mostramos el resultado
print("Display horizontal: indice original|costo|volumen|indice relacion|productos seleccionados")
print(matriz_ordenada)
print(resultado)