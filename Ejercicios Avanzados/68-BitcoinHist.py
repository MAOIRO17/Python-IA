import requests
import time
import csv
from datetime import datetime
from pathlib import Path

ApiKey = "ApiKey de tu API aquí"
url = "https://rest.coincap.io/v3/assets/bitcoin"
headers = {"Authorization": f"Bearer {ApiKey}"}

archivo = Path("BitcoinHist.csv")
if not archivo.exists():
    with archivo.open("w", newline='',encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Fecha", "Precio USD"])
try:
    while True:
        try:
            response = requests.get(url,timeout=10, headers=headers)
            if response.status_code == 200:
                data = response.json()
                precio = float(data["data"]["priceUsd"])
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with archivo.open("a", newline='', encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([fecha, precio])
                print(f"{fecha} - Precio: ${precio:.2f} USD")
            else:
                print(f"Error al obtener datos: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión: {e}")
        time.sleep(10)  # Espera 10 segundos antes de la siguiente consulta
except KeyboardInterrupt:
            print("\nDeteniendo la recopilación de datos.")
            