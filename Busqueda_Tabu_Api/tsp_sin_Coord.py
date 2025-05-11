import random
from Busqueda_Tabu import tabu_search

def calcular_costo(ruta, matriz):
    return sum(matriz[ruta[i]][ruta[(i + 1) % len(ruta)]] for i in range(len(ruta)))

def generar_vecinos(ruta):
    vecinos = []
    for i in range(1, len(ruta) - 1):
        for j in range(i + 1, len(ruta)):
            vecino = ruta.copy()
            vecino[i], vecino[j] = vecino[j], vecino[i]
            vecinos.append((vecino, (i, j)))
    return vecinos

def resolver_tsp_tabu(matriz, iteraciones=200, tabu_tamano=10):
    n = len(matriz)
    solucion_inicial = list(range(n))
    random.shuffle(solucion_inicial)

    return tabu_search(
        initial_solution=solucion_inicial,
        cost_function=lambda ruta: calcular_costo(ruta, matriz),
        neighbor_function=generar_vecinos,
        iterations=iteraciones,
        tabu_size=tabu_tamano
    )
