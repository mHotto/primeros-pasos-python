import time
import tkinter as tk
cancion=[
"dime baby como andas dime como vas",
"por aqui ha pasado de todo pero me da todo igual",
"un saludo pa tu amiga",
"un beso de mi mama",
"dice q fue d tu rosa",
"q una espina ta clava' "]
time.sleep(12)
contador=0
ventana = tk.Tk()
ventana.geometry("1000x200")
texto = tk.Label(text = cancion[contador], pady=20) 
texto.pack()
def cambio():
    global contador
    if contador < len(cancion):
     texto.configure(text=cancion[contador])
     contador+=1
     ventana.after(1700, cambio)
     if contador == 20:
      contador = 0
ventana.after(2800, cambio) 
ventana.mainloop()