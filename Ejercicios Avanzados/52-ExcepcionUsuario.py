class UsuarioExistenteError(Exception):
    pass
usuarios_registrados = ["usuario1", "usuario2", "usuario3"]
def registrar_usuario(usuario):
    if usuario in usuarios_registrados:
        raise UsuarioExistenteError(f"El usuario '{usuario}' ya está registrado")
    usuarios_registrados.append(usuario)
    return f"Usuario '{usuario}' registrado con éxito"
try:
    registrar_usuario("usuario1")
except UsuarioExistenteError as e:
    print(e)
finally:
    print (f"Usuarios registrados: {usuarios_registrados}")
    print("Fin del proceso de registro")

    