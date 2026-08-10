import curses

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

def dibujar_mapa(stdscr, mapa, jugador_x, jugador_y, objetos):
    stdscr.clear()
    for y, fila in enumerate(mapa):
        for x, casilla in enumerate(fila):

            objeto = buscar_objeto(objetos, x, y)

            if jugador_x == x and jugador_y == y:
                stdscr.addstr(y, x, "@")
            elif objeto is not None:
                simbolo = tipos_objeto[objeto["tipo"]]["simbolo"]
                stdscr.addstr(y, x, simbolo)
            else:
                stdscr.addstr(y, x, casilla)

    stdscr.refresh()



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

def interactuar(stdscr, objeto):
    if objeto["tipo"] == "arbol":
        stdscr.addstr(6, 0, "Es un árbol.")
    elif objeto["tipo"] == "cofre":
        stdscr.addstr(6, 0, "Has encontrado un cofre.")
    stdscr.refresh()
    stdscr.getch()

#Main para iniciar el juego con curses
def main(stdscr):
    global jugador_x
    global jugador_y
    global direccion

    while True:
        dibujar_mapa(stdscr, mapa, jugador_x, jugador_y, objetos)

        #Iniciamos las nuevas coordenadas del jugador poniendo las mismas que las iniciales
        nueva_x = jugador_x
        nueva_y = jugador_y

        #Pedimos la tecla
        tecla = stdscr.getch()

        #Teclas de movimiento
        #Dependiendo de la tecla, actualizamos las nuevas coordenadas
        if tecla in [ord('w'), ord('W')] or tecla == curses.KEY_UP:   
            nueva_y = nueva_y - 1
            direccion = "arriba"
        elif tecla in [ord('s'), ord('S')] or tecla == curses.KEY_DOWN:
            nueva_y = nueva_y + 1
            direccion = "abajo"
        elif tecla in [ord('a'), ord('A')] or tecla == curses.KEY_LEFT:
            nueva_x = nueva_x - 1
            direccion = "izquierda"
        elif tecla in [ord('d'), ord('D')] or tecla == curses.KEY_RIGHT:
            nueva_x = nueva_x + 1
            direccion = "derecha"

        if puede_mover(mapa, nueva_x, nueva_y):
            #Actualizamos las coordenadas del jugador con las nuevas
            jugador_x = nueva_x
            jugador_y = nueva_y

        #Teclas de interacción
        if tecla in [ord('e'), ord('E')]:
            casilla_x, casilla_y = obtener_casilla_enfrente(jugador_x, jugador_y, direccion)
            objeto = buscar_objeto(objetos, casilla_x, casilla_y)
            '''
            También funcionaría así:

            objeto = buscar_objeto(
                objetos,
                *obtener_casilla_enfrente(jugador_x, jugador_y, direccion)
            )

            El * desempaqueta la tupla que devuelve obtener_casilla_enfrente(),
            permitiendo pasar sus valores como argumentos separados.
            '''
            if objeto is not None:
                interactuar(stdscr, objeto)
            else:
                stdscr.addstr(6, 0, "No hay nada aquí.")
                stdscr.refresh()
                stdscr.getch()

        if tecla in [ord('q'), ord('Q')]:
            break

curses.wrapper(main)

