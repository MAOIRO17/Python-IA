import json

datos = [
    {"Nombre": "Juan", "Edad": 30, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 25, "Ciudad": "Barcelona"},
    {"Nombre": "Luis", "Edad": 35, "Ciudad": "Valencia"}
]

# Escribir datos en un archivo JSON
with open("personas2.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, ensure_ascii=False, indent=4)

# Leer datos desde el archivo JSON
with open("personas2.json", "r", encoding="utf-8") as archivo:
    personas = json.load(archivo)
    for persona in personas:
        print(persona)
        print(f"Nombre: {persona['Nombre']}")