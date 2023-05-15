# --- Importando ---

from tkinter import *

# --- Ventana Principal (Inicio) ---

def Ventana_Principal():
    Ventana = Tk()
    Ventana.title("4 PAISES 1 BANDERA")
    Ventana.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
    Ventana.resizable(0,0)
    Ventana.configure(background="black")
    Ventana.geometry("1200x800")
    Ventana.geometry("+30+70")
    Ventana.config(cursor="plus")
    
    lbl_Titulo = Label(Ventana, text="4 Paises 1 Bandera", fg="blue", bg="yellow", font=("Verdana", 80),  borderwidth=5, relief="groove")
    lbl_Titulo.place(x=75, y=40)
    
    Btn_Comenazar = Button(Ventana, text="COMENZAR", width=30, height=3, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10))
    Btn_Comenazar.place(x=450, y=300)
    
    Btn_Record = Button(Ventana, text="RECORDS", width=30, height=3, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10))
    Btn_Record.place(x=450, y=380)
    
    Btn_Salir = Button(Ventana, text="SALIR", width=30, height=3, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10))
    Btn_Salir.place(x=450, y=460)
    
    lbl_Create = Label(Ventana, text="Propiedad Intelectual y Creativa de: Jose Abrham Beristain Navarro y Josue Franciso Rojas Aripez", fg="white", bg="black", font=("Verdana", 10),  borderwidth=5)
    lbl_Create.place(x=5, y=770)
    
    Ventana.mainloop()
    
Ventana_Principal()
