#Pide dos números y muestra si el primero es mayor, menor o igual que el segundo
num1=float(input("Introduce el primer número: "))
num2=float(input("Introduce el segundo número: "))
#Condición para determinar si el primer número es mayor, menor o igual que el segundo
if num1 > num2:
    print(f"{num1} es mayor que {num2}.")
elif num1 < num2:
    print(f"{num1} es menor que {num2}.")
else:
    print(f"{num1} es igual a {num2}.")
#Fin del programa