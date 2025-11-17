from ..db.database import gerar_conexao, fechar_conexao

class Aluno:
    def __init__(self, id, nome, idade, turma):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.turma = turma

    # CREATE
    @staticmethod
    def create_aluno(nome, idade, turma):
        conexao = gerar_conexao()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO alunos (nome, idade, turma)
            VALUES (?, ?, ?)
        """, (nome, idade, turma))

        conexao.commit()
        fechar_conexao(conexao)

    # READ
    @staticmethod
    def get_aluno_by_id(aluno_id):
        conexao = gerar_conexao()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id, nome, idade, turma
            FROM alunos WHERE id = ?
        """, (aluno_id,))
        row = cursor.fetchone()
        fechar_conexao(conexao)

        if row:
            return Aluno(*row)
        return None
    
    # UPDATE
    def save(self):
        conexao = gerar_conexao()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE alunos
            SET nome = ?, idade = ?, turma = ?
            WHERE id = ?
        """, (self.nome, self.idade, self.turma, self.id))

        conexao.commit()
        fechar_conexao(conexao)

    # DELETE
    @staticmethod
    def delete_aluno(aluno_id):
        conexao = gerar_conexao()
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM alunos WHERE id = ?
        """, (aluno_id,))

        conexao.commit()
        fechar_conexao(conexao)