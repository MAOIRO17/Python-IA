# Muestra una lista de tareas y las imprime una por una
tareas=[]
tareas.append("Aprender Python")
tareas.append("Practicar GitHub Copilot")
tareas.append("Desarrollar proyectos")
tareas.append("Contribuir a la comunidad")
tareas.append("Explorar nuevas tecnologías")
tareas.append("Leer documentación")
tareas.append("Colaborar en proyectos de código abierto")
print("Lista de tareas:")
for tarea in tareas:
    print(f"- {tarea}")

#Elimina una tarea específica de la lista
tareas.remove("Leer documentación")
print("\nLista de tareas actualizada:")
for tarea in tareas:
    print(f"- {tarea}")
# Fin del programa