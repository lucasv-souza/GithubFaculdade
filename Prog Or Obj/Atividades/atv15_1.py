from abc import ABC, abstractmethod 
class FormaGeometrica(ABC):         
    ct_figura = 0                  
    @classmethod                    
    def get_ct_figura(cls):
        return cls.ct_figura        
        
    def __init__(self, cor):
        self.cor = cor
        FormaGeometrica.ct_figura += 1
   
    def get_cor(self):
        return self.cor
    def set_cor(self, nova_cor):
        self.cor = nova_cor
    @abstractmethod                
    def area(self):             
        ...                        
    @abstractmethod                 
    def perimetro(self):            
        pass                        


class Quadrado(FormaGeometrica): 
    def __init__(self, cor, lado=2): 
        super().__init__(cor)       
        self.lado = lado
    def get_lado(self):
        return self.lado
    def set_lado(self, valor):
        self.lado = valor
   
    def area(self):                  
        vl_area = self.lado ** 2    
        return vl_area
    
    def perimetro(self):             
        vl_perimetro = 4 * self.lado
        return vl_perimetro


class Circulo(FormaGeometrica): 
    def __init__(self, cor, raio=1):    
        super().__init__(cor)          
        self.raio = raio               
    def get_raio(self):
        return self.raio
    def set_raio(self, valor):
        self.raio = valor
    
    def area(self):                     
        vl_area = 3.14 * pow(self.raio, 2)
        return vl_area
    
    def perimetro(self):                
        vl_perimetro = 2 * 3.14 * self.raio
        return vl_perimetro