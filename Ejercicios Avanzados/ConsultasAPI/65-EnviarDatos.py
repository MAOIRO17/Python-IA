import requests

url = "https://jsonplaceholder.typicode.com/posts"
nuevoPost= {"title": "Nuevo Título", "body": "Contenido del nuevo post", "userId": 1}
response = requests.post(url, json=nuevoPost)
print(f"Estado de la respuesta: {response.status_code}")
print(f"Respuesta del servidor: {response.json()}")