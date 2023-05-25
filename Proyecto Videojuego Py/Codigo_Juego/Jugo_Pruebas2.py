# El MAMALON PERRON CHINGON

# --- Importando --- 

from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import random

# --- Funciones ---

def Oceania():
    ventana_Oceania = Toplevel()
    ventana_Oceania.title("4 PAISES 1 BANDERA")
    ventana_Oceania.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_Oceania.resizable(0,0)
    ventana_Oceania.configure(background="white")
    ventana_Oceania.geometry("1200x650")
    ventana_Oceania.geometry("+75+10")
    ventana_Oceania.config(cursor="hand2")


    lbl_Titulo = Label(ventana_Oceania, text="OCEANIA:", background="white", fg="black")
    lbl_Titulo.place(x=10, y=10)


    # --- Imagenes Aleatorias ---

    imagenes = ["Proyecto Videojuego Py\imagenes\Banderas\Oceania\Australia.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Fiyi.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Islas-Marshall.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Islas-Solomon.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Kiribati.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Micronesia.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\BNauru.png","Proyecto Videojuego Py\imagenes\Banderas\Oceania\BNueva-Zelanda.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Palaos.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Papua-Nueva-Guinea.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Samoa.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Tonga.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Tuvalu.png", "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Vanuatu.png"]
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

def Africa():
    ventana_Africa= Toplevel()
    ventana_Africa.title("4 PAISES 1 BANDERA")
    ventana_Africa.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_Africa.resizable(0,0)
    ventana_Africa.configure(background="white")
    ventana_Africa.geometry("1200x650")
    ventana_Africa.geometry("+75+10")
    ventana_Africa.config(cursor="hand2")


    lbl_Titulo = Label(ventana_Africa, text="IMAGENES ALEATORIAS:", background="white", fg="black")
    lbl_Titulo.place(x=10, y=10)


    #Abraham: Para imagenes aleatorias
    imagenes = ["Proyecto videojuego Py/imagenes/Banderas/Africa/Angola-Bandera-Africa.png", "Proyecto videojuego Py/imagenes/Banderas/Africa/Argelia-Bandera-Africa.png", "Proyecto videojuego Py/imagenes/Banderas/Africa/Benin-Bandera-Africa.png", "Proyecto videojuego Py/imagenes/Banderas/Africa/Botsuana-Bandera-Africa.png", "Proyecto videojuego Py/imagenes/Banderas/Africa/Burkina-Faso-Bandera-Africa.png"]
    bandera = random.choice(imagenes)
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_Africa, image=foto)
    lbl_Bandera.place(x=480, y=100)

    #Abraham: Texto de los botones aleatorio
    paises = ["Angola", "Argelia", "Benin", "Botsuana", "Burkina Faso"]
    texto = random.choice(paises)
    btn_Opcion1 = Button(ventana_Africa, text=texto, width=35, height=10)
    btn_Opcion1.place(x=30, y=450)

    texto = random.choice(paises)
    btn_Opcion2 = Button(ventana_Africa, text=texto, width=35, height=10)
    btn_Opcion2.place(x=320, y=450)

    texto = random.choice(paises)
    btn_Opcion3 = Button(ventana_Africa, text=texto, width=35, height=10)
    btn_Opcion3.place(x=610, y=450)

    texto = random.choice(paises)
    btn_Opcion4 = Button(ventana_Africa, text=texto, width=35, height=10)
    btn_Opcion4.place(x=900, y=450)

    # --- Fin ---

    ventana_Africa.mainloop()

def Records():
    print("")
    import webbrowser
    webbrowser.open("https://github.com/JosueAripez/Proyecto_Videojuego_Py")
    
def Salir():
    respuesta = messagebox.askquestion("4 Paises 1 Bandera", "¿Estas seguro que deseas salir?")
    if respuesta == "yes":
        Ventana_Principal.destroy()

# --- Ventana_ Menu Menu (Seleccion de Continente) ---

def Abrir_Ventana_Menu():
    
    def Volver():
        Ventana_Menu.destroy()
    
    Ventana_Menu = Toplevel()
    Ventana_Menu.title("4 PAISES 1 BANDERA")
    Ventana_Menu.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    Ventana_Menu.resizable(0,0)
    #Ventana_Menu.configure(background="black")
    Ventana_Menu.geometry("1200x650")
    Ventana_Menu.geometry("+75+10")
    Ventana_Menu.config(cursor="hand2")

    imagen = PhotoImage(file="Proyecto Videojuego Py\imagenes\Fondo_Band.png")
    lbl_imagen = Label(Ventana_Menu, image=imagen)
    lbl_imagen.place(x=0,y=0)

    #Selec_Con = LabelFrame(Ventana_Menu, text="SELECCIONA UN CONTINENTE", width=1160, height=600, background="black", fg="white", font=("Verdana", 20))
    #Selec_Con.place(x=20, y=20)

    lbl_seleccion = Label(Ventana_Menu, text="SELECCIONA UN CONTINENTE:", fg="black", bg="yellow", font=("Verdana", 35),  borderwidth=5, relief="groove" )
    lbl_seleccion.place(x=75, y=30)

    Btn_Africa = Button(Ventana_Menu, text="AFRICA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command= Africa)
    Btn_Africa.place(x=42, y=110)
    
    Btn_America = Button(Ventana_Menu, text="AMERICA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command=Volver)
    Btn_America.place(x=42, y=210)
    
    Btn_Asia = Button(Ventana_Menu, text="ASIA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command=Volver)
    Btn_Asia.place(x=42, y=310)
    
    Btn_Europa = Button(Ventana_Menu, text="EUROPA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command=Volver)
    Btn_Europa.place(x=42, y=410)
    
    Btn_Oceania = Button(Ventana_Menu, text="OCEANIA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command=Oceania)
    Btn_Oceania.place(x=42, y=510)
    

    Btn_Volver = Button(Ventana_Menu, text="VOLVER", width=10, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10), command=Volver)
    Btn_Volver.place(x=1070, y=50) #x=530
    
    Ventana_Menu.mainloop()
    #Ventana_Menu.state(newstate = "normal")
    #Ventana_Principal.state(newstate = "withdraw")
    
# --- Ventana_Principal Principal (Inicio) ---

Ventana_Principal = Tk()
Ventana_Principal.title("4 PAISES 1 BANDERA")
Ventana_Principal.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
Ventana_Principal.resizable(0,0)
Ventana_Principal.geometry("1200x650") #650
Ventana_Principal.geometry("+75+10")
Ventana_Principal.config(cursor="hand2")

imagen = PhotoImage(file="Proyecto Videojuego Py\imagenes\Fondo_Band.png")
lbl_imagen = Label(Ventana_Principal, image=imagen)
lbl_imagen.place(x=0,y=0)




#Selec_Con = LabelFrame(Ventana_Principal, text="BIENVENIDO A", width=1054, height=175, background="black", fg="white", font=("Verdana", 20))
#Selec_Con.place(x=70, y=10)

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
