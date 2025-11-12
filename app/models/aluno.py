
class Aluno:
    def __init__(self, nome: str, idade: int, matricula: str, sexo: str, data_nascimento: str, nacionalidade: str, necessidades_especiais: str, nome_mae: str, nome_pai: str, contato_responsavel: str, cpf: str):
        self.nome = nome
        self.idade = idade
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
