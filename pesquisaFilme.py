from flask import Flask,redirect,request
import requests



app = Flask(__name__)

@app.route('/', methods=['POST',])
def buscar():
    nome_filme = request.form['film']
    querystring = {"query": nome_filme,"page":"1"}
    
    return f'O nome do filme é: {nome_filme}'

app.run(debug=True)