# --- Importando ---

import random
from tkinter import *

# ---  Ventana Oceania ---

ventana_Oceania= Tk()
ventana_Oceania.title("4 PAISES 1 BANDERA")
ventana_Oceania.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
ventana_Oceania.resizable(0,0)
ventana_Oceania.configure(background="black")
ventana_Oceania.geometry("1200x650")
ventana_Oceania.geometry("+75+10")
ventana_Oceania.config(cursor="hand2")


lbl_Titulo = Label(ventana_Oceania, text="OCEANIA:", background="black", fg="white")
lbl_Titulo.place(x=10, y=10)


# --- Imagenes Aleatorias ---

imagenes = ["Proyecto Videojuego Py\imagenes\Banderas\Oceania\Australia.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Fiyi.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Islas-Marshall.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Islas-Solomon.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Kiribati.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Micronesia.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Nauru.png","Proyecto Videojuego Py\imagenes\Banderas\Oceania\Nueva-Zelanda.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Palaos.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Papua-Nueva-Guinea.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Samoa.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Tonga.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Tuvalu.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Vanuatu.png"]
bandera = random.choice(imagenes)
foto=PhotoImage(file=bandera)
lbl_Bandera = Label(ventana_Oceania, image=foto)
lbl_Bandera.place(x=480, y=100)

# --- Textp de los Botones Aleatorio ---

paises = ["Australia", "Fiyi", "Islas Marshall", "Islas Solomon", "Kiribati", "Micronesia", "Nauru", "Nueva Zealanda", "Palaos", "Papua Nueva Guinea", "Samoa", "Tonga", "Tuvalu", "Vanuatu"]

texto = random.choice(paises)
btn_Opcion1 = Button(ventana_Oceania, text=texto, width=35, height=10)
btn_Opcion1.place(x=30, y=450)

texto = random.choice(paises)
btn_Opcion2 = Button(ventana_Oceania, text=texto, width=35, height=10)
btn_Opcion2.place(x=320, y=450)

texto = random.choice(paises)
btn_Opcion3 = Button(ventana_Oceania, text=texto, width=35, height=10)
btn_Opcion3.place(x=610, y=450)
texto = random.choice(paises)
btn_Opcion4 = Button(ventana_Oceania, text=texto, width=35, height=10)
btn_Opcion4.place(x=900, y=450)
ventana_Oceania.mainloop()