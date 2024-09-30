import json
from class_json import Pessoa, caminho_arquivo

with open (caminho_arquivo, 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)
    
    p1 = Pessoa(**dados)

print(p1.nome)


# versao prof
# import json

# from aula127_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

# # fazer_dump()

# with open(CAMINHO_ARQUIVO, 'r') as arquivo:
#     pessoas = json.load(arquivo)
#     p1 = Pessoa(**pessoas[0])
#     p2 = Pessoa(**pessoas[1])
#     p3 = Pessoa(**pessoas[2])

#     print(p1.nome, p1.idade)
#     print(p2.nome, p2.idade)
#     print(p3.nome, p3.idade)
