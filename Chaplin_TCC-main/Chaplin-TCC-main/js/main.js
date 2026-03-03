// Alternância do Menu Mobile (Hambúrguer)
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');
const sidebarToggle = document.getElementById('sidebar-toggle');
const sidebar = document.getElementById('sidebar');

if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', () => {
        if (mobileMenu) {
            mobileMenu.classList.toggle('hidden');
        }
    });
}

if (sidebarToggle) {
    sidebarToggle.addEventListener('click', () => {
        if (sidebar) {
            sidebar.classList.toggle('-translate-x-full');
        }
    });
}

// Fecha o menu mobile ao clicar em um link
const mobileMenuLinks = document.querySelectorAll('#mobile-menu a');
mobileMenuLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (mobileMenu) {
            mobileMenu.classList.add('hidden');
        }
    });
});

// Fecha a barra lateral (sidebar) ao clicar em um link (mobile)
const sidebarLinks = document.querySelectorAll('#sidebar a');
sidebarLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (sidebar && window.innerWidth < 768) {
            sidebar.classList.add('-translate-x-full');
        }
    });
});

// Validação de Formulário
const forms = document.querySelectorAll('form');
forms.forEach(form => {
    form.addEventListener('submit', (e) => {
        const requiredFields = form.querySelectorAll('[required]');
        let isValid = true;

        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                field.classList.add('border-red-500');
                isValid = false;
            } else {
                field.classList.remove('border-red-500');
            }
        });

        if (!isValid) {
            e.preventDefault();
            showNotification('Por favor, preencha todos os campos obrigatórios', 'error');
        }
    });
});

// Remove o estilo de erro quando o usuário começa a digitar
const inputs = document.querySelectorAll('input, textarea, select');
inputs.forEach(input => {
    input.addEventListener('input', () => {
        input.classList.remove('border-red-500');
    });
});

// Sistema de Notificação
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `fixed top-4 right-4 p-4 rounded-lg text-white z-50 animate-fade-in`;

    const bgColor = {
        'success': 'bg-green-500',
        'error': 'bg-red-500',
        'warning': 'bg-yellow-500',
        'info': 'bg-blue-500'
    }[type] || 'bg-blue-500';

    notification.className += ` ${bgColor}`;
    notification.textContent = message;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Rolagem Suave para Links de Âncora
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#') {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// Alternância de Checkbox para Tarefas
const checkboxes = document.querySelectorAll('input[type="checkbox"]');
checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function () {
        const taskRow = this.closest('tr') || this.closest('.bg-white');
        if (taskRow) {
            if (this.checked) {
                taskRow.classList.add('opacity-50');
            } else {
                taskRow.classList.remove('opacity-50');
            }
        }
    });
});

// Barra Lateral Responsiva
window.addEventListener('resize', () => {
    if (window.innerWidth >= 768 && sidebar) {
        sidebar.classList.remove('-translate-x-full');
    }
});

// Inicialização ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
    console.log('Chaplin - Aplicação Carregada');

    // Adiciona animação de fade-in aos cards
    const cards = document.querySelectorAll('.card, .bg-white');
    cards.forEach((card, index) => {
        card.style.animation = `fadeIn 0.3s ease-out ${index * 0.1}s both`;
    });
});

// Previne o envio do formulário para demonstração (demo)
const demoForms = document.querySelectorAll('form');
demoForms.forEach(form => {
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        showNotification('Formulário enviado com sucesso! (Demo)', 'success');
        // Reseta o formulário após 1 segundo
        setTimeout(() => {
            form.reset();
        }, 500);
    });
});

// Adiciona atalhos de teclado
document.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + K para focar na busca
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const searchInput = document.querySelector('input[placeholder*="Buscar"]');
        if (searchInput) {
            searchInput.focus();
        }
    }

    // Escape para fechar a barra lateral
    if (e.key === 'Escape' && sidebar) {
        sidebar.classList.add('-translate-x-full');
    }
});

// Animação de Fade In
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);