import random
palabritas = ["guitarra", "viento", "espejo", "manzana", "planeta", "cuaderno", "trueno", "camino", "silencio", "oceano"]
contador = 0
palabra = palabritas[random.randint(0,9)]
while contador < 6:
 jugador = input("type ur word: ").lower()
 if jugador == palabra:
  print("u won")
  break
 if not jugador == palabra:
   letrascomunes = set(jugador) & set(palabra)
   if letrascomunes:
    print("the word have this letters:", letrascomunes)
   else:
    print("no matching")

 contador += 1
 print("try number:",contador,"/6" )
 
 if contador == 6:
  print("u lose haha")

 
