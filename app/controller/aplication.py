from flask import render_template, request, redirect, url_for, session
from app.models.user import User

class Aplication:
    def __init__(self):
        self.pages = {
            'login': self.handle_login,
            'principal': self.render_principal,
            'planejamento': self.render_planejamento,
            'gestao': self.render_gestao,
            'ajuda': self.render_ajuda
        }

    def render(self, page):
        content_function = self.pages.get(page, self.render_principal) 
        return content_function()
    
    def render_principal(self):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return render_template('inicio.html', name=session.get('name')) 
    
    def render_login(self, message=None):
        return render_template('login.html', message=message)
    
    def render_planejamento(self):
        return render_template('planejamento.html')
    
    def render_gestao(self):
        return render_template('gestao.html')
    
    def render_ajuda(self):
        return render_template('ajuda.html')

    def handle_login(self):
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            user = User.get_user_by_username(username)
            if user and user.validate_password(password):
                session['logged_in'] = True
                session['name'] = user.full_name
                return redirect(url_for('principal'))
            else:
                return self.render_login(message="Invalid username or password.")
        return self.render_login()
    
    def handle_logout(self):
        session.clear()
        return redirect(url_for('login'))
    
    def handle_registration(self):
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            full_name = request.form.get('full_name')
            password = request.form.get('password')
            existing_user = User.get_user_by_username(username)
            if existing_user:
                return self.render_login(message="Username already exists.")
            User.create_user(username, email, full_name, password)
            return redirect(url_for('login'))
        return self.render_login()