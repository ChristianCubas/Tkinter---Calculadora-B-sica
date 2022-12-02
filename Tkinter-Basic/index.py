import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("My first program")

bienvenida = ttk.Label(ventana, text="Bienvenido a la calculadora", background="skyblue", foreground="white",font="sans-serif")
bienvenida.grid(row=0,column=0,sticky="NSWE")
valor = ttk.Label(ventana, text="Ingrese un valor")
valor.grid(row=1, column=0)
entrada = ttk.Entry(ventana)
entrada.grid(row=1, column=1)
valor2 = ttk.Label(ventana, text="Ingrese otro valor")
valor2.grid(row=2, column=0)
entrada1 = ttk.Entry(ventana)
entrada1.grid(row=2, column=1)


def sumar():
    print(int(entrada.get()) + int(entrada1.get()))


def restar():
    print(int(entrada.get()) - int(entrada1.get()))

def multiplicar():
    print(int(entrada.get()) * int(entrada1.get()))


def dividir():
    print(int(entrada.get()) / int(entrada1.get()))

operacion = ttk.Label(ventana, text="Seleccione la operación a realizar")
operacion.grid(row=3, column=0)
print("\n")
print("\n")
boton1 = ttk.Button(ventana, text="+", command=sumar)
boton1.grid(row=4, column=0, sticky="NSWE")
boton2 = ttk.Button(ventana, text="-", command=restar)
boton2.grid(row=4, column=1, sticky="NSWE")
boton3 = ttk.Button(ventana, text="x", command=multiplicar)
boton3.grid(row=4, column=2, sticky="NSWE")
boton4 = ttk.Button(ventana, text="÷", command=dividir)
boton4.grid(row=4, column=3, sticky="NSWE")

ventana.mainloop()