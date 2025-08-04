class Motor:
    def arrancar(self):
        print("Motor arrancado")
class Coche:
    def __init__(self):
        self.motor = Motor()
    def arrancar(self):
        self.motor.arrancar()
miCoche = Coche()
miCoche.arrancar()
