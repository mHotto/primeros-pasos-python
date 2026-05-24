while True:
 opciones = input("1. Add" "\n" "2. Read" "\n" "3. Stop" "\n")
 if opciones == "1":
  with open("textito.txt", "a") as arch:
   newtarea = input("type new task: ")
   arch.write(newtarea + "\n")
 elif opciones == "3":
  print("get out")
  break
 elif opciones == "2":
   with open("textito.txt", "r") as arch:
    cosas = arch.read()
    print(cosas)
 else:
  print("pls type 1, 2 or 3")
