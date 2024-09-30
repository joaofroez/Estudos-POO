class Carro():
    def  __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, nome):
        self._motor = nome
    
    @property
    def fabricante(self):
        return self._fabricante
    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante = nome
    
    def exibir_dados_carro(self):
        print(f'O {self.nome} é fabricado pela {self.fabricante.nome} e usa o motor {self.motor.nome}')

class Motor():
    def  __init__(self, nome):
        self.nome = nome

class Fabricante():
    def  __init__(self, nome):
        self.nome = nome

palio_g1 = Carro('Palio G1')
fiasa_1_0 = Motor('Fiasa 1.0')
fiat = Fabricante('Fiat')
palio_g1.motor = fiasa_1_0
palio_g1.fabricante = fiat
palio_g1.exibir_dados_carro()

palio_g2 = Carro('Palio G2')
fire_1_0 = Motor('Fire 1.0')
palio_g2.motor = fire_1_0
palio_g2.fabricante = fiat
palio_g2.exibir_dados_carro()

