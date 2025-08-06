class Usuario:
    """
    Clase que representa un usuario con nombre y email.
    """
    def __init__(self, nombre, email):
        """
        Inicializa un nuevo usuario con nombre y email.
        Parametros:
        nombre (str): El nombre del usuario.
        email (str): El email del usuario.
        """
        self.nombre = nombre
        self.email = email
print(Usuario.__doc__)
Marcos=Usuario("Marcos", "Marcos@gmail.com")
print(Marcos.__doc__)
help(Marcos)
print(Marcos.__init__.__doc__)