try:
    numero = int(input("Introduce un número: "))
    print(f"El doble es {numero * 2}")
except ValueError:
    print("¡Eso no es un número válido!")
