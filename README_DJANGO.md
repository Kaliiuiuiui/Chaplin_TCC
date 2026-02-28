# Chaplin - Plataforma de Gestão de Tarefas de Manutenção

## 🎯 Sobre o Projeto

Chaplin é uma plataforma web desenvolvida como projeto de TCC para empresas terceirizadas de manutenção em hotéis e propriedades de aluguel. A aplicação centraliza a comunicação entre gestores de prédios e equipes de manutenção.

## 📋 Requisitos

- Python 3.8+
- MySQL 5.7+
- pip (gerenciador de pacotes Python)
- Git

## 🚀 Como Rodar Localmente

### 1. Clonar o Repositório

```bash
git clone https://github.com/Kayque-Freitas/Chaplin-TCC.git
cd Chaplin-TCC
```

### 2. Criar Ambiente Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Banco de Dados

#### Criar banco de dados MySQL:

```sql
CREATE DATABASE chaplin_db;
CREATE USER 'chaplin_user'@'localhost' IDENTIFIED BY 'admin123';
GRANT ALL PRIVILEGES ON chaplin_db.* TO 'chaplin_user'@'localhost';
FLUSH PRIVILEGES;
```

#### Criar arquivo `.env`:

```bash
cp .env.example .env
```

Editar `.env` com suas configurações:

```
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
DB_NAME=chaplin_db
DB_USER=chaplin_user
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306
```

### 5. Executar Migrações

```bash
python manage.py migrate
```

### 6. Criar Superusuário (Admin)

```bash
python manage.py createsuperuser
```

Siga as instruções para criar um usuário administrador.

### 7. Rodar o Servidor

```bash
python manage.py runserver
```

Acesse: `http://localhost:8000`

## 📊 Estrutura do Projeto

```
Chaplin-TCC/
├── chaplin_project/          # Configurações principais
│   ├── settings.py           # Configurações do Django
│   ├── urls.py               # URLs principais
│   └── wsgi.py               # WSGI para deploy
├── apps/
│   ├── users/                # App de usuários
│   │   ├── models.py         # Modelos (UserProfile)
│   │   ├── views.py          # Views (login, registro)
│   │   ├── urls.py           # URLs do app
│   │   └── forms.py          # Formulários
│   ├── tasks/                # App de tarefas
│   │   ├── models.py         # Modelos (Task, Evidence, Message)
│   │   ├── views.py          # Views (CRUD de tarefas)
│   │   ├── urls.py           # URLs do app
│   │   └── forms.py          # Formulários
│   └── core/                 # App principal
│       ├── views.py          # Views (home, about)
│       └── urls.py           # URLs
├── templates/                # Templates HTML
├── static/                   # Arquivos estáticos (CSS, JS)
├── manage.py                 # Gerenciador do Django
└── requirements.txt          # Dependências
```

## 🔐 Roles de Usuário

1. **Admin**: Gerencia empresa, usuários e relatórios
2. **Gestor do Prédio**: Cria tarefas e valida conclusão
3. **Líder de Equipe**: Recebe tarefas e aloca a colaboradores
4. **Colaborador**: Executa tarefas e registra evidências

## 📝 Fluxo de Tarefas

1. Gestor cria tarefa na plataforma
2. Tarefa é enviada para o Líder (o "tobogã")
3. Líder aloca tarefa ao Colaborador
4. Colaborador executa e registra evidências
5. Gestor valida e finaliza

## 🛠️ Comandos Úteis

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Coletar arquivos estáticos
python manage.py collectstatic

# Acessar shell do Django
python manage.py shell

# Rodar testes
python manage.py test
```

## 🎨 Customização de Design

O projeto usa **Tailwind CSS** via CDN. Os estilos customizados estão em:
- `static/css/styles.css` - Estilos customizados
- `templates/` - Templates HTML

Cores principais:
- **Primária**: Orange (#f97316)
- **Secundária**: Gray (#1f2937)

## 📚 Documentação Adicional

- [Documento TCC](./CHAPLIN_TCC_DOCUMENTO_REFORMULADO.pdf)
- [Plano de Implementação](./CHAPLIN_PLANO_IMPLEMENTACAO.md)
- [Guia de Banco de Dados](./GUIA_BANCO_DADOS.md)

## 🤝 Contribuindo

Este é um projeto de TCC. Para contribuir:

1. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
2. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
3. Push para a branch (`git push origin feature/AmazingFeature`)
4. Abra um Pull Request

## 📧 Contato

Para dúvidas sobre o projeto, abra uma issue no GitHub.

---

**Desenvolvido como Projeto de TCC - ETEC**
