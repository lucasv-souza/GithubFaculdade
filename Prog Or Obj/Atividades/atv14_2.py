from atv14_1 import FormaGeometrica, Quadrado, Circulo

if __name__ == '__main__':

    try:
        obj_forma = FormaGeometrica("Amarelo")
    except TypeError as e:
        print("Não foi possível instanciar a classe abstrata FormaGeometrica (esperado):")
        print(e)
    
    obj_quad1 = Quadrado(cor="Azul", lado=3)
    print("\n--- Quadrado:")
    print("Cor:", obj_quad1.get_cor())
    print("Lado:", obj_quad1.get_lado())
    print("Área:", obj_quad1.area())
    print("Perímetro:", obj_quad1.perimetro())

    obj_quad1.set_lado(4)
    print("\nLado alterado:")
    print("Lado:", obj_quad1.get_lado())
    print("Área:", obj_quad1.area())
    
    obj_circ1 = Circulo("Laranja", 5)
    print("\n--- Círculo:")
    print("Cor:", obj_circ1.get_cor())
    print("Raio:", obj_circ1.get_raio())
    print("Área:", obj_circ1.area())
    print("Perímetro:", obj_circ1.perimetro())

    obj_circ1.set_raio(3)
    print("\nRaio alterado:")
    print("Raio:", obj_circ1.get_raio())
    print("Área:", obj_circ1.area())
    print("Perímetro:", obj_circ1.perimetro())
    
    obj_circ2 = Circulo("Roxo")
    print("\n--- Círculo (Padrão):")
    print("Cor:", obj_circ2.get_cor())
    print("Raio:", obj_circ2.get_raio())
    print("Área:", obj_circ2.area())