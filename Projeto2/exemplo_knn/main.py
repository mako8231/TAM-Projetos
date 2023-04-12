import numpy as np
import algoritmo as alg
import plotly.graph_objects as go


#carregar os objetos
objetos = np.loadtxt("database/sintetica.m")
rotulos = np.loadtxt("database/rotulos.m")
print(objetos)
print(rotulos)


fig = go.Figure()
fig.add_trace(go.Scatter(x=objetos[:,0], y=objetos[:,1], mode='markers', name='pontos'))
fig.show()

alg.kNN(3, objetos[38], objetos, rotulos)