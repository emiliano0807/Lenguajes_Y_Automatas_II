import random
import math
import matplotlib.pyplot as plt

# Diccionario de coordenadas de las ciudades
ciudades_coord = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754, -103.346253),
    'Monterrey': (25.691611, -100.321838),
    'QuintanaRoo': (21.163111, -86.802315),
    'Michohacan': (19.701400, -101.208296),
    'Aguascalientes': (21.876410, -102.264386),
    'CDMX': (19.432713, -99.133183),
    'QRO': (20.597194, -100.386670)
}
nombres_ciudades = list(ciudades_coord.keys())
coordenadas = [ciudades_coord[ciudad] for ciudad in nombres_ciudades]

# Distancia Euclidiana entre dos cuidades.
def distancia(ciudad1, ciudad2):
    return math.sqrt((ciudad1[0] - ciudad2[0])**2 + (ciudad1[1] - ciudad2[1])**2)
# Longitud total de la ruta.
def longitud_ruta(ruta, coords):
    return sum(distancia(coords[ruta[i]], coords[ruta[(i + 1) % len(ruta)]]) for i in range(len(ruta)))
# Vecinos intercambiando dos ciudades en la ruta.
def generar_vecinos(ruta):
    vecinos = []
    for i in range(len(rute)):
        for j in range(i + 1, len(ruta)):
            vecino = ruta[:]
            vecino[i], vecino[j], vecino[i]
            vecino.append((vecino, (ruta[i], ruta[j])))
    return vecinos
# Algoritmo de busqueda Tabú.

