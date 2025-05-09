from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

conexiones = {
    "EDO.MEX": ["QRO", "SLP", "SONORA"],
    "PUEBLA": ["HIDALGO", "SLP"],
    "CDMX": ["MICHOACAN"],
    "MICHOACAN": ["SONORA"],
    "SLP": ["QRO", "PUEBLA", "EDO.MEX", "SONORA", "GUADALAJARA"],
    "QRO": ["EDO.MEX", "SLP"],
    "HIDALGO": ["PUEBLA", "GUADALAJARA", "SONORA"],
    "MONTERREY": ["HIDALGO", "SLP"],
    "SONORA": ["MONTERREY", "HIDALGO", "SLP", "EDO.MEX", "MICHOACAN"]
}

class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.padre = None
        self.hijos = []

    def set_padre(self, padre):
        self.padre = padre

def DFS_prof_iter(inicio, solucion):
    nodo_inicial = Nodo(inicio)
    for limite in range(0, 100):
        visitados = []
        sol = buscar_solucion_DFS_Rec(nodo_inicial, solucion, visitados, limite)
        if sol is not None:
            return sol
    return None

def buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite):
    if limite > 0:
        visitados.append(nodo.datos)
        if nodo.datos == solucion:
            return nodo
        else:
            lista_hijos = []
            if nodo.datos in conexiones:
                for un_hijo in conexiones[nodo.datos]:
                    if un_hijo not in visitados:
                        hijo = Nodo(un_hijo)
                        hijo.set_padre(nodo)
                        lista_hijos.append(hijo)
            nodo.hijos = lista_hijos

        for nodo_hijo in nodo.hijos:
            sol = buscar_solucion_DFS_Rec(nodo_hijo, solucion, visitados, limite - 1)
            if sol is not None:
                return sol

    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar", methods=["POST"])
def buscar():
    data = request.json
    inicio = data.get("inicio")
    fin = data.get("fin")

    if inicio not in conexiones or fin not in conexiones:
        return jsonify({"error": "Uno o ambos estados no existen"}), 400

    nodo = DFS_prof_iter(inicio, fin)

    if nodo is not None:
        resultado = []
        while nodo.padre is not None:
            resultado.append(nodo.datos)
            nodo = nodo.padre
        resultado.append(inicio)
        resultado.reverse()
        return jsonify({"ruta": resultado})
    else:
        return jsonify({"mensaje": "Ruta no encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)
