import math
import random

def poblacion_inicial(max_poblacion, num_vars):
    poblacion = []
    for _ in range(max_poblacion):
        gen = [random.randint(0, 1) for _ in range(num_vars)]
        poblacion.append(gen)
    return poblacion

def adaptacion_3sat(gen, solucion):
    # Se asume que cada cláusula tiene 3 variables
    cont = 0
    for i in range(0, len(gen), 3):
        clausula_ok = False
        for j in range(3):
            if i + j < len(gen) and gen[i + j] == solucion[i + j]:
                clausula_ok = True
        if clausula_ok:
            cont += 1
    return cont

def evalua_poblacion(poblacion, solucion):
    adaptacion = []
    for individuo in poblacion:
        adaptacion.append(adaptacion_3sat(individuo, solucion))
    return adaptacion

def seleccion(poblacion, solucion):
    adaptacion = evalua_poblacion(poblacion, solucion)
    total = sum(adaptacion)

    def ruleta(total):
        r = random.randint(0, total)
        suma = 0
        for i in range(len(adaptacion)):
            suma += adaptacion[i]
            if suma >= r:
                return poblacion[i]
        return poblacion[-1]  # por si acaso

    return ruleta(total), ruleta(total)

def cruce(gen1, gen2):
    corte = random.randint(1, len(gen1) - 1)
    nuevo_gen1 = gen1[:corte] + gen2[corte:]
    nuevo_gen2 = gen2[:corte] + gen1[corte:]
    return nuevo_gen1, nuevo_gen2

def mutacion(prob, gen):
    if random.random() < prob:
        idx = random.randint(0, len(gen) - 1)
        gen[idx] = 1 - gen[idx]
    return gen

def elimina_peores_genes(poblacion, solucion):
    adaptacion = evalua_poblacion(poblacion, solucion)
    for _ in range(2):
        i = adaptacion.index(min(adaptacion))
        del poblacion[i]
        del adaptacion[i]

def mejor_gen(poblacion, solucion):
    adaptacion = evalua_poblacion(poblacion, solucion)
    return poblacion[adaptacion.index(max(adaptacion))]

def algoritmo_genetico():
    max_iter = 10
    max_poblacion = 50
    num_vars = 10
    solucion = poblacion_inicial(1, num_vars)[0]
    poblacion = poblacion_inicial(max_poblacion, num_vars)

    for iteracion in range(max_iter):
        for _ in range(len(poblacion) // 2):
            gen1, gen2 = seleccion(poblacion, solucion)
            nuevo_gen1, nuevo_gen2 = cruce(gen1, gen2)
            nuevo_gen1 = mutacion(0.1, nuevo_gen1)
            nuevo_gen2 = mutacion(0.1, nuevo_gen2)
            poblacion.append(nuevo_gen1)
            poblacion.append(nuevo_gen2)
            elimina_peores_genes(poblacion, solucion)

    mejor = mejor_gen(poblacion, solucion)
    print("Solución: " + str(solucion))
    return mejor, adaptacion_3sat(mejor, solucion)

if __name__ == "__main__":
    random.seed()
    mejor_gen_encontrado, adaptacion = algoritmo_genetico()
    print("Mejor gen encontrado: " + str(mejor_gen_encontrado))
    print("Función de adaptación: " + str(adaptacion))