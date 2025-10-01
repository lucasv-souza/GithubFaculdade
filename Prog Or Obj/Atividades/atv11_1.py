class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_salario(self):
        return self.salario
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def aumento_salarial(self, valor_aumento):          
        self.salario += valor_aumento
