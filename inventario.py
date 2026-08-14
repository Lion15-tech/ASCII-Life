inventario = {
    "manzanas": 0,
    "agua": 0
}

def agregar_item(nombre, cantidad):
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        inventario[nombre] = cantidad


def quitar_item(nombre, cantidad):
    if nombre in inventario:
        inventario[nombre] = max(0, inventario[nombre] - cantidad)


def obtener_cantidad(nombre):
    if nombre in inventario:
        return inventario[nombre]
    return 0