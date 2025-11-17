from .aluno import Aluno

class Turma:
    def __init__(self, nome: str, codigo: str):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []

    def adicionar_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        return self.alunos
    
    def __repr__(self):
        return f'<Turma {self.nome} (Código: {self.codigo})>'
    
    def contar_alunos(self):
        return len(self.alunos)
    
    def buscar_aluno_por_matricula(self, matricula: str):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None 
    
    def remover_aluno_por_nome_ou_matricula(self, identificador: str):
        for aluno in self.alunos:
            if aluno.nome == identificador or aluno.matricula == identificador:
                self.alunos.remove(aluno)
                return True
        return False
    
