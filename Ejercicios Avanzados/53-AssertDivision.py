def dividir(a, b):
    assert b != 0, "División por cero no permitida."
    return a / b

print(dividir(10, 2))  # Esto debería funcionar
# print(dividir(10, 0))  # Esto debería lanzar una excepción
try:
    resultado = dividir(10, 0)
except AssertionError as e:
    print(f"Error: {e}")