from flask import Flask,redirect,request
import requests


url = "https://advanced-movie-search.p.rapidapi.com/search/movie"

headers = {
	"x-rapidapi-key": "681a22aa5cmsh35e4e17b7039abcp1b366bjsndb25fcbb2eb8",
	"x-rapidapi-host": "advanced-movie-search.p.rapidapi.com"
}

app = Flask(__name__)

@app.route('/', methods=['POST',])
def buscar():
    nome_filme = request.form['film']
    querystring = {"query": nome_filme,"page":"1"}
    
    return f'O nome do filme é: {nome_filme}'
