class Conexion:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Conexión establecida.")
    def __del__(self):
        print(f"Conexión cerrada.")
conexion1= Conexion()
conexion2=Conexion()
del conexion1
del conexion2
