
class Aluno:
    def __init__(self, nome: str, 
                 matricula: str, 
                 sexo: str, 
                 data_nascimento: str, 
                 nacionalidade: str, 
                 necessidades_especiais: str, 
                 nome_mae: str, 
                 nome_pai: str, 
                 contato_responsavel: str, cpf: str):
        
        self.nome = nome
        self.matricula = matricula
        self.sexo = sexo
        self.data_nascimento = data_nascimento 
        self.nacionalidade = nacionalidade
        self.necessidades_especiais = necessidades_especiais
        self.nome_mae = nome_mae
        self.nome_pai = nome_pai
        self.contato_responsavel = contato_responsavel
        self.cpf = cpf

    def cpf_formatado(self):
        """Retorna o CPF formatado como XXX.XXX.XXX-XX"""
        cpf_numeros = ''.join(filter(str.isdigit, self.cpf))
        if len(cpf_numeros) == 11:
            return f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"
        return self.cpf
    
    def cpf_valido(self):
        """Valida o CPF utilizando o algoritmo padrão de validação."""
        cpf_numeros = ''.join(filter(str.isdigit, self.cpf))
        if len(cpf_numeros) != 11 or cpf_numeros == cpf_numeros[0] * 11:
            return False

        def calcular_digito(cpf_parcial):
            soma = sum(int(cpf_parcial[i]) * (len(cpf_parcial) + 1 - i) for i in range(len(cpf_parcial)))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)

        digito1 = calcular_digito(cpf_numeros[:9])
        digito2 = calcular_digito(cpf_numeros[:10])
        return cpf_numeros[-2:] == digito1 + digito2
    
    def pegar_idade(self):
        """Calcula a idade do aluno com base na data de nascimento."""
        from datetime import datetime, date

        nascimento = datetime.strptime(self.data_nascimento, "%Y-%m-%d").date()
        hoje = date.today()
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        return idade
    
    def __str__(self):
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}, CPF: {self.cpf_formatado()}"
    
    def atualizar_contato_responsavel(self, novo_contato: str):
        """Atualiza o contato do responsável."""
        self.contato_responsavel = novo_contato

    def adicionar_e_remover_necessidade_especial(self, necessidade: str):
        """Adiciona ou remove uma necessidade especial do aluno."""
        necessidades = [n.strip() for n in self.necessidades_especiais.split(',')]
        if necessidade in necessidades:
            necessidades.remove(necessidade)
        else:
            necessidades.append(necessidade)
        self.necessidades_especiais = ', '.join(necessidades)

    def obter_dados_completos(self):
        """Retorna uma string com todos os dados do aluno."""
        return (f"Nome: {self.nome}\n"
                f"Matrícula: {self.matricula}\n"
                f"Sexo: {self.sexo}\n"
                f"Data de Nascimento: {self.data_nascimento}\n"
                f"Nacionalidade: {self.nacionalidade}\n"
                f"Necessidades Especiais: {self.necessidades_especiais}\n"
                f"Nome da Mãe: {self.nome_mae}\n"
                f"Nome do Pai: {self.nome_pai}\n"
                f"Contato do Responsável: {self.contato_responsavel}\n"
                f"CPF: {self.cpf_formatado()}")