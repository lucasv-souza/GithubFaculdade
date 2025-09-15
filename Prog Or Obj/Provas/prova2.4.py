def calcular_area_circulo(raio):
    pi = 3.14159
    area = pi * (raio ** 2)
    return area

if __name__ == '__main__':
    print("--- Calculadora de Área de Círculo ---")
    raio_circulo = float(input("Digite o valor do raio do círculo: "))
    area_calculada = calcular_area_circulo(raio_circulo)
    print(f"\nA área de um círculo com raio {raio_circulo} é: {area_calculada:.2f}")