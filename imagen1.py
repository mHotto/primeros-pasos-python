
import tkinter as tk
from PIL import Image, ImageTk


programa = tk.Tk()

ubicacion = r"c:\Users\Manu\Downloads\lenalena.jpg"


foto_original = Image.open(ubicacion)
foto_lista = ImageTk.PhotoImage(foto_original)

cuadro = tk.Label(programa, image=foto_lista)
cuadro.pack()

programa.mainloop()