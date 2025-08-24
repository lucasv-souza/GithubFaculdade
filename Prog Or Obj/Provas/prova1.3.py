# ==================================================
# Exercício 3 - Função soma de dois valores
# ==================================================

def soma(a, b):
    return a + b

def main():
    x = float(input("\nDigite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
    resultado = soma(x, y)
    print("Resultado da soma:", resultado)

# executa o programa principal
if __name__ == "__main__":
    main()