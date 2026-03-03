from abc import ABC,abstractmethod #Este metodo es para hacer clases abstractas
import math

class FG(ABC):
    def __init__(self,lado1:float): #No hace falta realmente tipar, pero al principio lo hacemos
        self.lado1 = lado1
        #Si no se pone nada por defecto es público, para ponerlo protegido self._lado1 y privado self.__lado1

    def __str__(self): #Esta funcion corresponde al toString de Java
        return f'FG({self.lado1:.2f})'  #No hay sobrecarga de constructores, hay atributos que pueden tener valores por defecto
        #No hay métodos en python, son funciones.

    @abstractmethod #Esto es lo que nos dice que es un metodo abstracto
    def calcular_perimetro(self) -> float: #Forzamos a que lo que vaya devolver la funcion sea un float. Es opcional
        pass
    @abstractmethod
    def calcular_area(self) -> float:
        pass


class Cuadrado(FG):
    #Hereda el constructor por defecto, no es necesario volverlo a poner
    def calcular_perimetro(self) -> float:
        return self.lado1*4
    def calcular_area(self) -> float:
        return math.pow(self.lado1,2)
    def __str__(self):
        return f'Cuadrado({self.lado1:.2f})'
        #return super().__str__()+f'Cuadrado({self.lado1:.2f})' Accede al toString de FiguraGeometrica

class Rectangulo(FG):
    def __init__(self,lado1,lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_perimetro(self) -> float:
        return (self.lado1 + self.lado2)*2
    def calcular_area(self) -> float:
        return self.lado1*self.lado2
    def __str__(self):
        return f'Rectangulo: Lado1 = {self.lado1:.2f}, Lado2 = {self.lado2:.2f}'

class Cubo(Cuadrado):

    def calcular_perimetro(self) -> float:
        return self.lado1*12
    def calcular_area(self) -> float:
        return super().calcular_area()*6
    def calcular_volumen(self):
        return math.pow(self.lado1,3)
    def __str__(self):
        return f'Cubo: Lado = {self.lado1:.2f}'