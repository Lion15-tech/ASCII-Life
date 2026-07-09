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

dibujar_mapa(mapa, jugador_x, jugador_y)

def puede_mover(mapa, nueva_x, nueva_y):
    casilla = mapa[nueva_y][nueva_x]

    if casilla == ".":
        return True

    return False
