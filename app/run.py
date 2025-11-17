from app.controller.aplication import Aplication
from flask import Flask, session, redirect, url_for, request
from app.models.user import User
from app.db.database import inicializar_banco_de_dados
import bcrypt

inicializar_banco_de_dados()

aplication = Aplication()
app = Flask(__name__, template_folder='views')

app.secret_key = 'sueree'


# ----------------------------
# LOGIN
# ----------------------------
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Se já estiver logado, vai para o portal
    if session.get('logged_in'):
        return redirect('/portal')

    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        # Busca o usuário
        user = User.get_user_by_username(username)

        # Verifica usuário e senha
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash):
            session['logged_in'] = True
            session['username'] = username
            return redirect('/portal')

        return "Usuário ou senha incorretos"

    return aplication.render('login')



# ----------------------------
# REGISTRO
# ----------------------------
@app.route("/register", methods=["POST"])
def register():
    full_name = request.form.get("full_name")
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    User.create_user(username, email, full_name, password)

    return redirect("/login")

# ----------------------------
# LOGOUT
# ----------------------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


# ----------------------------
# ROTAS INTERNAS
# ----------------------------
@app.route('/portal')
def principal():
    if not session.get('logged_in'):
        return redirect('/login')
    return aplication.render('principal')   

@app.route('/planejamento')
def planejamento():
    return aplication.render('planejamento')

@app.route('/gestao')
def gestao():
    return aplication.render('gestao')

@app.route('/ajuda')
def ajuda():
    return aplication.render('ajuda')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
