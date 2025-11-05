from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self, cor):
        self.cor = cor

    def get_cor(self):
        return self.cor

    def set_cor(self, nova_cor):
        self.cor = nova_cor

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, cor, lado=2):
        super().__init__(cor)
        self.lado = lado

    def get_lado(self):
        return self.lado

    def set_lado(self, novo_lado):
        self.lado = novo_lado

    def area(self):
        vl_area = self.lado ** 2
        return vl_area

    def perimetro(self):
        return 4 * self.lado