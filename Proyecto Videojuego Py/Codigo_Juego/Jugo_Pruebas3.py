# --- Importando --- 

from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import random

# --- Funciones ---

# --- Abrir 2 y Cerrar 1  ---

def Abrir_Ventana_Menu():
    Ventana_Menu.state(newstate = "normal")
    Ventana_Principal.state(newstate = "withdraw")
      
    # --- Menu (Seleccion de Continente) ---
    Ventana_Menu = Toplevel()
    Ventana_Menu.title("4 PAISES 1 BANDERA")
    Ventana_Menu.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    Ventana_Menu.state(newstate = "withdraw")
    Ventana_Menu.resizable(0,0)
    Ventana_Menu.geometry("1200x650")
    Ventana_Menu.geometry("+75+10")
    Ventana_Menu.config(cursor="hand2")
    imagen = PhotoImage(file="Proyecto Videojuego Py\imagenes\Fondo_Band.png")
    lbl_imagen = Label(Ventana_Menu, image=imagen)
    lbl_imagen.place(x=0,y=0)
    lbl_seleccion = Label(Ventana_Menu, text="SELECCIONA UN CONTINENTE:", fg="black", bg="yellow", font=("Verdana", 35),  borderwidth=5, relief="groove" )
    lbl_seleccion.place(x=75, y=30)
    Btn_Africa = Button(Ventana_Menu, text="AFRICA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20))
    Btn_Africa.place(x=42, y=110)
    Btn_America = Button(Ventana_Menu, text="AMERICA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20))
    Btn_America.place(x=42, y=210)
    Btn_Asia = Button(Ventana_Menu, text="ASIA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20))
    Btn_Asia.place(x=42, y=310)
    Btn_Europa = Button(Ventana_Menu, text="EUROPA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20))
    Btn_Europa.place(x=42, y=410)
    Btn_Oceania = Button(Ventana_Menu, text="OCEANIA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20))
    Btn_Oceania.place(x=42, y=510)
    Btn_Volver = Button(Ventana_Menu, text="VOLVER", width=10, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10), command=Volver)
    Btn_Volver.place(x=1070, y=50)
    Ventana_Menu.mainloop()




# --- Cerrar 2 y Abrir 1 ---

def Volver():
    Ventana_Menu.state(newstate = "withdraw")
    Ventana_Principal.state(newstate = "normal") 

def Records():
    import webbrowser
    webbrowser.open("https://github.com/JosueAripez/Proyecto_Videojuego_Py")
    
def Salir():
    respuesta = messagebox.askquestion("4 Paises 1 Bandera", "¿Estas seguro que deseas salir?")
    if respuesta == "yes":
        Ventana_Principal.destroy()


# --- Principal (Inicio) ---

Ventana_Principal = Tk()
Ventana_Principal.title("4 PAISES 1 BANDERA")
Ventana_Principal.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
Ventana_Principal.state(newstate = "normal")
Ventana_Principal.resizable(0,0)
Ventana_Principal.geometry("1200x650")
Ventana_Principal.geometry("+75+10")
Ventana_Principal.config(cursor="hand2")
imagen = PhotoImage(file="Proyecto Videojuego Py\imagenes\Fondo_Band.png")
lbl_imagen = Label(Ventana_Principal, image=imagen)
lbl_imagen.place(x=0,y=0)
lbl_Titulo = Label(Ventana_Principal, text="4 Paises 1 Bandera", fg="black", bg="yellow", font=("Verdana", 80),  borderwidth=5, relief="groove")
lbl_Titulo.place(x=75, y=40)
Btn_Comenazar = Button(Ventana_Principal, text="COMENZAR", width=30, height=3, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10), command=Abrir_Ventana_Menu)
Btn_Comenazar.place(x=450, y=300)
Btn_Record = Button(Ventana_Principal, text="RECORDS", width=30, height=3, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10), command=Records)
Btn_Record.place(x=450, y=380)
Btn_Salir = Button(Ventana_Principal, text="SALIR", width=30, height=3, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10), command=Salir)
Btn_Salir.place(x=450, y=460)
lbl_Create = Label(Ventana_Principal, text="Propiedad Intelectual y Creativa de: Jose Abraham Beristain Navarro y Josue Franciso Rojas Aripez", fg="white", bg="black", font=("Verdana", 10),  borderwidth=5)
lbl_Create.place(x=5, y=620)

# --- Fin ---

Ventana_Principal.mainloop()
