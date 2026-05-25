import requests
url = "https://open.er-api.com/v6/latest/USD"

while True:
 print("1. converse" "\n" "2. exit" "\n")
 opcion = input("choose: ")
    
 if opcion == "2":
        print("bye")
        break
 elif opcion == "1":
        dinero = float(input("how many money u want convert?"))
        coin = (input("which coin? (EUR, LIB, etc.)""\n")).upper()
        respuesta = requests.get(url)
        datos_monedas = respuesta.json()
        precio_moneda = datos_monedas['rates'][coin]
        resultado = dinero * precio_moneda
        print(f"\n total: {resultado:.2f} {coin}\n")