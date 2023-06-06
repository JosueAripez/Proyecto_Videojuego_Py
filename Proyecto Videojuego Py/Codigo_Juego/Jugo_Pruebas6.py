# El MAMALON PERRON CHINGON

# --- Importando --- 

from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import random
import time 
import pygame

# --- Funciones ---

pygame.mixer.init()
#Son_Click = pygame.mixer.Sound("Proyecto Videojuego Py\Musica\Click.ogg")

def respuesta(boton, op, cont):
    continente = [Africa, America, Asia, Europa, Oceania]

    if op == 1:
        #Son_Click.play()
        boton.config(bg="green")
        time.sleep(0.2)
        #ventana.after(1000)
        #continente[cont]().withdraw()
        continente[cont]()
        
    else:
        #Son_Click.play()
        boton.config(bg="red")
        
"""     vidas = vidas -1
        if vidas > 0:
            boton.config(bg="red")
        else:
            print("")
            #aqui tiene que imprimir la pantalla de cuando pierde
"""

def Records():
    #Son_Click.play()
    import webbrowser
    webbrowser.open("https://github.com/JosueAripez/Proyecto_Videojuego_Py")
    
def Salir():
    #Son_Click.play()
    respuesta = messagebox.askquestion("4 Paises 1 Bandera", "¿Estas seguro que deseas salir?")
    if respuesta == "yes":
        #Son_Click.play()
        Ventana_Principal.destroy()
        
# --- Continentes Funciones ----

def Africa():
    #Son_Click.play()
    ventana_Africa= Toplevel()
    ventana_Africa.title("4 PAISES 1 BANDERA")
    ventana_Africa.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_Africa.resizable(0,0)
    ventana_Africa.configure(background="white")
    ventana_Africa.geometry("1200x650+75+10")

    lbl_Titulo = Label(ventana_Africa, text="AFRICA:", background="white", fg="black")
    lbl_Titulo.place(x=10, y=10)

    # --- Imagenes Aleatorias ---
    
    num = random.sample(range(1,56),4)

    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Africa\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_Africa, image=foto)
    lbl_Bandera.place(x=480, y=100)

    # --- Contadores ---
    vidas = 3
    puntos = 0
    lbl_vidas = Label(ventana_Africa, text=f"Vidas: {vidas}", bg="white", font=("Arial Black", 24))
    lbl_vidas.place(x=900, y=10)
    
    lbl_puntaje = Label(ventana_Africa, text=f"Puntaje: {puntos}", bg="white", font=("Arial Black", 24))
    lbl_puntaje.place(x=900, y=60)

    def contador_puntos():
        nonlocal puntos
        puntos += 1
        lbl_puntaje.config(text=f"Puntaje: {puntos}")
        btn_Opcion1.config(bg="green")
        #time.sleep(0.2)

        # --- configurar bandera ---
        num = random.sample(range(1,56),4)
        bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Africa\\band{num[0]}.png"
        foto=PhotoImage(file=bandera)
        lbl_Bandera.config(image=foto)

        # --- configurar botones ---
        paises = ["Relleno", "Angola", "Argelia", "Benin", "Botsuana", "Burkina Faso", "Burundi", "Cabo Verde", "Camerun", "Chad", "Comoras", "Costa de Marfil", "Egipto", "Eritrea", "Etiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea Bisau", "Guinea Ecuatorial", "Kenia", "Lesoto", "Liberia", "Libia", "Madagascar", "Malaui", "Mali", "Marruecos", "Mauricio", "Mauritania", "Mozambique", "Naminia", "Niger", "Nigeria", "Republica Centroafricana", "Rpublica del Congo", "Republica Democratica del combo", "Ruanda", "Sahara", "Santo Tome y Principe", "Senegal", "Seychelles", "Sierra Leona", "Somalia", "Somalilandia", "Sauzilandia", "Sudafrica", "Sudan", "Sudan del Sur", "Tanzania", "Togo", "Tunez", "Uganda", "Yibuti", "Zambia", "Zimbaue"]
        pos = [30, 320, 610, 900]
        posx = random.sample(range(0,4), 4)
        
        texto = paises[num[0]]
        btn_Opcion1.config(bg="white", text=texto)
        btn_Opcion1.config.place(x=pos[posx[0]], y=450)

        texto = paises[num[1]]
        btn_Opcion2.config(bg="white", text=texto)
        #btn_Opcion2.place(x=pos[posx[0]], y=450)

        texto = paises[num[2]]
        btn_Opcion3.config(bg="white", text=texto)
        #btn_Opcion3.place(x=pos[posx[0]], y=450)

        texto = paises[num[3]]
        btn_Opcion4.config(bg="white", text=texto)
        #btn_Opcion4.place(x=pos[posx[0]], y=450)



    def contador_vidas(op):
        nonlocal vidas
        vidas -= 1
        lbl_vidas.config(text=f"Vidas: {vidas}")
        if op == 2:
            btn_Opcion2.config(bg="red")
        elif op == 3:
            btn_Opcion3.config(bg="red")
        else:
            btn_Opcion4.config(bg="red")


    # --- Texto de los botones aleatortios ---
    
    paises = ["Relleno", "Angola", "Argelia", "Benin", "Botsuana", "Burkina Faso", "Burundi", "Cabo Verde", "Camerun", "Chad", "Comoras", "Costa de Marfil", "Egipto", "Eritrea", "Etiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea Bisau", "Guinea Ecuatorial", "Kenia", "Lesoto", "Liberia", "Libia", "Madagascar", "Malaui", "Mali", "Marruecos", "Mauricio", "Mauritania", "Mozambique", "Naminia", "Niger", "Nigeria", "Republica Centroafricana", "Rpublica del Congo", "Republica Democratica del combo", "Ruanda", "Sahara", "Santo Tome y Principe", "Senegal", "Seychelles", "Sierra Leona", "Somalia", "Somalilandia", "Sauzilandia", "Sudafrica", "Sudan", "Sudan del Sur", "Tanzania", "Togo", "Tunez", "Uganda", "Yibuti", "Zambia", "Zimbaue"]
    
    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]]
    btn_Opcion1 = Button(ventana_Africa, cursor="hand2", text=texto, width=35, height=10, command= contador_puntos)
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]]
    print(texto)
    btn_Opcion2 = Button(ventana_Africa, cursor="hand2",  text=texto, width=35, height=10, command=lambda: contador_vidas(2))#lambda: respuesta(btn_Opcion2, 2, 0)
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]]
    btn_Opcion3 = Button(ventana_Africa, cursor="hand2",  text=texto, width=35, height=10, command=lambda: contador_vidas(3))#lambda: respuesta(btn_Opcion3, 3, 0)
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]]
    btn_Opcion4 = Button(ventana_Africa, cursor="hand2",  text=texto, width=35, height=10, command=lambda: contador_vidas(4))#lambda: respuesta(btn_Opcion4, 4, 0)
    btn_Opcion4.place(x=pos[posx[3]], y=450)

    if btn_Opcion1 == 0:
        print(vidas)

    ventana_Africa.mainloop()


def America():
    #Son_Click.play()
    ventana_America = Toplevel()
    ventana_America.title("4 PAISES 1 BANDERA")
    ventana_America.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_America.resizable(0,0)
    ventana_America.configure(background="white")
    ventana_America.geometry("1200x650+75+10")

    lbl_Titulo = Label(ventana_America, text="AMERICA:", background="white", fg="black")
    lbl_Titulo.place(x=10, y=10)

    # --- Imagenes Aleatorias ---
    
    num = random.sample(range(1,36),4)

    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\America\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_America, image=foto)
    lbl_Bandera.place(x=480, y=100)

    # --- Contadores ---
    vidas = 3
    lbl_vidas = Label(ventana_America, text=f"Vidas: {vidas}", bg="white", font=("Arial Black", 24))
    lbl_vidas.place(x=900, y=10)
    Puntos = 0
    lbl_puntaje = Label(ventana_America, text=f"Puntaje: {Puntos}", bg="white", font=("Arial Black", 24))
    lbl_puntaje.place(x=900, y=60)

    # --- Texto de los Botones Aleatorio ---
    
    paises = ["Relleno", "Antigua y Barbuba", "Argentina", "Bahamas", "Barbados", "Belice", "Bolivia", "Brasil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominica", "Ecuador", "EEUU", "El Salvador", "Granada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Republica Dominicana", "San Cristobal y Nieves", "San Vicente y las Granadinas", "Sanata Lucia", "Surinam", "Trinidad y Tobago", "Uruguay", "Venezuela"]

    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]]
    btn_Opcion1 = Button(ventana_America, cursor="hand2",  text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion1, 1, 1))
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]]
    btn_Opcion2 = Button(ventana_America, cursor="hand2",  text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion2, 2, 1))
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]]
    btn_Opcion3 = Button(ventana_America, cursor="hand2", text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion3, 3, 1))
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]]
    btn_Opcion4 = Button(ventana_America, cursor="hand2", text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion4, 4, 1))
    btn_Opcion4.place(x=pos[posx[3]], y=450)
    
    ventana_America.mainloop()


def Asia():
    #Son_Click.play()
    ventana_Asia = Toplevel()
    ventana_Asia.title("4 PAISES 1 BANDERA")
    ventana_Asia.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_Asia.resizable(0,0)
    ventana_Asia.configure(background="white")
    ventana_Asia.geometry("1200x650+75+10")
    lbl_Titulo = Label(ventana_Asia, text="ASIA:", background="white", fg="black")
    lbl_Titulo.place(x=10, y=10)

    # --- Imagenes Aleatorias ---
    
    num = random.sample(range(1,44),4)

    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Asia\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_Asia, image=foto)
    lbl_Bandera.place(x=480, y=100)

    # --- Contadores ---
    vidas = 3
    lbl_vidas = Label(ventana_Asia, text=f"Vidas: {vidas}", bg="white", font=("Arial Black", 24))
    lbl_vidas.place(x=900, y=10)
    Puntos = 0
    lbl_puntaje = Label(ventana_Asia, text=f"Puntaje: {Puntos}", bg="white", font=("Arial Black", 24))
    lbl_puntaje.place(x=900, y=60)

    # --- Texto de los Botones Aleatorio ---
    
    paises = ["Relleno", "Afganistan", "Arabia Saudita", "Banglades", "Barein", "Birmania", "Brunei", "Butan", "Camboya", "Catar", "China", "Corea del Norte", "Corea del Sur", "Emiratos Arabes Unidos", "Filipinas", "India", "Indonesia", "Irak", "Iran", "Israel", "Japon", "Jordania", "Kazajistan", "Kuwait", "Laos", "Libano", "Malasia", "Maldivas", "Mongolia", "Nepal", "Oman", "Pakistan", "Palestina", "Singapur", "Siria", "Sri Lanka", "Tailandia", "Taiwan", "Tayikistan", "Timor Oriental", "Turkmenistan", "Turquia", "Uzbekistain", "Vietnam", "Yemen"]

    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]]
    btn_Opcion1 = Button(ventana_Asia, cursor="hand2",  text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion1, 1, 2))
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]]
    btn_Opcion2 = Button(ventana_Asia, cursor="hand2", text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion2, 2, 2))
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]]
    btn_Opcion3 = Button(ventana_Asia, cursor="hand2", text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion3, 3, 2))
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]]
    btn_Opcion4 = Button(ventana_Asia, cursor="hand2",  text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion4, 4, 2))
    btn_Opcion4.place(x=pos[posx[3]], y=450)
    
    ventana_Asia.mainloop()


def Europa():
    #Son_Click.play()
    ventana_Europa = Toplevel()
    ventana_Europa.title("4 PAISES 1 BANDERA")
    ventana_Europa.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_Europa.resizable(0,0)
    ventana_Europa.configure(background="white")
    ventana_Europa.geometry("1200x650+75+10")

    lbl_Titulo = Label(ventana_Europa, text="EUROPA:", background="white", fg="black")
    lbl_Titulo.place(x=10, y=10)

    # --- Imagenes Aleatorias ---
    
    num = random.sample(range(1,48),4)

    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Europa\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_Europa, image=foto)
    lbl_Bandera.place(x=480, y=100)

    # --- Contadores ---
    vidas = 3
    lbl_vidas = Label(ventana_Europa, text=f"Vidas: {vidas}", bg="white", font=("Arial Black", 24))
    lbl_vidas.place(x=900, y=10)
    Puntos = 0
    lbl_puntaje = Label(ventana_Europa, text=f"Puntaje: {Puntos}", bg="white", font=("Arial Black", 24))
    lbl_puntaje.place(x=900, y=60)

    # --- Texto de los Botones Aleatorio ---
    
    paises = ["Relleno", "Albania", "Alemania", "Andorra", "Armenia", "Austria", "Azerbaiyan", "Belgica", "Bielorrusia", "Bosnia y Herzegovina", "Bulgaria", "Chipre", "Croacia", "Dinamarca", "Eslovaquia", "Eslovenia", "España", "Estonia", "Filandia", "Francia", "Georgia", "Grecia", "Hungria", "Irlanda", "Islandia", "Italia", "Letonia", "Liechtenstein", "Litunia", "Luxemburgo", "Macedonia del Norte", "Malta", "Moldavia", "Monaco", "Montenegro", "Noruega", "Paises Bajos", "Polonia", "Portugal", "Reino Unido", "Republica Checa", "Rumania", "Rusia", "San Marino", "Serbia", "Suecia", "Suiza", "Ucrania", "Vaticano"]

    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]]
    btn_Opcion1 = Button(ventana_Europa, cursor="hand2", text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion1, 1, 3))
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]]
    btn_Opcion2 = Button(ventana_Europa, cursor="hand2", text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion2, 2, 3))
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]]
    btn_Opcion3 = Button(ventana_Europa, cursor="hand2", text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion3, 3, 3))
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]]
    btn_Opcion4 = Button(ventana_Europa, cursor="hand2", text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion4, 4, 3))
    btn_Opcion4.place(x=pos[posx[3]], y=450)
    
    ventana_Europa.mainloop()


def Oceania():
    #Son_Click.play()
    ventana_Oceania = Toplevel()
    ventana_Oceania.title("4 PAISES 1 BANDERA")
    ventana_Oceania.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_Oceania.resizable(0,0)
    #ventana_Oceania.configure(background="white")
    ventana_Oceania.geometry("1200x650+75+10")
    
    imagen = PhotoImage(file="Proyecto Videojuego Py\imagenes\MapaMundi.png")
    lbl_imagen = Label(ventana_Oceania, image=imagen)
    lbl_imagen.place(x=0,y=0)

    lbl_Titulo = Label(ventana_Oceania, text="OCEANIA:", bg="white")
    lbl_Titulo.place(x=10, y=10)

    # --- Imagenes Aleatorias ---
    
    num = random.sample(range(1,14),4)
    
    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Oceania\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_Oceania, image=foto)
    lbl_Bandera.place(x=440, y=100)
    #lbl_Bandera.zoom(2)

    # --- Contadores ---
    vidas = 3
    lbl_vidas = Label(ventana_Oceania, text=f"Vidas: {vidas}", bg="white", font=("Arial Black", 24))
    lbl_vidas.place(x=900, y=10)
    Puntos = 0
    lbl_puntaje = Label(ventana_Oceania, text=f"Puntaje: {Puntos}", bg="white", font=("Arial Black", 24))
    lbl_puntaje.place(x=900, y=60)

    # --- Texto de los Botones Aleatorio ---
    
    paises = ["Relleno", "Australia", "Nauru", "Nueva Zelanda", "Fiyi", "Islas Marshall", "Islas Salomon", "Kiribati", "Micronesia", "Palaos", "Papua Nueva Guinea", "Samoa", "Tonga", "Tuvalu", "Vanuatu"]

    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]]
    btn_Opcion1 = Button(ventana_Oceania, cursor="hand2", text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion1, 1, 4))
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]]
    btn_Opcion2 = Button(ventana_Oceania, cursor="hand2", text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion2, 2, 4))
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]]
    btn_Opcion3 = Button(ventana_Oceania, cursor="hand2", text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion3, 3, 4))
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]]
    btn_Opcion4 = Button(ventana_Oceania, cursor="hand2", text=texto, width=35, height=10, command=lambda: respuesta(btn_Opcion4, 4, 4))
    btn_Opcion4.place(x=pos[posx[3]], y=450)
    
    ventana_Oceania.mainloop()

# --- Menu (Seleccion de Continente) ---

def Abrir_Ventana_Menu():
    #Son_Click.play()
    
    def Volver():
        Ventana_Menu.destroy()
        #Son_Click.play()

    Ventana_Menu = Toplevel()
    Ventana_Menu.title("4 PAISES 1 BANDERA")
    Ventana_Menu.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    Ventana_Menu.resizable(0,0)
    Ventana_Menu.geometry("1200x650+75+10")

    imagen = PhotoImage(file="Proyecto Videojuego Py\imagenes\Fondo_Band.png")
    lbl_imagen = Label(Ventana_Menu, image=imagen)
    lbl_imagen.place(x=0,y=0)

    lbl_seleccion = Label(Ventana_Menu, text="SELECCIONA UN CONTINENTE:", fg="black", bg="yellow", font=("Verdana", 35),  borderwidth=5, relief="groove" )
    lbl_seleccion.place(x=75, y=30)

    Btn_Africa = Button(Ventana_Menu, activebackground="gray70", cursor="hand2", text="AFRICA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command= Africa)
    Btn_Africa.place(x=42, y=110)
    
    Btn_America = Button(Ventana_Menu, activebackground="gray70", cursor="hand2", text="AMERICA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command=America)
    Btn_America.place(x=42, y=210)
    
    Btn_Asia = Button(Ventana_Menu, activebackground="gray70", cursor="hand2",  text="ASIA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command=Asia)
    Btn_Asia.place(x=42, y=310)
    
    Btn_Europa = Button(Ventana_Menu, activebackground="gray70", cursor="hand2",  text="EUROPA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command=Europa)
    Btn_Europa.place(x=42, y=410)
    
    Btn_Oceania = Button(Ventana_Menu, activebackground="gray70", cursor="hand2", text="OCEANIA", width=65, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command=Oceania)
    Btn_Oceania.place(x=42, y=510)

    Btn_Volver = Button(Ventana_Menu, activebackground="gray70", cursor="hand2", text="VOLVER", width=10, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10), command=Volver)
    Btn_Volver.place(x=1070, y=50)
    
    Ventana_Menu.mainloop()
    
# --- Principal (Inicio) ---

Ventana_Principal = Tk()
Ventana_Principal.title("4 PAISES 1 BANDERA")
Ventana_Principal.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
Ventana_Principal.resizable(0,0)
Ventana_Principal.geometry("1200x650+75+10")

imagen = PhotoImage(file="Proyecto Videojuego Py\imagenes\Fondo_Band.png")
lbl_imagen = Label(Ventana_Principal, image=imagen)
lbl_imagen.place(x=0,y=0)

lbl_Titulo = Label(Ventana_Principal, text="4 Paises 1 Bandera", fg="black", bg="yellow", font=("Verdana", 80),  borderwidth=5, relief="groove")
lbl_Titulo.place(x=75, y=40)

Btn_Comenazar = Button(Ventana_Principal, activebackground="gray70", cursor="hand2",  text="JUGAR", width=30, height=3, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10), command=Abrir_Ventana_Menu)
Btn_Comenazar.place(x=465, y=300)

#Img_P = PhotoImage(file="Proyecto Videojuego Py\imagenes\Botones\Puntaje1.png")
Btn_Record = Button(Ventana_Principal, activebackground="gray70", cursor="hand2", text="PUNTAJES", width=30, height=3, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10), command=Records)
Btn_Record.place(x=465, y=380)

Btn_Salir = Button(Ventana_Principal, activebackground="gray70", cursor="hand2", text="SALIR", width=30, height=3, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10), command=Salir)
Btn_Salir.place(x=465, y=460)

lbl_Create = Label(Ventana_Principal, text="Propiedad Intelectual y Creativa de: Jose Abraham Beristain Navarro y Josue Franciso Rojas Aripez", fg="white", bg="black", font=("Verdana", 10),  borderwidth=5)
lbl_Create.place(x=5, y=620)

# --- Fin ---

Ventana_Principal.mainloop()
