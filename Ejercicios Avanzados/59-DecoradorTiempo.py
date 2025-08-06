import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        func()
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
    return wrapper

@medir_tiempo
def funcion_lenta():
    print("Iniciando una tarea lenta...")
    time.sleep(2)  # Simula una tarea que toma tiempo
    print("Tarea lenta completada.")

funcion_lenta()