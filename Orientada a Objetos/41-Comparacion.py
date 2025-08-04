class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
    def __eq__(self, otro):
        return self.titulo == otro.titulo
libro1= Libro("Brave New World")
libro2= Libro("Brave New World")
print(libro1 == libro2) # True
libro3= Libro("1984")
print(libro1 == libro3) # False
