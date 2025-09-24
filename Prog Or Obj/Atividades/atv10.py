class Empregado:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_salario(self):
        return self.salario
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def aumento_salarial(self, valor_aumento):          
        self.salario += valor_aumento

if __name__ == '__main__':
    emp1 = Empregado('Lucas', 5000.00)
    emp2 = Empregado('Ana', 7000.00)
    print(f"Salário inicial: R$ {emp1.get_salario():.2f}")
    emp1.set_nome('Lucas Vinícius')
    print(f"Nome atualizado: {emp1.nome}")
    emp1.aumento_salarial(700.00)
    print(f"Salário atualizado: R$ {emp1.get_salario():.2f}")
    print("\n")
    print(f"Salário inicial: R$ {emp2.get_salario():.2f}")
    emp2.set_nome('Ana Clara')
    print(f"Nome atualizado: {emp2.nome}")
    emp2.aumento_salarial(500.00)
    print(f"Salário atualizado: R$ {emp2.get_salario():.2f}")