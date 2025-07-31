lineas = ["Primera linea\n", "Segunda linea\n", "Tercera linea\n", "Cuarta linea\n"]
with open("lineas.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas)
with open("lineas.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())