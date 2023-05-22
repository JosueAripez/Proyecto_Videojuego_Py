#Abaham: Pruebas de imagenes aleatorias

import random
from tkinter import *

root=Tk()
root.title("Ejemplo")


frame=Frame(root)
frame.pack()

Label(frame, text="IMAGENES ALEATORIAS:", width=50).pack()

imagenes = ["Proyecto videojuego Py/imagenes/Banderas/Africa/Angola-Bandera-Africa.png", "Proyecto videojuego Py/imagenes/Banderas/Africa/Argelia-Bandera-Africa.png", "Proyecto videojuego Py/imagenes/Banderas/Africa/Benin-Bandera-Africa.png", "Proyecto videojuego Py/imagenes/Banderas/Africa/Botsuana-Bandera-Africa.png", "Proyecto videojuego Py/imagenes/Banderas/Africa/Burkina-Faso-Bandera-Africa.png"]
palabra = random.choice(imagenes)
foto=PhotoImage(file=palabra)
Label(root, image=foto).pack()



root.mainloop()