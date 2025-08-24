# ==================================================
# Exercício 4 - Função valor absoluto
# ==================================================

def valor_absoluto(n):
    if n < 0:
        return -n
    else:
        return n

numero = float(input("\nDigite um número: "))
resultado = valor_absoluto(numero)
print("Valor absoluto:", resultado)