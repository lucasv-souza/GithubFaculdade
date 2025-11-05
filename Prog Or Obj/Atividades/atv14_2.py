from atv14_1 import FormaGeometrica, Quadrado

if __name__ == '__main__':

    try:
        obj_forma = FormaGeometrica("Amarelo")
    except TypeError as e:
        print("Não foi possível instanciar a classe abstrata FormaGeometrica (esperado):")
        print(e)
    
    obj_quad1 = Quadrado(cor="Azul", lado=3)
    print("\n--- Quadrado 1:")
    print("Cor:", obj_quad1.get_cor())
    print("Lado:", obj_quad1.get_lado())
    print("Área:", obj_quad1.area())
    print("Perímetro:", obj_quad1.perimetro())

    obj_quad1.set_lado(4)
    print("\nLado alterado:")
    print("Lado:", obj_quad1.get_lado())
    print("Área:", obj_quad1.area())
    
    obj_quad2 = Quadrado("Verde")
    print("\n--- Quadrado 2 (Padrão):")
    print("Cor:", obj_quad2.get_cor())
    print("Lado:", obj_quad2.get_lado())
    print("Área:", obj_quad2.area())