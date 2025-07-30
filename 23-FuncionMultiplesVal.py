def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    
    return suma, resta, multiplicacion, division
resultadoSuma,resultadoResta, resultadoMultiplicacion, resultadoDivision = operaciones(5, 3)
print(f"Suma: {resultadoSuma},.. Resta: {resultadoResta}, Multiplicación: {resultadoMultiplicacion}, División: {resultadoDivision}")