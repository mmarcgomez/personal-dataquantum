import math
import random

import char


class Persona():
    # Constante para el sexo por defecto
    sexo_por_defecto = "H"

    """
        Si quisieramos 'más constructures' usariamos @clasmethod y los hariamos ,
        pero realmente este actua como varios 
    """

    def __init__(self,dni:str,nombre:str="",edad:int=0,sexo:str=sexo_por_defecto,peso:float=0.0,altura:float=0.0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura

    def calcularIMC(self):
        """
        calculara si la persona esta en su peso ideal (peso en kg/(altura^2 en m)),
        si esta fórmula devuelve un valor menor que 20, la función devuelve un -1,
        si devuelve un número entre 20 y 25 (incluidos), significa que esta por debajo
        de su peso ideal la función devuelve un 0 y si devuelve un valor mayor que 25
        significa que tiene sobrepeso, la función devuelve un 1.
        Te recomiendo que uses constantes para devolver estos valores.
        """
        p = self.__peso
        a = self.__altura
        res = p / math.pow(a, 2)
        imc = 0
        imcs = ["Infrapeso","Peso ideal","Sobrepeso"]
        if  res < 20 :
            imc =  -1 # Por debajo
        elif res >= 20:
            imc = 0 # Peso ideal
        else:
            imc = 1 # Sobrepeso

        return imcs[imc+1]
    def esMayordeEdad(self) -> bool:
        return self.__edad >= 18
    def comprobarSexo(self)-> str:
        if self.__sexo not in ["H","M"]:
            # print("(!) Sexo incorrecto") -> No es visible al exterior
            self.__sexo =  "H"
        else:
            pass
    def toString(self):
       print("______________________________________"
             "\nDNI: "+self.__dni+
             "\nNombre: "+self.__nombre+
             "\nEdad: "+str(self.__edad)+
             "\nSexo: "+self.__sexo+
             "\nPeso: "+str(self.__peso)+
             "\nAltura: "+str(self.__altura)
             )
    @staticmethod
    #Lo ponemos estatico para que podamos utilizarlo en el main sin tener que tener el objeto creado, ya que no depende de el
    def generaDNI() -> str:
        gen = "".join(str(random.randint(0, 9)) for _ in range(8)) #cadena de 8 numeros aleatorios del 0 al 9
        letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L',
                  'C', 'K', 'E']
        indice = int(gen) % 23
        return gen+letras[indice]
    def setNombre(self,nombre:str):
        self.__nombre = nombre
    def setEdad(self,edad:int):
        self.__edad = edad
    def setSexo(self,sexo:str):
        self.__sexo = sexo
    def setAltura(self,altura:float):
        self.__altura = altura
    def setPeso(self,peso:float):
        self.__peso = peso