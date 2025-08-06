def mi_decorador(function):
    def nueva_funcion():
        print("Antes de llamar a la función")
        function()
        print("Después de llamar a la función")
    return nueva_funcion
@mi_decorador
def saludar():
    print("¡Hola, mundo!")
saludar()