from ccuenta import ccuenta
from datetime import date


class CCuentaAhorro(ccuenta):
    def __init__(self, cuotaMantenimiento: float):
        super().__init__(cuotaMantenimiento)
        self.cuotaMantenimiento = cuotaMantenimiento

    def asignarCuotaMantenimiento(self, cuotaMantenimiento: float):
        self.cuotaMantenimiento = cuotaMantenimiento

    def obtenerCuotaMantenimiento(self, cuotaMantenimiento: float):
        return self.cuotaMantenimiento

    def comisiones(self):
        dia = date.today().day
        c = self.cuotaMantenimiento
        if dia == 1:
            self.saldo -= (c * self.saldo) / 100
        else:
            pass
