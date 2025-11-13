from app.models.turma import Turma
from app.models.aluno import Aluno

def test_adicionar_e_listar_alunos():   
    turma = Turma(nome="Matemática", codigo="MATH101")
     
    aluno1 = Aluno(
        nome="Ana Souza",
        matricula="2023002",
        sexo="F",
        data_nascimento="2004-08-22",
        nacionalidade="Brasileira",
        necessidades_especiais="Nenhuma",
        nome_mae="Clara Souza",
        nome_pai="Pedro Souza",
        contato_responsavel="(21) 98888-8888",
        cpf="12345678909"
    )
    
    aluno2 = Aluno(
        nome="Bruno Lima",
        matricula="2023003",
        sexo="M",
        data_nascimento="2003-11-30",
        nacionalidade="Brasileiro",
        necessidades_especiais="Nenhuma",
        nome_mae="Sofia Lima",
        nome_pai="Ricardo Lima",
        contato_responsavel="(31) 97777-7777",
        cpf="98765432100"
    )
    
    turma.adicionar_aluno(aluno1)
    turma.adicionar_aluno(aluno2)
    
if __name__ == "__main__":
    turma = Turma(nome="Matemática", codigo="MATH101")
    print(f"Turma criada: {turma}")
    print("Alunos na turma:")
    for aluno in turma.listar_alunos():
        print(aluno)