import json
import os

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'email': self.email
        }

class UsuarioCRUD:
    def __init__(self, archivo):
        self.archivo = archivo
        self.usuarios = self.cargar()
    def cargar(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r', encoding="utf-8") as f:
                datos = json.load(f)
                return [Usuario(**d) for d in datos]
        return []
    def guardar(self):
        with open(self.archivo, 'w', encoding="utf-8") as f:
            json.dump([usuario.to_dict() for usuario in self.usuarios], f, ensure_ascii=False, indent=4)
    def crear_usuario(self, nombre, email):
        self.usuarios.append(Usuario(nombre, email))
        self.guardar()
    def listar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            for i, usuario in enumerate(self.usuarios, 1):
                print(f"{i}. Nombre: {usuario.nombre}, Email: {usuario.email}")
    def actualizar(self, index, nombre, email):
        if 0 <= index < len(self.usuarios):
            self.usuarios[index].nombre = nombre
            self.usuarios[index].email = email
            self.guardar()
            print("Usuario actualizado correctamente.")
        else:
            print("Índice no válido.")
    def eliminar(self, index):
        if 0 <= index < len(self.usuarios):
            eliminado = self.usuarios.pop(index)
            self.guardar()
            print(f"Usuario '{eliminado.nombre}' eliminado correctamente.")
        else:
            print("Índice no válido.")

gestor = UsuarioCRUD('usuarios.json')
while True:
    print("\n1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == '1':
        nombre = input("Nombre: ")
        email = input("Email: ")
        gestor.crear_usuario(nombre, email)
    elif opcion == '2':
        gestor.listar_usuarios()
    elif opcion == '3':
        gestor.listar_usuarios()
        try:
            index = int(input("Índice del usuario a actualizar: ")) - 1
            nombre = input("Nuevo nombre: ")
            email = input("Nuevo email: ")
            gestor.actualizar(index, nombre, email)
        except ValueError:
            print("Por favor, introduce un número válido.")
    elif opcion == '4':
        gestor.listar_usuarios()
        try:
            index = int(input("Índice del usuario a eliminar: ")) - 1
            gestor.eliminar(index)
        except ValueError:
            print("Por favor, introduce un número válido.")
    elif opcion == '5':
        break