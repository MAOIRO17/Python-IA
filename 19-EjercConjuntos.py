#Muestra los nombres en un conjunto y realiza operaciones de adición, verificación y eliminación
nombres={"Juan", "María", "Pedro", "Ana", "Luis", "Laura", "Carlos", "Sofía", "Javier", "Isabel"}
nombres.add("Miguel") 
if "Ana" in nombres:
    print("Ana está en el conjunto de nombres.")
print("Nombres en el conjunto:")
for nombre in nombres:
    print("-",nombre)
    # Fin del programa