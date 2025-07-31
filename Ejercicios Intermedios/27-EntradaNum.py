import math

try:
    numero = float(input("Introduce un número positivo: "))
    if numero < 0:
        print("No se puede calcular la raíz cuadrada de un número negativo.")
    else:
        raiz = math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es {raiz}")
except ValueError:
    print("¡Debes introducir un número válido!")