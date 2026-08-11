import curses

def dibujar_interfaz(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "┌─────────mapa──────────┐")
    stdscr.addstr(1, 0, "│                       │")
    stdscr.addstr(2, 0, "│                       │")
    stdscr.addstr(3, 0, "│                       │")
    stdscr.addstr(4, 0, "│                       │")
    stdscr.addstr(5, 0, "│                       │")
    stdscr.addstr(6, 0, "│                       │")
    stdscr.addstr(7, 0, "└───────────────────────┘")

    stdscr.addstr(0, 24, "┌──────inventario──────┐")
    stdscr.addstr(1, 24, "│                      │")
    stdscr.addstr(2, 24, "│                      │")
    stdscr.addstr(3, 24, "│                      │")
    stdscr.addstr(4, 24, "│                      │")
    stdscr.addstr(5, 24, "│                      │")
    stdscr.addstr(6, 24, "│                      │")
    stdscr.addstr(7, 24, "└──────────────────────┘")

    stdscr.addstr(8, 0, "┌──────────────────────────────────────────────┐")
    stdscr.addstr(9, 0, "│                                              │")
    stdscr.addstr(10, 0, "└──────────────────────────────────────────────┘")





def main(stdscr):

    #coordenadas iniciales del jugador
    jugador_x = 3
    jugador_y = 2

    #Iniciamos al jugador
    stdscr.clear()
    stdscr.refresh()
    dibujar_interfaz(stdscr)
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



