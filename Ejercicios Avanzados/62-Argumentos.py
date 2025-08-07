import argparse

parser = argparse.ArgumentParser(description="Ejemplo de Argparse")
parser.add_argument("--nombre", type=str, help="Nombre del usuario")
parser.add_argument("--edad", type=int, help="Edad del usuario")
args = parser.parse_args()
print(f"Hola {args.nombre}, tienes {args.edad} años.")