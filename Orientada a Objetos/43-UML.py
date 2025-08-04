class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            return False
    def devolver(self):
        self.disponible = True

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
    def prestar_libro(self, titulo, nombre_usuario):
        libro = next((libro for libro in self.libros if libro.titulo == titulo and libro.disponible), None)
        usuario = next((u for u in self.usuarios if u.nombre == nombre_usuario), None)
        if libro and usuario:
            if libro.prestar():
                usuario.libros_prestados.append(libro)
                return f"Libro '{titulo}' prestado a {usuario.nombre}."
            else:
                return f"El libro '{titulo}' no está disponible."
        else:
            return "Libro o usuario no encontrado."


Mibiblioteca = Biblioteca()
Mibiblioteca.registrar_usuario(Usuario("Alice"))
Mibiblioteca.agregar_libro(Libro("1984", "George Orwell"))
Mibiblioteca.agregar_libro(Libro("Brave New World", "Aldous Huxley"))

print(Mibiblioteca.prestar_libro("1984", "Alice"))