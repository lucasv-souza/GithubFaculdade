class DispositivoEletronico:
    def __init__(self, marca, preco):
        self._marca = marca
        self._preco = preco

    def get_marca(self):
        return self._marca

    def get_preco(self):
        return self._preco

    def set_marca(self, nova_marca):
        self._marca = nova_marca

    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self._preco = novo_preco
        else:
            print("Erro: O preço deve ser um valor positivo.")

    def calcular_desconto(self, percentual):
        if 0 < percentual < 100:
            desconto = self._preco * (percentual / 100)
            self.set_preco(self._preco - desconto)
            print(f"Desconto de {percentual}% aplicado. Novo preço: R$ {self._preco:.2f}")
        else:
            print("Erro: O percentual de desconto deve ser entre 1 e 99.")


class Smartphone(DispositivoEletronico):
    def __init__(self, marca, preco, sistema_op="Android"):
        super().__init__(marca, preco)
        self._sistema_op = sistema_op

    def get_sistema_op(self):
        return self._sistema_op

    def set_sistema_op(self, novo_sistema):
        if novo_sistema in ["Android", "iOS"]:
            self._sistema_op = novo_sistema
        else:
            print("Erro: Sistema Operacional deve ser 'Android' ou 'iOS'.")


class Notebook(DispositivoEletronico):
    def __init__(self, marca, preco, ram_gb=8):
        super().__init__(marca, preco)
        self._ram_gb = ram_gb

    def get_ram_gb(self):
        return self._ram_gb

    def set_ram_gb(self, nova_ram):
        if nova_ram > 0 and nova_ram % 4 == 0:
            self._ram_gb = nova_ram
        else:
            print(f"Erro: {nova_ram}GB não é uma RAM válida (deve ser > 0 e múltiplo de 4).")