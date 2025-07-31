#Muestra los animales únicos de una lista utilizando un conjunto (set) y recorre el conjunto para imprimirlos
animales= ["Perro", "Gato", "Elefante", "León", "Tigre", "Jirafa", "Cebra", "Hipopótamo", "Rinoceronte", "Osos"]
print("Lista de animales:", animales)
unicos = set(animales)
print("Animales únicos:", unicos)
print(type(unicos))
for animal in unicos:
    print(animal)
# Fin del programa