class Veiculo:
    def __init__(self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def get_modelo(self):
        return self.modelo
    
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
        
    def get_ano(self):
        return self.ano
        
    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def get_valor(self):
        return self.valor
    
    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def aumenta_valor(self, valor_aumento):
        self.valor = self.valor + valor_aumento

if __name__ == '__main__':

    carro1 = Veiculo('HB', 2022, 80000.00)
    print("Endereço hexadecimal do carro 1: ", carro1)
    print("Dados do carro1:\nModelo:", carro1.get_modelo())
    print("Ano:", carro1.get_ano())
    print(f"Valor: R$", carro1.get_valor())

    carro1.set_modelo('HB20')
    print("Modelo atualizado:", carro1.get_modelo())

    novo_valor = float(input("Novo valor: "))
    carro1.set_valor(novo_valor)
    print("Valor atualizado:", carro1.get_valor())

    print("\n")

    carro2 = Veiculo('Corolla', 2024, 190000.00)
    print("Endereço hexadecimal do carro 2: ", carro2)
    print("Dados do carro2:\nModelo:", carro2.get_modelo())
    print("Ano:", carro2.get_ano())
    print(f"Valor: R$", carro2.get_valor())

    novo_valor = float(input("Novo valor: "))
    carro2.set_valor(novo_valor)
    print("Valor atualizado", carro2.get_valor())