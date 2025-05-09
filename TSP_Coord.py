import math
import random
from Busqueda_Tabu import tabu_search

coord = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754472859146, -103.34625354877137),
    'Monterrey': (25.69161110159454, -100.321838480256),
    'QuintanaRoo': (21.163111924844458, -86.80231502121464),
    'Michohacan': (19.701400113725654, -101.20829680213464),
    'Aguascalientes': (21.87641043660486, -102.26438663286967),
    'CDMX': (19.432713075976878, -99.13318344772986),
    'QRO': (20.59719437542255, -100.38667040246602)
}

def distancia(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def evalua_ruta(ruta):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(coord[ruta[i]], coord[ruta[i+1]])
    total += distancia(coord[ruta[-1]], coord[ruta[0]])  # vuelta a origen
    return total

def generar_vecinos(ruta):
    vecinos = []
    for i in range(len(ruta)):
        for j in range(i + 1, len(ruta)):
            nueva_ruta = ruta[:]
            nueva_ruta[i], nueva_ruta[j] = nueva_ruta[j], nueva_ruta[i]
            vecinos.append((nueva_ruta, (i, j)))
    return vecinos

def tsp_tabu_con_coordenadas():
    ciudades = list(coord.keys())
    random.shuffle(ciudades)
    mejor_ruta, costo = tabu_search(ciudades, evalua_ruta, generar_vecinos, iterations=500, tabu_size=15)
    return mejor_ruta, costo

if __name__ == "__main__":
    ruta, costo = tsp_tabu_con_coordenadas()
    print("Mejor ruta:", ruta)
    print("Distancia total:", costo)
