import objetos

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

    stdscr.addstr(0, 25, "┌──────inventario──────┐")
    stdscr.addstr(1, 25, "│                      │")
    stdscr.addstr(2, 25, "│                      │")
    stdscr.addstr(3, 25, "│                      │")
    stdscr.addstr(4, 25, "│                      │")
    stdscr.addstr(5, 25, "│                      │")
    stdscr.addstr(6, 25, "│                      │")
    stdscr.addstr(7, 25, "└──────────────────────┘")

    stdscr.addstr(8, 0, "┌───────────────────────────────────────────────┐")
    stdscr.addstr(9, 0, "│                                               │")
    stdscr.addstr(10, 0, "└───────────────────────────────────────────────┘")


def dibujar_mapa(stdscr, mapa, jugador_x, jugador_y):
    for y, fila in enumerate(mapa):
        for x, casilla in enumerate(fila):

            objeto = objetos.buscar_objeto(objetos.objetos, x, y)

            if jugador_x == x and jugador_y == y:
                stdscr.addstr(y + 1, x + 1, "@")
            elif objeto is not None:
                simbolo = objetos.tipos_objeto[objeto["tipo"]]["simbolo"]
                stdscr.addstr(y + 1, x + 1, simbolo)
            else:
                stdscr.addstr(y + 1, x + 1, casilla)


def dibujar_inventario(stdscr, inventario):
    stdscr.addstr(1, 26, f"Manzanas: {inventario['manzanas']}")
    stdscr.addstr(2, 26, f"Agua: {inventario['agua']}")