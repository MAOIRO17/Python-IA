class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")
    
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Coche:{ self.marca}, Modelo: {self.modelo}, Puertas: {self.puertas}")
coche1 = Coche("Opel", "Corsa", 4)
coche1.mostrar_info()  # Marca: Toyota, Modelo: Corolla, Puertas: 4
class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Moto: {self.marca}, Modelo: {self.modelo}, Cilindrada: {self.cilindrada}cc")
moto1 = Moto("Yamaha", "MT-07", 689)
moto1.mostrar_info()  # Marca: Yamaha, Modelo: MT-07, Cilindrada: 689cc