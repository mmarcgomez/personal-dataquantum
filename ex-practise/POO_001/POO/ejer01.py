#Separamos las clases a otro .py y las importamos
from ctypes import c_ushort
from itertools import count
from time import process_time_ns

from clases1 import FG,Cuadrado,Rectangulo,Cubo
#Podemos acceder a variables globales dentro de los metodos

def imprimir():
    global lista #Accede a la lista que este en el general
    for item in lista:
        print(item)
        print(f'> Perimetro: {item.calcular_perimetro()}')
        print(f'> Area: {item.calcular_area()}')
        if isinstance(item, Cubo): #Vemos si el primer parametro que le pasamos es una instancia del segundo, vamos de abajo para arriba
            print(f'> Volumen: {item.calcular_volumen()}')


def rellenar():
    global lista
    lista.append(Cuadrado(4))
    lista.append(Cuadrado(5))
    lista.append(Cubo(3))
    lista.append(Cuadrado(10))
    lista.append(Rectangulo(5,2))
    lista.append(Rectangulo(10,4))
    lista.append(Cubo(4))

def contar():
    global lista
    cubo = 0
    cua = 0
    rectangulo = 0

    for item in lista:
        if type(item) == Cubo:
            cubo+=1
        elif type(item) == Rectangulo:
            rectangulo+=1
        elif type(item) == Cuadrado:
            cua+=1

    print(f'Cubos: {cubo}')
    print(f'Rectangulos: {rectangulo}')
    print(f'Cuadrados: {cua}')
def contar2(li):
    c = {"Cuadrado":0,"Rectangulo":0,"Cubo":0}
    for item in li:
        c[item.__class__.__name__] +=1
    for c,v in c.items():
        print(f'{c}: {v}')
        
if __name__ == '__main__':

    lista = []
    rellenar()
    imprimir()
    contar()
