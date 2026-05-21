import tkinter as tkk
def suma():
    try:
     resultado = float(x.get()) + float(y.get())
     z.config(text=resultado)
    except ValueError: 
     z.config(text="Ingrese un numero valido")

calculadora = tkk.Tk()
calculadora.title("Calculadora")
calculadora.geometry("500x500")
calculadora.configure(bg="#000000")
calculadora.resizable(False, False)

x = tkk.Entry(calculadora)
x.pack(pady=20)

y = tkk.Entry(calculadora)
y.pack(pady=20)

sumar = tkk.Button(calculadora, text="sumar", width=20, height=5, command= suma)
sumar.pack(pady=20)
sumar.place(x=150, y=200)

z = tkk.Label(calculadora, width=20, height=10)
z.place(x=200, y=300)

tkk.mainloop()