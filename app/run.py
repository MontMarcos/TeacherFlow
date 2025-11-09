from controller.aplication import Aplication
from flask import Flask, session, redirect, url_for 

aplication = Aplication()
app = Flask(__name__, template_folder='views')

# Chave secreta simples para sessões (SIMPLIFICADA PARA TESTES)
app.secret_key = 'superretkey' 

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session and session['logged_in']: 
        return redirect(url_for('principal'))
        
    return aplication.render('login')

@app.route('/portal', methods=['GET'])
def principal():
    return aplication.render('principal') 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)