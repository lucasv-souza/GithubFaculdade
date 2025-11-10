from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    
    def __init__(self, titular, agencia, numero, saldo=0.0):
        self._titular = titular
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

    def get_titular(self):
        return self._titular
    
    def get_agencia(self):
        return self._agencia
    
    def get_numero(self):
        return self._numero
    
    def get_saldo(self):
        return self._saldo

    def set_titular(self, novo_titular):
        if len(novo_titular) > 2:
            self._titular = novo_titular
        else:
            print("Erro: Nome do titular deve ter mais de 2 caracteres.")
    
    def set_agencia(self, nova_agencia):
        self._agencia = nova_agencia
    
    def set_numero(self, novo_numero):
        self._numero = novo_numero

    @abstractmethod
    def calcular_taxa_mensal(self):
        pass

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self._saldo:.2f}")
        else:
            print("Erro: Valor de depósito deve ser positivo.")
    
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self._saldo:.2f}")
            return True
        else:
            print("Erro: Saldo insuficiente ou valor de saque inválido.")
            return False


class ContaCorrente(ContaBancaria):
    
    def __init__(self, titular, agencia, numero, saldo=0.0, limite_cheque_especial=500.0):
        super().__init__(titular, agencia, numero, saldo)
        self._limite_cheque_especial = limite_cheque_especial

    def get_limite_cheque_especial(self):
        return self._limite_cheque_especial

    def set_limite_cheque_especial(self, novo_limite):
        if novo_limite >= 0:
            self._limite_cheque_especial = novo_limite
        else:
            print("Erro: O limite do cheque especial não pode ser negativo.")

    def calcular_taxa_mensal(self):
        taxa = 25.0
        print(f"Cobrando taxa de manutenção de R$ {taxa:.2f} da conta {self.get_numero()}.")
        self._saldo -= taxa

    def consultar_limite_total(self):
        limite_total = self._saldo + self._limite_cheque_especial
        return limite_total


class ContaPoupanca(ContaBancaria):

    def __init__(self, titular, agencia, numero, saldo=0.0, taxa_rendimento=0.005):
        super().__init__(titular, agencia, numero, saldo)
        self._taxa_rendimento = taxa_rendimento
    
    def get_taxa_rendimento(self):
        return self._taxa_rendimento

    def set_taxa_rendimento(self, nova_taxa):
        if 0 < nova_taxa < 1:
            self._taxa_rendimento = nova_taxa
        else:
            print("Erro: Taxa de rendimento deve ser um valor decimal, ex: 0.005")

    def calcular_taxa_mensal(self):
        print(f"Conta poupança {self.get_numero()} não possui taxa de manutenção.")

    def aplicar_rendimento(self):
        rendimento = self.get_saldo() * self._taxa_rendimento
        self.depositar(rendimento)
        print(f"Rendimento de R$ {rendimento:.2f} aplicado.")