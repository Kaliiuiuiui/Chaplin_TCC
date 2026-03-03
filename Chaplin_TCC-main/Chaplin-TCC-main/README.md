# Chaplin - Plataforma de Gerenciamento de Tarefas

Um projeto HTML/CSS estático com Tailwind CSS, responsivo e pronto para ser expandido com funcionalidades backend.

## 📋 Estrutura do Projeto

```
chaplin_static/
├── index.html              # Página inicial (Homepage)
├── css/
│   └── styles.css         # Estilos customizados
├── js/
│   └── main.js            # Scripts de interatividade
├── pages/
│   ├── login.html         # Página de login
│   ├── dashboard.html     # Dashboard principal
│   ├── tarefas.html       # Listagem de tarefas
│   ├── nova-tarefa.html   # Formulário de nova tarefa
│   └── configuracoes.html # Página de configurações
├── assets/
│   └── images/            # Pasta para imagens
└── README.md              # Este arquivo
```

## 🚀 Como Usar

### 1. Abrir no VS Code
```bash
# Abra a pasta do projeto no VS Code
code chaplin_static/
```

### 2. Servir Localmente
Você pode usar a extensão "Live Server" do VS Code:
- Clique com botão direito em `index.html`
- Selecione "Open with Live Server"

Ou use um servidor Python:
```bash
python -m http.server 8000
```

Acesse: `http://localhost:8000`

### 3. Estrutura de Páginas

#### **Homepage (index.html)**
- Navegação responsiva com menu hambúrguer
- Hero section com CTA
- Seção "Sobre Nós"
- Cards de serviços
- Footer com links

#### **Login (pages/login.html)**
- Formulário de autenticação
- Email e senha
- Links para recuperação de senha e cadastro

#### **Dashboard (pages/dashboard.html)**
- Sidebar colapsável (responsivo)
- Cards de estatísticas
- Listagem de tarefas recentes
- Menu de navegação

#### **Tarefas (pages/tarefas.html)**
- Tabela de tarefas (desktop)
- Cards de tarefas (mobile)
- Filtros por status, prioridade e responsável
- Ações de editar/deletar

#### **Nova Tarefa (pages/nova-tarefa.html)**
- Formulário completo com campos:
  - Título (obrigatório)
  - Descrição
  - Prioridade
  - Data de vencimento
  - Responsável
  - Tags
  - Notificações

#### **Configurações (pages/configuracoes.html)**
- Abas de configuração
- Formulário de perfil
- Upload de foto de perfil

## 🎨 Design e Estilos

### Tailwind CSS
O projeto usa **Tailwind CSS via CDN**. Para customizar:

1. Edite as cores em `css/styles.css` (variáveis CSS)
2. Adicione classes Tailwind direto no HTML
3. Customize em `css/styles.css` para estilos globais

### Cores Principais
- **Primária**: Orange (#f97316)
- **Secundária**: Gray (#1f2937)
- **Fundo**: White (#ffffff)
- **Fundo Secundário**: Light Gray (#f9fafb)

## 📱 Responsividade

O projeto é **mobile-first** com breakpoints:
- **Mobile**: < 640px
- **Tablet**: 640px - 1024px
- **Desktop**: > 1024px

### Componentes Responsivos
- ✅ Navegação com menu hambúrguer
- ✅ Sidebar colapsável
- ✅ Tabelas que viram cards em mobile
- ✅ Grid layouts adaptativos
- ✅ Imagens responsivas

## 🔧 Funcionalidades Implementadas

### ✅ Completas
- [x] Estrutura HTML semântica
- [x] Estilos Tailwind CSS
- [x] Menu responsivo mobile-first
- [x] Sidebar colapsável
- [x] Formulários estilizados
- [x] Cards e componentes reutilizáveis
- [x] Animações suaves
- [x] Validação básica de formulários
- [x] Sistema de notificações
- [x] Atalhos de teclado (Ctrl+K, Esc)

### ⏳ Prontas para Expansão
- [ ] Integração com backend (API)
- [ ] Autenticação real
- [ ] Persistência de dados
- [ ] Funcionalidades de CRUD
- [ ] Filtros dinâmicos
- [ ] Paginação
- [ ] Busca em tempo real
- [ ] Temas dark/light

## 📝 Como Expandir

### Adicionar Nova Página
1. Crie um arquivo `pages/nova-pagina.html`
2. Copie a estrutura de outra página
3. Customize o HTML e CSS
4. Adicione o link na navegação

### Adicionar Novo Componente
1. Crie um novo arquivo em `components/` (opcional)
2. Ou adicione direto no HTML com classes Tailwind
3. Reutilize em outras páginas

### Integrar com Backend
1. Remova `e.preventDefault()` dos formulários em `js/main.js`
2. Adicione endpoints da API
3. Use `fetch()` para comunicação com servidor
4. Processe respostas JSON

Exemplo:
```javascript
// Em js/main.js
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const response = await fetch('/api/tarefas', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(formData))
    });
    const data = await response.json();
    showNotification('Tarefa criada!', 'success');
});
```

## 🎯 Próximos Passos Recomendados

1. **Substituir Tailwind CDN por Build Tool**
   ```bash
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```

2. **Adicionar Backend**
   - Node.js + Express
   - Python + Flask
   - Ou qualquer framework de sua preferência

3. **Implementar Banco de Dados**
   - MySQL/PostgreSQL
   - MongoDB
   - Firebase

4. **Adicionar Autenticação Real**
   - JWT
   - OAuth
   - Sessões

5. **Melhorar Performance**
   - Minificar CSS/JS
   - Otimizar imagens
   - Implementar lazy loading

## 🛠️ Tecnologias Usadas

- **HTML5** - Estrutura semântica
- **CSS3** - Estilos e animações
- **Tailwind CSS** - Framework de estilos
- **JavaScript Vanilla** - Interatividade
- **Responsive Design** - Mobile-first

## 📄 Licença

Este projeto é fornecido como base para desenvolvimento. Sinta-se livre para modificar e expandir conforme necessário.

## 💡 Dicas

- Use o DevTools do navegador para testar responsividade
- Teste em diferentes dispositivos/tamanhos de tela
- Mantenha o código limpo e bem organizado
- Adicione comentários para facilitar manutenção futura
- Considere usar um build tool quando escalar o projeto

---

**Desenvolvido com ❤️ para Chaplin**
