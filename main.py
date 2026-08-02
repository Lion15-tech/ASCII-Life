import os

#Definimos el mapa como una lista de listas 
mapa = [
    # 0    1    2    3    4    5    6    7    8    9
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"], # 0
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"], # 1
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"], # 2
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"], # 3
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]  # 4
]
objetos = [
    {
        "tipo": "arbol",
        "simbolo": "T",
        "x": 4,
        "y": 1
    },
    {
        "tipo": "cofre",
        "simbolo": "C",
        "x": 1,
        "y": 1
    }
]


#Coordenadas del jugador
jugador_x = 4  
jugador_y = 2

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
            
            objeto_encontrado = False

            #Revisamos todos los objetos de la lista
            for objeto in objetos:
                if objeto["x"] == x and objeto["y"] == y:
                    print(objeto["simbolo"], end="")
                    objeto_encontrado = True
                    break 

            #Si revisamos todos los objetos y NO encontramos ninguno, dibujamos el terreno normal
            if not objeto_encontrado:
                print(casilla, end="")

        print()


def puede_mover(mapa, nueva_x, nueva_y):
    casilla = mapa[nueva_y][nueva_x]

    if casilla == ".":
        return True

    return False

while True:
    limpiar_pantalla()
    dibujar_mapa(mapa, jugador_x, jugador_y, objetos)

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
