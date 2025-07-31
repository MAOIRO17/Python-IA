import csv

datos= [ ["Nombre","Edad","Ciudad"],
["Juan",30,"Madrid"],["Ana",25,"Barcelona"],["Luis",35,"Valencia"],]
with open("personas.csv", "w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerows(datos)
with open("personas.csv", "r", encoding="utf-8") as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        print(fila)