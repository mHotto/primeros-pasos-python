import tkinter as tk
import time
def xx():
   ventana.destroy()
   time.sleep(0.5)
   ventana3 = tk.Tk()
   ventana3.geometry("350x350")
   bienvenido=tk.Label(ventana3, text="bienvenido a tu cuenta :)")
   bienvenido.pack(pady=20)
   

e = False

while e == False:  
  a = int(input("primer numero: "))
  b = int(input("segundo numero: "))
  c = int(input("tercer numero: "))
  d = int(input("cuarto numero: "))
  if a == 1 and b == 9 and c == 0 and d == 3:
   e = True
   ventana = tk.Tk()
   ventana.geometry("200x200")
   texto = tk.Label(ventana, text="Contraseña correcta")
   texto.pack(pady=20)
   textitocorrecto = tk.Button(ventana, text="nice", command=xx) 
   textitocorrecto.pack(pady=20)
   ventana.mainloop()
  else:
    print("contraseña incorrecta, intentalo de nuevo")
    ventana2 = tk.Tk()
    botondeerror=tk.Button(ventana2, text="reintentar", command=ventana2.destroy)
    botondeerror.pack(pady=20)
    ventana2.mainloop()