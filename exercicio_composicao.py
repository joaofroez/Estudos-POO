class Fabricante():

    def __init__(self, montadora):
        self.montadora = montadora
        self.modelos = []
    def criar_carro(self, *modelo):
        self.modelos.append(Carro(modelo))
    
class Carro():
    def __init__(self, nome):
        self.nome = nome

def listar_especificacao(modelos, montadora):
    
    print(f'O {modelos} são fabricados pela {montadora}.') 


fiat_carros = Fabricante('Fiat')
fiat_carros.criar_carro('Palio G1', 'Uno G1', 'Siena', 'Palio G2')


toyota_carros = Fabricante('Toyota')
toyota_carros.criar_carro('Etios', 'Corolla', 'Hilux')

listar_especificacao(fiat_carros.modelos[0].nome, fiat_carros.montadora)

