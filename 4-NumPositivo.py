#Pide un número y determina si es positivo, negativo o cero
num=float(input("Introduce un número: "))
#Condición para determinar si el número es positivo, negativo o cero
if num > 0:
    print(f"{num} es un número positivo.")
elif num < 0:
    print(f"{num} es un número negativo.")
else:
    print("El número es cero.")
# Fin del programa