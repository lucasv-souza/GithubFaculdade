def positivo_nulo_negativo(numero):
    if numero > 0:
        print("Mensagem: Valor Positivo")
    elif numero == 0:
        print("Mensagem: Valor nulo")
    else:
        print("Mensagem: Valor negativo")

if __name__ == '__main__':
    print("--- Verificador de Número ---")
    valor_lido = float(input("Digite um número real qualquer: "))
    positivo_nulo_negativo(valor_lido)