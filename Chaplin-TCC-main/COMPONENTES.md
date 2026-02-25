# Componentes Reutilizáveis - Chaplin

Documentação dos componentes HTML/CSS reutilizáveis do projeto.

## 📦 Componentes Disponíveis

### 1. Botões

#### Botão Primário
```html
<button class="bg-orange-500 hover:bg-orange-600 text-white font-semibold py-2 px-4 rounded-lg transition">
    Botão Primário
</button>
```

#### Botão Secundário
```html
<button class="border-2 border-orange-500 text-orange-500 hover:bg-orange-500 hover:text-white font-semibold py-2 px-4 rounded-lg transition">
    Botão Secundário
</button>
```

#### Botão Pequeno
```html
<button class="bg-orange-500 hover:bg-orange-600 text-white font-semibold py-1 px-3 rounded text-sm transition">
    Pequeno
</button>
```

#### Botão Grande
```html
<button class="bg-orange-500 hover:bg-orange-600 text-white font-semibold py-3 px-8 rounded-lg transition text-lg">
    Grande
</button>
```

---

### 2. Cards

#### Card Básico
```html
<div class="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition">
    <h3 class="text-xl font-bold mb-3">Título do Card</h3>
    <p class="text-gray-600">Conteúdo do card</p>
</div>
```

#### Card com Ícone
```html
<div class="bg-white rounded-lg shadow-md p-8 hover:shadow-lg transition">
    <div class="w-16 h-16 bg-orange-100 rounded-full flex items-center justify-center mb-4">
        <svg class="w-8 h-8 text-orange-500" fill="currentColor" viewBox="0 0 20 20">
            <!-- SVG Icon -->
        </svg>
    </div>
    <h3 class="text-xl font-bold mb-3">Título</h3>
    <p class="text-gray-600">Descrição</p>
</div>
```

#### Card de Tarefa
```html
<div class="bg-white rounded-lg shadow-md p-6">
    <div class="flex justify-between items-start mb-4">
        <h3 class="text-lg font-semibold text-gray-900">Título da Tarefa</h3>
        <span class="inline-block bg-blue-100 text-blue-800 px-2 py-1 rounded text-xs font-semibold">
            Status
        </span>
    </div>
    <div class="space-y-2 mb-4">
        <p class="text-sm text-gray-600"><strong>Responsável:</strong> Nome</p>
        <p class="text-sm text-gray-600"><strong>Vencimento:</strong> Data</p>
    </div>
    <div class="flex gap-2">
        <button class="flex-1 text-orange-500 hover:bg-orange-50 py-2 rounded">Editar</button>
        <button class="flex-1 text-red-500 hover:bg-red-50 py-2 rounded">Deletar</button>
    </div>
</div>
```

---

### 3. Inputs e Formulários

#### Input de Texto
```html
<div>
    <label for="name" class="block text-sm font-medium text-gray-700 mb-2">
        Nome
    </label>
    <input
        type="text"
        id="name"
        placeholder="Digite seu nome"
        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent"
    >
</div>
```

#### Input de Email
```html
<div>
    <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
        Email
    </label>
    <input
        type="email"
        id="email"
        placeholder="seu@email.com"
        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent"
    >
</div>
```

#### Textarea
```html
<div>
    <label for="message" class="block text-sm font-medium text-gray-700 mb-2">
        Mensagem
    </label>
    <textarea
        id="message"
        rows="5"
        placeholder="Digite sua mensagem"
        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent"
    ></textarea>
</div>
```

#### Select
```html
<div>
    <label for="priority" class="block text-sm font-medium text-gray-700 mb-2">
        Prioridade
    </label>
    <select
        id="priority"
        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent"
    >
        <option value="">Selecione</option>
        <option value="baixa">Baixa</option>
        <option value="media">Média</option>
        <option value="alta">Alta</option>
    </select>
</div>
```

#### Checkbox
```html
<label class="flex items-center">
    <input type="checkbox" class="rounded border-gray-300 text-orange-500">
    <span class="ml-2 text-sm text-gray-600">Concordo com os termos</span>
</label>
```

#### Radio Button
```html
<label class="flex items-center">
    <input type="radio" name="option" class="rounded-full border-gray-300 text-orange-500">
    <span class="ml-2 text-sm text-gray-600">Opção 1</span>
</label>
```

---

### 4. Badges/Tags

#### Badge de Sucesso
```html
<span class="inline-block bg-green-100 text-green-800 px-3 py-1 rounded-full text-xs font-semibold">
    Concluída
</span>
```

#### Badge de Aviso
```html
<span class="inline-block bg-yellow-100 text-yellow-800 px-3 py-1 rounded-full text-xs font-semibold">
    Pendente
</span>
```

#### Badge de Erro
```html
<span class="inline-block bg-red-100 text-red-800 px-3 py-1 rounded-full text-xs font-semibold">
    Urgente
</span>
```

#### Badge de Informação
```html
<span class="inline-block bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-xs font-semibold">
    Em Progresso
</span>
```

---

### 5. Navegação

#### Menu Horizontal
```html
<nav class="bg-white border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
            <a href="/" class="text-2xl font-bold text-orange-500">Logo</a>
            <div class="hidden md:flex space-x-8">
                <a href="#" class="text-gray-700 hover:text-orange-500">Link 1</a>
                <a href="#" class="text-gray-700 hover:text-orange-500">Link 2</a>
            </div>
        </div>
    </div>
</nav>
```

#### Menu Hambúrguer (Mobile)
```html
<button id="mobile-menu-btn" class="md:hidden text-gray-700 hover:text-orange-500">
    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
    </svg>
</button>

<div id="mobile-menu" class="hidden md:hidden">
    <a href="#" class="block px-2 py-2">Link 1</a>
    <a href="#" class="block px-2 py-2">Link 2</a>
</div>
```

---

### 6. Tabelas

#### Tabela Responsiva
```html
<table class="w-full">
    <thead class="bg-gray-100 border-b border-gray-200">
        <tr>
            <th class="px-6 py-3 text-left text-sm font-semibold text-gray-700">Coluna 1</th>
            <th class="px-6 py-3 text-left text-sm font-semibold text-gray-700">Coluna 2</th>
            <th class="px-6 py-3 text-left text-sm font-semibold text-gray-700">Ações</th>
        </tr>
    </thead>
    <tbody class="divide-y divide-gray-200">
        <tr class="hover:bg-gray-50 transition">
            <td class="px-6 py-4 text-sm text-gray-900">Dado 1</td>
            <td class="px-6 py-4 text-sm text-gray-900">Dado 2</td>
            <td class="px-6 py-4 text-sm">
                <button class="text-orange-500 hover:text-orange-600">Editar</button>
            </td>
        </tr>
    </tbody>
</table>
```

---

### 7. Modais/Diálogos

#### Modal Básico
```html
<div id="modal" class="hidden fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div class="bg-white rounded-lg shadow-lg p-8 max-w-md w-full mx-4">
        <h2 class="text-2xl font-bold mb-4">Título do Modal</h2>
        <p class="text-gray-600 mb-6">Conteúdo do modal</p>
        <div class="flex gap-4">
            <button class="flex-1 bg-orange-500 hover:bg-orange-600 text-white font-semibold py-2 rounded-lg">
                Confirmar
            </button>
            <button class="flex-1 bg-gray-200 hover:bg-gray-300 text-gray-700 font-semibold py-2 rounded-lg">
                Cancelar
            </button>
        </div>
    </div>
</div>
```

---

### 8. Alertas

#### Alerta de Sucesso
```html
<div class="bg-green-50 border border-green-200 rounded-lg p-4 mb-4">
    <p class="text-green-800 font-semibold">Sucesso!</p>
    <p class="text-green-700 text-sm">Operação realizada com sucesso.</p>
</div>
```

#### Alerta de Erro
```html
<div class="bg-red-50 border border-red-200 rounded-lg p-4 mb-4">
    <p class="text-red-800 font-semibold">Erro!</p>
    <p class="text-red-700 text-sm">Ocorreu um erro ao processar.</p>
</div>
```

#### Alerta de Aviso
```html
<div class="bg-yellow-50 border border-yellow-200 rounded-lg p-4 mb-4">
    <p class="text-yellow-800 font-semibold">Aviso!</p>
    <p class="text-yellow-700 text-sm">Atenção: verifique antes de continuar.</p>
</div>
```

---

### 9. Grids

#### Grid 2 Colunas
```html
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    <div>Coluna 1</div>
    <div>Coluna 2</div>
</div>
```

#### Grid 3 Colunas
```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
    <div>Coluna 1</div>
    <div>Coluna 2</div>
    <div>Coluna 3</div>
</div>
```

#### Grid 4 Colunas
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
    <div>Coluna 1</div>
    <div>Coluna 2</div>
    <div>Coluna 3</div>
    <div>Coluna 4</div>
</div>
```

---

## 🎨 Cores Disponíveis

### Primárias
- `text-orange-500` - Laranja principal
- `bg-orange-500` - Fundo laranja
- `hover:bg-orange-600` - Hover laranja escuro

### Neutras
- `text-gray-900` - Texto escuro
- `text-gray-600` - Texto médio
- `text-gray-400` - Texto claro
- `bg-gray-50` - Fundo claro
- `bg-gray-100` - Fundo médio
- `bg-gray-900` - Fundo escuro

### Estados
- `bg-green-100 text-green-800` - Sucesso
- `bg-red-100 text-red-800` - Erro
- `bg-yellow-100 text-yellow-800` - Aviso
- `bg-blue-100 text-blue-800` - Informação

---

## 💡 Dicas de Uso

1. **Reutilize componentes**: Copie o código e adapte conforme necessário
2. **Mantenha consistência**: Use as mesmas cores e espaçamentos
3. **Teste responsividade**: Sempre teste em mobile, tablet e desktop
4. **Acessibilidade**: Sempre use labels em inputs e alt em imagens
5. **Performance**: Minimize o uso de animações pesadas

---

**Desenvolvido com ❤️ para Chaplin**
