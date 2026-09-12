import requests

url="https://jsonplaceholder.typicode.com/users"

respuesta = requests.get(url)

datos = respuesta.json()

for usuario in datos:
    print(usuario["name"])
    print(usuario["email"])
    print("================")