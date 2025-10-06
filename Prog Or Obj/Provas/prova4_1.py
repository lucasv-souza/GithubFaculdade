class Funcionario:
    def __init__(self, nome, matricula, salario):
        self._nome = nome
        self._matricula = matricula
        self._salario = salario

    def get_nome(self):
        return self._nome

    def get_matricula(self):
        return self._matricula

    def get_salario(self):
        return self._salario

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def set_matricula(self, nova_matricula):
        self._matricula = nova_matricula

    def set_salario(self, novo_salario):
        if novo_salario > 0:
            self._salario = novo_salario
        else:
            print("Erro: O salário deve ser um valor positivo.")

    def calcular_aumento(self, percentual):
        if percentual > 0:
            aumento = self._salario * (percentual / 100)
            self.set_salario(self._salario + aumento)
            print(f"Aumento de {percentual}% aplicado ao salário de {self.get_nome()}.")
        else:
            print("Erro: O percentual de aumento deve ser positivo.")


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, setor, bonus_anual):
        super().__init__(nome, matricula, salario)
        self._setor = setor
        self._bonus_anual = bonus_anual

    def get_setor(self):
        return self._setor

    def get_bonus_anual(self):
        return self._bonus_anual

    def set_setor(self, novo_setor):
        self._setor = novo_setor

    def set_bonus_anual(self, novo_bonus):
        if novo_bonus >= 0:
            self._bonus_anual = novo_bonus
        else:
            print("Erro: O bônus não pode ser um valor negativo.")