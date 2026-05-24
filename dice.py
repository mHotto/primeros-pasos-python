import random
salario=100
caras = ["tails", "heads"]
print("money initial:", salario)
while salario>0:
 apuesta = int(input("how many want u bet?"))
 if (apuesta > salario):
  print("and the money?")
  continue
 tipo = input("dice or coin?").lower()
 if tipo == "dice":
  numero = input("pick a number (1,6)")
  moneda=random.randint(1,6)
  print(moneda)
  if (numero == moneda):
   salario= salario + apuesta*5
   print("nice, currect money:", salario)
  else:
   salario -= int(apuesta)
   print("u lose, current money:", salario) 
 elif tipo == "coin":
  numero = input("pick heads or tails: ")
  moneda=random.choice(caras)
  print("result: ", moneda)
  if (int(numero == moneda)):
   salario= salario + apuesta*2
   print("nice, currect money:", salario)
  else:
   salario -= int(apuesta)
   print("u lose, current money:", salario)
 elif salario<1:
  break 
  
   
  