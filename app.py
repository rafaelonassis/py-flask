from flask import Flask, jsonify, request

from models.pessoa import Pessoa
from services.imc import calculate

app = Flask(__name__)

@app.route('/imc/calculate', methods=['POST'])
def calculate_imc():
    pessoa = Pessoa.from_dict(request.json)
    calculate(pessoa)

    return jsonify(p.to_dict())

app.run(host='localhost', port=4200, debug=True)