from ccuenta import ccuenta
from ccuentaahorro import CCuentaAhorro
from ccuentacorriente import ccuentacorriente
def menu():
    banco = CBanco()

    while True:
        print("\n1. Saldo")
        print("2. Buscar")
        print("3. Ingreso")
        print("4. Reintegro")
        print("5. Añadir")
        print("6. Eliminar")
        print("7. Mantenimiento")
        print("8. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            cuenta = input("Número cuenta: ")
            clientes = banco.buscar(cuenta)
            if clientes:
                print("Saldo:", clientes[0].estado())

        elif opcion == "3":
            cuenta = input("Número cuenta: ")
            cantidad = float(input("Cantidad: "))
            clientes = banco.buscar(cuenta)
            if clientes:
                clientes[0].ingreso(cantidad)

        elif opcion == "4":
            cuenta = input("Número cuenta: ")
            cantidad = float(input("Cantidad: "))
            clientes = banco.buscar(cuenta)
            if clientes:
                clientes[0].reintegro(cantidad)

        elif opcion == "5":
            nombre = input("Nombre: ")
            cuenta = input("Cuenta: ")
            saldo = float(input("Saldo inicial: "))
            interes = float(input("Tipo interés: "))

            cliente = CCuentaAhorro(nombre, cuenta, saldo, interes, 10)
            banco.insertarCliente(cliente)

        elif opcion == "6":
            cuenta = input("Número cuenta a eliminar: ")
            banco.eliminarCliente(cuenta)

        elif opcion == "7":
            for c in banco.obtenerClientes():
                c.comisiones()
                c.intereses()

        elif opcion == "8":
            break