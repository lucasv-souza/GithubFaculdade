class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_salario(self, novo_salario):          
        self.salario += novo_salario

    def bonificacao(self):
        bonus = self.salario * 0.10
        self.salario += bonus
        return bonus

class Gerente(Funcionario):
    def __init__(self, nome, salario, qtd_gerencia):
        self.nome = nome
        self.salario = salario

        super().__init__(nome, salario)
        self.qtd_gerencia = qtd_gerencia

    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_salario(self):
        return self.salario

    def set_salario(self, novo_salario):
        self.salario = novo_salario

    def get_qtd_gerencia(self):
        return self.qtd_gerencia

    def set_qtd_gerencia(self, nova_qtd):
        self.qtd_gerencia = nova_qtd