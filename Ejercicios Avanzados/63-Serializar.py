import pickle

datos = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
with open("datos.pkl", "wb") as archivo:
    pickle.dump(datos, archivo)

print("Datos serializados correctamente.")

with open("datos.pkl", "rb") as archivo:
    datos_cargados = pickle.load(archivo)
print(f"Datos cargados: {datos_cargados}")
