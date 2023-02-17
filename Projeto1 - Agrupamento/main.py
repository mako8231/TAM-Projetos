import carregar_dados as loader 
import utils as ut
import kmeans as k 

dados = loader.carregar_base_dados("ruspini.m")
dados_normais = ut.normalizar(dados)
k.kmeans(dados_normais, 4)
print(dados_normais)