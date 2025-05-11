from flask import Flask, render_template, request, jsonify
from tsp_sin_Coord import resolver_tsp_tabu

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resolver', methods=['POST'])
def resolver():
    data = request.get_json()
    matriz = data['matriz']
    ruta, costo = resolver_tsp_tabu(matriz)
    return jsonify({'ruta': ruta, 'costo': costo})

if __name__ == '__main__':
    app.run(debug=True)
