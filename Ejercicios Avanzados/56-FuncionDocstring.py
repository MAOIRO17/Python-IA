def saludar(nombre):
    """
    Esta función saluda a una persona por su nombre.
    
    Parámetros:
    nombre (str): El nombre de la persona a saludar.
    
    Retorna:
    str: Un saludo personalizado.
    """
    return f"Hola, {nombre}!"

print(saludar.__doc__)
help(saludar)