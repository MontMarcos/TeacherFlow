import sqlite3
from app.db.database import gerar_conexao, fechar_conexao
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, id, username, email, full_name, password_hash):
        self.id = id
        self.username = username
        self.email = email
        self.full_name = full_name
        self.password_hash = password_hash

    @staticmethod
    def create_user(username, email, full_name, password):
        conn = gerar_conexao()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, full_name, password_hash) VALUES (?, ?, ?, ?)",
            (username, email, full_name, generate_password_hash(password))
        )
        conn.commit()
        fechar_conexao(conn)

    @staticmethod
    def get_user_by_username(username):
        conn = gerar_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        fechar_conexao(conn)

        if row:
            return User(*row)

        return None
    
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
