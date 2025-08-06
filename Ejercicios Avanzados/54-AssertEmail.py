def registrar_usuario(nombre, email):
    assert "@" in email, "El email debe contener un '@'."
    return{
        "nombre": nombre,
        "email": email
    }
try:
        usuario = registrar_usuario("Juan", "juan@gmail.com")
except AssertionError as e:
    print(f"Error: {e}")
else:
    print(f"Usuario registrado: {usuario}")