import numpy as np
from scipy import stats

def kNN(k:int, obj_entrada, objetos, rotulos):
    vetor_dist = []
    for obj in objetos:
        vetor_dist.append(distancia_euclidiana(obj_entrada, obj))
    #ordena o vetor 
    sort_v = np.sort(vetor_dist)
    #e mostra os indices originais 
    sort_i = np.argsort(vetor_dist)

    print(sort_v[1:k+1])
    print(sort_i[1:k+1])

    #obter o vetor de rotulos:
    r = np.zeros(k)
    print(r)
    for i in range(k):
        r[i] = rotulos[sort_i[i]]
    
    print(r)
    moda = stats.mode(r)
    print(moda.mode)

    pass

def distancia_euclidiana(obj_1, obj_2):
    dist = np.sqrt(np.sum(np.float_power(np.subtract(obj_1, obj_2), 2)))
    return dist
    pass