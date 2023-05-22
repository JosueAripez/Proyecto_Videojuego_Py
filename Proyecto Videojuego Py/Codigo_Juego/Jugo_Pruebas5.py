#Abaham: Pruebas de imagenes aleatorias

import random
from tkinter import *

ventana = Tk()
ventana.title("Ejemplo")
ventana.geometry("500x500")
ventana.resizable(0,0)


lbl_Titulo = Label(ventana, text="IMAGENES ALEATORIAS:")
lbl_Titulo.place(x=10, y=10)


#Abraham: Para imagenes aleatorias
imagenes = ["Proyecto videojuego Py/imagenes/Banderas/Africa/Angola-Bandera-Africa.png", "Proyecto videojuego Py/imagenes/Banderas/Africa/Argelia-Bandera-Africa.png", "Proyecto videojuego Py/imagenes/Banderas/Africa/Benin-Bandera-Africa.png", "Proyecto videojuego Py/imagenes/Banderas/Africa/Botsuana-Bandera-Africa.png", "Proyecto videojuego Py/imagenes/Banderas/Africa/Burkina-Faso-Bandera-Africa.png"]
bandera = random.choice(imagenes)
foto=PhotoImage(file=bandera)
lbl_Bandera = Label(ventana, image=foto)
lbl_Bandera.place(x=100, y=50)


#Abraham: Texto de los botones aleatorio
paises = ["Angola", "Argelia", "Benin", "Botsuana", "Burkina Faso"]

texto = random.choice(paises)
btn_Opcion1 = Button(ventana, text=texto)
btn_Opcion1.place(x=50, y=300)

texto = random.choice(paises)
btn_Opcion2 = Button(ventana, text=texto)
btn_Opcion2.place(x=200, y=300)

texto = random.choice(paises)
btn_Opcion3 = Button(ventana, text=texto)
btn_Opcion3.place(x=50, y=400)

texto = random.choice(paises)
btn_Opcion4 = Button(ventana, text=texto)
btn_Opcion4.place(x=200, y=400)



ventana.mainloop()