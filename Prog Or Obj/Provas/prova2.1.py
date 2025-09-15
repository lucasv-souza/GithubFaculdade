def somar_tres_valores(v1, v2, v3):
    soma = v1 + v2 + v3
    return soma

if __name__ == '__main__':
    print("--- Soma de Três Valores ---")
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    valor3 = int(input('Digite o terceiro valor: '))

    resultado = somar_tres_valores(valor1, valor2, valor3)

    print("\nO resultado da soma é:", resultado)