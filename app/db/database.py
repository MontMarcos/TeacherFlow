import sqlite3

def gerar_conexao(db_path='app/db/database.db'):
    """Gera uma conexão com o banco de dados SQLite."""
    conexao = sqlite3.connect("teacher.db")
    conexao.commit()
    return conexao

def fechar_conexao(conexao):
    """Fecha a conexão com o banco de dados SQLite."""
    if conexao:
        conexao.close()

def inicializar_banco_de_dados(db_path='app/db/database.db'):
    """Inicializa o banco de dados com a tabela de usuários."""
    conexao = gerar_conexao(db_path)
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
            full_name TEXT NOT NULL,
            password_hash BLOB NOT NULL
        )
    ''')
    conexao.commit()
    fechar_conexao(conexao)