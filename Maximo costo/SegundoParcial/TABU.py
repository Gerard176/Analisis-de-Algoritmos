# importing libraries
import numpy as np
import pandas as pd
import random

# Recoleccion de datos
datasheet = pd.read_csv("text1.csv",header=None)
print(datasheet)
matriz = datasheet.to_numpy().tolist()
print(matriz)



#Declaramos variables
vecindades = []
cantidad_vecindades = 300
restriccion = 26
vecindad = 0

#Creamos un bucle para crear las diferentes vecindades

while vecindad < cantidad_vecindades:
    valores_seleccionados = [0 for i in range(len(matriz[0]))]
    valores_resultado = [0 for i in range(len(matriz[0]))]  
    rep = 0
    vol = 0 
    cos = 0 
    v = vol

    if v > restriccion:
        v = 0
 
    while rep < 500:
    
        r = random.randint(0, len(matriz[0])-1)
    
        # print("Rand:", r)
        # print("costo: ", matriz[0][r])
        # print("vol: ", matriz[1][r])

        if valores_seleccionados[r] == 0:
        
            if vol <= restriccion:    
                vol = vol + matriz[1][r]
                cos = cos + matriz[0][r]
                valores_seleccionados[r] = 1
                # print(valores_seleccionados)
                # print("Sumando-Costo-volumen: ",cos, vol)    
        else:
            if vol >= restriccion:
                cos = cos - matriz[0][r]
                vol = vol - matriz[1][r]
                valores_seleccionados[r] = 0
                # print(valores_seleccionados)
                # print("Restando-Costo-volumen: ",cos, vol) 

        if vol > v and vol <= restriccion:
            resultado = "Costo: " + str(cos) +" Volumen: " +str(vol)  #Guardamos los valores
            for i in range(len(valores_resultado)):
                valores_resultado[i] = valores_seleccionados[i]
            v = vol
            # print("mejoro:", vol)
    
        rep = rep + 1


    # anclado = zip(matriz[0],matriz[1],valores_resultado)
    # valores_ordenados = sorted(anclado, key = lambda x:x[0] )
    vecindades.append(valores_resultado)
    vecindad += 1
   

print(vecindades)

#Instanciamos variables
capacidad_memoria = 3
rep_vecindades = 0
rep_mejora = 0
mejor_vol = 0
mejor_cos = 0
mejor_resultado = [0 for i in range(len(matriz[0]))]
memoria = []
#Creamos el bucle que mirara en vecindades aleatorias segun la memoria
while rep_vecindades < 300:
    print("Nueva vecindad")
    #Creamos la memoria
    r = random.randint(0, len(vecindades)-1)
    print(matriz[0])
    print(matriz[1])
    print(vecindades[r])
    # print("Random: ",r)

    if len(memoria) < capacidad_memoria and r not in memoria: #Miramos que la capacidad de la memoria no este llena y que el numero que vamos a agregar no este repetido
        memoria.append(r) 
    elif r in memoria: # Si el numero esta repetido entonces
        # print("El numero se repite dentro de la memoria: ", r)  
        r2 = random.randint(0, 9) #Se crea un nuevo aleatorio
        print("Nuevo numero: ",r2)
        while r2 in memoria: #Se mira que este nuevo aleatorio no este repetido otra vez
            # print("Vuelve a estar dentro de la memoria: ",r2)
            r2 = random.randint(0, 9) # Si se repite otra vez, se genera un nuevo aleatorio   
            
        # print("numero resultante: ",r2)    
        r = r2 #Se reemplaza el antiguo por el nuevo
        if len(memoria) < capacidad_memoria: # Se mira que la capacidad de la memoria no este llena
            memoria.append(r) # Se agrega el numero 
        else: #Si esta llena la memoria  
            memoria.pop(0) #borra el primer numero 
            memoria.append(r)# y agrega el nuevo    
    else: # Si esta llena la memoria 
        memoria.pop(0) #Se borra el primer numero
        memoria.append(r) #y se agrega el nuevo    
    
    print("random: ",r)
    print(memoria,"Iteracion: ", rep_vecindades)

    #Hacemos la sumatoria de la vecindad actual
    costoSum = 0
    volumSum = 0
    i = 0
    while volumSum < restriccion and i < len(vecindades[0]):
        #miramos los valores de la vecindad
        if vecindades[r][i] == 1:
            #Hacemos la suma    
            costoSum  += matriz[0][i] 
            volumSum += matriz[1][i]
            resultado = "Costo: " + str(costoSum) +" Volumen: " +str(volumSum)
                # print(costoSum)
            
        i += 1 
    print("Costo",costoSum)
    print("Volumen",volumSum)

#Mejoramos la solucion   
    valores_seleccionados = [0 for i in range(len(matriz[0]))]
    #llenamos valores_seleccionados con los valores que tiene el vecindario actual
    for i in range(len(vecindades[0])):
        valores_seleccionados[i] = vecindades[r][i]

    valores_resultado = [0 for i in range(len(matriz[0]))]  
    rep_mejora = 0
    #Igualamos los valores obtenidos de la suma a los valores que se usan en la mejora
    vol = volumSum 
    cos = costoSum 
    v = vol
    # si los valores actuales son mejores que los mejores entonces se guardan
    if cos > mejor_cos and vol >= mejor_vol and vol<= restriccion:
                    print("Costo maximo: ",cos)
                    print("Volumen maximo: ",vol)
                    mejor_cos = cos
                    mejor_vol = vol
                    for i in range(len(valores_resultado)):
                        mejor_resultado[i] = valores_seleccionados[i]
    if v > restriccion:
        v = 0
    # se realiza la mejora 
    while rep_mejora < 500:
        
        r_mejora = random.randint(0, len(matriz[0])-1)
    
        print("Rand:", r_mejora)
        print("costo: ", matriz[0][r_mejora])
        print("vol: ", matriz[1][r_mejora])

        if valores_seleccionados[r_mejora] == 0:
        
            if vol <= restriccion:    
                vol = vol + matriz[1][r_mejora]
                cos = cos + matriz[0][r_mejora]
                valores_seleccionados[r_mejora] = 1
                print(valores_seleccionados)
                print("Sumando-Costo-volumen: ",cos, vol)    
        else:
            if vol >= restriccion:
                cos = cos - matriz[0][r_mejora]
                vol = vol - matriz[1][r_mejora]
                valores_seleccionados[r_mejora] = 0
                print(valores_seleccionados)
                print("Restando-Costo-volumen: ",cos, vol) 

        if vol > v and vol <= restriccion:
            print("entra en mejores valores")
            resultado = "Costo: " + str(cos) +" Volumen: " +str(vol)  #Guardamos los valores
            for i in range(len(valores_resultado)):
                valores_resultado[i] = valores_seleccionados[i]
            v = vol
            print("mejoro:", vol)    
        if cos > mejor_cos and vol >= mejor_vol and vol<= restriccion: # Si la mejora resulta en un mejor valor entonces se guarda la solucion
                    print("Costo maximo: ",cos)
                    print("Volumen maximo: ",vol)
                    mejor_cos = cos
                    mejor_vol = vol
                    for i in range(len(valores_resultado)):
                        mejor_resultado[i] = valores_seleccionados[i]
            
            

        rep_mejora = rep_mejora + 1 #Aumentamos el contador de iteraciones de mejora


    rep_vecindades = rep_vecindades + 1 #Aumentamos el contador de Aspiracion    
print(mejor_cos, mejor_vol)


    #MEJORADO DE VALORES POR COMPARACION DE SOLUCIONES EN LA LISTA TABU-----------------------


#Realizamos la suma
# for x in range(len(vecindades)):

    #MEJORADO DE VALORES POR MEJORADO DE SOULUCIONES Y COMPARACION DE VALORES------------------
        # if vol <= restriccion:
            
        #     if valores_seleccionados[r] == 0 :    
        #         vol = vol + matriz[1][r]
        #         cos = cos + matriz[0][r]
        #         valores_seleccionados[r] = 1
        #         print(valores_seleccionados)
        #         print("Sumando: ", vol)    
        # else:
        #     if valores_seleccionados[r] == 1:
        #         cos = cos - matriz[0][r]
        #         vol = vol - matriz[1][r]
        #         valores_seleccionados[r] = 0
        #         print(valores_seleccionados)
        #         print("restando:", vol)

        # if vol > v and vol <= restriccion:
        #     resultado = "Costo: " + str(cos) +" Volumen: " +str(vol)  #Guardamos los valores
        #     for i in range(len(valores_resultado)):
        #         valores_resultado[i] = valores_seleccionados[i]
            
        #     v = vol
        #     print("mejoro:", vol)
        
    