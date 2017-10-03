#!/user/bin/python
import sys
from tkinter import *




# Funciones
# def funcion():
# 	print("OH SI! Me Gusta!")


# Definir variables
raiz = Tk()
etiqueta = Label(raiz, text="Hola mundo!")
boton = Button(raiz, text="Pulsame!")


# Ejecuciones
raiz.title("JulietMind")
etiqueta.pack()
raiz.mainloop()

boton.pack()