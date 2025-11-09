from flask import render_template

class Aplication:
    def __init__(self):
        self.pages = {
            'principal': self.render_principal,
            'login': self.render_login
        }

    def render(self, page):
        content_function = self.pages.get(page, self.render_principal) 
        return content_function()
    
    def render_principal(self):
        return render_template('inicio.html')
    
    def render_login(self):
        return render_template('login.html')

