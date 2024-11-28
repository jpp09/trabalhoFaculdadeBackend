from flask import Flask, jsonify,request,session
from flask_cors import CORS
import requests,random

app = Flask(__name__)
'''CORS(app,origins=['https://jpp09.github.io'])'''
CORS(app)

cadastro_pessoas = {
    'nome' : [],
    'id' : [],
    'email': [],
    'usuario':[],
    'senha':[]
}

@app.route('/home')
def home():

    url = "https://api.themoviedb.org/3/trending/all/day?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmODZmNmQ2YzZkNTVhODJiNmY5MmU4NWE0ODc0MTljYyIsIm5iZiI6MTczMjM2MDAzMC45ODI5NjcsInN1YiI6IjY3MmU5M2U4N2ZkNzI0MzQyYTkwMDNhNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.qIYC-ShZPXNXYcJLc6dQZ_ohzXkscej-3yQterP3GZ0"
    }

    response = requests.get(url, headers=headers)

    return jsonify(response.json())

@app.route('/cadastro',methods=['POST'])

def cadastro():
    response = request.get_json()
    cadastro_pessoas['nome'].append(response['nome'])
    cadastro_pessoas['email'].append(response['email'])
    cadastro_pessoas['usuario'].append(response['usuario'])
    cadastro_pessoas['senha'].append(response['senha'])
    id_gerador = f'{random.randint(0,100)}{random.randint(0,100)}'
    if id_gerador in cadastro_pessoas['id']:
        id_gerador = f'{random.randint(0,100)}{random.randint(0,100)}'
    else:
        cadastro_pessoas['id'].append(id_gerador)
    return jsonify({'mensagem':f'O cadastro do {response["nome"]} foi realizado com sucesso'})


@app.route('/login',methods=['POST'])

def login():
    response = request.get_json()
    usuario = response['user']
    senha = response['password']
    if usuario in cadastro_pessoas['usuario']:
        index = cadastro_pessoas['usuario'].index(usuario)
        if senha == cadastro_pessoas['senha'][index]:
            return jsonify({'mensagem' : 'Login realizado com sucesso'})
        else: 
            return jsonify({'mensagem': 'Senha incorreta'})
    else:
        return jsonify({'mensagem': 'Usuário não detectado'})
        

 

@app.route('/conteudo')
def add():
    url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmODZmNmQ2YzZkNTVhODJiNmY5MmU4NWE0ODc0MTljYyIsIm5iZiI6MTczMjc1Nzk5NS43NDA1MTIsInN1YiI6IjY3MmU5M2U4N2ZkNzI0MzQyYTkwMDNhNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.K5n_n3wR4GdP2ZEbXkKfd4C5H_YQ8akZl7TTuG3HGoo"
    }

    response = requests.get(url,headers=headers)
    return jsonify(response.json())



