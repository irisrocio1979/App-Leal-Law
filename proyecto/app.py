from flask import Flask, request, jsonify, render_template
from model.trained_model import get_response  # Ajusta esto según tu estructura real

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta', methods=['POST'])
def consulta():
    data = request.json
    query = data['query']
    response = get_response(query)  # Esta función usa tu modelo entrenado para obtener una respuesta
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
