import curses
import interfaz
import objetos 
import jugador

#Definimos el mapa como una lista de listas 
mapa = [
    # 0    1    2    3    4    5    6    7    8    9
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"], # 0
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"], # 1
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"], # 2
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"], # 3
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]  # 4
]

inventario = {
    "manzanas": 0,
    "agua": 0
}

#Main para iniciar el juego con curses
def main(stdscr):
    while True:
        interfaz.dibujar_interfaz(stdscr)
        interfaz.dibujar_inventario(stdscr, inventario)
        interfaz.dibujar_mapa(stdscr, mapa, jugador.jugador_x, jugador.jugador_y)

        #Iniciamos las nuevas coordenadas del jugador poniendo las mismas que las iniciales
        nueva_x = jugador.jugador_x
        nueva_y = jugador.jugador_y

        #Pedimos la tecla
        tecla = stdscr.getch()

        #Teclas de movimiento
        #Dependiendo de la tecla, actualizamos las nuevas coordenadas
        if tecla in [ord('w'), ord('W')] or tecla == curses.KEY_UP:   
            nueva_y = nueva_y - 1
            jugador.direccion = "arriba"
        elif tecla in [ord('s'), ord('S')] or tecla == curses.KEY_DOWN:
            nueva_y = nueva_y + 1
            jugador.direccion = "abajo"
        elif tecla in [ord('a'), ord('A')] or tecla == curses.KEY_LEFT:
            nueva_x = nueva_x - 1
            jugador.direccion = "izquierda"
        elif tecla in [ord('d'), ord('D')] or tecla == curses.KEY_RIGHT:
            nueva_x = nueva_x + 1
            jugador.direccion = "derecha"

        if jugador.puede_mover(mapa, nueva_x, nueva_y):
            #Actualizamos las coordenadas del jugador con las nuevas
            jugador.jugador_x = nueva_x
            jugador.jugador_y = nueva_y

        #Teclas de interacción
        if tecla in [ord('e'), ord('E')]:
            casilla_x, casilla_y = jugador.obtener_casilla_enfrente(jugador.jugador_x, 
                                                                    jugador.jugador_y, 
                                                                    jugador.direccion)
            objeto = objetos.buscar_objeto(objetos.objetos, casilla_x, casilla_y)
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
                objetos.interactuar(stdscr, objeto)
            else:
                stdscr.addstr(9, 1, "No hay nada aquí.")
                stdscr.refresh()
                stdscr.getch()

        if tecla in [ord('q'), ord('Q')]:
            break

curses.wrapper(main)

