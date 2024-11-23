from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

@app.route('/home', methods=['POST'])
def home():
    mensagem = 'Deu certo'
    return jsonify({'mensagem': mensagem}), 200

