# --- Importando ---

from tkinter import *
from tkinter import messagebox
#import Jugo_Pruebas2

# --- Funciones ---



# --- Ventana_Menu Menu (Seleccion te continentes) ---

Ventana_Menu = Tk()
Ventana_Menu.title("4 PAISES 1 BANDERA")
Ventana_Menu.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
Ventana_Menu.resizable(0,0)
Ventana_Menu.configure(background="black")
Ventana_Menu.geometry("1200x800")
Ventana_Menu.geometry("+30+70")
Ventana_Menu.config(cursor="hand2")

Selec_Con = LabelFrame(Ventana_Menu, text="SELECCIONA UN CONTINENTE", width=1160, height=760, background="black", fg="white", font=("Verdana", 20))
Selec_Con.place(x=20, y=20)

# --- Final ---

Ventana_Menu.mainloop()