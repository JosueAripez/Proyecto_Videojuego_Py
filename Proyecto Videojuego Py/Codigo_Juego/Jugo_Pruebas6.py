# El MAMALON PERRON CHINGON

# --- Importando --- 

from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import random

# --- Funciones ---
def Africa():
    ventana_Africa= Toplevel()
    ventana_Africa.title("4 PAISES 1 BANDERA")
    ventana_Africa.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_Africa.resizable(0,0)
    ventana_Africa.configure(background="white")
    ventana_Africa.geometry("1200x650")
    ventana_Africa.geometry("+75+10")
    ventana_Africa.config(cursor="hand2")


    lbl_Titulo = Label(ventana_Africa, text="AFRICA:", background="white", fg="black")
    lbl_Titulo.place(x=10, y=10)

    #Abraham: Para imagenes aleatorias
    num = random.sample(range(1,56),4)

    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Africa\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_Africa, image=foto)
    lbl_Bandera.place(x=480, y=100)

    #Abraham: Texto de los botones aleatorio
    paises = ["Angola", "Argelia", "Benin", "Botsuana", "Burkina Faso", "Burundi", "Cabo Verde", "Camerun", "Chad", "Comoras", "Costa de Marfil", "Egipto", "Eritrea", "Etiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea Bisau", "Guinea Ecuatorial", "Kenia", "Lesoto", "Liberia", "Libia", "Madagascar", "Malaui", "Mali", "Marruecos", "Mauricio", "Mauritania", "Mozambique", "Naminia", "Niger", "Nigeria", "Republica Centroafricana", "Rpublica del Congo", "Republica Democratica del combo", "Ruanda", "Sahara", "Santo Tome y Principe", "Senegal", "Seychelles", "Sierra Leona", "Somalia", "Somalilandia", "Sauzilandia", "Sudafrica", "Sudan", "Sudan del Sur", "Tanzania", "Togo", "Tunez", "Uganda", "Yibuti", "Zambia", "Zimbaue"]
    
    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]-1]
    btn_Opcion1 = Button(ventana_Africa, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion1, 1))
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]-1]
    btn_Opcion2 = Button(ventana_Africa, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion2, 2))
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]-1]
    btn_Opcion3 = Button(ventana_Africa, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion3, 3))
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]-1]
    btn_Opcion4 = Button(ventana_Africa, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion4, 4))
    btn_Opcion4.place(x=pos[posx[3]], y=450)

    ventana_Africa.mainloop()


def America():
    ventana_America = Toplevel()
    ventana_America.title("4 PAISES 1 BANDERA")
    ventana_America.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_America.resizable(0,0)
    ventana_America.configure(background="white")
    ventana_America.geometry("1200x650")
    ventana_America.geometry("+75+10")
    ventana_America.config(cursor="hand2")

    lbl_Titulo = Label(ventana_America, text="AMERICA:", background="white", fg="black")
    lbl_Titulo.place(x=10, y=10)

    # --- Imagenes Aleatorias ---
    num = random.sample(range(1,36),4)

    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\America\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_America, image=foto)
    lbl_Bandera.place(x=480, y=100)

    # --- Texto de los Botones Aleatorio ---
    paises = ["Antigua y Barbuba", "Argentina", "Bahamas", "Barbados", "Belice", "Bolivia", "Brasil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominica", "Ecuador", "EEUU", "El Salvador", "Granada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Republica Dominicana", "San Cristobal y Nieves", "San Vicente y las Granadinas", "Snata Lucia", "Surinam", "Trinidad y Tobago", "Uruguay", "Venezuela"]

    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]-1]
    btn_Opcion1 = Button(ventana_America, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion1, 1))
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]-1]
    btn_Opcion2 = Button(ventana_America, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion2, 2))
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]-1]
    btn_Opcion3 = Button(ventana_America, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion3, 3))
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]-1]
    btn_Opcion4 = Button(ventana_America, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion4, 4))
    btn_Opcion4.place(x=pos[posx[3]], y=450)
    
    ventana_America.mainloop()


def Asia():
    ventana_Asia = Toplevel()
    ventana_Asia.title("4 PAISES 1 BANDERA")
    ventana_Asia.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_Asia.resizable(0,0)
    ventana_Asia.configure(background="white")
    ventana_Asia.geometry("1200x650")
    ventana_Asia.geometry("+75+10")
    ventana_Asia.config(cursor="hand2")

    lbl_Titulo = Label(ventana_Asia, text="ASIA:", background="white", fg="black")
    lbl_Titulo.place(x=10, y=10)

    # --- Imagenes Aleatorias ---
    num = random.sample(range(1,44),4)

    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Asia\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_Asia, image=foto)
    lbl_Bandera.place(x=480, y=100)

    # --- Texto de los Botones Aleatorio ---
    paises = ["Afganistan", "Arabia Saudita", "Banglades", "Barein", "Birmania", "Brunei", "Butan", "Camboya", "Catar", "China", "Corea del Norte", "Corea del Sur", "Emiratos Arabes Unidos", "Filipinas", "India", "Indonesia", "Irak", "Iran", "Israel", "Japon", "Jordania", "Kazajistan", "Kuwait", "Laos", "Libano", "Malasia", "Maldivas", "Mongolia", "Nepal", "Oman", "Pakistan", "Palestina", "Singapur", "Siria", "Sri Lanka", "Tailandia", "Taiwan", "Tayikistan", "Timor Oriental", "Turkmenistan", "Turquia", "Uzbekistain", "Vietnam", "Yemen"]

    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]-1]
    btn_Opcion1 = Button(ventana_Asia, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion1, 1))
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]-1]
    btn_Opcion2 = Button(ventana_Asia, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion2, 2))
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]-1]
    btn_Opcion3 = Button(ventana_Asia, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion3, 3))
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]-1]
    btn_Opcion4 = Button(ventana_Asia, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion4, 4))
    btn_Opcion4.place(x=pos[posx[3]], y=450)
    
    ventana_Asia.mainloop()


def Europa():
    ventana_Europa = Toplevel()
    ventana_Europa.title("4 PAISES 1 BANDERA")
    ventana_Europa.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_Europa.resizable(0,0)
    ventana_Europa.configure(background="white")
    ventana_Europa.geometry("1200x650")
    ventana_Europa.geometry("+75+10")
    ventana_Europa.config(cursor="hand2")

    lbl_Titulo = Label(ventana_Europa, text="EUROPA:", background="white", fg="black")
    lbl_Titulo.place(x=10, y=10)

    # --- Imagenes Aleatorias ---
    num = random.sample(range(1,48),4)

    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Europa\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_Europa, image=foto)
    lbl_Bandera.place(x=480, y=100)

    # --- Texto de los Botones Aleatorio ---
    paises = ["Albania", "Alemania", "Andorra", "Armenia", "Austria", "Azerbaiyan", "Belgica", "Bielorrusia", "Bosnia y Herzegovina", "Bulgaria", "Chipre", "Croacia", "Dinamarca", "Eslovaquia", "Eslovenia", "España", "Estonia", "Filandia", "Francia", "Georgia", "Grecia", "Hungria", "Irlanda", "Islandia", "Italia", "Letonia", "Liechtenstein", "Litunia", "Luxemburgo", "Macedonia del Norte", "Malta", "Moldavia", "Monaco", "Montenegro", "Noruega", "Paises Bajos", "Polonia", "Portugal", "Reino Unido", "Republica Checa", "Rumania", "Rusia", "San Marino", "Serbia", "Suecia", "Suiza", "Ucrania", "Vaticano"]

    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]-1]
    btn_Opcion1 = Button(ventana_Europa, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion1, 1))
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]-1]
    btn_Opcion2 = Button(ventana_Europa, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion2, 2))
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]-1]
    btn_Opcion3 = Button(ventana_Europa, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion3, 3))
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]-1]
    btn_Opcion4 = Button(ventana_Europa, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion4, 4))
    btn_Opcion4.place(x=pos[posx[3]], y=450)
    
    ventana_Europa.mainloop()


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
    num = random.sample(range(1,14),4)

    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Oceania\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_Oceania, image=foto)
    lbl_Bandera.place(x=480, y=100)

    # --- Texto de los Botones Aleatorio ---
    paises = ["Australia", "Nauru", "Nueva Zelanda", "Fiyi", "Islas Marshall", "Islas Salomon", "Kiribati", "Micronesia", "Palaos", "Papua Nueva Guinea", "Samoa", "Tonga", "Tuvalu", "Vanuatu"]

    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]-1]
    btn_Opcion1 = Button(ventana_Oceania, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion1, 1))
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]-1]
    btn_Opcion2 = Button(ventana_Oceania, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion2, 2))
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]-1]
    btn_Opcion3 = Button(ventana_Oceania, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion3, 3))
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]-1]
    btn_Opcion4 = Button(ventana_Oceania, text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion4, 4))
    btn_Opcion4.place(x=pos[posx[3]], y=450)
    
    ventana_Oceania.mainloop()


def respuesta(boton, op):
    if op == 1:
        boton.config(bg="green")
    elif op == 2:
        boton.config(bg="red")
    elif op == 3:
        boton.config(bg="red")
    elif op == 4:
        boton.config(bg="red")


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
    
    Btn_America = Button(Ventana_Menu, text="AMERICA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command=America)
    Btn_America.place(x=42, y=210)
    
    Btn_Asia = Button(Ventana_Menu, text="ASIA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command=Asia)
    Btn_Asia.place(x=42, y=310)
    
    Btn_Europa = Button(Ventana_Menu, text="EUROPA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command=Europa)
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
