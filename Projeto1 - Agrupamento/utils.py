import numpy as np 
import plotly.express as px 

def normalizar(conjunto):
    min = np.min(conjunto)
    max = np.max(conjunto)
    conjunto_normalizado = []
    for valor in conjunto:
        print(valor)
        conjunto_normalizado.append((valor - min)/(max - min))
    return conjunto_normalizado    
    
def para_dict(matriz, rotulo):
    array_dict = []
    for i in range(len(matriz)):
        array_dict.append({"x":matriz[i][0], "y": matriz[i][1], "rotulo": rotulo})
    return array_dict

def adicionar_dados(matriz, rotulo, array_dict):
    for i in range(len(matriz)):
        array_dict.append({"x":matriz[i][0], "y": matriz[i][1], "rotulo": rotulo})

    pass

def plotar(base_de_dados, axis_x:str, axis_y:str):
    fig = px.scatter(base_de_dados, x="x", y="y", color="rotulo", symbol="rotulo")
    fig.show()