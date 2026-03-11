# Chaplin — Plataforma de Gestão de Tarefas Predial

**Chaplin** é um sistema web de gerenciamento de tarefas de manutenção predial, desenvolvido como TCC. Permite que gestores criem e acompanhem ordens de serviço, atribuam responsáveis, coletem evidências fotográficas e mantenham comunicação integrada por tarefa.

---

## ✅ Funcionalidades Implementadas

| Funcionalidade | Status |
|---|---|
| Login / Logout / Registro | ✅ |
| Sistema de Roles (Admin, Gestor, Líder, Colaborador) | ✅ |
| RBAC — controle de acesso por role | ✅ |
| CRUD de Tarefas | ✅ |
| Alocação de responsável por tarefa | ✅ |
| Evidências fotográficas (foto + descrição) | ✅ |
| Comunicação por tarefa (mensagens) | ✅ |
| Endereço de tarefa via ViaCEP (preenchimento automático) | ✅ |
| Gestão de Áreas do Prédio | ✅ |
| Visualização Kanban | ✅ |
| Visualização em Calendário | ✅ |
| Sistema de Notificações em tempo real | ✅ |
| Tema Claro / Escuro (persistente) | ✅ |
| Autenticação de Dois Fatores — 2FA (TOTP) | ✅ |
| Painel de Admin — Gestão de Contas | ✅ |

---

## 🏗️ Estrutura do Projeto

```
Chaplin-TCC/
├── apps/
│   ├── core/              # Home, landing page
│   ├── tasks/             # Tarefas, notificações, áreas
│   │   ├── models.py      # Task, Notification, AreaPredio, TaskEvidence, Message
│   │   ├── views.py       # Toda a lógica de negócio
│   │   ├── forms.py       # Formulários Django
│   │   └── urls.py        # Rotas de tarefas
│   └── users/
│       ├── models.py      # UserProfile (role, 2FA, especialidade, endereço)
│       ├── views.py       # Login, 2FA, perfil, admin de contas
│       └── urls.py        # Rotas de usuários
├── templates/
│   ├── shared/
│   │   └── base_dashboard.html   # Layout base (navbar, sidebar, toggle tema)
│   ├── tasks/                    # Todos os HTMLs de tarefas
│   └── users/                    # Login, 2FA, admin de contas
├── static/
│   ├── css/styles.css
│   ├── js/main.js
│   └── docs/              # Documentação auxiliar
├── chaplin_project/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt       # Todas as dependências Python
└── .env                   # Variáveis de ambiente (NÃO commitar)
```

---

## 🚀 Como Rodar Localmente

> Leia o guia completo em [`static/docs/GUIA_RODAR_LOCALMENTE.md`](static/docs/GUIA_RODAR_LOCALMENTE.md)

**Resumo rápido:**
```bash
git clone https://github.com/Kayque-Freitas/Chaplin-TCC.git
cd Chaplin-TCC
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
# Criar .env (veja o guia)
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Acesse: http://127.0.0.1:8000

---

## 👥 Roles e Permissões

| Role | Criar Tarefa | Alocar | Editar | Ver todos | Admin Contas |
|---|:---:|:---:|:---:|:---:|:---:|
| `admin` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `gestor` | ✅ | ✅ | ✅ | As próprias | ❌ |
| `lider` | ✅ | ✅ | ✅ | ✅ | ❌ |
| `colaborador` | ❌ | ❌ | ❌ | Só as suas | ❌ |

---

## 🔐 Segurança

- CSRF Protection (embutida no Django)
- Senhas com hash (PBKDF2 — padrão Django)
- 2FA via TOTP (pyotp) — opcional por usuário
- RBAC server-side (não depende só do front-end)

---

## 🌐 Principais URLs

| Página | URL |
|---|---|
| Home | `/` |
| Login | `/usuarios/login/` |
| Dashboard | `/tasks/dashboard/` |
| Lista de Tarefas | `/tasks/lista/` |
| Nova Tarefa | `/tasks/criar/` |
| Kanban | `/tasks/kanban/` |
| Calendário | `/tasks/calendario/` |
| Notificações | `/tasks/notificacoes/` |
| Configurações | `/tasks/configuracoes/` |
| Áreas do Prédio | `/tasks/areas/` |
| Ativar 2FA | `/usuarios/2fa/configurar/` |
| Admin de Contas | `/usuarios/admin-panel/usuarios/` |

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia |
|---|---|
| Backend | Python 3.13, Django 4.2 |
| Banco de dados | SQLite (dev) |
| Frontend | HTML5, Tailwind CSS (CDN), JavaScript Vanilla |
| 2FA | pyotp + qrcode |
| CEP | API pública ViaCEP |
| Imagens | Pillow |

---

## 📄 Documentação

- [Guia Completo de Setup](static/docs/GUIA_RODAR_LOCALMENTE.md)
- [Arquitetura Técnica](static/docs/ARQUITETURA_TECNICA.md)
- [Resumo para o Grupo](static/docs/RESUMO_GRUPO.md)
