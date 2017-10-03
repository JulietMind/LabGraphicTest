#!/user/bin/python
import sys
from tkinter import *


app = Tk()
app.title("JulietMind")

# VP -> ventana principal
vp = Frame(app)
vp.grid()
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0,weight=1)


etiqueta = Label(vp,text="Escribe algo:")
etiqueta.grid(column=2,row=2)

boton = Button(vp,text="Aceptar")
boton.grid(column=1,row=1)

valor = ""
entrada_txt = Entry(vp, width=10, textvariable=valor)
entrada_txt.grid(column=2,row=1)

app.mainloop()