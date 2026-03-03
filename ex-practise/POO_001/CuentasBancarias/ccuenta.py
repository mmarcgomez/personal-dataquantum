from abc import abstractmethod


class ccuenta():
    def __init__(self,nombre:str,cuenta:str,saldo:float,tipo_de_interes:float):
        self.nombre = nombre
        self.cuenta = cuenta
        self.saldo = saldo
        self.tipo_de_interes = tipo_de_interes

    def asignarNombre(self,nombre:str):
        self.nombre = nombre
    def obtenerNombre(self,nombre:str):
        return self.nombre
    def asignarCuenta(self,cuenta):
        self.cuenta = cuenta
    def obtenerCuenta(self,cuenta:str):
        return self.cuenta
    def asignarTipoDeInteres(self,tipo_de_interes:float):
        self.tipo_de_interes = tipo_de_interes
    def obtenerTipoDeInteres(self,tipo_de_interes:float):
        return self.tipo_de_interes
    def ingreso(self,saldo:float,ingreso:float):
        self.saldo += ingreso
    def reintegro(self,saldo:float,reintegro:float):
        self.saldo -= reintegro
    def estado(self,saldo:float):
        return self.saldo

    @abstractmethod
    def comisiones(self):
        pass
    @abstractmethod
    def intereses (self):
        pass