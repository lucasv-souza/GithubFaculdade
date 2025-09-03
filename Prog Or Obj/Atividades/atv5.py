def maximo(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def minimo(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

def main():
    num1 = int(input("Primeiro número: "))
    num2 = int(input("Segundo número: "))

    print("Maior valor: ", maximo(num1, num2))
    print("Maior valor: ", maximo(5, 7))
    print("Menor valor: ", minimo(num1, num2))

if __name__ == '__main__':
    main()