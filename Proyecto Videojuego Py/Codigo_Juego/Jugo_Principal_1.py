# El MAMALON PERRON CHINGON

# --- Importando --- 

from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import random
import time 
import pygame

# --- Funciones ---

def Links():
    import webbrowser
    webbrowser.open("https://github.com/JosueAripez/Proyecto_Videojuego_Py")

pygame.mixer.init()
pygame.mixer.music.load("Proyecto Videojuego Py\Musica\Musica_Fondo.mp3")
pygame.mixer.music.play(-1)
Son_Click = pygame.mixer.Sound("Proyecto Videojuego Py\Musica\click_btn.mp3")
Crt_Click = pygame.mixer.Sound("Proyecto Videojuego Py\Musica\Estrellas.mp3")
Inct_Click = pygame.mixer.Sound("Proyecto Videojuego Py\Musica\error.mp3")

def ajuste():
    Son_Click.play()
    W_ajustes = Toplevel()
    W_ajustes.title("AJUSTES")
    W_ajustes.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    W_ajustes.resizable(0,0)
    pygame.mixer.music.unpause()
    lblsond = Label(W_ajustes, text="Sonido")
    lblsond.place(x=10, y=15)
    
    opcion = IntVar() # Como StrinVar pero en entero

    Radiobutton(W_ajustes, text="SI", variable=opcion, value=1).pack()
    Radiobutton(W_ajustes, text="NO", variable=opcion, value=2).pack()
    if opcion == 1:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.pause()
    
    W_ajustes.geometry("300x300+75+10")
    
    W_ajustes.mainloop()

def respuesta(boton, op, cont):
    continente = [Africa, America, Asia, Europa, Oceania]

    if op == 1:
        Crt_Click.play()
        boton.config(bg="green")
        time.sleep(0.2)
        continente[cont]()
        
    else:
        Inct_Click.play()
        boton.config(bg="red")

def cargar_puntajes():
    Son_Click.play()
    puntajes = []
    
    # Cargar puntajes desde el archivo de texto
    with open("puntajes.txt", "r") as archivo:
        for linea in archivo:
            puntajes.append(linea.strip())
    
    # Crear una nueva ventana para mostrar los puntajes
    ventana_puntajes = Toplevel(Ventana_Principal)
    ventana_puntajes.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_puntajes.resizable(0,0)
    
    ventana_puntajes.geometry("200x400+75+10")
    ventana_puntajes.title("Puntajes")
  
    # Crear una etiqueta para cada puntaje
    for puntaje in puntajes:
        label_puntaje = Label(ventana_puntajes, text=puntaje)
        label_puntaje.pack()
    
def Salir():
    Son_Click.play()
    respuesta = messagebox.askquestion("4 Paises 1 Bandera", "¿Estas seguro que deseas salir?")
    if respuesta == "yes":
        Son_Click.play()
        Ventana_Principal.destroy()
        
# --- Continentes Funciones ----

def Africa():
    Son_Click.play()
    ventana_Africa= Toplevel()
    ventana_Africa.title("4 PAISES 1 BANDERA")
    ventana_Africa.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_Africa.resizable(0,0)
    ventana_Africa.configure(background="DeepSkyBlue3")
    imagen = PhotoImage(file="Proyecto Videojuego Py\imagenes\Flags_Fond (Custom).png")
    lbl_imagen = Label(ventana_Africa, image=imagen)
    lbl_imagen.place(x=0,y=0)
    ventana_Africa.geometry("1200x650+75+10")

    lbl_Titulo = Label(ventana_Africa, text="Africa", background="white", fg="black", font=("Arial Black", 24), bg="white")
    lbl_Titulo.place(x=50, y=10)

    # --- Contadores ---
    vidas = 3
    puntos = 0
    lbl_vidas = Label(ventana_Africa, text=f"Vidas: {vidas}", bg="white", font=("Arial Black", 24), background="white")
    lbl_vidas.place(x=980, y=10)
    
    lbl_puntaje = Label(ventana_Africa, text=f" Puntaje:{puntos}", bg="white", font=("Arial Black", 24), background="white")
    lbl_puntaje.place(x=500, y=10)

    def contador_puntos():
        nonlocal puntos
        puntos += 1
        lbl_puntaje.config(text=f"Puntaje: {puntos}")
        Crt_Click.play()
        btn_Opcion1.config(bg="green")

        # --- configurar bandera ---
        num = random.sample(range(1,56),4)
        bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Africa\\band{num[0]}.png"
        foto=PhotoImage(file=bandera)
        lbl_Bandera.config(image=foto)
        lbl_Bandera.place(x=410, y=100)
        lbl_Bandera.image = foto

        # --- configurar botones ---
        paises = ["Relleno", "Angola", "Argelia", "Benin", "Botsuana", "Burkina Faso", "Burundi", "Cabo Verde", "Camerun", "Chad", "Comoras", "Costa de Marfil", "Egipto", "Eritrea", "Etiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea Bisau", "Guinea Ecuatorial", "Kenia", "Lesoto", "Liberia", "Libia", "Madagascar", "Malaui", "Mali", "Marruecos", "Mauricio", "Mauritania", "Mozambique", "Naminia", "Niger", "Nigeria", "Republica Centroafricana", "Rpublica del Congo", "Republica Democratica del combo", "Ruanda", "Sahara", "Santo Tome y Principe", "Senegal", "Seychelles", "Sierra Leona", "Somalia", "Somalilandia", "Sauzilandia", "Sudafrica", "Sudan", "Sudan del Sur", "Tanzania", "Togo", "Tunez", "Uganda", "Yibuti", "Zambia", "Zimbaue"]
        pos = [30, 320, 610, 900]
        posx = random.sample(range(0,4), 4)
        
        texto = paises[num[0]]
        btn_Opcion1.config(bg="white", text=texto)
        btn_Opcion1.place(x=pos[posx[0]], y=450)

        texto = paises[num[1]]
        btn_Opcion2.config(bg="white", text=texto)
        btn_Opcion2.place(x=pos[posx[1]], y=450)

        texto = paises[num[2]]
        btn_Opcion3.config(bg="white", text=texto)
        btn_Opcion3.place(x=pos[posx[2]], y=450)

        texto = paises[num[3]]
        btn_Opcion4.config(bg="white", text=texto)
        btn_Opcion4.place(x=pos[posx[3]], y=450)
    
    def contador_vidas(op):
        
        def fulls():
            ventana_Africa.destroy()
            W_perdio.destroy()
            
        nonlocal vidas
        vidas -= 1
        lbl_vidas.config(text=f"Vidas: {vidas}")
        if op == 2:
            Inct_Click.play()
            btn_Opcion2.config(bg="red")
        elif op == 3:
            Inct_Click.play()
            btn_Opcion3.config(bg="red")
        else:
            Inct_Click.play()
            btn_Opcion4.config(bg="red")
        
        if vidas == 0:
            
            def guardar_puntaje():
                nombre_jugador = nombre_entry.get()
                        
                # Guardar puntaje en un archivo de texto
                with open("puntajes.txt", "a") as archivo:
                    archivo.write(f"{nombre_jugador}: {puntos}\n")
                fulls()
                
                    
            #aqui va ventana de cuando pierde
            Son_Click.play()
            W_perdio = Toplevel()
            W_perdio.title("JUEGO TERMINADO")
            W_perdio.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
            W_perdio.resizable(0,0)
            imagenf = PhotoImage(file="Proyecto Videojuego Py\imagenes\Fondo_Pantalla (Custom).png")
            lbl_imagen = Label(W_perdio, image=imagenf)
            lbl_imagen.place(x=0,y=0)
            W_perdio.geometry("700x400+350+170")
        
            lbl_Titulo = Label(W_perdio, text="PUNTUACION", fg="black", font=("Verdana", 30))
            lbl_Titulo.place(x=217, y=28)
            
            lbl_point = Label(W_perdio, text=f"Puntaje: {puntos}", font=("Verdana", 20))
            lbl_point.place(x=280, y=98)
            
            nombre_label = Label(W_perdio, text="Nombre:", font=("Verdana", 30))
            nombre_label.place(x=260, y=140)
            
            nombre_entry = Entry(W_perdio)
            nombre_entry.place(x=290, y=210)
            
            lbl_Titulo = Label(W_perdio, text="¿Quieres guardar tu puntaje?", fg="black", borderwidth=5, font=("Verdana", 30))
            lbl_Titulo.place(x=50, y=237)

            Btn_Puntaje = Button(W_perdio, activebackground="gray70", cursor="hand2",  text="SI", background="white", fg="black", borderwidth=5, font=("Verdana", 20), command=guardar_puntaje)
            Btn_Puntaje.place(x=244, y=310)
            
            Btn_Cerrar = Button(W_perdio, activebackground="gray70", cursor="hand2",  text="NO", background="white", fg="black", borderwidth=5, font=("Verdana", 20), command=fulls)
            Btn_Cerrar.place(x=365, y=310)
            
            W_perdio.protocol("WM_DELETE_WINDOW", lambda: None)
            
            print("MURIDO!!!!!!!!!!!!!!!!!!!!!!!111")
            
            


    # --- Imagenes Aleatorias ---
    
    num = random.sample(range(1,56),4)

    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Africa\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_Africa, image=foto)
    lbl_Bandera.place(x=480, y=100)


    # --- Texto de los botones aleatortios ---
    
    paises = ["Relleno", "Angola", "Argelia", "Benin", "Botsuana", "Burkina Faso", "Burundi", "Cabo Verde", "Camerun", "Chad", "Comoras", "Costa de Marfil", "Egipto", "Eritrea", "Etiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea Bisau", "Guinea Ecuatorial", "Kenia", "Lesoto", "Liberia", "Libia", "Madagascar", "Malaui", "Mali", "Marruecos", "Mauricio", "Mauritania", "Mozambique", "Naminia", "Niger", "Nigeria", "Republica Centroafricana", "Rpublica del Congo", "Republica Democratica del combo", "Ruanda", "Sahara", "Santo Tome y Principe", "Senegal", "Seychelles", "Sierra Leona", "Somalia", "Somalilandia", "Sauzilandia", "Sudafrica", "Sudan", "Sudan del Sur", "Tanzania", "Togo", "Tunez", "Uganda", "Yibuti", "Zambia", "Zimbaue"]
    
    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]]
    btn_Opcion1 = Button(ventana_Africa, cursor="hand2", text=texto, width=35, height=10, command= contador_puntos)
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]]
    btn_Opcion2 = Button(ventana_Africa, cursor="hand2",  text=texto, width=35, height=10, command=lambda: contador_vidas(2))
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]]
    btn_Opcion3 = Button(ventana_Africa, cursor="hand2",  text=texto, width=35, height=10, command=lambda: contador_vidas(3))
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]]
    btn_Opcion4 = Button(ventana_Africa, cursor="hand2",  text=texto, width=35, height=10, command=lambda: contador_vidas(4))
    btn_Opcion4.place(x=pos[posx[3]], y=450)

    ventana_Africa.mainloop()


def America():
    Son_Click.play()
    ventana_America = Toplevel()
    ventana_America.title("4 PAISES 1 BANDERA")
    ventana_America.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_America.resizable(0,0)
    imagen = PhotoImage(file="Proyecto Videojuego Py\imagenes\Flags_Fond (Custom).png")
    lbl_imagen = Label(ventana_America, image=imagen)
    lbl_imagen.place(x=0,y=0)
    ventana_America.geometry("1200x650+75+10")

    lbl_Titulo = Label(ventana_America, text="America", background="white", fg="black", font=("Arial Black", 24), bg="white")
    lbl_Titulo.place(x=50, y=10)

    # --- Contadores ---
    vidas = 3
    puntos = 0
    lbl_vidas = Label(ventana_America, text=f"Vidas: {vidas}", bg="white", font=("Arial Black", 24), background="white")
    lbl_vidas.place(x=980, y=10)
    
    lbl_puntaje = Label(ventana_America, text=f" Puntaje:{puntos}", bg="white", font=("Arial Black", 24), background="white")
    lbl_puntaje.place(x=500, y=10)

    def contador_puntos():
        nonlocal puntos
        puntos += 1
        lbl_puntaje.config(text=f"Puntaje: {puntos}")
        Crt_Click.play()
        btn_Opcion1.config(bg="green")

        # --- configurar bandera ---
        num = random.sample(range(1,36),4)
        bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\America\\band{num[0]}.png"
        foto=PhotoImage(file=bandera)
        lbl_Bandera.config(image=foto)
        lbl_Bandera.place(x=410, y=100)
        lbl_Bandera.image = foto

        # --- configurar botones ---
        paises = ["Relleno", "Antigua y Barbuba", "Argentina", "Bahamas", "Barbados", "Belice", "Bolivia", "Brasil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominica", "Ecuador", "EEUU", "El Salvador", "Granada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Republica Dominicana", "San Cristobal y Nieves", "San Vicente y las Granadinas", "Sanata Lucia", "Surinam", "Trinidad y Tobago", "Uruguay", "Venezuela"]
        pos = [30, 320, 610, 900]
        posx = random.sample(range(0,4), 4)
        
        texto = paises[num[0]]
        btn_Opcion1.config(bg="white", text=texto)
        btn_Opcion1.place(x=pos[posx[0]], y=450)

        texto = paises[num[1]]
        btn_Opcion2.config(bg="white", text=texto)
        btn_Opcion2.place(x=pos[posx[1]], y=450)

        texto = paises[num[2]]
        btn_Opcion3.config(bg="white", text=texto)
        btn_Opcion3.place(x=pos[posx[2]], y=450)

        texto = paises[num[3]]
        btn_Opcion4.config(bg="white", text=texto)
        btn_Opcion4.place(x=pos[posx[3]], y=450)
        
    def contador_vidas(op):
        
        def fulls():
            ventana_America.destroy()
            W_perdio.destroy()
            
        nonlocal vidas
        vidas -= 1
        lbl_vidas.config(text=f"Vidas: {vidas}")
        if op == 2:
            Inct_Click.play()
            btn_Opcion2.config(bg="red")
        elif op == 3:
            Inct_Click.play()
            btn_Opcion3.config(bg="red")
        else:
            Inct_Click.play()
            btn_Opcion4.config(bg="red")
        
        if vidas == 0:
            
            def guardar_puntaje():
                nombre_jugador = nombre_entry.get()
                        
                # Guardar puntaje en un archivo de texto
                with open("puntajes.txt", "a") as archivo:
                    archivo.write(f"{nombre_jugador}: {puntos}\n")
                fulls()
                
            #aqui va ventana de cuando pierde
            Son_Click.play()
            W_perdio = Toplevel()
            W_perdio.title("JUEGO TERMINADO")
            W_perdio.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
            W_perdio.resizable(0,0)
            imagenf = PhotoImage(file="Proyecto Videojuego Py\imagenes\Fondo_Pantalla (Custom).png")
            lbl_imagen = Label(W_perdio, image=imagenf)
            lbl_imagen.place(x=0,y=0)
            W_perdio.geometry("700x400+350+170")
        
            lbl_Titulo = Label(W_perdio, text="PUNTUACION", fg="black", font=("Verdana", 30))
            lbl_Titulo.place(x=217, y=28)
            
            lbl_point = Label(W_perdio, text=f"Puntaje: {puntos}", font=("Verdana", 20))
            lbl_point.place(x=280, y=98)
            
            nombre_label = Label(W_perdio, text="Nombre:", font=("Verdana", 30))
            nombre_label.place(x=260, y=140)
            
            nombre_entry = Entry(W_perdio)
            nombre_entry.place(x=290, y=210)
            
            lbl_Titulo = Label(W_perdio, text="¿Quieres guardar tu puntaje?", fg="black", borderwidth=5, font=("Verdana", 30))
            lbl_Titulo.place(x=50, y=237)

            Btn_Puntaje = Button(W_perdio, activebackground="gray70", cursor="hand2",  text="SI", background="white", fg="black", borderwidth=5, font=("Verdana", 20), command=guardar_puntaje)
            Btn_Puntaje.place(x=244, y=310)
            
            Btn_Cerrar = Button(W_perdio, activebackground="gray70", cursor="hand2",  text="NO", background="white", fg="black", borderwidth=5, font=("Verdana", 20), command=fulls)
            Btn_Cerrar.place(x=365, y=310)
            
            W_perdio.protocol("WM_DELETE_WINDOW", lambda: None)
            
            print("MURIDO!!!!!!!!!!!!!!!!!!!!!!!111")

    # --- Imagenes Aleatorias ---
    
    num = random.sample(range(1,36),4)

    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\America\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_America, image=foto)
    lbl_Bandera.place(x=480, y=100)

    # --- Texto de los Botones Aleatorio ---
    
    paises = ["Relleno", "Antigua y Barbuba", "Argentina", "Bahamas", "Barbados", "Belice", "Bolivia", "Brasil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominica", "Ecuador", "EEUU", "El Salvador", "Granada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Republica Dominicana", "San Cristobal y Nieves", "San Vicente y las Granadinas", "Sanata Lucia", "Surinam", "Trinidad y Tobago", "Uruguay", "Venezuela"]

    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]]
    btn_Opcion1 = Button(ventana_America, cursor="hand2",  text=texto, width=35, height=10, command= contador_puntos)
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]]
    btn_Opcion2 = Button(ventana_America, cursor="hand2",  text=texto, width=35, height=10, command=lambda: contador_vidas(2))
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]]
    btn_Opcion3 = Button(ventana_America, cursor="hand2", text=texto, width=35, height=10, command=lambda: contador_vidas(3))
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]]
    btn_Opcion4 = Button(ventana_America, cursor="hand2", text=texto, width=35, height=10, command=lambda: contador_vidas(4))
    btn_Opcion4.place(x=pos[posx[3]], y=450)
    
    ventana_America.mainloop()
    

def Asia():
    Son_Click.play()
    ventana_Asia = Toplevel()
    ventana_Asia.title("4 PAISES 1 BANDERA")
    ventana_Asia.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_Asia.resizable(0,0)
    ventana_Asia.configure(background="white")
    imagen = PhotoImage(file="Proyecto Videojuego Py\imagenes\Flags_Fond (Custom).png")
    lbl_imagen = Label(ventana_Asia, image=imagen)
    lbl_imagen.place(x=0,y=0)
    ventana_Asia.geometry("1200x650+75+10")
    lbl_Titulo = Label(ventana_Asia, text="Asia", background="white", fg="black", font=("Arial Black", 24), bg="white")
    lbl_Titulo.place(x=50, y=10)

    # --- Contadores ---
    vidas = 3
    puntos = 0
    lbl_vidas = Label(ventana_Asia, text=f"Vidas: {vidas}", bg="white", font=("Arial Black", 24), background="white")
    lbl_vidas.place(x=980, y=10)
    
    lbl_puntaje = Label(ventana_Asia, text=f" Puntaje:{puntos}", bg="white", font=("Arial Black", 24), background="white")
    lbl_puntaje.place(x=500, y=10)

    def contador_puntos():
        nonlocal puntos
        puntos += 1
        lbl_puntaje.config(text=f"Puntaje: {puntos}")
        Crt_Click.play()
        btn_Opcion1.config(bg="green")

        # --- configurar bandera ---
        num = random.sample(range(1,44),4)
        bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Asia\\band{num[0]}.png"
        foto=PhotoImage(file=bandera)
        lbl_Bandera.config(image=foto)
        lbl_Bandera.place(x=410, y=100)
        lbl_Bandera.image = foto

        # --- configurar botones ---
        paises = ["Relleno", "Afganistan", "Arabia Saudita", "Banglades", "Barein", "Birmania", "Brunei", "Butan", "Camboya", "Catar", "China", "Corea del Norte", "Corea del Sur", "Emiratos Arabes Unidos", "Filipinas", "India", "Indonesia", "Irak", "Iran", "Israel", "Japon", "Jordania", "Kazajistan", "Kuwait", "Laos", "Libano", "Malasia", "Maldivas", "Mongolia", "Nepal", "Oman", "Pakistan", "Palestina", "Singapur", "Siria", "Sri Lanka", "Tailandia", "Taiwan", "Tayikistan", "Timor Oriental", "Turkmenistan", "Turquia", "Uzbekistain", "Vietnam", "Yemen"]
        pos = [30, 320, 610, 900]
        posx = random.sample(range(0,4), 4)
        
        texto = paises[num[0]]
        btn_Opcion1.config(bg="white", text=texto)
        btn_Opcion1.place(x=pos[posx[0]], y=450)

        texto = paises[num[1]]
        btn_Opcion2.config(bg="white", text=texto)
        btn_Opcion2.place(x=pos[posx[1]], y=450)

        texto = paises[num[2]]
        btn_Opcion3.config(bg="white", text=texto)
        btn_Opcion3.place(x=pos[posx[2]], y=450)

        texto = paises[num[3]]
        btn_Opcion4.config(bg="white", text=texto)
        btn_Opcion4.place(x=pos[posx[3]], y=450)


    def contador_vidas(op):
        
        def fulls():
            ventana_Asia.destroy()
            W_perdio.destroy()
            
        nonlocal vidas
        vidas -= 1
        lbl_vidas.config(text=f"Vidas: {vidas}")
        if op == 2:
            Inct_Click.play()
            btn_Opcion2.config(bg="red")
        elif op == 3:
            Inct_Click.play()
            btn_Opcion3.config(bg="red")
        else:
            Inct_Click.play()
            btn_Opcion4.config(bg="red")
        
        if vidas == 0:
            
            def guardar_puntaje():
                nombre_jugador = nombre_entry.get()
                        
                # Guardar puntaje en un archivo de texto
                with open("puntajes.txt", "a") as archivo:
                    archivo.write(f"{nombre_jugador}: {puntos}\n")
                fulls()
                
            #aqui va ventana de cuando pierde
            Son_Click.play()
            W_perdio = Toplevel()
            W_perdio.title("JUEGO TERMINADO")
            W_perdio.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
            W_perdio.resizable(0,0)
            imagenf = PhotoImage(file="Proyecto Videojuego Py\imagenes\Fondo_Pantalla (Custom).png")
            lbl_imagen = Label(W_perdio, image=imagenf)
            lbl_imagen.place(x=0,y=0)
            W_perdio.geometry("700x400+350+170")
        
            lbl_Titulo = Label(W_perdio, text="PUNTUACION", fg="black", font=("Verdana", 30))
            lbl_Titulo.place(x=217, y=28)
            
            lbl_point = Label(W_perdio, text=f"Puntaje: {puntos}", font=("Verdana", 20))
            lbl_point.place(x=280, y=98)
            
            nombre_label = Label(W_perdio, text="Nombre:", font=("Verdana", 30))
            nombre_label.place(x=260, y=140)
            
            nombre_entry = Entry(W_perdio)
            nombre_entry.place(x=290, y=210)
            
            lbl_Titulo = Label(W_perdio, text="¿Quieres guardar tu puntaje?", fg="black", borderwidth=5, font=("Verdana", 30))
            lbl_Titulo.place(x=50, y=237)

            Btn_Puntaje = Button(W_perdio, activebackground="gray70", cursor="hand2",  text="SI", background="white", fg="black", borderwidth=5, font=("Verdana", 20), command=guardar_puntaje)
            Btn_Puntaje.place(x=244, y=310)
            
            Btn_Cerrar = Button(W_perdio, activebackground="gray70", cursor="hand2",  text="NO", background="white", fg="black", borderwidth=5, font=("Verdana", 20), command=fulls)
            Btn_Cerrar.place(x=365, y=310)
            
            W_perdio.protocol("WM_DELETE_WINDOW", lambda: None)
            
            print("MURIDO!!!!!!!!!!!!!!!!!!!!!!!111")

    # --- Imagenes Aleatorias ---
    
    num = random.sample(range(1,44),4)

    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Asia\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_Asia, image=foto)
    lbl_Bandera.place(x=480, y=100)

    # --- Texto de los Botones Aleatorio ---
    
    paises = ["Relleno", "Afganistan", "Arabia Saudita", "Banglades", "Barein", "Birmania", "Brunei", "Butan", "Camboya", "Catar", "China", "Corea del Norte", "Corea del Sur", "Emiratos Arabes Unidos", "Filipinas", "India", "Indonesia", "Irak", "Iran", "Israel", "Japon", "Jordania", "Kazajistan", "Kuwait", "Laos", "Libano", "Malasia", "Maldivas", "Mongolia", "Nepal", "Oman", "Pakistan", "Palestina", "Singapur", "Siria", "Sri Lanka", "Tailandia", "Taiwan", "Tayikistan", "Timor Oriental", "Turkmenistan", "Turquia", "Uzbekistain", "Vietnam", "Yemen"]

    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]]
    btn_Opcion1 = Button(ventana_Asia, cursor="hand2",  text=texto, width=35, height=10, command= contador_puntos)
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]]
    btn_Opcion2 = Button(ventana_Asia, cursor="hand2", text=texto, width=35, height=10, command=lambda: contador_vidas(2))
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]]
    btn_Opcion3 = Button(ventana_Asia, cursor="hand2", text=texto, width=35, height=10, command=lambda: contador_vidas(3))
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]]
    btn_Opcion4 = Button(ventana_Asia, cursor="hand2",  text=texto, width=35, height=10, command=lambda: contador_vidas(4))
    btn_Opcion4.place(x=pos[posx[3]], y=450)
    
    ventana_Asia.mainloop()


def Europa():
    Son_Click.play()
    ventana_Europa = Toplevel()
    ventana_Europa.title("4 PAISES 1 BANDERA")
    ventana_Europa.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_Europa.resizable(0,0)
    ventana_Europa.configure(background="white")
    imagen = PhotoImage(file="Proyecto Videojuego Py\imagenes\Flags_Fond (Custom).png")
    lbl_imagen = Label(ventana_Europa, image=imagen)
    lbl_imagen.place(x=0,y=0)
    ventana_Europa.geometry("1200x650+75+10")

    lbl_Titulo = Label(ventana_Europa, text="Europa", background="white", fg="black", font=("Arial Black", 24), bg="white")
    lbl_Titulo.place(x=50, y=10)

    # --- Contadores ---
    vidas = 3
    puntos = 0
    lbl_vidas = Label(ventana_Europa, text=f"Vidas: {vidas}", bg="white", font=("Arial Black", 24), background="white")
    lbl_vidas.place(x=980, y=10)
    
    lbl_puntaje = Label(ventana_Europa, text=f" Puntaje:{puntos}", bg="white", font=("Arial Black", 24), background="white")
    lbl_puntaje.place(x=500, y=10)

    def contador_puntos():
        nonlocal puntos
        puntos += 1
        lbl_puntaje.config(text=f"Puntaje: {puntos}")
        Crt_Click.play()
        btn_Opcion1.config(bg="green")

        # --- configurar bandera ---
        num = random.sample(range(1,48),4)
        bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Europa\\band{num[0]}.png"
        foto=PhotoImage(file=bandera)
        lbl_Bandera.config(image=foto)
        lbl_Bandera.place(x=410, y=100)
        lbl_Bandera.image = foto

        # --- configurar botones ---
        paises = ["Relleno", "Albania", "Alemania", "Andorra", "Armenia", "Austria", "Azerbaiyan", "Belgica", "Bielorrusia", "Bosnia y Herzegovina", "Bulgaria", "Chipre", "Croacia", "Dinamarca", "Eslovaquia", "Eslovenia", "España", "Estonia", "Filandia", "Francia", "Georgia", "Grecia", "Hungria", "Irlanda", "Islandia", "Italia", "Letonia", "Liechtenstein", "Litunia", "Luxemburgo", "Macedonia del Norte", "Malta", "Moldavia", "Monaco", "Montenegro", "Noruega", "Paises Bajos", "Polonia", "Portugal", "Reino Unido", "Republica Checa", "Rumania", "Rusia", "San Marino", "Serbia", "Suecia", "Suiza", "Ucrania", "Vaticano"]
        pos = [30, 320, 610, 900]
        posx = random.sample(range(0,4), 4)
        
        texto = paises[num[0]]
        btn_Opcion1.config(bg="white", text=texto)
        btn_Opcion1.place(x=pos[posx[0]], y=450)

        texto = paises[num[1]]
        btn_Opcion2.config(bg="white", text=texto)
        btn_Opcion2.place(x=pos[posx[1]], y=450)

        texto = paises[num[2]]
        btn_Opcion3.config(bg="white", text=texto)
        btn_Opcion3.place(x=pos[posx[2]], y=450)

        texto = paises[num[3]]
        btn_Opcion4.config(bg="white", text=texto)
        btn_Opcion4.place(x=pos[posx[3]], y=450)


    def contador_vidas(op):
        
        def fulls():
            ventana_Europa.destroy()
            W_perdio.destroy()
            
        nonlocal vidas
        vidas -= 1
        lbl_vidas.config(text=f"Vidas: {vidas}")
        if op == 2:
            Inct_Click.play()
            btn_Opcion2.config(bg="red")
        elif op == 3:
            Inct_Click.play()
            btn_Opcion3.config(bg="red")
        else:
            Inct_Click.play()
            btn_Opcion4.config(bg="red")
        
        if vidas == 0:
            
            def guardar_puntaje():
                nombre_jugador = nombre_entry.get()
                        
                # Guardar puntaje en un archivo de texto
                with open("puntajes.txt", "a") as archivo:
                    archivo.write(f"{nombre_jugador}: {puntos}\n")
                fulls()
                    
            #aqui va ventana de cuando pierde
            Son_Click.play()
            W_perdio = Toplevel()
            W_perdio.title("JUEGO TERMINADO")
            W_perdio.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
            W_perdio.resizable(0,0)
            imagenf = PhotoImage(file="Proyecto Videojuego Py\imagenes\Fondo_Pantalla (Custom).png")
            lbl_imagen = Label(W_perdio, image=imagenf)
            lbl_imagen.place(x=0,y=0)
            W_perdio.geometry("700x400+350+170")
        
            lbl_Titulo = Label(W_perdio, text="PUNTUACION", fg="black", font=("Verdana", 30))
            lbl_Titulo.place(x=217, y=28)
            
            lbl_point = Label(W_perdio, text=f"Puntaje: {puntos}", font=("Verdana", 20))
            lbl_point.place(x=280, y=98)
            
            nombre_label = Label(W_perdio, text="Nombre:", font=("Verdana", 30))
            nombre_label.place(x=260, y=140)
            
            nombre_entry = Entry(W_perdio)
            nombre_entry.place(x=290, y=210)
            
            lbl_Titulo = Label(W_perdio, text="¿Quieres guardar tu puntaje?", fg="black", borderwidth=5, font=("Verdana", 30))
            lbl_Titulo.place(x=50, y=237)

            Btn_Puntaje = Button(W_perdio, activebackground="gray70", cursor="hand2",  text="SI", background="white", fg="black", borderwidth=5, font=("Verdana", 20), command=guardar_puntaje)
            Btn_Puntaje.place(x=244, y=310)
            
            Btn_Cerrar = Button(W_perdio, activebackground="gray70", cursor="hand2",  text="NO", background="white", fg="black", borderwidth=5, font=("Verdana", 20), command=fulls)
            Btn_Cerrar.place(x=365, y=310)
            
            W_perdio.protocol("WM_DELETE_WINDOW", lambda: None)
            
            print("MURIDO!!!!!!!!!!!!!!!!!!!!!!!111")


    # --- Imagenes Aleatorias ---
    
    num = random.sample(range(1,48),4)

    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Europa\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_Europa, image=foto)
    lbl_Bandera.place(x=480, y=100)

    # --- Texto de los Botones Aleatorio ---
    
    paises = ["Relleno", "Albania", "Alemania", "Andorra", "Armenia", "Austria", "Azerbaiyan", "Belgica", "Bielorrusia", "Bosnia y Herzegovina", "Bulgaria", "Chipre", "Croacia", "Dinamarca", "Eslovaquia", "Eslovenia", "España", "Estonia", "Filandia", "Francia", "Georgia", "Grecia", "Hungria", "Irlanda", "Islandia", "Italia", "Letonia", "Liechtenstein", "Litunia", "Luxemburgo", "Macedonia del Norte", "Malta", "Moldavia", "Monaco", "Montenegro", "Noruega", "Paises Bajos", "Polonia", "Portugal", "Reino Unido", "Republica Checa", "Rumania", "Rusia", "San Marino", "Serbia", "Suecia", "Suiza", "Ucrania", "Vaticano"]

    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]]
    btn_Opcion1 = Button(ventana_Europa, cursor="hand2", text=texto, width=35, height=10, command= contador_puntos)
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]]
    btn_Opcion2 = Button(ventana_Europa, cursor="hand2", text=texto, width=35, height=10, command=lambda: contador_vidas(2))
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]]
    btn_Opcion3 = Button(ventana_Europa, cursor="hand2", text=texto, width=35, height=10, command=lambda: contador_vidas(3))
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]]
    btn_Opcion4 = Button(ventana_Europa, cursor="hand2", text=texto, width=35, height=10, command=lambda: contador_vidas(4))
    btn_Opcion4.place(x=pos[posx[3]], y=450)
    
    ventana_Europa.mainloop()


def Oceania():
    Son_Click.play()
    ventana_Oceania = Toplevel()
    ventana_Oceania.title("4 PAISES 1 BANDERA")
    ventana_Oceania.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    ventana_Oceania.resizable(0,0)
    ventana_Oceania.geometry("1200x650+75+10")
    imagen = PhotoImage(file="Proyecto Videojuego Py\imagenes\Flags_Fond (Custom).png")
    lbl_imagen = Label(ventana_Oceania, image=imagen)
    lbl_imagen.place(x=0,y=0)

    lbl_Titulo = Label(ventana_Oceania, text="Oceania", background="white", fg="black", font=("Arial Black", 24), bg="white")
    lbl_Titulo.place(x=50, y=10)

    # --- Contadores ---
    vidas = 3
    puntos = 0
    lbl_vidas = Label(ventana_Oceania, text=f"Vidas: {vidas}", bg="white", font=("Arial Black", 24), background="white")
    lbl_vidas.place(x=980, y=10)
    
    lbl_puntaje = Label(ventana_Oceania, text=f" Puntaje:{puntos}", bg="white", font=("Arial Black", 24), background="white")
    lbl_puntaje.place(x=500, y=10)

    def contador_puntos():
        nonlocal puntos
        puntos += 1
        lbl_puntaje.config(text=f"Puntaje: {puntos}")
        Crt_Click.play()
        btn_Opcion1.config(bg="green")

        # --- configurar bandera ---
        num = random.sample(range(1,14),4)
        bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Oceania\\band{num[0]}.png"
        foto=PhotoImage(file=bandera)
        lbl_Bandera.config(image=foto)
        lbl_Bandera.place(x=480, y=100)
        lbl_Bandera.image = foto

        # --- configurar botones ---
        paises = ["Relleno", "Australia", "Nauru", "Nueva Zelanda", "Fiyi", "Islas Marshall", "Islas Salomon", "Kiribati", "Micronesia", "Palaos", "Papua Nueva Guinea", "Samoa", "Tonga", "Tuvalu", "Vanuatu"]
        pos = [30, 320, 610, 900]
        posx = random.sample(range(0,4), 4)
        
        texto = paises[num[0]]
        btn_Opcion1.config(bg="white", text=texto)
        btn_Opcion1.place(x=pos[posx[0]], y=450)

        texto = paises[num[1]]
        btn_Opcion2.config(bg="white", text=texto)
        btn_Opcion2.place(x=pos[posx[1]], y=450)

        texto = paises[num[2]]
        btn_Opcion3.config(bg="white", text=texto)
        btn_Opcion3.place(x=pos[posx[2]], y=450)

        texto = paises[num[3]]
        btn_Opcion4.config(bg="white", text=texto)
        btn_Opcion4.place(x=pos[posx[3]], y=450)
    
    def contador_vidas(op):
        
        def fulls():
            ventana_Oceania.destroy()
            W_perdio.destroy()
            
        nonlocal vidas
        vidas -= 1
        lbl_vidas.config(text=f"Vidas: {vidas}")
        if op == 2:
            Inct_Click.play()
            btn_Opcion2.config(bg="red")
        elif op == 3:
            Inct_Click.play()
            btn_Opcion3.config(bg="red")
        else:
            Inct_Click.play()
            btn_Opcion4.config(bg="red")
        
        if vidas == 0:
            
            def guardar_puntaje():
                nombre_jugador = nombre_entry.get()
                        
                # Guardar puntaje en un archivo de texto
                with open("puntajes.txt", "a") as archivo:
                    archivo.write(f"{nombre_jugador}: {puntos}\n")
                fulls()
                
            #aqui va ventana de cuando pierde
            Son_Click.play()
            W_perdio = Toplevel()
            W_perdio.title("JUEGO TERMINADO")
            W_perdio.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
            W_perdio.resizable(0,0)
            imagenf = PhotoImage(file="Proyecto Videojuego Py\imagenes\Fondo_Pantalla (Custom).png")
            lbl_imagen = Label(W_perdio, image=imagenf)
            lbl_imagen.place(x=0,y=0)
            W_perdio.geometry("700x400+350+170")
        
            lbl_Titulo = Label(W_perdio, text="PUNTUACION", fg="black", font=("Verdana", 30))
            lbl_Titulo.place(x=217, y=28)
            
            lbl_point = Label(W_perdio, text=f"Puntaje: {puntos}", font=("Verdana", 20))
            lbl_point.place(x=280, y=98)
            
            nombre_label = Label(W_perdio, text="Nombre:", font=("Verdana", 30))
            nombre_label.place(x=260, y=140)
            
            nombre_entry = Entry(W_perdio)
            nombre_entry.place(x=290, y=210)
            
            lbl_Titulo = Label(W_perdio, text="¿Quieres guardar tu puntaje?", fg="black", borderwidth=5, font=("Verdana", 30))
            lbl_Titulo.place(x=50, y=237)

            Btn_Puntaje = Button(W_perdio, activebackground="gray70", cursor="hand2",  text="SI", background="white", fg="black", borderwidth=5, font=("Verdana", 20), command=guardar_puntaje)
            Btn_Puntaje.place(x=244, y=310)
            
            Btn_Cerrar = Button(W_perdio, activebackground="gray70", cursor="hand2",  text="NO", background="white", fg="black", borderwidth=5, font=("Verdana", 20), command=fulls)
            Btn_Cerrar.place(x=365, y=310)
            
            W_perdio.protocol("WM_DELETE_WINDOW", lambda: None)
            
            print("MURIDO!!!!!!!!!!!!!!!!!!!!!!!111")

    # --- Imagenes Aleatorias ---
    
    num = random.sample(range(1,14),4)
    
    bandera = f"Proyecto Videojuego Py\imagenes\Banderas2\Oceania\\band{num[0]}.png"
    foto=PhotoImage(file=bandera)
    lbl_Bandera = Label(ventana_Oceania, image=foto)
    lbl_Bandera.place(x=440, y=100)

    # --- Texto de los Botones Aleatorio ---
    
    paises = ["Relleno", "Australia", "Nauru", "Nueva Zelanda", "Fiyi", "Islas Marshall", "Islas Salomon", "Kiribati", "Micronesia", "Palaos", "Papua Nueva Guinea", "Samoa", "Tonga", "Tuvalu", "Vanuatu"]

    pos = [30, 320, 610, 900]
    posx = random.sample(range(0,4), 4)

    texto = paises[num[0]]
    btn_Opcion1 = Button(ventana_Oceania, cursor="hand2", text=texto, width=35, height=10, command= contador_puntos)
    btn_Opcion1.place(x=pos[posx[0]], y=450)

    texto = paises[num[1]]
    btn_Opcion2 = Button(ventana_Oceania, cursor="hand2", text=texto, width=35, height=10, command=lambda: contador_vidas(2))
    btn_Opcion2.place(x=pos[posx[1]], y=450)

    texto = paises[num[2]]
    btn_Opcion3 = Button(ventana_Oceania, cursor="hand2", text=texto, width=35, height=10, command=lambda: contador_vidas(3))
    btn_Opcion3.place(x=pos[posx[2]], y=450)

    texto = paises[num[3]]
    btn_Opcion4 = Button(ventana_Oceania, cursor="hand2", text=texto, width=35, height=10, command=lambda: contador_vidas(4))
    btn_Opcion4.place(x=pos[posx[3]], y=450)
    
    ventana_Oceania.mainloop()

# --- Menu (Seleccion de Continente) ---

def Abrir_Ventana_Menu():
    Son_Click.play()
    
    def Volver():
        Ventana_Menu.destroy()
        Son_Click.play()

    Ventana_Menu = Toplevel()
    Ventana_Menu.title("4 PAISES 1 BANDERA")
    Ventana_Menu.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    Ventana_Menu.resizable(0,0)
    Ventana_Menu.geometry("1200x650+75+10")

    imagen = PhotoImage(file="Proyecto Videojuego Py\imagenes\Flags_Fond (Custom).png")
    lbl_imagen = Label(Ventana_Menu, image=imagen)
    lbl_imagen.place(x=0,y=0)
    
    lbl_seleccion = Label(Ventana_Menu, text="SELECCIONA UN CONTINENTE:", fg="DeepSkyBlue4", bg="yellow", font=("Verdana", 35),  borderwidth=5, relief="groove" )
    lbl_seleccion.place(x=0, y=0)

    imgAfrica = PhotoImage(file="Proyecto Videojuego Py\imagenes\Africa (Custom).png")
    Btn_Africa = Button(Ventana_Menu, image=imgAfrica, cursor="hand2", width=270, height=170, background="white", command= Africa)
    Btn_Africa.place(x=280, y=450)
    
    imgAmerica = PhotoImage(file="Proyecto Videojuego Py\imagenes\America (Custom).png")
    Btn_America = Button(Ventana_Menu, image=imgAmerica, cursor="hand2", width=270, height=170, background="white", command=America)
    Btn_America.place(x=30, y=150)
    
    imgAsia = PhotoImage(file="Proyecto Videojuego Py\imagenes\Asia (Custom).png")
    Btn_Asia = Button(Ventana_Menu, image=imgAsia, cursor="hand2", width=270, height=170, background="white", command=Asia)
    Btn_Asia.place(x=900, y=150)
    
    imgEuropa = PhotoImage(file="Proyecto Videojuego Py\imagenes\Europa (Custom).png")
    Btn_Europa = Button(Ventana_Menu, image=imgEuropa, cursor="hand2", width=270, height=170, background="white", command=Europa)
    Btn_Europa.place(x=480, y=150)
    
    imgOceania = PhotoImage(file="Proyecto Videojuego Py\imagenes\Oceania (Custom).png")
    Btn_Oceania = Button(Ventana_Menu, image=imgOceania, cursor="hand2", width=270, height=170, background="white", command=Oceania)
    Btn_Oceania.place(x=700, y=450)

    Btn_Volver = Button(Ventana_Menu, activebackground="gray70", cursor="hand2", text="VOLVER", width=10, height=2, background="white", fg="black", font=("Verdana", 10), command=Volver)
    Btn_Volver.place(x=1105, y=0)
    
    Ventana_Menu.mainloop()
    
# --- Principal (Inicio) ---

Ventana_Principal = Tk()
Ventana_Principal.title("4 PAISES 1 BANDERA")
Ventana_Principal.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
Ventana_Principal.resizable(0,0)
Ventana_Principal.geometry("1200x650+75+10")

imagen = PhotoImage(file="Proyecto Videojuego Py\imagenes\Flags_Fond (Custom).png")
lbl_imagen = Label(Ventana_Principal, image=imagen)
lbl_imagen.place(x=0,y=0)

lbl_Titulo = Label(Ventana_Principal, text="4 Paises 1 Bandera", fg="DeepSkyBlue4", bg="yellow", font=("Verdana", 80),  borderwidth=5, relief="groove")
lbl_Titulo.place(x=75, y=40)

Btn_Comenazar = Button(Ventana_Principal, activebackground="gray70", cursor="hand2",  text="JUGAR", width=20, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command=Abrir_Ventana_Menu)
Btn_Comenazar.place(x=430, y=300)


Btn_Record = Button(Ventana_Principal, activebackground="gray70", cursor="hand2", text="PUNTAJE", width=20, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command=cargar_puntajes)
Btn_Record.place(x=430, y=400)

Btn_Salir = Button(Ventana_Principal, activebackground="gray70", cursor="hand2", text="SALIR", width=20, height=2, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 20), command=Salir)
Btn_Salir.place(x=430, y=500)

"""ajuste_img = PhotoImage(file="Proyecto Videojuego Py\imagenes\co.png")"""
Btn_ajustes = Button(Ventana_Principal, text="+", cursor="hand2", bg="white", command=Links)
Btn_ajustes.place(x=1180, y=622)

lbl_Create = Label(Ventana_Principal, text="Propiedad Intelectual y Creativa de: Jose Abraham Beristain Navarro y Josue Franciso Rojas Aripez ©", fg="black", bg="white", font=("Verdana", 10),  borderwidth=5)
lbl_Create.place(x=5, y=620)

Ventana_Principal.protocol("WM_DELETE_WINDOW", lambda: None)

# --- Fin --- 

Ventana_Principal.mainloop()
