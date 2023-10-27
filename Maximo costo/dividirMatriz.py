import pandas as pd

arrayDesordenado  = {}
data = pd.read_excel(
    "matriz.xlsx", sheet_name="Hoja1", index_col=None, header=None
)
NUMERO_DIVISIONES = 2

matriz = data.to_numpy().tolist()
indice = 0
print(matriz[0],matriz[1])
longitud = len(matriz[0])
for i in range(NUMERO_DIVISIONES):
    n = longitud//NUMERO_DIVISIONES + indice
    aux  = []
    aux1  = []
    for k in range(indice, n):
        aux.append(matriz[0][k])
        aux1.append(matriz[1][k])
        print(indice, n)
    arrayDesordenado[f"data_{i+1}"] = [aux,aux1]
    
    longitud-=n
    NUMERO_DIVISIONES-=1
    indice = n

print(arrayDesordenado)