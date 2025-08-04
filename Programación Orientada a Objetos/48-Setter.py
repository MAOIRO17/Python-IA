class Producto:
    def __init__(self, precio):
        self._precio = precio
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = nuevo_precio

producto = Producto(100)
producto.precio = 150
print(producto.precio) # Imprime el nuevo precio