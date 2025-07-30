# Pide al usuario una cantidad de números a sumar y luego solicita cada número, mostrando al final la suma total.
cantidad=float(input("Introduce la cantidad de números a sumar: "))
suma=0
for i in range(1, int(cantidad) + 1):
    num=float(input(f"Introduce el número {i}: "))
    suma += num
print(f"La suma de los números es: {suma}")
# Fin del programa