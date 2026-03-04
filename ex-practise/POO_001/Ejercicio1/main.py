from ctypes.macholib.dylib import dylib_info

from persona import *

def introducir():

    dni = input("Introduce el DNI: ")
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    sexo = input("Introduce tu sexo: ")
    peso = float(input("Introduce tu peso: "))
    altura = float(input("Introduce tu altura: "))

    Persona1 = Persona(dni, nombre, edad, sexo, peso, altura)
    Persona2 = Persona(Persona.generaDNI(), nombre, edad, sexo)
    Persona3 = Persona(Persona.generaDNI()) #Los demas atributos por defecto, ademas luego ponemos los setters

    Persona1.toString()
    Persona2.toString()
    Persona3.toString()



if __name__=="__main__":
    introducir()
