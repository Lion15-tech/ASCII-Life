import os
import time

#Definimos el mapa como una lista de listas 
mapa = [
    # 0    1    2    3    4    5    6    7    8    9
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"], # 0
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"], # 1
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"], # 2
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"], # 3
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]  # 4
]
tipos_objeto = {
    "arbol": {
        "simbolo": "T"
    },
    "cofre": {
        "simbolo": "C"
    }
}
objetos = [
    {
        "tipo": "arbol",
        "x": 4,
        "y": 1
    },
    {
        "tipo": "cofre",
        "x": 1,
        "y": 1
    }
]

#Coordenadas del jugador
jugador_x = 4  
jugador_y = 2
direccion = "arriba"  # Dirección inicial del jugador

def limpiar_pantalla():                                
    if os.name == 'nt': 
        os.system('cls') 
    else:
        os.system('clear')

def dibujar_mapa(mapa, jugador_x, jugador_y, objetos): 
    #Para cada fila del mapa
    for y, fila in enumerate(mapa): 
        #Por cada casilla de la fila
        for x, casilla in enumerate(fila):   
            #Si la casilla es la del jugador, lo dibujamos primero
            if x == jugador_x and y == jugador_y:
                print("@", end="")
                continue # Saltamos a la siguiente casilla para no dibujar nada más aquí

            #Revisamos todos los objetos de la lista
            objeto = buscar_objeto(objetos, x, y)
            if objeto is not None:
                print(tipos_objeto[objeto["tipo"]]["simbolo"], end="")
            else:
            #Si revisamos todos los objetos y NO encontramos ninguno, dibujamos el terreno normal
                print(casilla, end="")

        print()


def puede_mover(mapa, nueva_x, nueva_y):
    casilla = mapa[nueva_y][nueva_x]

    if casilla == ".":
        return True

    return False

def buscar_objeto(objetos, x, y):
    for objeto in objetos:
        if objeto["x"] == x and objeto["y"] == y:
            return objeto
    return None

def obtener_casilla_enfrente(jugador_x, jugador_y, direccion):
    if direccion == "arriba":
        return jugador_x, jugador_y - 1
    elif direccion == "abajo":
        return jugador_x, jugador_y + 1
    elif direccion == "izquierda":
        return jugador_x - 1, jugador_y
    elif direccion == "derecha":
        return jugador_x + 1, jugador_y

def interactuar(objeto):
    if objeto["tipo"] == "arbol":
        print("Es un árbol.")
    elif objeto["tipo"] == "cofre":
        print("Has encontrado un cofre.")

while True:
    limpiar_pantalla()
    dibujar_mapa(mapa, jugador_x, jugador_y, objetos)

    nueva_x = jugador_x
    nueva_y = jugador_y

    tecla_presionada = input("WASD: ").lower()

    if tecla_presionada == "a":
        nueva_x = jugador_x - 1
        direccion = "izquierda"
    elif tecla_presionada == "s":
        nueva_y = jugador_y + 1
        direccion = "abajo"
    elif tecla_presionada == "d":
        nueva_x = jugador_x + 1
        direccion = "derecha"
    elif tecla_presionada == "w":
        nueva_y = jugador_y - 1
        direccion = "arriba"

    if tecla_presionada == "e":
        casilla_x, casilla_y = obtener_casilla_enfrente(jugador_x, jugador_y, direccion)
        objeto = buscar_objeto(objetos, casilla_x, casilla_y) 
        if objeto is not None:
            interactuar(objeto)
            time.sleep(1.5)  # Pausa para que el jugador pueda leer el mensaje
        else:
            print("No hay nada aquí")
            time.sleep(1.5)
        '''
        También funcionaría así:

        objeto = buscar_objeto(
            objetos,
            *obtener_casilla_enfrente(jugador_x, jugador_y, direccion)
        )

        El * desempaqueta la tupla que devuelve obtener_casilla_enfrente(),
        permitiendo pasar sus valores como argumentos separados.
        '''
    
    if puede_mover(mapa, nueva_x, nueva_y):
        jugador_x = nueva_x
        jugador_y = nueva_y
