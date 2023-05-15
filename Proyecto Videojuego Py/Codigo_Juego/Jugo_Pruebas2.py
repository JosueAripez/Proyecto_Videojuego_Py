# --- Importando ---

from tkinter import *
from tkinter import messagebox

# --- Funciones ---

def Ventana_Menu():
    print("")

def Records():
    print("")
    import webbrowser
    webbrowser.open("www.google.com")
    
def Salir():
    Ventana_Principal.destroy()
    
# --- Ventana_Principal Principal (Inicio) ---

Ventana_Principal = Tk()
Ventana_Principal.title("4 PAISES 1 BANDERA")
Ventana_Principal.iconbitmap("Proyecto Videojuego Py\imagenes\icono.ico")
Ventana_Principal.resizable(0,0)
Ventana_Principal.configure(background="black")
Ventana_Principal.geometry("1200x800")
Ventana_Principal.geometry("+30+70")
Ventana_Principal.config(cursor="plus")
    
lbl_Titulo = Label(Ventana_Principal, text="4 Paises 1 Bandera", fg="blue", bg="yellow", font=("Verdana", 80),  borderwidth=5, relief="groove")
lbl_Titulo.place(x=75, y=40)
    
Btn_Comenazar = Button(Ventana_Principal, text="COMENZAR", width=30, height=3, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10))
Btn_Comenazar.place(x=450, y=300)
    
Btn_Record = Button(Ventana_Principal, text="RECORDS", width=30, height=3, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10), command=Records)
Btn_Record.place(x=450, y=380)
    
Btn_Salir = Button(Ventana_Principal, text="SALIR", width=30, height=3, background="white", fg="black", borderwidth=5, relief="raised", font=("Verdana", 10), command=Salir)
Btn_Salir.place(x=450, y=460)
    
lbl_Create = Label(Ventana_Principal, text="Propiedad Intelectual y Creativa de: Jose Abrham Beristain Navarro y Josue Franciso Rojas Aripez", fg="white", bg="black", font=("Verdana", 10),  borderwidth=5)
lbl_Create.place(x=5, y=770)
    
Ventana_Principal.mainloop()
    

