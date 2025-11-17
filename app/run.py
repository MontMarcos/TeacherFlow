from app.controller.aplication import Aplication
from flask import Flask, session, redirect, url_for 

aplication = Aplication()
app = Flask(__name__, template_folder='views')

# Chave secreta simples para sessões (SIMPLIFICADA PARA TESTES)
app.secret_key = 'sueree' 

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session and session['logged_in']: 
        return redirect(url_for('principal'))
        
    return aplication.render('login')

@app.route('/portal', methods=['GET'])
def principal():
    return aplication.render('principal')   

@app.route('/planejamento', methods=['GET'])
def planejamento():
    return aplication.render('planejamento')

@app.route('/gestao', methods=['GET'])
def gestao():
    return aplication.render('gestao')

@app.route('/ajuda', methods=['GET'])
def ajuda():
    return aplication.render('ajuda')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 