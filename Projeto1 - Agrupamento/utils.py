import numpy as np 
def normalizar(conjunto):
    min = np.min(conjunto)
    max = np.max(conjunto)
    conjunto_normalizado = []
    for valor in conjunto:
        conjunto_normalizado.append((valor - min)/(max - min))
    return conjunto_normalizado    
    
