#Muestra los datos de un usuario en un diccionario
usuario={
    "nombre": "Carlos",
    "edad": 51,
    "email": "carlos@gmail.com",
    "telefono": "123456789",  
}
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")
# Fin del programa