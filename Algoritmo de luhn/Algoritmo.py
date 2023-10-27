#Gerardo Alejandro Duarte - 192055
#Ibeth Dariana Ortega - 191988

import random
numeroAleatorio = []

for i in range (0,16): 
    numeroAleatorio.append(random.randint(0,9))




sumaTotal = 0
print(numeroAleatorio)

for i in range(0,16,2):
    numeroAleatorio[i] = numeroAleatorio[i]*2
    if numeroAleatorio[i] >= 10:
        sumaDigitos = 0
        while numeroAleatorio[i] > 0:
            sumaDigitos = sumaDigitos + numeroAleatorio[i]%10
            numeroAleatorio[i] = numeroAleatorio[i] // 10
        numeroAleatorio[i] = sumaDigitos    


print("Numero procesado:")
print(numeroAleatorio)        

for digito in numeroAleatorio:
    digito = digito
    sumaTotal = sumaTotal + digito
print("Resultado de la suma:")
print(sumaTotal)    

if sumaTotal % 10 == 0:
    print("Numero de tarjeta valido")
else:
    print("Numero de tarjeta invalido")    



