from flask import Flask, session, redirect, url_for, request
from app.controller.aplication import Aplication
from app.models.user import User
from app.db.database import inicializar_banco_de_dados
import bcrypt
import os

# Inicializa BD
inicializar_banco_de_dados()

aplication = Aplication()
app = Flask(__name__, template_folder='views')

# SECRET KEY segura
app.secret_key = os.urandom(32)


# ----------------------------------------
# LOGIN
# ----------------------------------------
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Se já está logado → portal
    if session.get("logged_in"):
        return redirect(url_for("portal"))

    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        # Busca usuário
        user = User.get_user_by_username(username)

        if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash):
            # Segurança: nova sessão para evitar fixation
            session.clear()
            session['logged_in'] = True
            session['username'] = user.username
            session['user_id'] = user.id
            
            return redirect(url_for("portal"))
        else:
            return "Usuário ou senha incorretos"

    return aplication.render("login")


# ----------------------------------------
# REGISTRO
# ----------------------------------------
@app.route('/register', methods=['POST'])
def register():
    full_name = request.form.get("full_name")
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    # Validação mínima
    if not username or not password or not email:
        return "Preencha tudo!"

    # Criar usuário com senha já criptografada
    created = User.create_user(username, email, full_name, password)

    if not created:
        return "Erro: usuário já existe"

    return redirect(url_for("login"))


# ----------------------------------------
# LOGOUT
# ----------------------------------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))


# ----------------------------------------
# PORTAL (precisa estar logado)
# ----------------------------------------
@app.route('/portal')
def portal():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return aplication.render("principal")


@app.route('/planejamento')
def planejamento():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return aplication.render("planejamento")


@app.route('/gestao')
def gestao():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return aplication.render("gestao")


@app.route('/ajuda')
def ajuda():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return aplication.render("ajuda")


# ----------------------------------------
# RUN
# ----------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
