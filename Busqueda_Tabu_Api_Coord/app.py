from flask import Flask, render_template, jsonify
from tsp_Coord import resolver_tsp_tabu

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resolver')
def resolver():
    ruta, costo, coords = resolver_tsp_tabu()
    coordenadas = [coords[ciudad] for ciudad in ruta]
    return jsonify({
        'ruta': ruta,
        'coordenadas': coordenadas,
        'costo': costo
    })

if __name__ == '__main__':
    app.run(debug=True)
