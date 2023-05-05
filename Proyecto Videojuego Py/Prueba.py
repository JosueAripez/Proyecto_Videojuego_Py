#Probando Visual Studio y Git Hub

import os

def Escribe_Mensaje():
    palabra = input("Ingresa una palabra a imprimir: ")
    print(palabra)
    
def Imprime_Mensaje():
    print("JACOB PAJERO")

def Imprime_Numero():
    print("12345098765432")

def menu():
    print("-------MENU-------")
    print("1.- Imprimir un mensaje ya escirto ")
    print("2.- Escribir tu propio mensaje ")
    print("3.- Imprime un numero ya escrito ")
    print("0.- Salir ")
    
while True:
    menu()
    
    op = int(input("Eliga una opcion: "))
    
    if op == 1:
        Imprime_Mensaje()
        input("Enter para borrar")
        os.system('cls')
        continue
    elif op == 2:
        Escribe_Mensaje()
        input("Enter para borrar")
        os.system('cls')
        continue
    elif op == 3:
        Imprime_Numero()
        input("Enter para borrar")
        os.system('cls')
    elif op == 0:
        break