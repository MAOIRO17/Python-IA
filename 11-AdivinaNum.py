#Pide un número al usuario y adivina un número aleatorio entre 1 y 100, dando pistas si el número es mayor o menor.
import random 
# Genera un número aleatorio entre 1 y 100
numAleatorio = random.randint(1, 100)  
intentos = 0
numUsuario = 0
while numUsuario != numAleatorio:
    numUsuario = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1
    if numUsuario < numAleatorio:
        print("El número es mayor.")
    elif numUsuario > numAleatorio:
        print("El número es menor.")
    else:
        print(f"¡Felicidades! Has adivinado el número {numAleatorio} en {intentos} intentos.")
# Fin del programa