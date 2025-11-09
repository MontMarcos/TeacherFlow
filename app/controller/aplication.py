from flask import render_template, request, redirect, url_for, session
from models.user import User 

class Aplication:
    def __init__(self):
        self.pages = {
            'login': self.handle_login,
            'principal': self.render_principal
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

    def handle_login(self):
        """Lida com requisições GET/POST no login."""
        
        if request.method == 'POST':
            name = request.form.get('username')
            password = request.form.get('password')
            
            user = User.get_by_name(name)
            
            if user and user.check_password(password):
                session['logged_in'] = True
                session['name'] = user.name
                return redirect(url_for('principal')) 
            else:
                return self.render_login(message="Nome ou senha incorretos.")
        
        return self.render_login()