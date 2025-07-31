class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Juan", 21)
persona1.saludar()
persona2 = Persona("Ana", 78)
persona2.saludar()
