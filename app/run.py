from flask import Flask, session, redirect, url_for, request, render_template
from app.controller.aplication import Aplication
from app.models.user import User
from app.db.database import inicializar_banco_de_dados
import os
import bcrypt
from functools import wraps
from dotenv import load_dotenv

load_dotenv()

# DECORADOR DE SEGURANÇA (login_required)
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

inicializar_banco_de_dados()

SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

aplication = Aplication()
app = Flask(__name__, template_folder='views')

app.secret_key = SECRET_KEY

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get("logged_in"):
        return redirect(url_for("portal"))

    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.get_user_by_username(username)

        if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash):
            session.clear()
            session['username'] = user.username
            session['user_id'] = user.id
            session['nome'] = user.full_name.split()[0].capitalize()
            session['logged_in'] = True
            
            return redirect(url_for("portal"))

        return render_template('login.html', message="Usuário ou senha inválidos.")

    return render_template('login.html') 


@app.route('/register', methods=['POST'])
def register():
    full_name = request.form.get("full_name")
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password") 

    if not username or not password or not email or not full_name:
        return render_template('login.html', message="Preencha todos os campos para registrar.")
    
    existing_user = User.get_user_by_username(username)
    if existing_user:
        return render_template('login.html', message="Nome de usuário já existe. Escolha outro.")

    User.create_user(username, email, full_name, password) 
    
    return redirect(url_for("login"))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))

#---------------------------------------------

@app.route('/portal')
@login_required
def portal():
    return aplication.render("principal")

@app.route('/planejamento')
@login_required
def planejamento():
    return aplication.render("planejamento")

@app.route('/gestao')
@login_required
def gestao():
    return aplication.render("gestao")

@app.route('/ajuda')
@login_required
def ajuda():
    return aplication.render("ajuda")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)