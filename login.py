from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/login',methods=['POST'])

def login():
    senha = request.form['input_senha']
    if senha == 1234:
        status = {
            'mesagem': f'O usuário: {request.form['input_email']} foi logado com sucesso.'
        }
    else:
        status = {
            'mensagem' : f'O usuário {request.form['input_email']} não foi logado.'
        }

    return ''
    
app.run(debug=True)
    
