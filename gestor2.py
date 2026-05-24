while True:
    opciones = input("1. Add contact" "\n" "2. See numbers" "\n" "3. Exit""\n")
    if opciones == "1":
        nombre = input("insert name of contact: ")
        numero = input("insert number of contact: ")
        with open("agenda.txt", "a") as agenda:
         agenda.write(nombre + "-" + numero + "\n")
    elif opciones == "2":
       with open("agenda.txt", "r") as agenda:
          mostrar = agenda.read()
          print(mostrar)
    elif opciones == "3":
       break
    else: 
       print("choose 1, 2 or 3")