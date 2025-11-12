from atv15_1 import FormaGeometrica, Quadrado, Circulo
if __name__ == '__main__':                 

    obj_quad = Quadrado("Azul", 3)          
    print('- Quadrado:\nLado:', obj_quad.get_lado())
    print('Área:', obj_quad.area())
    print('Perímetro:', obj_quad.perimetro())
    obj_quad.set_lado(4)                        
    print('- Lado alterado:', obj_quad.get_lado())
    print('Área:', obj_quad.area())
    print('Perímetro:', obj_quad.perimetro())

    obj_circ = Circulo("Verde",3)          
    print('\n- Círculo:\nRaio:', obj_circ.get_raio())
    print('Área:', obj_circ.area())
    print('Perímetro:', obj_circ.perimetro())
    obj_circ.set_raio(2)
    print('- Raio alterado:', obj_circ.get_raio())
    print(f"Área: {obj_circ.area():.3f}") 
    print('Perímetro:', obj_circ.perimetro())
    print("Quantidade de objetos:", FormaGeometrica.get_ct_figura())