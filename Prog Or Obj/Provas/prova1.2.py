# ==================================================
# Exercício 2 - Sequência do dobro
# ==================================================

soma = 0
print("\nDobro na ordem crescente:")

for i in range(0, 10 + 1, 1):   # de 0 até 10
    dobro = i * 2
    print(dobro)
    soma += dobro

print("Soma dos valores:", soma)