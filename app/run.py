from flask import Flask, session, redirect, url_for, request
from app.controller.aplication import Aplication
from app.models.user import User
from app.db.database import inicializar_banco_de_dados
import os
from functools import wraps
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv

load_dotenv()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

inicializar_banco_de_dados()

aplication = Aplication()
app = Flask(__name__, template_folder='views')

csrf = CSRFProtect(app)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
# ----------------------------------------
# LOGIN
# ----------------------------------------
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get("logged_in"):
        return redirect(url_for("portal"))

    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        # Busca usuário
        user = User.get_user_by_username(username)

        if user and user.validate_password(password):
            # Segurança: nova sessão para evitar fixation
            session.clear()
            session['logged_in'] = True
            session['username'] = user.username
            session['user_id'] = user.id
            session['nome'] = user.full_name.split()[0].capitalize()

            
            return redirect(url_for("portal"))

    return aplication.render("login")


# ----------------------------------------
# REGISTRO
# ----------------------------------------
@app.route('/register', methods=['POST'])
def register():
    full_name = request.form.get("full_name")
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")  # <--- aqui é o CORRETO

    if not username or not password or not email or not full_name:
        return "Preencha tudo!"


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


# ----------------------------------------
# RUN
# ----------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
