import random
import time
while True:
 jugador = input("rock, paper or scissors?  ").lower()
 maquina = random.randint(0,2)
 posibilidades = [ "rock","paper","scissors"]
 pe = posibilidades[maquina]
 print("the machine chose...")
 print(pe) 
 time.sleep(1)
 if jugador == "rock" and pe == "paper" or jugador == "paper" and pe == "scissors" or jugador == "scissors" and pe == "rock":
    print("player loses")
 elif jugador == "rock" and pe == "scissors" or jugador == "scissors" and pe == "paper" or jugador == "paper" and pe == "rock":
    print("player wins")
 elif jugador == pe:
    print("draw")

 else:
    print("por favor elige una opcion valida") 
 salir = input("enter to continue or type s to exit").lower()
 if salir == "s":
    break
    
