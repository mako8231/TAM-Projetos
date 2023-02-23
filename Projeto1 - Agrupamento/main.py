import carregar_dados as loader 
import utils as ut
import kmeans as k 
import plotly.express as px 
import pureza_matriz as pu
import numpy as np

#carregar a base de dados
dados = loader.carregar_base_dados("dataset/heart.txt")
#normalizando os dados 
dados_normais = ut.normalizar(dados)
#obtenção da matriz de pertinência e a matriz de prototipos 
#Traduzindo as matrizes para um dicionário em python
dados_traduzidos = ut.para_dict(dados_normais, "objeto")
prototipos, matriz_pertinencia = k.kmeans(dados_normais, dados_traduzidos, 4, 10)
ut.adicionar_dados(prototipos, "centroide", dados_traduzidos)
#plotar o gráfico 
#ut.plotar(dados_traduzidos, "sepal length", "sepal width")
#imprimir a pureza 
#matriz_pertinencia = np.array(matriz_pertinencia)
C = pu.matriz_contingencia(matriz_pertinencia, pu.rotulos)
p = pu.pureza(C)
print(C)
print(p)

#print(dados_normais)
#print(a,b)
#print(dados_normais)