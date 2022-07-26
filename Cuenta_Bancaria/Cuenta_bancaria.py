class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente {self.nombre} {self.apellido}\nBalance de cuenta: {self.numero_cuenta}: $ {self.balance}"

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print(f"Deposito Aceptado\nUsted ahora tiene: {self.balance}")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print(f"Retiro realizado\nUsted ahora tiene: {self.balance}")
        else:
            print(f"Fondos Insuficientes\nUsted tiene: {self.balance}")


def crear_cliente():
    nombre_cliente = input("Ingresa tu nombre: ")
    apellido_cliente = input("Ingresa tu apellido: ")
    numero_cuenta = input("Ingresa tu numero de cuenta: ")
    cliente = Cliente(nombre_cliente, apellido_cliente, numero_cuenta)
    return cliente


def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    eleccion = 1
    while not eleccion not in range(1, 3):
        print('''
           [1] - Depositar 
           [2] - Retirar
           [3] - Salir ''')
        eleccion = int(input("Elige una opcion: "))

        if eleccion == 1:
            print(f"Balance: {mi_cliente.balance}")
            monto_depositar = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_depositar)

        elif eleccion == 2:
            print(f"Balance: {mi_cliente.balance}")
            montro_retirar = int(input("Monto a retirar: "))
            mi_cliente.retirar(montro_retirar)

        elif eleccion >= 3:
            print(mi_cliente)
            print("Gracias por operar en Banco Python")
            break


inicio()



