import numpy as np 
import utils

data = np.loadtxt("dataset/base_de_dados_cleveland.txt")
rotulos = np.loadtxt("dataset/rotulos_cleveland")

def main():
    #print(rotulos)
    #print(data)
    #normalizando os dados
    normalizado = utils.normalizar_base_dados(data)
    #print(normalizado)
    
    mat_classes = utils.organizar_classes(rotulos)
    #print(mat_classes)
    
    amostras = utils.separar_classes(data, utils.organizar_classes(rotulos))
    res = utils.testar_amostras(1, amostras, data, rotulos)
    print(res)
    mat = utils.matriz_confusao(res)
    print(mat)
    pass


main()