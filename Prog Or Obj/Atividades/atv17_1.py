class Conta: 
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
    def get_saldo(self):
        return self.saldo

class Conta_corrente(Conta):
    def __init__(self, nome, saldo, cheque_especial=0):
        super().__init__(nome, saldo)
        self.cheque_especial = cheque_especial

    def saldo_total(self):
        return self.saldo + self.cheque_especial
    
class Conta_poupanca(Conta):
    def __init__(self, nome, saldo, porcentagem_rendimento=0.05):
        super().__init__(nome, saldo)
        self.porcentagem_rendimento = porcentagem_rendimento
    def saldo_atualizado(self):
        rendimento = self.saldo * self.porcentagem_rendimento
        return self.saldo + rendimento
