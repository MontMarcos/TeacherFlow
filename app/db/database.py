import sqlite3
import os

DB_PATH = "app/db/database.db"

def gerar_conexao():
    os.makedirs("app/db", exist_ok=True)
    return sqlite3.connect(DB_PATH)

def fechar_conexao(conexao):
    if conexao:
        conexao.close()

def inicializar_banco_de_dados():
    conexao = gerar_conexao()
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