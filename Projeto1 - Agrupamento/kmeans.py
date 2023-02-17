import numpy as np
def kmeans(base_de_dados, qtd_classes):
    protipos = np.random.rand(qtd_classes, len(base_de_dados[0]))
    matriz_pertinecia = np.zeros((len(base_de_dados), qtd_classes), dtype=int)
    print(matriz_pertinecia)