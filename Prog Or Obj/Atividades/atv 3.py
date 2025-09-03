ct = 0
soma = 0

print('Digite [-1] para sair')
for i in range(1, 5+1, 1):
    nota = float(input("Nota:"))
    soma += nota
    ct += 1
media = soma / ct

print('Média', media)