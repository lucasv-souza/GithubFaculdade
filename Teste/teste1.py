# Estrutura de repetição FOR
'''
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')
'''


# Estrutura de repetição WHILE
'''
n = 1
impar = par = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares')
'''


# Função sem parâmetro
'''
def lin():
    print('-' * 30)
    
# Programa principal
lin()
print('Olá, Mundo!')        
lin()
print('Python')
lin()
print('Programação')
lin()
'''


# Função com parâmetro
'''
def título(txt):
    # Calcula o tamanho da linha baseado no tamanho do texto + 4 espaços (2 de cada lado)
    tamanho = len(txt) + 4
    
    print('-' * tamanho)
    # Centraliza o texto 'txt' em um espaço de 30 caracteres
    print(txt.center(tamanho)) 
    print('-' * tamanho)

# Parâmetros
título('Olá, Mundo!')
título('Python')
título('Programação')
'''

# Função com retorno
'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
    
# Programa principal
soma(b=4, a=5)
soma(7, 2)
'''


# Função com número variável de argumentos
'''
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
    
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''


# Função que modifica uma lista
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
        
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''


# Função com retorno de lista
'''
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
    
soma(5, 2)
soma(2, 9, 4)
'''