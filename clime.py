import requests

while True:
    inicio=input("1. look clime. 2. exit""\n")
    if inicio == "2":
        break
    elif inicio == "1":
        ciudad = input("insert city: ")
        url = f"https://wttr.in/{ciudad}?format=j1"
        respuesta = requests.get(url)
        datosclima = respuesta.json()
        crn = datosclima['current_condition'][0]
        temperatura = crn['temp_C']
        humedad = crn['humidity']
        print(f"temp: {temperatura}°C\n humedity: {humedad} \n")
        