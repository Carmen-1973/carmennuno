#Juego del dragón: el jugador se enfrenta a dos cuevas, una 
#con un dragón bueno que comparte su tesoro, y otra con un
#dragón malo que se come a cualquiera que pise su cueva
#el jugador tiene que elegir a que cueva entrar, sin saber de 
#antemano que dragón la ocupa


#empezamos importando los modulos random y time
#random nos permite elegir numeros al azar
#time para funciones relacionadas con el tiempo

import random
import time
from pip._vendor.distlib.compat import raw_input

#definicion de la función introducción()

def introduccion():
    print("Estamos en una tierra llena de dragones. Delante nuestro ")
    print("se ven dos cuevas. En una cueva, el dragón es amigable ")
    print("y compartirá el tesoro contigo. El otro dragón ")
    print("es codicioso y hambriento, y te va a comer ni bien te vea.")
    print("")
#end introduccion()

#definición de la funcion cambiarCueva()
#con esta función el usuario tiene que elegir si entra en la cueva 1
#o en la 2
#creamos la variable cueva que almacena una cadena vacia
#generamos un bucle while que se ejecuta siempre que el usuario elija
#1 o 2 

def cambiarCueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        print("A qué cueva quieres entrar? 1 o 2?")
        cueva = input()
    #end while    
    return cueva
#end CambiarCueva()

#definición de la función cheqCueva(cambiarCueva)
#esta función va a necesitar un parámetro de entrada, en este
#caso, cambiarCueva, por lo que se pone entre los paréntesis al
#definir la función

#llamamos a la función time.sleep() para que haga una pausa
#(2 segundos) después de cada frase

def cheqCueva(cambiarCueva):
    print("Te acercas a la cueva...")
    time.sleep(2)
    print("Esta oscuro y tenebroso...")
    time.sleep(2)
    print("Un gran dragón salta delante tuyo, abre su boca y...")
    print("")
    time.sleep(2)
    
    #ahora decidimos al azar en que cueva esta el dragón amistoso
    friendlyCueva = random.randint(1,2)
    
    if cambiarCueva == str(friendlyCueva):
        print("Te entrega el tesoro...")
        puntos = 100
        print("Has ganado " + str(puntos) + " puntos")
    else:
        print("El dragón te come de un bocado...")
#end cheqCueva()

#Aqui comienza el juego

empezarNuevo = ("si")

#iniciamos con la variable empezarNuevo con el valor "si" para 
#que la primera vez que entramos en el juego el ciclo sea verdadero
#y se inicie

while empezarNuevo == ("s") or empezarNuevo == ("si"):
    
    introduccion()
    
    numCaverna = cambiarCueva()
    #la funcion cambiarCueva() permite al jugador elegir la
    #caverna en la que quiere entrar, y lo que elija se guarda
    #en la variable numCaverna
    
    cheqCueva(numCaverna)
    
    print("Quieres jugar de nuevo? si o no?")
    empezarNuevo = input()
    
    if empezarNuevo != ("s") or empezarNuevo != ("si"):
        puntos = 100
        pass
    
    
    
    
    
    

    
    
    