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

## 🚀 Status do Projeto

⚠️ **Projeto em desenvolvimento ativo** - MVP planejado para conclusão em 6 semanas.

### Roadmap

- [x] Planejamento e documentação completa
- [ ] **Semana 1-2:** Setup inicial + Autenticação + Models base
- [ ] **Semana 3:** Gestão de Turmas e Alunos
- [ ] **Semana 4:** Banco de Atividades + Busca
- [ ] **Semana 5:** Planos de Aula + Sistema de Presença
- [ ] **Semana 6:** Sistema de Notas + Relatórios + Polimento

---

## 🛠️ Stack Tecnológica

### Backend
- **Framework:** Flask 3.0
- **ORM:** Flask-SQLAlchemy
- **Autenticação:** Flask-Login
- **Formulários:** Flask-WTF
- **Migrations:** Flask-Migrate

### Frontend
- **Template Engine:** Jinja2
- **CSS Framework:** TailwindCSS (via CDN)
- **JavaScript:** Alpine.js

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

---

## 🎯 Funcionalidades Principais (MVP)

### ✅ MUST HAVE - Essenciais

1. **Dashboard do Professor**
   - Visão geral de turmas e pendências
   - Ações rápidas para tarefas comuns

2. **Autenticação Completa**
   - Login/Signup seguro
   - Proteção de rotas
   - Gerenciamento de sessão

3. **Gestão de Turmas**
   - CRUD completo de turmas
   - Gerenciamento de alunos
   - Histórico individual dos alunos

4. **Banco de Atividades**
   - Criação e organização de atividades
   - Busca por texto e filtros combinados
   - Sistema de tags
   - Reutilização de conteúdo

5. **Planos de Aula**
   - Criação rápida (2 minutos)
   - Vinculação com atividades do banco
   - Histórico de aulas

6. **Registro de Presença**
   - Interface ágil de marcação
   - Relatórios de frequência
   - Alertas de faltas excessivas

7. **Sistema de Avaliações**
   - Criação de avaliações
   - Lançamento de notas
   - Estatísticas automáticas
   - Exportação de boletins

8. **Anotações sobre Alunos**
   - Registro de observações
   - Categorização (comportamento, aprendizado)
   - Preparação para reuniões de pais

### 🎁 SHOULD HAVE - Valor Adicional

9. **Gerador de PDF**
   - Listas de exercícios formatadas
   - Inclusão de gabarito

10. **Relatórios Automáticos**
    - Frequência e desempenho
    - Comparativos entre turmas

11. **Calendário de Aulas**
    - Visão mensal de planejamento
    - Sincronização com planos

---

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

A aplicação estará disponível em `http://localhost:5000`

---

## 🧪 Testes

```bash
# Execute os testes
pytest

# Com cobertura
pytest --cov=app tests/

# Testes específicos
pytest tests/test_auth.py
```

---

## 📊 Modelo de Dados

### Entidades Principais

- **User (Professor):** Informações do professor
- **Turma:** Turmas lecionadas
- **Aluno:** Alunos de cada turma
- **Atividade:** Banco de questões e materiais
- **PlanoAula:** Planejamento de aulas
- **RegistroPresenca:** Controle de frequência
- **Avaliacao:** Provas e trabalhos
- **NotaAluno:** Notas dos alunos
- **AnotacaoAluno:** Observações sobre alunos

### Relacionamentos

```
User (1) -----> (N) Turma
Turma (1) ----> (N) Aluno
User (1) -----> (N) Atividade
Turma (1) ----> (N) PlanoAula
PlanoAula (N) <---> (N) Atividade (Many-to-Many)
Aluno (1) ----> (N) RegistroPresenca
Turma (1) ----> (N) Avaliacao
Avaliacao (1) -> (N) NotaAluno
Aluno (1) ----> (N) AnotacaoAluno
```

---

## 📖 Documentação

- **[Documento Completo do MVP](docs/OO_bmvc.pdf)** - Planejamento detalhado
- **[Guia de Contribuição](CONTRIBUTING.md)** *(em breve)*
- **[Changelog](CHANGELOG.md)** *(em breve)*

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

- **Seu Nome** - *Desenvolvimento Inicial* - [@seu-usuario](https://github.com/seu-usuario)

---

## 🎯 Métricas de Sucesso do MVP

- ✅ 10 professores ativos (usando 2x por semana)
- ✅ Cada professor com pelo menos 2 turmas cadastradas
- ✅ Pelo menos 10 atividades no banco por professor
- ✅ 50+ planos de aula criados
- ✅ 100+ registros de presença
- ✅ Feedback qualitativo: "Economizou meu tempo?"

---

## 📧 Contato

Para dúvidas, sugestões ou feedback:

- **Email:** seu.email@exemplo.com
- **LinkedIn:** [Seu Nome](https://linkedin.com/in/seu-perfil)
- **Twitter:** [@seu_usuario](https://twitter.com/seu_usuario)

---

## 🙏 Agradecimentos

- Professores que inspiraram este projeto
- Comunidade Flask
- Todos os educadores que dedicam suas vidas ao ensino

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