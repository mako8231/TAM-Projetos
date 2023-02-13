import numpy as np 

def criarDadosRuspini(ruspini_pos, ruspini_rot):
    #ler as posições primeiro 
    dados_finais = []
    arquivo1 = open(ruspini_pos, 'r')
    arquivo2 = open(ruspini_rot, 'r')
    linhas = arquivo1.readlines()
    rotulos = arquivo2.readlines()

    #criando o dataset
    for linha in linhas:
        dado = linha.split()
        dado_dict = {"x": int(dado[0]), "y": int(dado[1])}
        dados_finais.append(dado_dict)
    pass

    
    for i in range(dados_finais.__len__()):
        dados_finais[i]["rotulo"] = int(rotulos[i].split()[0])
    
    arquivo1.close()
    arquivo2.close()

    return dados_finais

def normalizacaoLinear(conjunto):
    
    max = np.max(conjunto)
    min = np.min(conjunto)
    dados_normalizados = []
    for dado in conjunto:
        normal = (dado - min)/(max - min) 
        dados_normalizados.append(normal)
    return dados_normalizados

def normalizarDados(dados):
    x = []
    y = []
    rotulos = []

    dados_normalizados = []

    for dado in dados:
        x.append(dado["x"])
        y.append(dado["y"])
        rotulos.append(dado["rotulo"])
    

    x_normal = normalizacaoLinear(x)
    y_normal = normalizacaoLinear(y)

    for i in range(rotulos.__len__()):
        dados_normalizados.append({"x":x_normal[i], "y":y_normal[i], "rotulo":str(rotulos[i])})
    
    return dados_normalizados
