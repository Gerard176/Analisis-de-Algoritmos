import warnings
warnings.filterwarnings("ignore")

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

#Inicializamos variables
largo = len(matriz[0])
print(largo)
numero_divisiones = 2 #declaramos el numero de divisiones
ListaAuxiliarCosto = []
ListaAuxiliarVolumen = []
matrizAuxiliar = []
relacion  = []
indices = []
n = (largo//numero_divisiones) #este es el largo que debe tener cada matriz al dividirla
a = n #guardamos el largo original

#Dividimos la matriz
for indice, numero in enumerate(matriz[0]):
    relacion.append(round(matriz[0][indice] / matriz[1][indice],2)) #Creamos un array para guardar el indice de relacion
    indices.append(indice) #Creamos un array de indices del 0 al 9
    
    print(indices)
    # recorremos los valores de costo y volumen hasta el largo n
    if indice < n:
        #Guardamos los valores en arrays auxiliares
        ListaAuxiliarCosto.append(matriz[0][indice]) 
        ListaAuxiliarVolumen.append(matriz[1][indice])
        print(ListaAuxiliarCosto)
        print(n)
        #Si estamos en la ultima posicion de la primera matriz
    if indice == n-1:
        #Guardamos los arrays en una nueva matriz
        matrizAuxiliar.append(relacion)
        matrizAuxiliar.append(ListaAuxiliarCosto) 
        matrizAuxiliar.append(ListaAuxiliarVolumen)
        matrizAuxiliar.append(indices)

        #reiniciamos los valores de cada array
        relacion = []
        indices = []
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

#Ordenamos la matrizAuxiliar
c = 0
matrices_ordenadas = []
for i in range(numero_divisiones): #Segun el numero de divisiones 
    print(i,c,  matrizAuxiliar[c], matrizAuxiliar[c+1])
    anclado = zip(matrizAuxiliar[c], matrizAuxiliar[c+1],matrizAuxiliar[c+2],matrizAuxiliar[c+3]) #asociamos los valores de la matriz que se encuentran intercalados(Costo,volumen,indice)
    valores_ordenados = sorted(anclado, key = lambda x:x[0], reverse=True) #Le decimos que los ordene de mayor a menor segun el costo   
    matriz_ordenada = []
    matriz_ordenada.append(matrizAuxiliar[c])
    matriz_ordenada.append(matrizAuxiliar[c+1])
    matriz_ordenada.append(matrizAuxiliar[c+2])
    matriz_ordenada.append(matrizAuxiliar[c+3])
    #Revisamos que todo vaya en orden
    print(matriz_ordenada) 
    for j in valores_ordenados:
        print(j)
    #Reemplazamos los valores de la matriz actual por los ordenados    
    for j in range(a):
        matriz_ordenada[0][j] = valores_ordenados[j][0]
        matriz_ordenada[1][j] = valores_ordenados[j][1]
        matriz_ordenada[2][j] = valores_ordenados[j][2]
        matriz_ordenada[3][j] = valores_ordenados[j][3]
    matrices_ordenadas.append(matriz_ordenada)        
    c += 4 #Aumentamos c en 3 para que en la proxima iteracion revise las proximas 3 posiciones de la matriz

print(matrices_ordenadas)
matrices_ordenadas = [elemento for sublista in matrices_ordenadas for elemento in sublista] #Simplificamos la matriz
print(matrices_ordenadas)
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
            costoSum  += matrices_ordenadas[c+1][i]
            volumSum += matrices_ordenadas[c+2][i]
            # print(costoSum)
            print(volumSum)
            if volumSum < restriccion:
                valores_seleccionados[r] = 1
            print(valores_seleccionados)    
            r += 1
            i += 1
                        
    c += 4 #aumentamos de 4 en 4

#Dividimos el array de valores_seleccionados para poderlo incluir en matrices_ordenadas
ListaAuxiliarValoresSeleccionados = []
ListaAuxiliar = []
print(a, "Esta es a")
b = a
#Realizamos el mismo proceso de arriba, teniendo en cuenta que el valor de n ha cambiado
for indice, numero in enumerate(matriz[0]):
    if indice < a:
        ListaAuxiliarValoresSeleccionados.append(valores_seleccionados[indice])
        print(ListaAuxiliarValoresSeleccionados)
        print(a)
    if indice == a-1:
        ListaAuxiliar.append(ListaAuxiliarValoresSeleccionados)
        ListaAuxiliarValoresSeleccionados = []
        j = 0
        while j != b:
            a = a+1
            j = j+1
            print(a, j, b)

        # print(n)
print(ListaAuxiliar)
print(matrices_ordenadas)
print(valores_seleccionados)
print(resultado)

matriz_resultante = []
#Reordenamos la matriz a sus posiciones originales
c = 0
for i in range(numero_divisiones):
    
    anclado = zip(matrices_ordenadas[c], matrices_ordenadas[c+1],matrices_ordenadas[c+2] ,ListaAuxiliar[i],matrices_ordenadas[c+3])# Asociamos todos los arrays de la matriz 
    valores_ordenados = sorted(anclado, key = lambda x:x[-1])   #la organizamos en base al tercer array que es el de indices normales
    matriz_ordenada = []
    matriz_ordenada.append(matrices_ordenadas[c])
    matriz_ordenada.append(matrices_ordenadas[c+1])
    matriz_ordenada.append(matrices_ordenadas[c+2])
    matriz_ordenada.append(ListaAuxiliar[i])
    matriz_ordenada.append(matrices_ordenadas[c+3])
    print("Display vertical: costo|volumen|indice original|productos seleccionados: por matriz individual ")
    
    for i in valores_ordenados:
        print(i)
    #Reemplazamos los valores de la matriz anterior por los nuevos
    for j in range(b): 
        matriz_ordenada[0][j] = valores_ordenados[j][0]
        matriz_ordenada[1][j] = valores_ordenados[j][1]
        matriz_ordenada[2][j] = valores_ordenados[j][2]
        matriz_ordenada[3][j] = valores_ordenados[j][3]
        matriz_ordenada[4][j] = valores_ordenados[j][4]
    matriz_resultante.append(matriz_ordenada)        
    c += 4
# mostramos el resultado
print("Display horizontal: costo|volumen|indice original|productos seleccionados:primeros cuatro vectores forman la primera matriz")

print(matriz_resultante)
print(resultado)
     




