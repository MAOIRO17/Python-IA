class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    def saludar(self):
        return f"Hola, mi nombre es {self._nombre} y tengo {self._edad} años."
    
persona1=input("Introduce el nombre de la persona: ")
edad1=int(input("Introduce la edad de la persona: "))
persona1 = Persona(persona1, edad1)
print(persona1.saludar()) 