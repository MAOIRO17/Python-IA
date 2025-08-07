import requests

ApiKey = "ApiKey de tu API aquí"
url = "https://rest.coincap.io/v3/assets/bitcoin"
headers = {"Authorization": f"Bearer {ApiKey}"}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        precio = data['data']['priceUsd']
        print(f"El precio del Bitcoin es: ${float(precio):.2f} USD")
    else:
        print(f"Error al obtener datos: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error de conexión: {e}")