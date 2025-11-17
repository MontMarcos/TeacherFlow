from ..db.database import gerar_conexao, fechar_conexao
import sqlite3
import bcrypt

class User:
    def __init__(self, username, email, full_name, password_hash, ):
        self.username = username
        self.email = email
        self.full_name = full_name
        self.password_hash = password_hash

    def save(self):
        conexao = gerar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE users SET email = ?, full_name = ?, password_hash = ? WHERE username = ?",
            (self.email, self.full_name, self.password_hash, self.username)
        )
        conexao.commit()
        fechar_conexao(conexao)


#CRUD Operations (CREATE, READ, UPDATE, DELETE)
    #CREATE
    @staticmethod
    def create_user(username, email, full_name, password):
        conexao = gerar_conexao()
        cursor = conexao.cursor()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute(
            "INSERT INTO users (username, email, full_name, password_hash) VALUES (?, ?, ?, ?)",
            (username, email, full_name, password_hash)
        )
        conexao.commit()
        fechar_conexao(conexao)
    
    def validate_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
    
    #READ
    @staticmethod
    def get_all_users():
        conexao = gerar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT username, email FROM users")
        users = cursor.fetchall()
        fechar_conexao(conexao)
        return [User(username, email) for username, email in users]
    
    @staticmethod
    def get_user_by_username(username):
        conexao = gerar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT username, email, full_name, password_hash FROM users WHERE username = ?",
            (username,)
        )
        row = cursor.fetchone()
        fechar_conexao(conexao)
        if row:
            return User(*row)
        return None
    
    #DELETE
    @staticmethod
    def delete_user(username):
        conexao = gerar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "DELETE FROM users WHERE username = ?",
            (username,)
        )
        conexao.commit()
        fechar_conexao(conexao)

    #UPDATE
    def update_user(self, email=None, full_name=None, password=None):
        if email:
            self.email = email
        if full_name:
            self.full_name = full_name
        if password:
            self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.save()

    def __repr__(self):
        return f"User(username={self.username}, email={self.email}, full_name={self.full_name})"
    
    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name
        }