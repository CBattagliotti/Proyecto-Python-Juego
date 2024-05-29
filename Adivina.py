from random import choice
from colorama import Fore,Style

opciones = ["Tazon", "karaoke", "Sistemas", "rosquita", "Cielo", "Oasis", "python"]

# Elige una palabra de la lista al azar.
elegir_palabra = lambda lista: choice(lista).upper()

palabra = elegir_palabra(opciones)



def decorador(funcion):
    def decorar():
        print("\n" + Fore.WHITE  + Style.BRIGHT + ("*" * 40) + "\n")
        funcion()
        print(Fore.WHITE + "*" * 40 + "\n")
    return decorar


@decorador
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



pedir_letra = lambda : input(Fore.LIGHTYELLOW_EX + "Por favor ingresa una letra: " + Fore.WHITE).upper()



def validar_letra(letra):
    numeros = ["1","2","3","4","5","6","7","8","9"]  

    if len(letra) != 1:
        print(Fore.LIGHTRED_EX + "\nError. Debes ingresar 1 letra a la vez" + Fore.WHITE)
        return False
    
    elif letra in numeros:
        print(Fore.LIGHTRED_EX + "\nValor incorrecto. Debes ingresar una letra, no un numero." + Fore.WHITE)
        return False
    
    elif letra in palabra:      
        print(Fore.LIGHTGREEN_EX + "\nMuy bien! Es correcta.\n" + Fore.WHITE)
        return True  
    
    else:
        print(Fore.LIGHTRED_EX + "\nQue mal, no adiviniste :(\n" + Fore.WHITE)
        return False



@decorador
def fin_juego():
    print("\n " + Fore.WHITE + ("=" * 10) + Fore.RED + "  FIN DEL JUEGO  " + Fore.WHITE + ("=" * 10) +"\n\n")
    print(Fore.RED + "Te quedaste sin vidas :(\nNo te preocupes, la proxima lo conseguiras!!\n")
    print(Fore.RED + f"La palabra era: '{palabra}'\n")



@decorador
def ganar():
    print(" " + Fore.WHITE + ("=" * 5) + Fore.GREEN + " FELICIDADES!! HAS GANADO!! " + Fore.WHITE + ("=" * 5) + "\n")
    print(Fore.GREEN + f"La palabra era: '{palabra}' ( pero eso ya lo sabias ;) )\n") 


@decorador
def salir():
    print(Fore.RED + "Has salido\n\nVuelve cuando quieras!\n" + Fore.WHITE)

