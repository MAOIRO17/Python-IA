#Muestra los datos de un contacto en un diccionario
contacto={
    "name": "Carlos",
    "apellido": "Pérez",
    "edad": 30,
}
print("Datos del contacto: ")
for clave, valor in contacto.items():
    print(f"{clave}: {valor}")
    
# Modifica el diccionario
contacto["apellido"] = "Gómez"
#elimina una clave del diccionario
del contacto["edad"]
print("\nDatos del contacto actualizado: ")
for clave, valor in contacto.items():
    print(f"{clave}: {valor}")
# Fin del programa