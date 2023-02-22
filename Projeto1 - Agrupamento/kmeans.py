import numpy as np
def kmeans(base_de_dados, qtd_classes):
    protipos = np.random.rand(qtd_classes, len(base_de_dados[0]))
    matriz_pertinecia = np.zeros((len(base_de_dados), qtd_classes), dtype=int)
    #print(base_de_dados)
    #começar a primeira iteração para atualizar a matriz de pertinência
    for i in range(len(base_de_dados)):
        indice_grupo = 0
        menor_dist = 0xFFFF
        for j in range(len(protipos)):
            d = dist_euclidiana(protipos[j], base_de_dados[i])
            if d < menor_dist:
                menor_dist = d
                indice_grupo = j 
            
            #atualizar a matriz de pertinencia
        matriz_pertinecia[i][indice_grupo] = 1
            #print("j=", j, np.floor(d))
    
     # atualizar a posição dos protótipos
    for j in range(len(protipos)):
        objetos_grupo = []
        for i in range(len(base_de_dados)):
            if matriz_pertinecia[i][j] == 1:
                objetos_grupo.append(base_de_dados[i])
        protipos[j] = np.mean(objetos_grupo, axis=0)
    
    
    print(matriz_pertinecia)

def dist_euclidiana(prototipo, objeto):
    d = np.sqrt(np.sum(np.float_power(np.subtract(prototipo, objeto), 2)))
    return d 
    pass
