ct_aluno = 0 
soma_idade = 0
mais_novo = 200
mais_velho = 0
ct_30 = 0

print("Digite 0 para sair da sequência.")
while True:
    idade = int(input("Idade do Aluno: "))
    if idade == 0:
        break
    ct_aluno += 1
    soma_idade += idade
    if idade < mais_novo:
        mais_novo = idade
    if idade > mais_velho:
        mais_velho = idade
    if idade > 30:
        ct_30 += 1
media = soma_idade / ct_aluno

print("\nQuantidade de Alunos analisados: ", ct_aluno)
print("Soma das Idades dos Alunos:", soma_idade)
print("Média de Idade dos Alunos: ", media)
print("Idade Aluno mais novo: ", mais_novo)
print("Idade Aluno mais velho:", mais_velho)
print("Alunos com mais de Trinta Anos: ", ct_30)