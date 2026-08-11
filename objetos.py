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

def buscar_objeto(objetos, x, y):
    for objeto in objetos:
        if objeto["x"] == x and objeto["y"] == y:
            return objeto
    return None


def interactuar(stdscr, objeto):
    if objeto["tipo"] == "arbol":
        stdscr.addstr(9, 1, "Es un árbol.")
    elif objeto["tipo"] == "cofre":
        stdscr.addstr(9, 1, "Has encontrado un cofre.")
    stdscr.refresh()
    stdscr.getch()
