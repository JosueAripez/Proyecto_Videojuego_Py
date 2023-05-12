# --- Importando ---

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

# --- Ventana 1 (Inicio) ---

def ventana_inicio():
    global ventana_inicio
    ventana_inicio = Tk()
    
    ventana_inicio.iconbitmap('Proyecto Videojuego Py\imagenes\icono.ico')
    ventana_inicio.title('4 PAISES UNA BANDERA')
    ventana_inicio.geometry('1000x700') # Ancho x Alto
    ventana_inicio.resizable(0,0)
    
    Label(ventana_inicio, text="4 Paises Una Bandera", fg="medium blue", font=("Arial",50)).grid(pady=5, row=0, column=2) 

    Button(ventana_inicio, text="Comenzar", width=20, command= ventana_menu).grid(pady=10, padx=10, row=2, column=2, )#.place(relx=0.5, rely=0.5)
    
    ventana_inicio.mainloop()
    
def ventana_menu():
    global ventana_menu
    ventana_menu = Toplevel(ventana_inicio)
    ventana_menu.iconbitmap('Proyecto Videojuego Py\imagenes\icono.ico')
    ventana_menu.title('4 PAISES UNA BANDERA')
    ventana_menu.geometry('1000x700') # Ancho x Alto
    ventana_menu.resizable(0,0)
    
    Label(ventana_menu, text="Selecciona el Continente", fg="medium blue", font=("Arial",50)).grid(pady=5, row=0, column=2) 
    Button(ventana_menu, text="Volver al inicio", width=20, command=volver_inicio).grid(pady=10, padx=10, row=2, column=2, )#.place(relx=0.5, rely=0.5)
    
    if(ventana_menu):
        ventana_inicio.withdraw()
    
    ventana_menu.mainloop()
    
def volver_inicio():
    ventana_inicio.iconify()
    ventana_inicio.deiconify()
    ventana_menu.destroy()
    
ventana_inicio()
