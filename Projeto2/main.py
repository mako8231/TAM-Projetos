import numpy as np 
import utils

data = np.loadtxt("dataset/base_de_dados_cleveland.txt")
rotulos = np.loadtxt("dataset/rotulos_cleveland")

def main():
    #resultados
    res = []
    #matrizes de confusão
    mat = []
    #metricas de classificacao
    classif = []
    #normalizando os dados
    normalizado = utils.normalizar_base_dados(data)
    #print(normalizado)
    
    mat_classes = utils.organizar_classes(rotulos)
    #print(mat_classes)
    
    amostras = utils.separar_classes(data, utils.organizar_classes(rotulos))
    res.append(utils.testar_amostras(1, amostras, data, rotulos))
    res.append(utils.testar_amostras(3, amostras, data, rotulos))
    res.append(utils.testar_amostras(5, amostras, data, rotulos))

    
    print(res)
    
    for i in range(len(res)):
        mat.append(utils.matriz_confusao(res[i]))
    
    for i in range(len(mat)):
        classif.append([utils.TPR(mat[i]), utils.FPR(mat[i]), utils.ACC(mat[i])])


    utils.plot_roc(mat)

    print(mat)
    print("Metricas de classificação: (tpr, fpr, acc)", classif)
    pass


main()