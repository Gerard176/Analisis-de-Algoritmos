# def factorial(n):
#     print(factorial(n))
#     return 1 if n == 0 else factorial(n-1)*n
    

# resultado = factorial(5)

# print(resultado)
# import random

# max_mem = 3
# my_set = []


# for i in range(10):
#     r = random.randint(0, 49)
#     print("Random: ",r)
#     if len(my_set) < max_mem and r not in my_set:
#         my_set.append(r) 
#     elif r in my_set:
#         print("El numero se repite dentro de la memoria: ", r)  
#         r2 = random.randint(0, 9)
#         print("Nuevo numero: ",r2)
#         while r2 in my_set:
#             print("Vuelve a estar dentro de la memoria: ",r2)
#             r2 = random.randint(0, 9)   
            
#         print("numero resultante: ",r2)    
#         r = r2
#         if len(my_set) < max_mem:
#             my_set.append(r)
#         else:
#             my_set.pop(0)
#             my_set.append(r)    
#     else:
#         my_set.pop(0)
#         my_set.append(r)    
#     #proceso
#     print(my_set,"Iteracion: ", i)


import numpy as np
import pandas as pd



# Recoleccion de datos
datasheet = pd.read_csv("data.csv",header=None)
print(datasheet)
matriz = datasheet.to_numpy().tolist()
print(matriz)

#Declaramos variables
rango = len(matriz[0]) # Largo de la matriz

vecindades = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

valores_seleccionados = [0 for i in range(rango)] #Creamos el vector de resultados inicializado en cero
# Declaramos variables
restriccion = 999
mejor_vol = 0
mejor_cos = 0

#Realizamos la suma
for x in range(len(vecindades)):
    
    costoSum = 0
    volumSum = 0
    i = 0
    while volumSum < restriccion and i < len(vecindades[0]):
         
        if vecindades[x][i] == 1:
                
            costoSum  += matriz[0][i] 
            volumSum += matriz[1][i]
            resultado = "Costo: " + str(costoSum) +" Volumen: " +str(volumSum)
                # print(costoSum)
            
        i += 1 
    
    print("Costo",costoSum)
    print("Volumen",volumSum)
    if costoSum > mejor_cos and volumSum >= mejor_vol:
         print("Costo maximo: ",costoSum)
         print("Volumen maximo: ",volumSum)
         
         mejor_cos = costoSum
         mejor_vol = volumSum


print(mejor_cos, mejor_vol)
