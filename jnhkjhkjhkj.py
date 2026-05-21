import tkinter as tk
import time 
import random
colores = "blue","red","gray","black"
def color():
    pagina.configure(bg = random.choice(colores))
    
pagina=tk.Tk()
pagina.geometry("220x220")
boton=tk.Button()
boton.pack(pady=20)
boton.configure(text="cambiar color", command=color)
pagina.mainloop()
