import plotly.express as px 
import numpy as np 
import utils 

dados = utils.criarDadosRuspini("ruspini.m", "rotulosRuspini.m")
dados_normais = utils.normalizarDados(dados)

fig = px.scatter(dados_normais, x="x", y="y", color="rotulo")
fig.show()