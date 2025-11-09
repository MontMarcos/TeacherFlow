from controller.aplication import Aplication
from flask import Flask

aplication = Aplication()
app = Flask(__name__, template_folder='views')

@app.route('/')
@app.route('/', methods=['GET'])
def principal():
    return aplication.render('principal') 

@app.route('/login', methods=['GET'])
def login():
    return aplication.render('login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)