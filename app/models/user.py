from app.db.database import gerar_conexao, fechar_conexao
import bcrypt

class User:
    def __init__(self, id, username, email, full_name, password_hash):
        self.id = id
        self.username = username
        self.email = email
        self.full_name = full_name
        self.password_hash = password_hash

    # CREATE
    @staticmethod
    def create_user(username, email, full_name, password):
        conexao = gerar_conexao()
        cursor = conexao.cursor()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cursor.execute("""
            INSERT INTO users (username, email, full_name, password_hash)
            VALUES (?, ?, ?, ?)
        """, (username, email, full_name, password_hash))

        conexao.commit()
        fechar_conexao(conexao)

    # READ
    @staticmethod
    def get_user_by_username(username):
        conexao = gerar_conexao()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id, username, email, full_name, password_hash
            FROM users WHERE username = ?
        """, (username,))
        row = cursor.fetchone()
        fechar_conexao(conexao)

        if row:
            return User(*row)  # agora retorna id também
        return None

    @staticmethod
    def get_user_by_id(user_id):
        conexao = gerar_conexao()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id, username, email, full_name, password_hash
            FROM users WHERE id = ?
        """, (user_id,))
        row = cursor.fetchone()
        fechar_conexao(conexao)

        if row:
            return User(*row)
        return None

    # UPDATE
    def save(self):
        conexao = gerar_conexao()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE users
            SET email = ?, full_name = ?, password_hash = ?
            WHERE id = ?
        """, (self.email, self.full_name, self.password_hash, self.id))

        conexao.commit()
        fechar_conexao(conexao)

    def edit_user(self, email=None, full_name=None, password=None):
        if email:
            self.email = email
        if full_name:
            self.full_name = full_name
        if password:
            self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.save()

    # DELETE
    @staticmethod
    def delete_user(user_id):
        conexao = gerar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conexao.commit()
        fechar_conexao(conexao)

    # AUTH
    def validate_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name
        }
