from flask import render_template

class Aplication:
    def __init__(self):
        self.pages = {
            'principal': self.render_inicio,
        }

    def render(self, page):
        content_function = self.pages.get(page, self.render_casamento)
        return content_function()
    
    def render_inicio(self):
        return render_template('inicio.html')

