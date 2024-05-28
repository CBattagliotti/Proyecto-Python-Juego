from random import choice

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