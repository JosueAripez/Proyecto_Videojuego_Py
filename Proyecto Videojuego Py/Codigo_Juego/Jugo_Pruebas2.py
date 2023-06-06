# --- Importando ---

from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import random
import time 
import pygame

# --- Variables Globales ---

puntaje = 0
vidas = 3

# --- Funciones ---

pygame.mixer.init()
#pygame.mixer.music.load("Proyecto Videojuego Py\Musica\Musica_Fondo.mp3")
#pygame.mixer.music.play(-1)
Son_Click = pygame.mixer.Sound("Proyecto Videojuego Py\Musica\click_btn.mp3")
Crt_Click = pygame.mixer.Sound("Proyecto Videojuego Py\Musica\Estrellas.mp3")
Inct_Click = pygame.mixer.Sound("Proyecto Videojuego Py\Musica\error.mp3")

def cargar_puntajes():
    Son_Click.play()
    puntajes = []
    
    # Cargar puntajes desde el archivo de texto
    with open("puntajes.txt", "r") as archivo:
        for linea in archivo:
            puntajes.append(linea.strip())
    
    # Crear una nueva ventana para mostrar los puntajes
    ventana_puntajes = Toplevel(Ventana_Principal)
    ventana_puntajes.title("Puntajes")
    ventana_puntajes.geometry("700x400+350+170")
    
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
        
# --- Continentes ---
        
def Africa():
    # Diccionario con las banderas y sus respectivos nombres
    banderas = {
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Australia.png": "AUSTRALIA",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Fiyi.png": "FIYI",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Palaos.png": "PALAOS",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Tonga.png": "TONGA"
    }

    def mostrar_banderas():
        # Obtener una lista de las banderas
        lista_banderas = list(banderas.keys())
        # Barajar las banderas para mostrarlas en orden aleatorio
        random.shuffle(lista_banderas)
        # Mostrar las banderas y generar las opciones
        opciones = []
        for i in range(4):
            opcion = lista_banderas[i]
            opciones.append(opcion)
            # Cargar la imagen de la bandera
            imagen = PhotoImage(file=opcion)
            # Mostrar la imagen en una etiqueta
            label_imagen.configure(image=imagen)
            label_imagen.image = imagen
            # Actualizar las opciones
            botones[i].configure(text=opcion)
        return opciones

    def verificar_respuesta(respuesta):
        global puntaje, vidas
        
        respuesta_bandera = respuesta.widget["text"]
        nombre_pais = banderas[respuesta_bandera]
        
        if respuesta_bandera in opciones:
            puntaje += 1
            info_label.configure(text="¡Respuesta correcta!", fg="green")
        else:
            vidas -= 1
            info_label.configure(text="Respuesta incorrecta. Pierdes una vida.", fg="red")
            
        del banderas[respuesta_bandera]
        
        puntaje_label.configure(text=f"Puntaje: {puntaje}")
        vidas_label.configure(text=f"Vidas restantes: {vidas}")
        
        if vidas > 0:
            jugar()
        else:
            guardar_puntaje()

    def jugar():
        global opciones
        
        opciones = mostrar_banderas()
        
        for boton in botones:
            boton.configure(state=NORMAL)

    def guardar_puntaje():
        nombre_jugador = nombre_entry.get()
        
        # Guardar puntaje en un archivo de texto
        with open("puntajes.txt", "a") as archivo:
            archivo.write(f"{nombre_jugador}: {puntaje}\n")
            
        root.destroy()

    # --- Ventana Principal ---

    root = Toplevel()
    root.title("4 PAISES 1 BANDERA")
    root.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    root.resizable(0,0)
    root.geometry("1200x650+75+10")

    # Etiqueta para mostrar la imagen de la bandera
    label_imagen = Label(root)
    label_imagen.pack(pady=10)

    # Botones para las opciones
    botones = []
    for _ in range(4):
        Son_Click.play()
        boton = Button(root, text="", width=20, state=DISABLED)
        boton.pack(pady=5)
        boton.configure(command=verificar_respuesta)
        botones.append(boton)

    # Etiquetas para el puntaje y las vidas
    puntaje_label = Label(root, text="Puntaje: 0")
    puntaje_label.pack()
    vidas_label = Label(root, text="Vidas restantes: 3")
    vidas_label.pack()

    # Etiqueta para mostrar información al jugador
    info_label = Label(root, text="")
    info_label.pack(pady=10)

    # Etiqueta y entrada para el nombre del jugador
    nombre_label = Label(root, text="Ingresa tu nombre:")
    nombre_label.pack()
    nombre_entry = Entry(root)
    nombre_entry.pack(pady=5)

    # Botón para guardar el puntaje
    guardar_button = Button(root, text="Guardar puntaje", command=guardar_puntaje)
    guardar_button.pack(pady=10)

    # Iniciar el juego
    jugar()

    root.mainloop()

#----------------------------------------------------------------
        
def America():
    # Diccionario con las banderas y sus respectivos nombres
    banderas = {
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Australia.png": "AUSTRALIA",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Fiyi.png": "FIYI",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Palaos.png": "PALAOS",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Tonga.png": "TONGA"
    }

    def mostrar_banderas():
        # Obtener una lista de las banderas
        lista_banderas = list(banderas.keys())
        # Barajar las banderas para mostrarlas en orden aleatorio
        random.shuffle(lista_banderas)
        # Mostrar las banderas y generar las opciones
        opciones = []
        for i in range(4):
            opcion = lista_banderas[i]
            opciones.append(opcion)
            # Cargar la imagen de la bandera
            imagen = PhotoImage(file=opcion)
            # Mostrar la imagen en una etiqueta
            label_imagen.configure(image=imagen)
            label_imagen.image = imagen
            # Actualizar las opciones
            botones[i].configure(text=opcion)
        return opciones

    def verificar_respuesta(respuesta):
        global puntaje, vidas
        
        respuesta_bandera = respuesta.widget["text"]
        nombre_pais = banderas[respuesta_bandera]
        
        if respuesta_bandera in opciones:
            puntaje += 1
            info_label.configure(text="¡Respuesta correcta!", fg="green")
        else:
            vidas -= 1
            info_label.configure(text="Respuesta incorrecta. Pierdes una vida.", fg="red")
            
        del banderas[respuesta_bandera]
        
        puntaje_label.configure(text=f"Puntaje: {puntaje}")
        vidas_label.configure(text=f"Vidas restantes: {vidas}")
        
        if vidas > 0:
            jugar()
        else:
            guardar_puntaje()

    def jugar():
        global opciones
        
        opciones = mostrar_banderas()
        
        for boton in botones:
            boton.configure(state=NORMAL)

    def guardar_puntaje():
        nombre_jugador = nombre_entry.get()
        
        # Guardar puntaje en un archivo de texto
        with open("puntajes.txt", "a") as archivo:
            archivo.write(f"{nombre_jugador}: {puntaje}\n")
            
        root.destroy()

    # --- Ventana Principal ---

    root = Toplevel()
    root.title("4 PAISES 1 BANDERA")
    root.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    root.resizable(0,0)
    root.geometry("1200x650+75+10")

    # Etiqueta para mostrar la imagen de la bandera
    label_imagen = Label(root)
    label_imagen.pack(pady=10)

    # Botones para las opciones
    botones = []
    for _ in range(4):
        Son_Click.play()
        boton = Button(root, text="", width=20, state=DISABLED)
        boton.pack(pady=5)
        boton.configure(command=verificar_respuesta)
        botones.append(boton)

    # Etiquetas para el puntaje y las vidas
    puntaje_label = Label(root, text="Puntaje: 0")
    puntaje_label.pack()
    vidas_label = Label(root, text="Vidas restantes: 3")
    vidas_label.pack()

    # Etiqueta para mostrar información al jugador
    info_label = Label(root, text="")
    info_label.pack(pady=10)

    # Etiqueta y entrada para el nombre del jugador
    nombre_label = Label(root, text="Ingresa tu nombre:")
    nombre_label.pack()
    nombre_entry = Entry(root)
    nombre_entry.pack(pady=5)

    # Botón para guardar el puntaje
    guardar_button = Button(root, text="Guardar puntaje", command=guardar_puntaje)
    guardar_button.pack(pady=10)

    # Iniciar el juego
    jugar()

    root.mainloop()
        
#---------------------------------------------------------------

def Asia():
    # Diccionario con las banderas y sus respectivos nombres
    banderas = {
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Australia.png": "AUSTRALIA",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Fiyi.png": "FIYI",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Palaos.png": "PALAOS",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Tonga.png": "TONGA"
    }

    def mostrar_banderas():
        # Obtener una lista de las banderas
        lista_banderas = list(banderas.keys())
        # Barajar las banderas para mostrarlas en orden aleatorio
        random.shuffle(lista_banderas)
        # Mostrar las banderas y generar las opciones
        opciones = []
        for i in range(4):
            opcion = lista_banderas[i]
            opciones.append(opcion)
            # Cargar la imagen de la bandera
            imagen = PhotoImage(file=opcion)
            # Mostrar la imagen en una etiqueta
            label_imagen.configure(image=imagen)
            label_imagen.image = imagen
            # Actualizar las opciones
            botones[i].configure(text=opcion)
        return opciones

    def verificar_respuesta(respuesta):
        global puntaje, vidas
        
        respuesta_bandera = respuesta.widget["text"]
        nombre_pais = banderas[respuesta_bandera]
        
        if respuesta_bandera in opciones:
            puntaje += 1
            info_label.configure(text="¡Respuesta correcta!", fg="green")
        else:
            vidas -= 1
            info_label.configure(text="Respuesta incorrecta. Pierdes una vida.", fg="red")
            
        del banderas[respuesta_bandera]
        
        puntaje_label.configure(text=f"Puntaje: {puntaje}")
        vidas_label.configure(text=f"Vidas restantes: {vidas}")
        
        if vidas > 0:
            jugar()
        else:
            guardar_puntaje()

    def jugar():
        global opciones
        
        opciones = mostrar_banderas()
        
        for boton in botones:
            boton.configure(state=NORMAL)

    def guardar_puntaje():
        nombre_jugador = nombre_entry.get()
        
        # Guardar puntaje en un archivo de texto
        with open("puntajes.txt", "a") as archivo:
            archivo.write(f"{nombre_jugador}: {puntaje}\n")
            
        root.destroy()

    # --- Ventana Principal ---

    root = Toplevel()
    root.title("4 PAISES 1 BANDERA")
    root.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    root.resizable(0,0)
    root.geometry("1200x650+75+10")

    # Etiqueta para mostrar la imagen de la bandera
    label_imagen = Label(root)
    label_imagen.pack(pady=10)

    # Botones para las opciones
    botones = []
    for _ in range(4):
        Son_Click.play()
        boton = Button(root, text="", width=20, state=DISABLED)
        boton.pack(pady=5)
        boton.configure(command=verificar_respuesta)
        botones.append(boton)

    # Etiquetas para el puntaje y las vidas
    puntaje_label = Label(root, text="Puntaje: 0")
    puntaje_label.pack()
    vidas_label = Label(root, text="Vidas restantes: 3")
    vidas_label.pack()

    # Etiqueta para mostrar información al jugador
    info_label = Label(root, text="")
    info_label.pack(pady=10)

    # Etiqueta y entrada para el nombre del jugador
    nombre_label = Label(root, text="Ingresa tu nombre:")
    nombre_label.pack()
    nombre_entry = Entry(root)
    nombre_entry.pack(pady=5)

    # Botón para guardar el puntaje
    guardar_button = Button(root, text="Guardar puntaje", command=guardar_puntaje)
    guardar_button.pack(pady=10)

    # Iniciar el juego
    jugar()

    root.mainloop()
        
#------------------------------------------------------------------

def Europa():
    # Diccionario con las banderas y sus respectivos nombres
    banderas = {
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Australia.png": "AUSTRALIA",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Fiyi.png": "FIYI",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Palaos.png": "PALAOS",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Tonga.png": "TONGA"
    }

    def mostrar_banderas():
        # Obtener una lista de las banderas
        lista_banderas = list(banderas.keys())
        # Barajar las banderas para mostrarlas en orden aleatorio
        random.shuffle(lista_banderas)
        # Mostrar las banderas y generar las opciones
        opciones = []
        for i in range(4):
            opcion = lista_banderas[i]
            opciones.append(opcion)
            # Cargar la imagen de la bandera
            imagen = PhotoImage(file=opcion)
            # Mostrar la imagen en una etiqueta
            label_imagen.configure(image=imagen)
            label_imagen.image = imagen
            # Actualizar las opciones
            botones[i].configure(text=opcion)
        return opciones

    def verificar_respuesta(respuesta):
        global puntaje, vidas
        
        respuesta_bandera = respuesta.widget["text"]
        nombre_pais = banderas[respuesta_bandera]
        
        if respuesta_bandera in opciones:
            puntaje += 1
            info_label.configure(text="¡Respuesta correcta!", fg="green")
        else:
            vidas -= 1
            info_label.configure(text="Respuesta incorrecta. Pierdes una vida.", fg="red")
            
        del banderas[respuesta_bandera]
        
        puntaje_label.configure(text=f"Puntaje: {puntaje}")
        vidas_label.configure(text=f"Vidas restantes: {vidas}")
        
        if vidas > 0:
            jugar()
        else:
            guardar_puntaje()

    def jugar():
        global opciones
        
        opciones = mostrar_banderas()
        
        for boton in botones:
            boton.configure(state=NORMAL)

    def guardar_puntaje():
        nombre_jugador = nombre_entry.get()
        
        # Guardar puntaje en un archivo de texto
        with open("puntajes.txt", "a") as archivo:
            archivo.write(f"{nombre_jugador}: {puntaje}\n")
            
        root.destroy()

    # --- Ventana Principal ---

    root = Toplevel()
    root.title("4 PAISES 1 BANDERA")
    root.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    root.resizable(0,0)
    root.geometry("1200x650+75+10")

    # Etiqueta para mostrar la imagen de la bandera
    label_imagen = Label(root)
    label_imagen.pack(pady=10)

    # Botones para las opciones
    botones = []
    for _ in range(4):
        Son_Click.play()
        boton = Button(root, text="", width=20, state=DISABLED)
        boton.pack(pady=5)
        boton.configure(command=verificar_respuesta)
        botones.append(boton)

    # Etiquetas para el puntaje y las vidas
    puntaje_label = Label(root, text="Puntaje: 0")
    puntaje_label.pack()
    vidas_label = Label(root, text="Vidas restantes: 3")
    vidas_label.pack()

    # Etiqueta para mostrar información al jugador
    info_label = Label(root, text="")
    info_label.pack(pady=10)

    # Etiqueta y entrada para el nombre del jugador
    nombre_label = Label(root, text="Ingresa tu nombre:")
    nombre_label.pack()
    nombre_entry = Entry(root)
    nombre_entry.pack(pady=5)

    # Botón para guardar el puntaje
    guardar_button = Button(root, text="Guardar puntaje", command=guardar_puntaje)
    guardar_button.pack(pady=10)

    # Iniciar el juego
    jugar()

    root.mainloop()
    
#-----------------------------------------------------------------------

def Oceania():
    # Diccionario con las banderas y sus respectivos nombres
    banderas = {
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Australia.png": "AUSTRALIA",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Fiyi.png": "FIYI",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Palaos.png": "PALAOS",
        "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Tonga.png": "TONGA"
    }

    def mostrar_banderas():
        # Obtener una lista de las banderas
        lista_banderas = list(banderas.keys())
        # Barajar las banderas para mostrarlas en orden aleatorio
        random.shuffle(lista_banderas)
        # Mostrar las banderas y generar las opciones
        opciones = []
        for i in range(4):
            opcion = lista_banderas[i]
            opciones.append(opcion)
            # Cargar la imagen de la bandera
            imagen = PhotoImage(file=opcion)
            # Mostrar la imagen en una etiqueta
            label_imagen.configure(image=imagen)
            label_imagen.image = imagen
            # Actualizar las opciones
            botones[i].configure(text=opcion)
        return opciones

    def verificar_respuesta(respuesta):
        global puntaje, vidas
        
        respuesta_bandera = respuesta.widget["text"]
        nombre_pais = banderas[respuesta_bandera]
        
        if respuesta_bandera in opciones:
            puntaje += 1
            info_label.configure(text="¡Respuesta correcta!", fg="green")
        else:
            vidas -= 1
            info_label.configure(text="Respuesta incorrecta. Pierdes una vida.", fg="red")
            
        del banderas[respuesta_bandera]
        
        puntaje_label.configure(text=f"Puntaje: {puntaje}")
        vidas_label.configure(text=f"Vidas restantes: {vidas}")
        
        if vidas > 0:
            jugar()
        else:
            guardar_puntaje()

    def jugar():
        global opciones
        
        opciones = mostrar_banderas()
        
        for boton in botones:
            boton.configure(state=NORMAL)

    def guardar_puntaje():
        nombre_jugador = nombre_entry.get()
        
        # Guardar puntaje en un archivo de texto
        with open("puntajes.txt", "a") as archivo:
            archivo.write(f"{nombre_jugador}: {puntaje}\n")
            
        root.destroy()

    # --- Ventana Principal ---

    root = Toplevel()
    root.title("4 PAISES 1 BANDERA")
    root.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    root.resizable(0,0)
    root.geometry("1200x650+75+10")

    # Etiqueta para mostrar la imagen de la bandera
    label_imagen = Label(root)
    label_imagen.pack(pady=10)

    # Botones para las opciones
    botones = []
    for _ in range(4):
        Son_Click.play()
        boton = Button(root, text="", width=20, state=DISABLED)
        boton.pack(pady=5)
        boton.configure(command=verificar_respuesta)
        botones.append(boton)

    # Etiquetas para el puntaje y las vidas
    puntaje_label = Label(root, text="Puntaje: 0")
    puntaje_label.pack()
    vidas_label = Label(root, text="Vidas restantes: 3")
    vidas_label.pack()

    # Etiqueta para mostrar información al jugador
    info_label = Label(root, text="")
    info_label.pack(pady=10)

    # Etiqueta y entrada para el nombre del jugador
    nombre_label = Label(root, text="Ingresa tu nombre:")
    nombre_label.pack()
    nombre_entry = Entry(root)
    nombre_entry.pack(pady=5)

    # Botón para guardar el puntaje
    guardar_button = Button(root, text="Guardar puntaje", command=guardar_puntaje)
    guardar_button.pack(pady=10)

    # Iniciar el juego
    jugar()

    root.mainloop()
    
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

def ajuste():
    Son_Click.play()
    W_ajustes = Toplevel()
    W_ajustes.title("AJUSTES")
    W_ajustes.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    W_ajustes.resizable(0,0)
    W_ajustes.geometry("700x400+350+170")
    W_ajustes.mainloop()
    
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

Btn_Record = Button(Ventana_Principal, activebackground="gray70", cursor="hand2", text="PUNTAJES", width=30, height=3, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10), command=cargar_puntajes)
Btn_Record.place(x=465, y=380)

Btn_Salir = Button(Ventana_Principal, activebackground="gray70", cursor="hand2", text="SALIR", width=30, height=3, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10), command=Salir)
Btn_Salir.place(x=465, y=460)


ajuste_img = PhotoImage(file="Proyecto Videojuego Py\imagenes\co.png")
Btn_ajustes = Button(Ventana_Principal, image=ajuste_img, cursor="hand2", command=ajuste)
Btn_ajustes.place(x=1130, y=580)


lbl_Create = Label(Ventana_Principal, text="Propiedad Intelectual y Creativa de: Jose Abraham Beristain Navarro y Josue Franciso Rojas Aripez", fg="white", bg="black", font=("Verdana", 10),  borderwidth=5)
lbl_Create.place(x=5, y=620)

# --- Fin ---

Ventana_Principal.mainloop()