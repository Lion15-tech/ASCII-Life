import inventario

#Qué objetos en concreto existen en el mapa y su estado
objetos = [
    {
        "tipo": "arbol",
        "x": 4,
        "y": 1
    },
    {
        "tipo": "cofre",
        "x": 1,
        "y": 1,
        "abierto": False 
    },
    {
        "tipo": "piedra",
        "x": 3,
        "y": 3,
    }
]
#Carácterísticas de los objetos del mapa, como su símbolo o mensaje que tiene que mostrar
tipos_objeto = {
    "arbol": {
        "simbolo": "T",
        "mensaje": "Es un arbol"
    },
    "cofre": {
        "simbolo": "C",
        "mensaje": "Has encontrado un cofre",
        "mensaje_abierto": "Es un cofre abierto",
        "contenido": {
            "manzanas": 3,
            "agua": 1,
            "piedras": 2,
            "pan": 1
        }
    },
    "piedra":{
        "simbolo": "o",
        "mensaje": "Es una piedra"
    }
}

def buscar_objeto(objetos, x, y):
    for objeto in objetos:
        if objeto["x"] == x and objeto["y"] == y:
            return objeto
    return None


def interactuar(stdscr, objeto):
    tipo = objeto["tipo"]
    informacion = tipos_objeto[tipo]

    if "contenido" in informacion:
        if not objeto["abierto"]:
            objeto["abierto"] = True
            #Ponemos + "     " para "limpiar" la pantalla por si hay más texto y así evitar que se encime
            stdscr.addstr(9, 1, informacion["mensaje"] + "        ")
            stdscr.getch()
            for item, cantidad in informacion["contenido"].items():
                stdscr.addstr(9, 1, f"Recibiste: {cantidad} {item}.        ")
                stdscr.getch()
                inventario.agregar_item(item, cantidad)
        else:
            stdscr.addstr(9, 1, informacion["mensaje_abierto"]+ "        ")

    else:
        stdscr.addstr(9, 1, informacion["mensaje"] + "        ")
    stdscr.refresh()
    stdscr.getch()
