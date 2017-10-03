#!/user/bin/python
import sys
from tkinter import *




# Functions
# def funcion():
# 	print("OH SI! Me Gusta!")


# Def variables
raiz = Tk()
etiqueta = Label(raiz, text="Hola mundo!")
boton = Button(raiz, text="Pulsame!")


# Executions

raiz.title("JulietMind")
etiqueta.pack()
boton.pack()
# mainloop() has to go at the end or the Executions doesn't work
raiz.mainloop()