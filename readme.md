    # 🎓 TeacherFlow

> **Assistente Digital para Professores** - Planejamento, organização e acompanhamento educacional simplificados.

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)](https://github.com/seu-usuario/teacherflow)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 📋 Sobre o Projeto

**TeacherFlow** é uma aplicação web desenvolvida para auxiliar professores nas atividades diárias de planejamento e gestão educacional. O sistema aborda as principais dores do cotidiano docente, oferecendo ferramentas práticas para:

### 🎯 Pré-Aula (Planejamento)
- 📝 Criação rápida de planos de aula
- 📚 Banco de atividades organizado com busca inteligente
- 🔍 Repositório centralizado de materiais
- 📄 Gerador de listas de exercícios e avaliações

### 📊 Pós-Aula (Gestão)
- ✅ Registro ágil de presença
- 📈 Lançamento e visualização de notas
- 📋 Sistema de anotações sobre alunos
- 📊 Relatórios automáticos e dashboards

---

## ✨ Proposta de Valor

> *"Gaste menos tempo com burocracia, mais tempo ensinando."*

TeacherFlow permite que professores organizem suas turmas, reutilizem materiais, acompanhem o desempenho dos alunos e gerem relatórios de forma simples e eficiente.

---

## 🛠️ Stack Tecnológica

### Backend
- **Framework:** Flask 3.0
- **Autenticação:** Flask
- **Formulários:** Flask
- **Migrations:** Flask

### Frontend
-**HTML** - TPL
- **CSS Framework:** 
- **JavaScript:** 

### Banco de Dados
- **Desenvolvimento:** SQLite
- **Produção:** PostgreSQL

### Outros
- **PDF Generation:** ReportLab
- **Deploy:** Railway / Render / Heroku

---

## 📁 Estrutura do Projeto

```
teacherflow/
├── app/
│   ├── __init__.py          # Factory da aplicação
│   ├── models/              # Modelos de dados (ORM)
│   │   ├── user.py
│   │   ├── turma.py
│   │   ├── aluno.py
│   │   ├── atividade.py
│   │   ├── plano_aula.py
│   │   ├── presenca.py
│   │   ├── avaliacao.py
│   │   └── anotacao.py
│   ├── routes/              # Rotas/Controllers (Blueprints)
│   │   ├── auth.py
│   │   ├── dashboard.py
│   │   ├── turmas.py
│   │   ├── atividades.py
│   │   ├── planos.py
│   │   ├── presenca.py
│   │   └── notas.py
│   ├── forms/               # Formulários (WTForms)
│   ├── templates/           # Templates HTML (Jinja2)
│   ├── static/              # CSS, JS, imagens
│   └── utils/               # Utilitários e helpers
├── migrations/              # Migrações do banco
├── tests/                   # Testes automatizados
├── config.py                # Configurações
├── requirements.txt         # Dependências
└── run.py                   # Ponto de entrada
```

## 🚦 Como Executar (Em Breve)

### Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/teacherflow.git
cd teacherflow

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas configurações

# Inicialize o banco de dados
flask db upgrade

# Execute a aplicação
python run.py
```

A aplicação estará disponível em `http://localhost:8080`

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Este projeto está em fase inicial de desenvolvimento.

### Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrões de Código

- **Python:** PEP 8
- **Commits:** [Conventional Commits](https://www.conventionalcommits.org/)
- **Testes:** Cobertura mínima de 80%

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👥 Autores

- **MontMarcos** - *Desenvolvimento Inicial* - [@montmarcos](https://github.com/montmarcos)

---

## 📧 Contato

Para dúvidas, sugestões ou feedback:

- **Email:** marcos.mont.dev@gmail.com    

---

## 🔗 Links Úteis

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [TailwindCSS Documentation](https://tailwindcss.com/docs)
- [Alpine.js Documentation](https://alpinejs.dev/)

---

<div align="center">

**Feito com ❤️ para professores que fazem a diferença**

⭐ Se este projeto te ajudou, considere dar uma estrela!

</div>
