import math
import random
from Busqueda_Tabu import tabu_search

coord = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754, -103.346254),
    'Monterrey': (25.691611, -100.321838),
    'QuintanaRoo': (21.163112, -86.802315),
    'Michohacan': (19.701400, -101.208297),
    'Aguascalientes': (21.876410, -102.264387),
    'CDMX': (19.432713, -99.133183),
    'QRO': (20.597194, -100.386670)
}

def distancia(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def evalua_ruta(ruta):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(coord[ruta[i]], coord[ruta[i+1]])
    total += distancia(coord[ruta[-1]], coord[ruta[0]])
    return total

def generar_vecinos(ruta):
    vecinos = []
    for i in range(len(ruta)):
        for j in range(i+1, len(ruta)):
            nuevo = ruta[:]
            nuevo[i], nuevo[j] = nuevo[j], nuevo[i]
            vecinos.append((nuevo, (i, j)))
    return vecinos

def resolver_tsp_tabu():
    ciudades = list(coord.keys())
    random.shuffle(ciudades)
    mejor_ruta, costo = tabu_search(ciudades, evalua_ruta, generar_vecinos, iterations=500, tabu_size=15)
    return mejor_ruta, costo, coord
