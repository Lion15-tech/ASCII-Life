#Coordenadas del jugador
jugador_x = 4  
jugador_y = 2

# Dirección inicial del jugador
direccion = "arriba"  

def obtener_casilla_enfrente(jugador_x, jugador_y, direccion):
    if direccion == "arriba":
        return jugador_x, jugador_y - 1
    elif direccion == "abajo":
        return jugador_x, jugador_y + 1
    elif direccion == "izquierda":
        return jugador_x - 1, jugador_y
    elif direccion == "derecha":
        return jugador_x + 1, jugador_y

def puede_mover(mapa, nueva_x, nueva_y):
    casilla = mapa[nueva_y][nueva_x]

    if casilla == ".":
        return True

    return False