import random
from Busqueda_Tabu import tabu_search

# Matriz de distancias entre ciudades
matriz = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def costo_tsp(ruta):
    return sum(matriz[ruta[i]][ruta[(i + 1) % len(ruta)]] for i in range(len(ruta)))

def generar_vecinos_tsp(ruta):
    vecinos = []
    for i in range(1, len(ruta) - 1):
        for j in range(i + 1, len(ruta)):
            vecino = ruta[:]
            vecino[i], vecino[j] = vecino[j], vecino[i]
            vecinos.append((vecino, (i, j)))
    return vecinos

def tsp_con_tabu(matriz, iteraciones=200, tabu_size=10):
    n = len(matriz)
    solucion_inicial = list(range(n))
    random.shuffle(solucion_inicial)
    return tabu_search(solucion_inicial, costo_tsp, generar_vecinos_tsp, iteraciones, tabu_size)

# Ejecución
if __name__ == "__main__":
    ruta, costo = tsp_con_tabu(matriz)
    print("Ruta encontrada:", ruta)
    print("Costo total:", costo)