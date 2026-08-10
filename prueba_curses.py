import curses

def main(stdscr):

    #coordenadas iniciales del jugador
    jugador_x = 10
    jugador_y = 5

    #Iniciamos al jugador
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(jugador_y, jugador_x, "@")
    stdscr.refresh()

    #Voy a comentar el código para ahorita que voy aprendiendo no perderme tanto
    while True:
        #Pedimos la tecla
        tecla = stdscr.getch()

        #Iniciamos las nuevas coordenadas del jugador poniendo las mismas que las iniciales
        nueva_x = jugador_x
        nueva_y = jugador_y

        #Dependiendo de la tecla, actualizamos las nuevas coordenadas
        if tecla in [ord('w'), ord('W')]:   
            nueva_y = nueva_y - 1
        elif tecla in [ord('s'), ord('S')]:
            nueva_y = nueva_y + 1
        elif tecla in [ord('a'), ord('A')]:
            nueva_x = nueva_x - 1
        elif tecla in [ord('d'), ord('D')]:
            nueva_x = nueva_x + 1

        #Guardamos las coordenadas anteriores del jugador, con las anteriores
        anterior_x = jugador_x
        anterior_y = jugador_y

        #Actualizamos las coordenadas del jugador con las nuevas
        jugador_x = nueva_x
        jugador_y = nueva_y

        #Borramos la posición anterior del jugador y dibujamos la nueva
        stdscr.addstr(anterior_y, anterior_x, ".")
        stdscr.addstr(jugador_y, jugador_x, "@")
        stdscr.refresh()

curses.wrapper(main)

# W = 87
# A = 97
# S = 115
# D = 100

# Flecha arriba = 259
# Flecha izquierda =  260
# Flecha abajo = 258
# Flecha derecha = 261



