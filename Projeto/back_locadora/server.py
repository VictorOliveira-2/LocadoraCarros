from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

# Rotas do Flask e leitura dos arquivos json
server = Flask(__name__)
CORS(server)  

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@server.route('/usuarios', methods=['GET'])
def get_usuarios():
    file_path = os.path.join(BASE_DIR, 'usuarios.json')
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Arquivo usuarios.json não encontrado"}), 404

@server.route('/carros', methods=['GET'])
def get_carros():
    file_path = os.path.join(BASE_DIR, 'veiculos.json')
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Arquivo veiculos.json não encontrado"}), 404

@server.route('/alugados', methods=['GET'])
def get_alugados():
    file_path = os.path.join(BASE_DIR, 'alugados.json')
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Arquivo alugados.json não encontrado"}), 404

if __name__ == '__main__':
    server.run(debug=True)