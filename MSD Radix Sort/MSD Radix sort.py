import pandas as pd
import sympy
# array = [10, 25, 8, 42, 17, 33, 5, 19, 14, 36, 7, 29, 12, 21, 3, 1, 50, 38, 23, 9, 11, 48, 27, 6, 16, 31, 4, 22, 35, 2, 45, 15, 13, 30, 20, 28, 18, 44, 26, 37, 24, 34, 40, 32, 46, 49, 43, 41, 47, 39]
# array = [10, 25, 8, 42, 17, 33, 5, 19, 14, 36, 7, 29, 12, 21, 3, 1, 50, 38, 23, 9, 11, 48, 27, 6, 16, 31, 4, 22, 35, 2, 45, 15, 13, 30, 20, 28, 18, 44, 26, 37, 24, 34, 40, 32, 46, 49, 43, 41, 47, 39, 61, 75, 58, 82, 67, 93, 55, 79, 64, 86, 73, 89, 52, 68, 53, 91, 76, 88, 74, 94, 57, 69, 62, 96, 51, 71, 63, 90, 56, 78, 54, 92, 72, 87, 66, 95, 60, 70, 59, 84, 65, 81, 80, 85, 83, 77]
array = [170, 45, 755, 700, 802, 2433, 2, 66]

# leyendo los vectores del excel
# ruta_archivo = 'vectores.xlsx'
# datos = pd.read_excel(ruta_archivo)
# vector1 = datos.iloc[3]
# vector1 = vector1[2:]
# array = vector1.astype(int).to_list()        
# print(array)

# for i in range(len(array)):
#     array[i] = sympy.Integer(array[i])





max_length = len(str(max(array)))


# print(max_length)

for i in range(len(array)):
    array[i] = str(array[i]).zfill(max_length)

print(array)

auxiliar = [[] for _ in range(100)]
for i in range(len(array)):
     auxiliar[i] = array[i]

auxiliar = [[valor] for valor in auxiliar]
otro_mas = []
# print(auxiliar)

for digit_pos in range(max_length):

    buckets = [[] for _ in range(10)]
    auxiliar_buckets = [[] for _ in range(10)]
    
    print(digit_pos)
    
    for subarray in auxiliar:
        
        if digit_pos != 0:
            # otro_mas = buckets+auxiliar_buckets
            # print(otro_mas)
            buckets = [[] for _ in range(10)]
        
        for num in subarray:
            
            if  num != []:
                
                
                print("ultimo numero",subarray[-1])
                print(num)
                digit = int(num[digit_pos])
                # print(digit) 
                buckets[digit].append(num)
                
                # print("auxiliar buckets")
                # print(auxiliar_buckets)

                print("buckets")
                print(buckets)

                if num == subarray[-1] :
                    if digit_pos != 0:    
                        otro_mas = auxiliar_buckets+buckets
                        auxiliar_buckets = otro_mas
                    else:     
                        for i in range(len(buckets)):
                            auxiliar_buckets[i] = buckets[i]
                    
                  
                
                
                print("otro mas")
                print(otro_mas)

                

                

    # print("otro mas fuera: ", otro_mas)            
    # print("hola")
    # print(auxiliar)
    # print("se termina") 

    auxiliar = [[] for _ in range(500)]
    for i in range(len(auxiliar_buckets)):
        auxiliar[i] = auxiliar_buckets[i]  

    # print("hola")
    # print(auxiliar)
    # print("se termina") 

lista_resultante = []

# Combinar todos los elementos en una sola lista
lista_resultante = []

for sublista in auxiliar:
    for elemento in sublista:
        if elemento.strip('0'):  # Eliminar ceros a la izquierda y verificar si el elemento no es vacío
            lista_resultante.append(elemento.lstrip('0'))

# Imprimir la lista resultante
print(lista_resultante)
        
    
     



    # array = buckets
# for bucket in buckets:
#     array.extend(bucket)





