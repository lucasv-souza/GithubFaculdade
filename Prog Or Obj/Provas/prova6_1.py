class Veiculo:
    def __init__(self, marca, preco_base):
        self._marca = marca
        self._preco_base = preco_base

    def get_marca(self):
        return self._marca

    def get_preco_base(self):
        return self._preco_base

    def set_marca(self, nova_marca):
        self._marca = nova_marca

    def set_preco_base(self, novo_preco):
        if novo_preco > 0:
            self._preco_base = novo_preco
        else:
            print("Erro: O preço base deve ser um valor positivo.")

    def aplicar_desconto(self, percentual):
        if 0 < percentual < 50:
            desconto = self._preco_base * (percentual / 100)
            novo_preco_calc = self._preco_base - desconto
            self.set_preco_base(novo_preco_calc)
            print(f"Desconto de {percentual}% aplicado. Novo preço: R$ {self._preco_base:.2f}")
        else:
            print("Erro: Percentual de desconto deve ser entre 1 e 49.")

    def calcular_preco_com_imposto(self, imposto_percentual):
        if imposto_percentual >= 0:
            preco_final = self._preco_base * (1 + imposto_percentual / 100)
            return preco_final
        else:
            print("Erro: Imposto não pode ser negativo.")
            return self._preco_base


class Carro(Veiculo):
    def __init__(self, marca, preco_base, numero_portas=4):
        super().__init__(marca, preco_base)
        self._numero_portas = numero_portas

    def get_numero_portas(self):
        return self._numero_portas

    def set_numero_portas(self, novo_num_portas):
        if novo_num_portas in [2, 4]:
            self._numero_portas = novo_num_portas
        else:
            print(f"Erro: Número de portas ({novo_num_portas}) inválido. Aceito apenas 2 ou 4.")


class Moto(Veiculo):
    def __init__(self, marca, preco_base, cilindradas=500):
        super().__init__(marca, preco_base)
        self._cilindradas = cilindradas

    def get_cilindradas(self):
        return self._cilindradas

    def set_cilindradas(self, novas_cc):
        if novas_cc >= 50:
            self._cilindradas = novas_cc
        else:
            print(f"Erro: Cilindradas ({novas_cc}cc) inválidas. Deve ser >= 50cc.")