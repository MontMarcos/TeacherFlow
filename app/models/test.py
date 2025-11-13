from aluno import Aluno

def test_cpf_formatado():
    aluno = Aluno(
            nome = "João Silva",
            idade = 20,
            matricula = "2023001",
            sexo = "M",
            data_nascimento = "2003-05-15",
            nacionalidade = "Brasileiro",
            necessidades_especiais = "Nenhuma",
            nome_mae = "Maria Silva",
            nome_pai = "Carlos Silva",
            contato_responsavel = "(11) 99999-9999",
            cpf = "12345678989"
    
    return aluno

if __name__ == "__main__":
    aluno = test_cpf_formatado()  
    print(f"CPF Formatado: {aluno.cpf_formatado()}")
    print(f"CPF válido: {aluno.cpf_valido()}")