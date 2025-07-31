try:
    archivo = open("datos.txt")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    print("Fin del intento de abrir el archivo.")