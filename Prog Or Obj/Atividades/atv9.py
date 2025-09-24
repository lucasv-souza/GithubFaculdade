def calcula_quadrado(numero):
    return numero ** 2

if __name__ == "__main__":
    num = int(input("Digite um número: "))
    print(f"O quadrado de {num} é {calcula_quadrado(num)}")
