import numpy as np

# Carregar o arquivo de rótulos
rotulos = np.loadtxt('rotulos-ruspini.m')

# Calcular a matriz de contingência a partir da matriz de pertinências e dos rótulos
def matriz_contingencia(matriz_pertinencia, rotulos):
    qtd_classes = len(np.unique(rotulos))
    C = np.zeros((qtd_classes, qtd_classes), dtype=int)
    for i in range(len(rotulos)):
        classe_real = int(rotulos[i]) - 1  # os rótulos começam em 1, então subtraímos 1 para começar em 0
        classe_predita = np.argmax(matriz_pertinencia[i])
        C[classe_real][classe_predita] += 1
    return C

# Calcular a pureza a partir da matriz de contingência
def pureza(matriz_contingencia):
    total = np.sum(matriz_contingencia)
    maximos = np.amax(matriz_contingencia, axis=0)
    return np.sum(maximos) / total

# Exemplo de uso
matriz_pertinencia = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1], [1, 0, 0], [0, 1, 0]])
C = matriz_contingencia(matriz_pertinencia, rotulos)
p = pureza(C)
print(C)
print(p)
