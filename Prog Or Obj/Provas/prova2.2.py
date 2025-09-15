def adicao(n1, n2):
    resultado = n1 + n2
    print(f"Resultado: {n1} + {n2} = {resultado}")

def subtracao(n1, n2):
    resultado = n1 - n2
    print(f"Resultado: {n1} - {n2} = {resultado}")

def multiplicacao(n1, n2):
    resultado = n1 * n2
    print(f"Resultado: {n1} * {n2} = {resultado}")

def divisao(n1, n2):
    if n2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        resultado = n1 / n2
        print(f"Resultado: {n1} / {n2} = {resultado:.2f}")

if __name__ == '__main__':
    print("--- Calculadora Simples ---")
    operador = input("Digite a operação (+, -, *, /): ")
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    if operador == '+':
        adicao(valor1, valor2)
    elif operador == '-':
        subtracao(valor1, valor2)
    elif operador == '*':
        multiplicacao(valor1, valor2)
    elif operador == '/':
        divisao(valor1, valor2)
    else:
        print("Operador inválido. Tente novamente.")