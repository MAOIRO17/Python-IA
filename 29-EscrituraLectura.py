with open ("datos.txt","w",encoding="utf-8") as archivo:
    archivo.write("Hola, mundo!\n")
with open ("datos.txt","r",encoding="utf-8") as archivo:
    contenido=archivo.read()
    print(contenido)
    