# ==================================================
# Exercício 1 - Valores reais
# ==================================================

ct = 0        # contador
soma = 0      # somador
maior20 = 0   # conta quantos valores são maiores que 20

qtd = int(input("Digite a quantidade de valores: "))

for i in range(1, qtd + 1, 1):
    valor = float(input(f"Digite o valor número {i}: "))
    ct += 1
    soma += valor
    if valor > 20:
        maior20 += 1

# saída
print("\nQuantidade de valores digitados:", ct)
print("Soma dos valores:", soma)
print(f"Média aritmética: {soma/ct:.2f}")
print("Quantidade de valores maiores que 20:", maior20)
