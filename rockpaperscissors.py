import random
import time
jugador = input("rock, paper or scissors?  ").lower()
maquina = random.randint(0,2)
posibilidades = [ "rock","paper","scissors"]
pe = posibilidades[maquina]
print("the machine chose...")
print(pe) 
time.sleep(1)
if jugador == "rock" and pe == "paper":
    print("player loses")
elif jugador == "rock" and pe == "scissors":
    print("player wins")
elif jugador == "rock" and pe == "rock":
    print("draw")
elif jugador == "paper" and pe == "rock":
    print("player wins")
elif jugador == "paper" and pe == "paper":
    print("draw")
elif jugador == "paper" and pe == "scissors":
    print("player loses")
elif jugador == "scissors" and pe == "rock":
    print("player loses")
elif jugador == "scissors" and pe == "paper":
    print("player wins")
elif jugador == "scissors" and pe == "scissors":
    print("draw")
else:
    print("por favor elige una opcion valida")
