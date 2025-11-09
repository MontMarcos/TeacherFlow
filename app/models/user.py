import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

APP_ROOT = os.path.dirname(BASE_DIR) 

USERS_FILE = os.path.join(APP_ROOT, 'db', 'user.json') 

class User:    
    def __init__(self, user_data):
        self.id = user_data.get('id')
        self.name = user_data.get('name') 
        self.password = user_data.get('password')

    def __repr__(self):
        return f'<User {self.name} (ID: {self.id})>'

    @staticmethod
    def load_users():
        with open(USERS_FILE, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                processed_users = []
                for item in data:
                    user_info = item.get('user', {}) 
                    user_info['id'] = item.get('id')
                    processed_users.append(user_info)
                
                return processed_users

    @staticmethod
    def get_by_name(name):
        """Busca um usuário pelo nome. Retorna uma instância de User ou None."""
        users_list = User.load_users()
        for user_data in users_list:
            if user_data.get('name') == name:
                return User(user_data) 
        return None

    def check_password(self, password):
        return str(self.password) == str(password)