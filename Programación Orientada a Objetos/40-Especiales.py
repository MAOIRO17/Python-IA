class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}"
producto1 = Producto("Laptop", 900)
print(producto1)
producto2 = Producto("Teléfono", 500)
print(producto2)