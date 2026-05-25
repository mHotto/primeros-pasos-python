import requests
while True:
    opcion = input("1. search pokemon" "\n" "2. Exit" "\n")
    if opcion == "2":
        break
    elif opcion == "1":
        peli=input("which poke?" "\n").lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{peli}"
        respuesta = requests.get(url)
        datospeli = respuesta.json()
        peso = datospeli['weight']
        nombre = datospeli['name']
       
        print("name:", nombre, "\n" "weight:",peso)