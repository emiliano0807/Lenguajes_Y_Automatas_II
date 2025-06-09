from flask import Flask, jsonify, request
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas 

def poblacion_inicial(max_poblacion, num_vars):
    poblacion = []
    for _ in range(max_poblacion):
        gen = [random.randint(0, 1) for _ in range(num_vars)]
        poblacion.append(gen)
    return poblacion

def adaptacion_3sat(gen, solucion):
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
    return [adaptacion_3sat(ind, solucion) for ind in poblacion]

def seleccion(poblacion, solucion):
    adaptacion = evalua_poblacion(poblacion, solucion)
    total = sum(adaptacion)

    def ruleta():
        r = random.randint(0, total)
        suma = 0
        for i, a in enumerate(adaptacion):
            suma += a
            if suma >= r:
                return poblacion[i]
        return poblacion[-1]

    return ruleta(), ruleta()

def cruce(gen1, gen2):
    corte = random.randint(1, len(gen1) - 1)
    return gen1[:corte] + gen2[corte:], gen2[:corte] + gen1[corte:]

def mutacion(prob, gen):
    if random.random() < prob:
        idx = random.randint(0, len(gen) - 1)
        gen[idx] = 1 - gen[idx]
    return gen

def elimina_peores_genes(poblacion, solucion):
    for _ in range(2):
        adaptacion = evalua_poblacion(poblacion, solucion)
        peor_idx = adaptacion.index(min(adaptacion))
        del poblacion[peor_idx]

def mejor_gen(poblacion, solucion):
    adaptacion = evalua_poblacion(poblacion, solucion)
    return poblacion[adaptacion.index(max(adaptacion))]

@app.route('/resolver', methods=['POST'])
def resolver_genetico():
    datos = request.json

    num_vars = datos.get("num_vars", 10)
    max_iter = datos.get("max_iter", 10)
    max_poblacion = datos.get("max_poblacion", 50)

    random.seed()

    solucion = poblacion_inicial(1, num_vars)[0]
    poblacion = poblacion_inicial(max_poblacion, num_vars)

    for _ in range(max_iter):
        for _ in range(len(poblacion) // 2):
            gen1, gen2 = seleccion(poblacion, solucion)
            nuevo_gen1, nuevo_gen2 = cruce(gen1, gen2)
            nuevo_gen1 = mutacion(0.1, nuevo_gen1)
            nuevo_gen2 = mutacion(0.1, nuevo_gen2)
            poblacion.extend([nuevo_gen1, nuevo_gen2])
            elimina_peores_genes(poblacion, solucion)

    mejor = mejor_gen(poblacion, solucion)
    return jsonify({
        "solucion_objetivo": solucion,
        "mejor_gen": mejor,
        "adaptacion": adaptacion_3sat(mejor, solucion)
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)