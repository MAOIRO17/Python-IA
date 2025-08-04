class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Punto({self.x}, {self.y})"
p= Punto(3, 4)
print(p)  # Imprime: Punto(3, 4)