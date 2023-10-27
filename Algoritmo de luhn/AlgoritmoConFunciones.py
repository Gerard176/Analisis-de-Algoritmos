import random
numeroAleatorio = ""

for i in range (0,16): 
    numeroAleatorio = numeroAleatorio + str(random.randint(0,9))


array = list(numeroAleatorio)

sumaTotal = 0
print("Numero Ingresado:" + numeroAleatorio)
print(array)

for i in range(0,16,2):
    array[i] = str(int(array[i])*2)
    if int(array[i]) >= 10:
        mayoraNueve = list(array[i])
        sumaDigitos = 0
        for digito in mayoraNueve:
            digito = int(digito)
            sumaDigitos = sumaDigitos + digito
        array[i] = str(sumaDigitos)    
print("Numero procesado:")
print(array)        
for digito in array:
    digito = int(digito)
    sumaTotal = sumaTotal + digito
print("Resultado de la suma:")
print(sumaTotal)    

if sumaTotal % 10 == 0:
    print("Numero de tarjeta valido")
else:
    print("Numero de tarjeta invalido")    



