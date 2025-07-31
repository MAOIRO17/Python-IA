class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("El animal hace un sonido.")

class Perro(Animal):  # Perro hereda de Animal
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")

class Gato(Animal):  # Gato hereda de Animal
    def hablar(self):
        print(f"{self.nombre} dice: ¡Miau!")

# Uso de las clases
perro = Perro("Toby")
gato = Gato("Misu")

perro.hablar()  # Toby dice: ¡Guau!
gato.hablar()   # Misu dice: ¡Miau!