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