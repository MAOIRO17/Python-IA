while True:
    edad = input("Introduce tu edad: ")
    try:
        edad = int(edad)
        assert edad >= 0, "La edad no puede ser negativa."
        print(f"Tu edad es: {edad}")
        break
    except ValueError:
        print("Por favor, introduce un número válido.")
    except AssertionError as e:
        print(e)