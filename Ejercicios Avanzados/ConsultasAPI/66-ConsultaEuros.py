import time
import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"
while True:
    try:
        respuesta = requests.get(url)
        if respuesta.ok:
            euro=respuesta.json().get("rates", {}).get("EUR")
            print(f"1 USD = {euro} EUR")
    except requests.RequestException as e:
        print(f"Error HTTP: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
    time.sleep(3)  # Espera 3 seg para la siguiente consulta