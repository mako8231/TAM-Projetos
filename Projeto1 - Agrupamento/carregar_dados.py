import numpy as np 
def carregar_base_dados(arquivo):
    file = open(arquivo, 'r')
    linhas = file.readlines()
    nova_linhas = []
    for linha in linhas:
        vetor_linha_str = linha.split()
        linha_numero = [0]*len(vetor_linha_str)    
        for i in range(len(vetor_linha_str)):
            linha_numero[i] = int(vetor_linha_str[i])
        nova_linhas.append(linha_numero)
    
    file.close()
    return nova_linhas