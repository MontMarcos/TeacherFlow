from .aluno import Aluno
from ..db.database import gerar_conexao, fechar_conexao

class Turma:
    def __init__(self, id, nome, descricao=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.alunos = []   # será carregado automaticamente

    # CREATE
    @staticmethod
    def create_turma(nome, descricao=None):
        conexao = gerar_conexao()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO turmas (nome, descricao)
            VALUES (?, ?)
        """, (nome, descricao))

        conexao.commit()
        fechar_conexao(conexao)

    # READ (carrega turma + lista de alunos)
    @staticmethod
    def get_turma_by_id(turma_id):
        conexao = gerar_conexao()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, nome, descricao
            FROM turmas
            WHERE id = ?
        """, (turma_id,))
        row = cursor.fetchone()

        if not row:
            fechar_conexao(conexao)
            return None

        turma = Turma(*row)

        # Agora carrega os alunos dessa turma
        cursor.execute("""
            SELECT id, nome, idade, turma
            FROM alunos
            WHERE turma = ?
        """, (turma.id,))
        aluno_rows = cursor.fetchall()

        turma.alunos = [Aluno(*a) for a in aluno_rows]

        fechar_conexao(conexao)
        return turma

    # UPDATE
    def save(self):
        conexao = gerar_conexao()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE turmas
            SET nome = ?, descricao = ?
            WHERE id = ?
        """, (self.nome, self.descricao, self.id))

        conexao.commit()
        fechar_conexao(conexao)

    # DELETE
    @staticmethod
    def delete_turma(turma_id):
        conexao = gerar_conexao()
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM turmas WHERE id = ?", (turma_id,))
        conexao.commit()

        fechar_conexao(conexao)
