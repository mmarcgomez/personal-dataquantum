
import random


class Password():
    def __init__(self,contraseña:str, longitud:int=8):

        self.__contraseña = contraseña
        self.__longitud = longitud

    def generaContraseña(self,contraseña:str,longitud:int):
        self.__contraseña = "".join(str(random.randint(0, 9)) for _ in range(longitud))

    def esFuerte(self,contraseña:str) -> bool:
        mayus = 0
        minus = 0
        for l in contraseña:
            if l.isupper():
                mayus +=1
            elif l.islower():
                minus +=1
        if mayus >= 2 and minus >=2 and len(contraseña) >= 5:
            return True
        else:
            return False
    @property
    def _contraseña(self):
        return self.__contraseña

    @property
    def longitud(self):
        return self.__longitud

    @longitud.setter
    def longitud(self,longitud: int):
        self.__longitud = longitud


if __name__ == '__main__':
    # pedir datos al usuario
    cantidad = int(input("Cuantos passwords quieres crear: "))
    longitud = int(input("Longitud de los passwords: "))

    # lista de passwords
    passwords = []

    # lista de booleanos
    fuertes = []

    # crear objetos
    for i in range(cantidad):
        p = Password("", longitud)  # crear objeto
        p.generaContraseña("", longitud)  # generar contraseña

        passwords.append(p)

        fuertes.append(p.esFuerte(p._contraseña))

    # mostrar resultados
    for i in range(cantidad):
        print(passwords[i]._contraseña, fuertes[i])