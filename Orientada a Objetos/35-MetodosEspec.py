class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona({self.nombre}, {self.edad})"
    def __repr__(self):
        return f"EJ:Persona({self.nombre}, {self.edad})"
persona2 = Persona("Carla", 58)
print(persona2)
print(repr(persona2))