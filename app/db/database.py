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

if __name__ == "__main__":
    conn = gerar_conexao()
    print("Conexão com o banco de dados estabelecida com sucesso.")
    fechar_conexao(conn)