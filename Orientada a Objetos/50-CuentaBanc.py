class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Cantidad no válida para retirar")
    def __str__(self):
        return f"Cuenta de {self.titular}, Saldo: {self.saldo}"

cuenta = CuentaBancaria("Juan Perez", 1000)
cuenta.depositar(500)
print(cuenta)  # Imprime: Cuenta de Juan Perez, Saldo: 1500
cuenta.retirar(200)
print(cuenta)  # Imprime: Cuenta de Juan Perez, Saldo: 1300