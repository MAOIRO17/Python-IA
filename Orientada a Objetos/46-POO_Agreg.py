class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
class Curso:
    def __init__(self,profesor):
        self.profesor = profesor
    def mostrar_profesor(self):
        print(f'Profesor: {self.profesor.nombre}')
profesor = Profesor('Dr. Smith')
curso = Curso(profesor)
curso.mostrar_profesor()