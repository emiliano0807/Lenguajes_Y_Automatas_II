from flask import Flask, request, jsonify, render_template
from Arbol import Nodo

app = Flask(__name__)

def buscar_solucion_BFS_rec(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())
    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial
    else:
        dato_nodo = nodo_inicial.get_datos()
        hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]])
        hijo_izquierdo.padre = nodo_inicial
        
        hijo_central = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]])
        hijo_central.padre = nodo_inicial
        
        hijo_derecho = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]])
        hijo_derecho.padre = nodo_inicial
        
        nodo_inicial.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])
        
        for nodo_hijo in nodo_inicial.get_hijos():
            if nodo_hijo.get_datos() not in visitados:
                sol = buscar_solucion_BFS_rec(nodo_hijo, solucion, visitados)
                if sol is not None:
                    return sol
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resolver', methods=['POST'])
def resolver():
    try:
        datos = request.json.get('estado_inicial')
        solucion = request.json.get('solucion')
        
        if not datos or not solucion or len(datos) != len(solucion):
            return jsonify({'error': 'Debe enviar dos listas de la misma longitud'}), 400

        estado_inicial = [int(i) for i in datos]
        solucion = [int(i) for i in solucion]
        visitados = []
        nodo_inicial = Nodo(estado_inicial)
        nodo_solucion = buscar_solucion_BFS_rec(nodo_inicial, solucion, visitados)
        
        if nodo_solucion:
            resultado = []
            nodo = nodo_solucion
            while nodo is not None:
                resultado.append(nodo.get_datos())
                nodo = nodo.get_padre()
            resultado.reverse()
            return jsonify({'solucion': resultado})
        else:
            return jsonify({'mensaje': 'No se encontró una solución'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
