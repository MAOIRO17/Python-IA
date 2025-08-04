class Cuenta:
    def __init__(self, titular, cantidad):
        self.__titular = titular
        self.__cantidad = cantidad
    def getTitular(self):
        return self.__titular
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
            print(f"Depósito realizado. Nueva cantidad: {self.__cantidad}")
        else:
            print("Cantidad a depositar debe ser positiva.")
    def mostrarInfo(self):
        print(f"Titular: {self.__titular}, Cantidad: {self.__cantidad}")
    
cuenta=Cuenta("Mario", 1040)
cuenta.mostrarInfo()
cuenta.__cantidad = 5000 # Esto no cambiará el valor de la cantidad en la clase
cuenta.mostrarInfo() # Intento de cambiar la cantidad directamente, no funcionará debido al encapsulamiento
cuenta.depositar(500) # Usando el método para depositar
cuenta.mostrarInfo() # Verificando la cantidad después del depósito