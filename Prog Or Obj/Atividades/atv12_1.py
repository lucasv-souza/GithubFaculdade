class Veiculo:
    def __init__(self, valor, km):
        self.valor = valor
        self.km = km

    def get_valor(self):
        return self.valor
    def set_valor(self, novo_valor):
        self.valor = novo_valor
    def get_km(self):
        return self.km
    def set_km(self, novo_km):
        self.km = novo_km
    def atualiza_valor(self, vlr_aumento):
         self.valor = self.valor + vlr_aumento

class Carro(Veiculo):
    def __init__ (self, valor, km, qtd_portas=0):
        super().__init__(valor, km)
        self.qtd_portas = qtd_portas
    def get_qtd_portas(self):   
            return self.qtd_portas
    def set_qtd_portas(self, nova_qtd):
            self.qtd_portas = nova_qtd

class Moto(Veiculo):
    def __init__ (self, valor, km, cilindradas=0):
        super().__init__(valor, km)
        self.cilindradas = cilindradas
    def get_cilindradas(self):   
            return self.cilindradas
    def set_cilindradas(self, nova_qtd):
            self.cilindradas = nova_qtd