# __dict__ e vars para atributos de instância
import json
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade, ano):
        self.nome = nome
        self.idade = idade
    def __init__(self, nome, idade, ano):
        self.nome = nome
        self.idade = idade
        self.ano = ano
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    def salvar(self, dicionario):
        with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
            json.dump(dicionario, arquivo, indent=2, ensure_ascii=False)
            return print(f'Sua Class foi salva com sucesso.')
    
    


caminho_arquivo = 'dict_class.json'
p1 = Pessoa('João', 20, None)
p1.get_ano_nascimento()

dados1 = Pessoa(p1.nome, p1.idade, p1.get_ano_nascimento())
dados1.salvar(dados1.__dict__)


# versao prof
# import json

# CAMINHO_ARQUIVO = 'aula127.json'


# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade


# p1 = Pessoa('João', 33)
# p2 = Pessoa('Helena', 21)
# p3 = Pessoa('Joana', 11)
# bd = [vars(p1), p2.__dict__, vars(p3)]


# def fazer_dump():
#     with open(CAMINHO_ARQUIVO, 'w') as arquivo:
#         print('FAZENDO DUMP')
#         json.dump(bd, arquivo, ensure_ascii=False, indent=2)


# if __name__ == '__main__':
#     print('ELE É O __main__')
#     fazer_dump()