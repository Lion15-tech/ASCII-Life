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
    #VALIDACIÓN VERTICAL (Filas)
    #len(mapa) nos da el número de filas porque cada fila es una lista dentro de la lista principal
    if nueva_y >= 0 and nueva_y < len(mapa):
        #VALIDACIÓN HORIZONTAL (Columnas)
        #len(mapa[nueva_y]) nos da el número de columnas de la fila específica (nueva_y)
        if nueva_x >= 0 and nueva_x < len(mapa[0]):
            # Como los dos 'if' anteriores confirmaron que la coordenada es 100% segura continuamos
            casilla = mapa[nueva_y][nueva_x]
            if casilla == ".":
                return True
    # Si el código llega a esta línea, significa que alguna de las condiciones de arriba falló
    return False
