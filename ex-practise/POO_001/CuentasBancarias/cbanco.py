from ccuenta import ccuenta
from ccuentacorriente import ccuentacorriente
from ccuentaahorro import CCuentaAhorro
class CBanco ():
    def __init__(self):
        self.clientes = []

    def obtenerClientes(self):
        return self.clientes

    def insertarCliente(self, cliente):
        self.clientes.append(cliente)

    def eliminarCliente(self, numeroCuenta):
        self.clientes = [c for c in self.clientes if c.obtenerCuenta() != numeroCuenta]

    def longitud(self):
        return len(self.clientes)

    def buscar(self, valor):
        resultados = []
        for c in self.clientes:
            if valor.lower() in c.obtenerNombre().lower() or valor in c.obtenerCuenta():
                resultados.append(c)
        return resultados