from random import choice
from colorama import Fore,Style

opciones = ["Tazon", "karaoke", "Sistemas", "rosquita", "Cielo", "Oasis", "python"]

# Elige una palabra de la lista al azar.
elegir_palabra = lambda lista: choice(lista).upper()

palabra = elegir_palabra(opciones)


# Agrega caracteristicas que seran utilizadas en otras funciones, sin modificarlas permanentemente
def decorador(funcion):
    def decorar():
        print("\n" + Fore.WHITE  + Style.BRIGHT + ("*" * 40) + "\n")
        funcion()
        print(Fore.WHITE + "*" * 40 + "\n")
    return decorar


# Imprime el saludo de bienvenida al juego
@decorador
def saludo():
     print(Fore.LIGHTCYAN_EX + "  Bienvenido a 'Adivina la palabra'!!\n\n  Comienzas con 5 vidas, aprovechalas!\n")

saludo()


# Muestra en la terminal la palabra reemplazando cada letra por un guion medio
def mostrar_guiones(palabra):
    palabra_escondida = ""
    for letra in palabra:
        letra = "-"
        palabra_escondida = palabra_escondida + letra
    print(Fore.WHITE + "\n[ Si en algun momento quieres salir del juego ingresa '#' ]\n")
    print(Fore.LIGHTMAGENTA_EX + f"\nLa palabra tiene {len(palabra)} letras: \n" + Fore.WHITE)
    print(palabra_escondida + "\n")
    return palabra_escondida 


# Solicita el ingreso de una letra y la guarda en una variable para ser utilizada por otras funciones
pedir_letra = lambda : input(Fore.LIGHTYELLOW_EX + "Por favor ingresa una letra: " + Fore.WHITE).upper()


# Evalua si la letra ingresada por el usuario en correcta
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


# Imprime mensajes de finalizacion del juego cuando el usuario ha perdido
@decorador
def fin_juego():
    print("\n " + Fore.WHITE + ("=" * 10) + Fore.RED + "  FIN DEL JUEGO  " + Fore.WHITE + ("=" * 10) +"\n\n")
    print(Fore.RED + "Te quedaste sin vidas :(\nNo te preocupes, la proxima lo conseguiras!!\n")
    print(Fore.RED + f"La palabra era: '{palabra}'\n")


# Imprime mensajes de finalizacion del juego cuando el usuario ha ganado
@decorador
def ganar():
    print(" " + Fore.WHITE + ("=" * 5) + Fore.GREEN + " FELICIDADES!! HAS GANADO!! " + Fore.WHITE + ("=" * 5) + "\n")
    print(Fore.GREEN + f"La palabra era: '{palabra}' ( pero eso ya lo sabias ;) )\n") 


# Imprime mensajes de salida cuando el usuario ha presionado la tecla de escape "#"
@decorador
def salir():
    print(Fore.RED + "Has salido\n\nVuelve cuando quieras!\n" + Fore.WHITE)


# Se encarga de reemplazar los guiones por las letras correctas, y de informar las letras incorrectas y vidas remanentes.
def funcionamiento(palabra_guiones):
    vidas = 5
    lista_incorrectas = []
    lista = list(palabra_guiones)
    
    while vidas > 0:
        letra = pedir_letra()
        if letra == "#":
            salir()
            break
            
        elif validar_letra(letra) == True:
            i = 0
            for l in palabra:
                if l == letra:
                    lista[i] = letra
                i += 1

            palabra_nueva = "".join(lista)
            print(palabra_nueva + "\n") 

            if palabra_nueva.count("-") == 0:
            #if palabra_nueva == palabra:
                ganar()
                break

        else:
            if letra in lista_incorrectas:
                print(Fore.LIGHTRED_EX + "Ya has intentado con esa letra. Ingresa una distinta" + Fore.WHITE)
            else:
                lista_incorrectas.append(letra)
                vidas -= 1
            print(f"Letras incorrectas ingresadas: {lista_incorrectas}")
            print(Fore.LIGHTRED_EX + f"Tienes ahora {vidas} vidas\n\n" + Fore.WHITE)
            if vidas == 0:
                fin_juego()
                break


palabra_escondida  = mostrar_guiones(palabra)

funcionamiento(palabra_escondida)