import os

#Definimos el mapa como una lista de listas 
mapa = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

#Coordenadas del jugador
jugador_x = 4  
jugador_y = 2

def limpiar_pantalla():                                
    if os.name == 'nt': 
        os.system('cls') 
    else:
        os.system('clear')

def dibujar_mapa(mapa, jugador_x, jugador_y): 
    #                                                 así tenemos "y"    
    #Para cada fila del mapa                                  0         # o .
    for y, fila in enumerate(mapa): #el enumerate nos da el indice y el valor de la lista
        #Por cada casilla de la fila
        for x, casilla in enumerate(fila):
            #Si esta casilla es donde esta el jugador 
            if x == jugador_x and y == jugador_y:
                #Dibujamos el jugador
                print("@", end="") #El end="" es para que no haga un salto de linea
            else:
                #Dibujamos el terreno normal
                print(casilla, end="")

        print()

def puede_mover(mapa, nueva_x, nueva_y):
    casilla = mapa[nueva_y][nueva_x]

    if casilla == ".":
        return True

    return False

while True:
    limpiar_pantalla()
    dibujar_mapa(mapa, jugador_x, jugador_y)

    nueva_x = jugador_x
    nueva_y = jugador_y

    tecla_presionada = input("WASD: ").lower()

    if tecla_presionada == "a":
        nueva_x = jugador_x - 1
    elif tecla_presionada == "s":
        nueva_y = jugador_y + 1
    elif tecla_presionada == "d":
        nueva_x = jugador_x + 1
    elif tecla_presionada == "w":
        nueva_y = jugador_y - 1
    
    if puede_mover(mapa, nueva_x, nueva_y):
        jugador_x = nueva_x
        jugador_y = nueva_y
