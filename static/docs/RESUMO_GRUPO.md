# 📖 Chaplin — Resumo para o Grupo

> Referência rápida para todos entenderem e explicarem o projeto.

---

## O que é o Chaplin?

Sistema web de **gestão de tarefas de manutenção predial**. Um gestor abre uma ordem de serviço (tarefa), atribui a um colaborador técnico, e o colaborador executa, documenta com fotos (evidências) e marca como concluída.

**Stack:** Python + Django (back-end) | HTML + Tailwind CSS (front-end) | SQLite ou PostgreSQL (banco de dados) | Host em Nuvem (Render)

---

## Roles — Tipos de Usuário

| Role | O que pode fazer |
|---|---|
| **admin** | Tudo + gerenciar contas |
| **gestor** | Criar/editar/alocar tarefas + gerenciar áreas |
| **lider** | Criar/editar/alocar tarefas |
| **colaborador** | Ver e concluir apenas as tarefas atribuídas a ele |

---

## Funcionalidades e Como Funcionam

### 🔐 Login e Autenticação
- **Arquivo:** `apps/users/views.py` → função `login_view`
- Django verifica usuário+senha com `authenticate()`
- Se 2FA ativado: salva o ID na sessão e redireciona para verificar o código antes de logar

### 🔑 2FA (Dois Fatores)
- Usa `pyotp` para gerar/verificar códigos TOTP (mudam a cada 30s)
- Setup: gera QR Code → usuário escaneia com Google Authenticator/Authy → confirma 1º código
- Na configuração: **Configurações → Segurança → Ativar 2FA**

### 📋 Tarefas
- **Model:** `Task` em `apps/tasks/models.py`
- Status: `aberta → alocada → concluida → finalizada`
- Prioridade: `baixa, normal, alta, urgente`
- Campos de endereço integrados ao ViaCEP

### 📍 ViaCEP — Endereço Automático
- Usuário digita o CEP no formulário
- JavaScript chama `https://viacep.com.br/ws/{cep}/json/`
- Preenche logradouro, bairro, cidade, estado automaticamente
- Detalhe da tarefa mostra link "Ver no Google Maps"

### 🔔 Notificações
- Criadas automaticamente pela função `_notify()` em `views.py`
- Gatilhos: tarefa criada, atribuída, concluída, nova mensagem
- Sino na navbar mostra badge vermelho com contagem (via AJAX)
- Central em `/tasks/notificacoes/`

### 🌙 Tema Claro/Escuro
- Botão sol/lua na navbar
- Usa Tailwind `darkMode: 'class'` — adiciona/remove classe `dark` na `<html>`
- Preferência salva no `localStorage` do navegador
- Script no `<head>` aplica o tema antes da página aparecer (sem piscar)

### 🏢 Áreas do Prédio
- Gestor cadastra as áreas físicas (ex: "Sala de Servidores - 3º Andar")
- Cada tarefa pode ser vinculada a uma área
- CRUD completo em `/tasks/areas/`

### 🛡️ RBAC — Controle de Acesso
- **Server-side:** views checam `_is_manager(user)` antes de executar
- **Front-end:** botões/menus são exibidos condicionalmente com `{% if %}`
- Colaborador que tenta acessar URL restrita é redirecionado com mensagem de erro

---

## Banco de Dados — Tabelas Principais

| Tabela | Guarda |
|---|---|
| `auth_user` | Usuários (Django padrão) |
| `users_userprofile` | Role, 2FA, especialidade, endereço pessoal |
| `tasks_task` | Tarefas (título, status, prioridade, endereço, área) |
| `tasks_taskevidence` | Evidências fotográficas das tarefas |
| `tasks_message` | Mensagens/comentários por tarefa |
| `tasks_notification` | Notificações do sistema |
| `tasks_areapredio` | Áreas físicas do prédio |

---

## Arquivos Mais Importantes

| Arquivo | Função |
|---|---|
| `apps/tasks/models.py` | Define o que é salvo no banco de dados |
| `apps/tasks/views.py` | Toda a lógica de negócio (o que acontece quando o usuário clica) |
| `apps/users/views.py` | Login, 2FA, gestão de contas |
| `templates/shared/base_dashboard.html` | Layout base: navbar, sidebar, tema |
| `templates/tasks/dashboard.html` | Página inicial com estatísticas |
| `chaplin_project/settings.py` | Configurações do Django (banco, apps, segurança) |
| `requirements.txt` | Lista de bibliotecas Python necessárias |
| `.env` | Chave secreta e configurações sensíveis (não está no git) |

---

## Setup Rápido (novo computador)

```bash
git clone https://github.com/Kayque-Freitas/Chaplin-TCC.git
cd Chaplin-TCC
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# criar .env com SECRET_KEY=qualquer-coisa e DEBUG=True
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

> Guia completo: `static/docs/GUIA_RODAR_LOCALMENTE.md`
