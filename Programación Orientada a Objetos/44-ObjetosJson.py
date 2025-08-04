import json

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'email': self.email
        }
usuarios= [Usuario('Juan', 'juan@gmail.com'),Usuario('Ana', 'ana@gmail.com') ] 
with open('usuarios.json', 'w', encoding="utf-8") as f:
    json.dump([usuario.to_dict() for usuario in usuarios], f, ensure_ascii=False, indent=4)

with open('usuarios.json', 'r', encoding="utf-8") as f:
    datos = json.load(f)
    print(datos)
    
usuarios_cargados = [Usuario(**d) for d in datos]
for usuario in usuarios_cargados:
    print(f'Nombre: {usuario.nombre}, Email: {usuario.email}')

