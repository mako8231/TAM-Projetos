import numpy as np
import plotly.express as px 
from scipy import stats

def kNN(k:int, obj_entrada, objetos, rotulos):
    vetor_dist = []
    for obj in objetos:
        vetor_dist.append(distancia_euclidiana(obj_entrada, obj))
    #ordena o vetor 
    sort_v = np.sort(vetor_dist)
    #e mostra os indices originais 
    sort_i = np.argsort(vetor_dist)


    #obter o vetor de rotulos:
    r = np.zeros(k)
    for i in range(k):
        r[i] = rotulos[sort_i[i]]
    
    moda = stats.mode(r)
    #print(moda.mode)
    return moda  
    pass

def distancia_euclidiana(obj_1, obj_2):
    dist = np.sqrt(np.sum(np.float_power(np.subtract(obj_1, obj_2), 2)))
    return dist
    pass

def normalizar_base_dados(dataset):
    #fazer até ir na coluna n 
    matriz_normalizada = dataset
    for i in range(len(dataset[0])):
        coluna = dataset[:,i]
        min = np.min(coluna)
        max = np.max(coluna)
        matriz_normalizada[:,i] = np.divide(coluna-min, max-min)
    return matriz_normalizada
    pass

def contar_classes(rotulos):
    #ordenar os rotulos
    rotulos_ordenados = np.sort(rotulos)
    ultima_classe = 0xfff 
    classe_atual = 0xfff
    classes = 0
    for i in range(len(rotulos_ordenados)):
        classe_atual = rotulos_ordenados[i]
        if classe_atual != ultima_classe:
            ultima_classe = classe_atual
            classes+=1
    
    return classes

def organizar_classes(rotulos):
    qtd_classes = contar_classes(rotulos)
    mat_classes = [0]*qtd_classes
    for i in range(qtd_classes):
        mat_classes[i] = []
    for i in range(len(rotulos)):
        mat_classes[int(rotulos[i])].append(i)

    return mat_classes

#separar 10% dos objetos, 5% de cada classe
def separar_classes(dataset, indices_classes):
    #obter a quantidade de 5% de cada classe
    classes_tam = []
    for i in range(len(indices_classes)):
        classes_tam.append(int(len(indices_classes[i]) * 0.05))
    
    amostras = [[]]*len(classes_tam)
    for i in range(len(classes_tam)):
        amostras[i] = []
        for j in range(classes_tam[i]):
            amostras[i].append(indices_classes[i][j])

    return amostras

def testar_amostras(k, amostras, dataset, rotulos):
    #print("aaaa",amostras)
    resultados = [[]]*len(amostras)
    for i in range(len(amostras)):
        resultados[i] = []
        for j in range(len(amostras[i])):
            indice_obj = amostras[i][j]
            #print("classe", i, amostras[i][j])
            res = kNN(k, dataset[indice_obj], dataset, rotulos)
            resultados[i].append(int(res.mode[0]))
            
    return resultados

def matriz_confusao(resultados):
    dimensao = len(resultados)
    matriz = np.zeros((dimensao,dimensao))
    for i in range(len(resultados)):
        for j in range(len(resultados[i])):
            matriz[i][resultados[i][j]] += 1
    return matriz
    pass

#so funciona com modelos de classes binarias
def TPR(matriz_contingencia):
    return (matriz_contingencia[0][0]/(matriz_contingencia[0][0] + matriz_contingencia[0][1]))
    pass

def FPR(matriz_contingencia):
    return (matriz_contingencia[1][0]/(matriz_contingencia[1][0] + matriz_contingencia[1][1]))
    pass

def ACC(matriz_contingencia):
    return (matriz_contingencia[0][0] + matriz_contingencia[1][1])/(matriz_contingencia[0][0] + matriz_contingencia[1][0] + matriz_contingencia[1][1] + matriz_contingencia[0][1])
    pass

def plot_roc(matrizes):
    tpr = []
    fpr = []

    for i in range(len(matrizes)):
        tpr.append(TPR(matrizes[i]))
        fpr.append(FPR(matrizes[i]))

    print(tpr, fpr)

    fig = px.area(
        x=fpr, y=tpr,
        title="Curva ROC",
        labels=dict(x='Falso positivo', y='Verdadeiro positivo'),
        width=700, height=800,
    )

    fig.add_shape(
        type="line", line=dict(dash='dash'),
        x0=0, x1=1, y0=0, y1=1
    )

    fig.update_yaxes(scaleanchor="x", scaleratio=1)
    fig.update_xaxes(constrain='domain')
    fig.show()