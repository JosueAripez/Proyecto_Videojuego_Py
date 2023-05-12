# --- Importando ---

import tkinter as tk
from tkinter import *
#from PIL import ImageTk, Image

# --- Ventana ---

ventana = tk.Tk()
ventana.title("4 PAISES UNA BANDERA")
ventana.geometry('1000x700') # Ancho x Alto
ventana.resizable(0,0)
ventana.iconbitmap('Proyecto Videojuego Py\imagenes\icono.ico')


# --- Probando Fondo --- 
"""
#1
fondo = PhotoImage(file = 'Proyecto Videojuego Py\imagenes\fondo_banderas.pgm')
lbl_fondo = Label(ventana, image = fondo)

#2
fondo = ImageTk.PhotoImage(Image.open('Proyecto Videojuego Py\imagenes\fondo_banderas.jpg'))
lbl_fondo = Label(fondo = Image)
lbl_fondo.pack()

"""
# --- Label (Texto en Pantalla) ---

Label(ventana, text="4 Paises Una Bandera", fg="medium blue", font=("Arial",50)).grid(pady=5, row=0, column=2, sticky=CENTER) 

# --- Boton Comenzar ---

#btn = tk.inter 




ventana.mainloop()
