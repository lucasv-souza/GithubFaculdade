def soma(numero1, numero2):
    return numero1 + numero2

def subtrai(numero1, numero2):
    return numero1 - numero2

def main():
    numero1 = int(input('Primeiro valor: '))
    numero2 = int(input('Segundo valor: '))
    numero3 = int(input('Terceiro Valor: '))
    numero4 = int(input('Quarto Valor: '))
    operacao = input('Selecione a operação: (+ ou -): ')

    soma1 = soma(numero1, numero2)
    soma2 = soma(numero3, numero4)
    calculo = soma1 + soma2

    sub1 = subtrai(numero1, numero2)
    sub2 = subtrai(numero3, numero4)
    calculo1 = sub1 - sub2

    if operacao == "+":
        print('Soma: ', soma(numero1, numero2))
        print('Soma de 4 valores: ', calculo)

    elif operacao == "-":
        print('Subtração: ', subtrai(numero1, numero2))
        print('Subtração de 4 valores: ', calculo1)
    else:
        print('Operação inválida')

if __name__ == '__main__':
    main()