import numpy as np 
import json 

sexo = []
idade = []
salario = []
cargo = []
num_filhos = []
estado_civil = []

media_sexo = 0
media_idade = 0
media_salario = 0
media_cargo = 0
media_num_filhos = 0
media_estado_civil = 0

dp_sexo = 0
dp_idade = 0
dp_salario = 0
dp_cargo = 0
dp_num_filhos = 0
dp_estado_civil = 0



def carregarDados():
    file = open("db.json", "r")
    r = file.read()
    data = json.loads(r)
    return data 

def normalizar(valor, media_valor, desvio_padrao):
    return np.abs((valor - media_valor)/desvio_padrao)

data = carregarDados()
print(data["funcionarios"])

#extrair as informações nos vetores
for f in data["funcionarios"]:
    sexo.append(f["sexo"])
    idade.append(f["idade"])
    salario.append(f["salario"])
    cargo.append(f["cargo"])
    num_filhos.append(f["num_filhos"])
    estado_civil.append(f["estado_civil"])

media_sexo = np.average(sexo)
media_idade = np.average(idade)
media_salario = np.average(salario)
media_cargo = np.average(cargo)
media_num_filhos = np.average(num_filhos)
media_estado_civil = np.average(estado_civil)

dp_sexo = np.sqrt(np.var(sexo))
dp_idade = np.sqrt(np.var(idade))
dp_salario = np.sqrt(np.var(salario))
dp_cargo = np.sqrt(np.var(cargo))
dp_num_filhos = np.sqrt(np.var(num_filhos))
dp_estado_civil = np.sqrt(np.var(estado_civil))

print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} ".format("matricula", "sexo", "idade", "salario", "cargo", "num_filhos", "estado_civil"))
for f in data["funcionarios"]:
    sexo_normal = normalizar(f["sexo"], media_sexo, dp_sexo)
    idade_normal = normalizar(f["idade"], media_idade, dp_idade)
    salario_normal = normalizar(f["salario"], media_salario, dp_salario)
    cargo_normal = normalizar(f["cargo"], media_cargo, dp_cargo)
    num_filhos_normal = normalizar(f["num_filhos"], media_num_filhos, dp_num_filhos)
    estado_civil_normal = normalizar(f["estado_civil"], media_estado_civil, dp_estado_civil)

    print("{:<8} {:<8.3f} {:<8.3f} {:<8.3f} {:<8.3f} {:<8.3f} {:<8.3f} ".format(f["matricula"], sexo_normal, idade_normal, salario_normal, cargo_normal, num_filhos_normal, estado_civil_normal))