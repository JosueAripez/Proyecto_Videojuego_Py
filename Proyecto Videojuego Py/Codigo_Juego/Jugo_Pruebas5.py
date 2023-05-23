#Abaham: Pruebas de imagenes aleatorias

import random
from tkinter import *
# --- Ventana (Africa) ---

ventana_Africa= Tk()
ventana_Africa.title("4 PAISES 1 BANDERA")
ventana_Africa.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
ventana_Africa.resizable(0,0)
ventana_Africa.configure(background="black")
ventana_Africa.geometry("1200x650")
ventana_Africa.geometry("+75+10")
ventana_Africa.config(cursor="hand2")


lbl_Titulo = Label(ventana_Africa, text="IMAGENES ALEATORIAS:", background="black", fg="white")
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