import requests

url="https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
if response.status_code == 200:
    data= response.json()
    print(f"*Título:{data['title']}")
else:
    print(f"Error al realizar la solicitud: {response.status_code}")