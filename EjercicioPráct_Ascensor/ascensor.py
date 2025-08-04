class Ascensor:
    def __init__(self, plantaInicial=0, plantaFinal=10,plantaMin=0):
        self.planta = plantaInicial
        self.plantaFinal = plantaFinal
        self.plantaMin = plantaMin
    def subir(self):
        if self.planta < self.plantaFinal:
            self.planta += 1
            print(f"Subiendo a la planta {self.planta}")
        else:
            print("Ya estás en la planta más alta.")
    def bajar(self):
        if self.planta> self.plantaMin:
            self.planta -= 1
            print(f"Bajando a la planta {self.planta}")
        else:
            print("Ya estás en la planta más baja.")
    def verPlanta(self):
        print(f"Estás en la planta {self.planta}")