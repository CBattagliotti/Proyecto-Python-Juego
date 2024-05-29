from random import choice
from colorama import Fore,Style

opciones = ["Tazon", "karaoke", "Sistemas", "rosquita", "Cielo", "Oasis", "python"]

# Elige una palabra de la lista al azar.
elegir_palabra = lambda lista: choice(lista).upper()

palabra = elegir_palabra(opciones)

# def elegir_palabra(lista):
#     palabra = random.choice(lista).upper()  Si solo puse "import random" debo poner "random.choice"
#     return palabra

#numero_oculto = random.randint(1,4)

#opciones = {1 : "Tazon",
            #2 : "Cielo",
            #3 : "python"
           #}
#palabra = opciones[numero_oculto]


def saludo():
     print(Fore.LIGHTCYAN_EX + "  Bienvenido a 'Adivina la palabra'!!\n\n  Comienzas con 5 vidas, aprovechalas!\n")

saludo()


def mostrar_guiones(palabra):
    palabra_escondida = ""
    for letra in palabra:
        letra = "-"
        palabra_escondida = palabra_escondida + letra
    print(Fore.WHITE + "\n[ Si en algun momento quieres salir del juego ingresa '#' ]\n")
    print(Fore.LIGHTMAGENTA_EX + f"\nLa palabra tiene {len(palabra)} letras: \n" + Fore.WHITE)
    print(palabra_escondida + "\n")
    return palabra_escondida 

print(mostrar_guiones(palabra))