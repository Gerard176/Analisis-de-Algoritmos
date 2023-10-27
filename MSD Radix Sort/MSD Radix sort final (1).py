import pandas as pd
import time
# leyendo los vectores del excel
sortArray = []
data = pd.read_excel("Vector 1er examen 8 VECTORES.xlsx", sheet_name='Hoja1', index_col=None, header=None)
vector_row = data[data.apply(lambda row: row.astype(str).str.contains('Vector 8').any(), axis=1)].index[0]
data_subset = data.loc[vector_row, 2:]
data_subset = data_subset.values.astype('int64')
array = data_subset.tolist() 
print(array)

inicio = time.time()
# inicio
max_length = len(str(max(array))) #Declaramos la cantidad de decimales del numero mayor del array
print(max_length)

# Agregamos ceros a la izquierda de cada numero para igualar la cantidad de digitos con el digito mayor
auxiliar = [[] for _ in range(100)]
for i in range(len(array)):
    array[i] = str(array[i]).zfill(max_length)
    auxiliar[i] = array[i] # guardamos el array en un array auxiliar
# print(array)
     
auxiliar = [[valor] for valor in auxiliar] #convertimos el auxiliar en una lista de listas
otro_mas = [] 
print(auxiliar)
c = 0


for digit_pos in range(max_length): # for para recorrer cada cada digito en cada numero

    # declaramos los arrays auxiliares que nos ayudaran a realizar el counting sort
    buckets = [[] for _ in range(10)] 
    auxiliar_buckets = [[] for _ in range(10)]
    
    print(digit_pos)
    
    for subarray in auxiliar: #for para recorrer cada sublista en auxiliar

    # para el primer momento,
    # cada lista va a contener solo un numero,
    # puesto que el counting sort se realiza con todos 
    # los numeros del array

        if digit_pos != 0: # por lo tanto para que el valor de buckets no se reinicie en la primera iteracion ponemos esta condicion   
            buckets = [[] for _ in range(10)]
        
        for indice, num in enumerate(subarray): # for para recorrer cada elemento de cada sublista dandoles a cada uno un indice y un valor(num)

            # para este momento descubrimos que el array auxiliar 
            # tiene muchos espacios en blanco y solo necesitamos 
            # los subarrays con numeros

            if  num != []:
                c += 1   
                print(subarray)
                print("ultimo numero",subarray[-1])
                print(num)
                digit = int(num[digit_pos]) # tomamos el valor del digito en el numero
                # print(digit) 
                buckets[digit].append(num) # lo colocamos dentro de buckets en su respectiva posicion haciendo asi el counting sort 
                
                print("auxiliar buckets")
                print(auxiliar_buckets)

                print("buckets")
                print(buckets)

                if indice == len(subarray)-1: # declaramos que si el valor del indice actual de la lista es igual al ultimo indice de esa sublista, entra

                    # si estamos en el primer digito entonces no realizamos este proceso
                    if digit_pos != 0: 
                        otro_mas = auxiliar_buckets+buckets # guardamos el array auxiliar de buckets mas el buckets en un nuevo array 
                        auxiliar_buckets = otro_mas # actualizamos el valor de auxiliar buckets con la informacion anterior  
                    else: # Realizamos este proceso si estamos en el primer digito     
                        auxiliar_buckets = buckets # guardamos los valores de buckets en auxiliar buckets
                        
                    
                  
                
                
                # print("otro mas")
                # print(otro_mas)
    print("otro mas fuera: ", otro_mas)            
    print("hola")
    print(auxiliar)
    print("se termina") 

    auxiliar = [[] for _ in range(1500)] # reiniciamos el valor de auxiliar 
    for i in range(len(auxiliar_buckets)): # volcamos toda la informacion de auxiliar buckets en auxiliar
        auxiliar[i] = auxiliar_buckets[i]  

    print("hola")
    print(auxiliar)
     



# Combinar todos los elementos en una sola lista
lista_resultante = []

for sublista in auxiliar:
    for elemento in sublista:
        if elemento.strip('0'):  # identificar si el elemento es diferente de vacio al aplicar strip('0')
            lista_resultante.append(elemento.lstrip('0')) # agrega el elemento despues de haberle quitado los ceros a la izquierda

# Imprimir la lista resultante
print(lista_resultante)

fin = time.time()

tiempo_transcurrido = fin - inicio
print("tiempo de ejecucion:",tiempo_transcurrido*1000, "ms")
print(c)
        