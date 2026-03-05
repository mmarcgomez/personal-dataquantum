from enum import Enum

class consumo_energetico(Enum):
    A=100
    B=80
    C=60
    D=50
    E=30
    F=10
class colores(Enum):
    BLANCO=1
    NEGRO=2
    ROJO=3
    AZUL=4
    GRIS=5

class electrodomestico:

    def __init__(self,precio=100,color="BLANCO",consumo="F",peso=5):
        self._precio=precio
        self._color=self.comprobarColor(color)
        self._consumo=self.comprobarConsumo_energetico(consumo)
        self._peso=peso

    @property
    def precio(self): return self._precio

    @precio.setter
    def precio(self, value): self._precio=value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color=value

    @property
    def consumo(self):
        return self._consumo

    @consumo.setter
    def consumo(self, value):
        self._consumo=value

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, value):
        self._peso=value

    def comprobarConsumo_energetico(self,consumo:str):
        for c in consumo_energetico:
            if c.name.lower() == consumo.lower():
                return c
        return consumo_energetico.F

    def comprobarColor(self,color:str):
        for c in colores:
            if c.name.lower() == color.lower():
                return c
        return colores.BLANCO

    def precioFinal(self):
        precio=self._precio
        precio +=self.consumo.value

        match True:
            case _ if self.peso>=80:
                precio+=100
            case _ if self.peso>=50:
                precio+=80
            case _ if self.peso>=20:
                precio+=50
            case _:
                precio +=10

        return precio

    def __str__(self):
        return f'Electrodomestico Precio: {self.precio} Color: {self.color.name} consumo: {self.consumo.name} peso: {self.peso}'


class lavadora(electrodomestico):
    def __init__(self,precio=100,color="BLANCO",consumo="F",peso=5,carga=5):
        super().__init__(precio,color,consumo,peso)
        self._carga=carga

    @property
    def carga(self):
        return self._carga

    @carga.setter
    def carga(self, value):
        self._carga=value

    def precioFinal(self):
        precio=super().precioFinal()
        precio =  precio+50   if self.carga>30 else precio
        return precio

    def __str__(self):
        return f'Lavadora Precio: {self.precio} Color: {self.color.name} consumo: {self.consumo.name} peso: {self.peso} Carga: {self._carga}'

class television(electrodomestico):
    def __init__(self, precio=100, color="BLANCO", consumo="F", peso=5,resolucion=20,sintonizador=False):
        super().__init__(precio, color, consumo, peso)
        self._resolucion=resolucion
        self._sintonizador=sintonizador

    @property
    def resolucion(self):
        return self._resolucion

    @resolucion.setter
    def resolucion(self, value):
        self._resolucion=value

    @property
    def sintonizador(self):
        return self._sintonizador

    @sintonizador.setter
    def sintonizador(self, value):
        self._sintonizador=value

    def precioFinal(self):
        precio = super().precioFinal()
        precio= precio*1.3   if self.resolucion>40 else precio
        precio= precio+50  if self._sintonizador else precio
        return precio

    def __str__(self):
        return f'Television Precio: {self.precio} Color: {self.color.name} consumo: {self.consumo.name} peso: {self.peso}  resolucion: {self._resolucion} sintonizador: {self._sintonizador}'

def imprimir(lista):
    for c in lista:
        print(f'{c} precio final: {c.precioFinal()}')

def imprimirlistaclase(lista,clase):
    suma=0
    for c in lista:
        if isinstance(c,clase):
            print(f'{c} precio final: {c.precioFinal()}')
            suma+=c.precioFinal()
    print(f'Sumatorio de precios: {suma}')

if __name__ == "__main__":
    lista=[]
    lista.append(electrodomestico(100,color="BLANCO"))
    lista.append(electrodomestico(200.0, "BLANCO", "A", 50))
    lista.append(lavadora(150.0, "AZUL", "C", 30, 10))
    lista.append(television(500.0, "NEGRO", "E", 20, 50, True))
    lista.append(electrodomestico(100.0, "GRIS", "B", 10))
    lista.append(lavadora(300.0, "BLANCO", "B", 40, 15))
    lista.append(television(800.0, "NEGRO", "A", 30, 60, False))
    lista.append(electrodomestico(50.0, "ROJO", "F", 5))
    lista.append(lavadora(250.0, "GRIS", "D", 20, 8))
    lista.append(television(400.0, "BLANCO", "C", 10, 40, True))
    lista.append(electrodomestico(120.0, "NEGRO", "B", 15))

    lista.sort(key=lambda x: x.__class__.__name__)

    imprimir(lista)

    print("\n***************Impresion de lavadoras**********************\n")
    imprimirlistaclase(lista,lavadora)
    print("\n***************Impresion de televisiones**********************\n")
    imprimirlistaclase(lista,television)
    print("\n***************Impresion de electrodomesticos**********************\n")
    imprimirlistaclase(lista, electrodomestico)

