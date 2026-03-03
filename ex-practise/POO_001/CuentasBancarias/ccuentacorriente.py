from ccuenta import ccuenta

class ccuentacorriente(ccuenta):
    def __init__(self,transacciones:int,importePorTrans:float,transExentas:int):
        super().__init__(transacciones,importePorTrans,transExentas)
        self.transacciones = transacciones
        self.importePorTrans = importePorTrans
        self.transExentas = transExentas

    def decrementarTransacciones(self):
        self.transacciones -= 1

    def asignarImportePorTrans(self,importePorTrans: float):
        self.importePorTrans = importePorTrans

    def obtenerImportePorTrans(self ):
        return self.importePorTrans

    def asignarTransExentas(self,transExentas: int):
        self.transExentas = transExentas

    def obtenerTransExentas(self):
        return self.transExentas

