import tkinter as tk
import random

# Diccionario con las banderas y sus respectivos nombres
banderas = {
    "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Australia.png": "AUSTRALIA",
    "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Fiyi.png": "FIYI",
    "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Palaos.png": "PALAOS",
    "Proyecto Videojuego Py\imagenes\Banderas\Oceania\Tonga.png": "TONGA"
}

# Puntaje inicial del jugador
puntaje = 0

# Vidas del jugador
vidas = 3

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
        imagen = tk.PhotoImage(file=opcion)
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
        boton.configure(state=tk.NORMAL)

def guardar_puntaje():
    nombre_jugador = nombre_entry.get()
    
    # Guardar puntaje en un archivo de texto
    with open("puntajes.txt", "a") as archivo:
        archivo.write(f"{nombre_jugador}: {puntaje}\n")
        
    #root.destroy()

def cargar_puntajes():
    puntajes = []
    
    # Cargar puntajes desde el archivo de texto
    with open("puntajes.txt", "r") as archivo:
        for linea in archivo:
            puntajes.append(linea.strip())
    
    # Crear una nueva ventana para mostrar los puntajes
    ventana_puntajes = tk.Toplevel(root)
    ventana_puntajes.title("Puntajes")
    
    # Crear una etiqueta para cada puntaje
    for puntaje in puntajes:
        label_puntaje = tk.Label(ventana_puntajes, text=puntaje)
        label_puntaje.pack()

# Crear la ventana principal
root = tk.Tk()

# Configurar la ventana principal
root.title("Juego de Banderas")
root.geometry("400x400")

# Etiqueta para mostrar la imagen de la bandera
label_imagen = tk.Label(root)
label_imagen.pack(pady=10)

# Botones para las opciones
botones = []
for _ in range(4):
    boton = tk.Button(root, text="", width=20, state=tk.DISABLED)
    boton.pack(pady=5)
    boton.configure(command=verificar_respuesta)
    botones.append(boton)

# Etiquetas para el puntaje y las vidas
puntaje_label = tk.Label(root, text="Puntaje: 0")
puntaje_label.pack()
vidas_label = tk.Label(root, text="Vidas restantes: 3")
vidas_label.pack()

# Etiqueta para mostrar información al jugador
info_label = tk.Label(root, text="")
info_label.pack(pady=10)

# Etiqueta y entrada para el nombre del jugador
nombre_label = tk.Label(root, text="Ingresa tu nombre:")
nombre_label.pack()
nombre_entry = tk.Entry(root)
nombre_entry.pack(pady=5)

# Botón para guardar el puntaje
guardar_button = tk.Button(root, text="Guardar puntaje", command=guardar_puntaje)
guardar_button.pack(pady=10)

# Botón para cargar los puntajes
cargar_button = tk.Button(root, text="Cargar puntajes", command=cargar_puntajes)
cargar_button.pack(pady=5)

# Iniciar el juego
jugar()

# Iniciar el bucle de la interfaz gráfica
root.mainloop()
