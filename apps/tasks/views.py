from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Task, TaskEvidence, Message, AreaPredio, Notification
from .forms import TaskForm
from apps.users.models import UserProfile
from django.db.models import Q
from django.contrib.auth.models import User as AuthUser
from django.contrib import messages as django_messages


def _notify(recipient, titulo, mensagem='', tipo='sistema', task=None):
    """Cria uma notificação para um usuário."""
    if recipient:
        Notification.objects.create(
            recipient=recipient,
            titulo=titulo,
            mensagem=mensagem,
            tipo=tipo,
            task=task,
        )


def _get_role(user):
    """Retorna o role do usuário ou 'colaborador' como padrão."""
    return getattr(getattr(user, 'profile', None), 'role', 'colaborador')


def _is_manager(user):
    """True para admin, gestor e lider (quem pode criar/editar/alocar tarefas)."""
    return _get_role(user) in ('admin', 'gestor', 'lider')

@login_required
def dashboard_view(request):
    """View do dashboard com estatísticas"""
    if not hasattr(request.user, 'profile'):
        UserProfile.objects.create(user=request.user, role='admin' if request.user.is_superuser else 'colaborador')
    user_profile = request.user.profile
    
    if user_profile.role == 'gestor':
        tasks = Task.objects.filter(created_by=request.user)
    elif user_profile.role == 'lider':
        tasks = Task.objects.filter(status__in=['aberta', 'alocada'])
    elif user_profile.role == 'colaborador':
        tasks = Task.objects.filter(assigned_to=request.user)
    else:
        tasks = Task.objects.all()
    
    context = {
        'tasks': tasks,
        'total_tasks': tasks.count(),
        'open_tasks': tasks.filter(status='aberta').count(),
        'assigned_tasks': tasks.filter(status='alocada').count(),
        'completed_tasks': tasks.filter(status__in=['concluida', 'finalizada']).count(),
    }
    return render(request, 'tasks/dashboard.html', context)

@login_required
def tasks_list_view(request):
    """View da lista de tarefas com filtros"""
    status = request.GET.get('status', '')
    priority = request.GET.get('priority', '')
    search = request.GET.get('search', '')
    responsavel = request.GET.get('responsavel', '')
    
    # Restrição baseada em Roles para listar tarefas
    user_profile = getattr(request.user, 'profile', None)
    if user_profile and user_profile.role == 'gestor':
        tasks = Task.objects.filter(created_by=request.user)
    elif user_profile and user_profile.role == 'colaborador':
        tasks = Task.objects.filter(assigned_to=request.user)
    else:
        # Lideres e admins veem todas (ou filtrado por alocada/aberta se líder, mas manteremos simples na listagem geral)
        tasks = Task.objects.all()
    
    # Filtro de Busca (Texto)
    if search:
        tasks = tasks.filter(
            Q(title__icontains=search) | 
            Q(description__icontains=search) |
            Q(location__icontains=search)
        )
        
    # Filtros exatos
    if status:
        tasks = tasks.filter(status=status)
    if priority:
        tasks = tasks.filter(priority=priority)
    if responsavel:
        tasks = tasks.filter(assigned_to__username=responsavel) # Ou ID, mas username é mais seguro pro dropdown
        
    context = {
        'tasks': tasks,
        'current_status': status,
        'current_priority': priority,
        'current_search': search,
    }
    
    return render(request, 'tasks/list.html', context)

@login_required
def create_task_view(request):
    """View para criar nova tarefa — restrito a gestor/admin/líder."""
    if not _is_manager(request.user):
        django_messages.error(request, 'Você não tem permissão para criar tarefas.')
        return redirect('tasks:list')
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            # Notificar gestores sobre nova tarefa (exceto o criador)
            for user in AuthUser.objects.filter(profile__role__in=['gestor', 'admin']).exclude(pk=request.user.pk):
                _notify(user, f'Nova tarefa criada: {task.title}',
                        mensagem=f'Criada por {request.user.get_full_name() or request.user.username}.',
                        tipo='tarefa_criada', task=task)
            return redirect('tasks:detail', pk=task.pk)
    else:
        form = TaskForm()

    return render(request, 'tasks/create.html', {'form': form})

@login_required
def task_detail_view(request, pk):
    """View do detalhe da tarefa.
    Colaboradores só podem ver tarefas atribuídas a eles.
    """
    task = get_object_or_404(Task, pk=pk)
    role = _get_role(request.user)
    # Colaboradores só acessam tarefas suas
    if role == 'colaborador' and task.assigned_to != request.user:
        django_messages.error(request, 'Você não tem acesso a esta tarefa.')
        return redirect('tasks:list')
    task_messages = task.messages.all()
    evidences = task.evidences.all()

    return render(request, 'tasks/detail.html', {
        'task': task,
        'messages': task_messages,
        'evidences': evidences,
        'can_manage': _is_manager(request.user),
    })

@login_required
def edit_task_view(request, pk):
    """View para editar tarefa — restrito a gestor/admin/líder."""
    if not _is_manager(request.user):
        django_messages.error(request, 'Você não tem permissão para editar tarefas.')
        return redirect('tasks:detail', pk=pk)
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/edit.html', {'form': form, 'task': task})

@login_required
def assign_task_view(request, pk):
    """View para alocar tarefa — restrito a gestor/admin/líder."""
    if not _is_manager(request.user):
        django_messages.error(request, 'Você não tem permissão para alocar tarefas.')
        return redirect('tasks:detail', pk=pk)
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        task.assigned_to_id = user_id
        task.status = 'alocada'
        task.save()
        # Notificar o responsavel alocado
        if task.assigned_to:
            _notify(task.assigned_to,
                    f'Tarefa atribuída: {task.title}',
                    mensagem=f'Você foi alocado para esta tarefa por {request.user.get_full_name() or request.user.username}.',
                    tipo='tarefa_atribuida', task=task)
        return redirect('tasks:detail', pk=task.pk)
    
    return render(request, 'tasks/assign.html', {'task': task})

@login_required
def complete_task_view(request, pk):
    """View para marcar tarefa como concluída"""
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        description = request.POST.get('description', '')
        tempo_gasto = request.POST.get('tempo_gasto', '')
        materiais_utilizados = request.POST.get('materiais_utilizados', '')
        photo = request.FILES.get('photo')
        
        # Opcionalmente exigir alguns campos ou apenas instanciar
        evidence = TaskEvidence(
            task=task,
            description=description,
            tempo_gasto=tempo_gasto,
            materiais_utilizados=materiais_utilizados
        )
        if photo:
            evidence.photo = photo
        evidence.save()
        
        task.status = 'concluida'
        task.save()
        # Notificar o criador da tarefa sobre conclusão
        if task.created_by and task.created_by != request.user:
            _notify(task.created_by,
                    f'Tarefa concluída: {task.title}',
                    mensagem=f'Concluída por {request.user.get_full_name() or request.user.username}.',
                    tipo='tarefa_concluida', task=task)
        return redirect('tasks:detail', pk=task.pk)
    
    return render(request, 'tasks/complete.html', {'task': task})

@login_required
def add_message_view(request, pk):
    """View para adicionar mensagem/comentário"""
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(task=task, sender=request.user, content=content)
            # Notificar o responsavel e o criador (exceto o remetente)
            recipients = set()
            if task.assigned_to and task.assigned_to != request.user:
                recipients.add(task.assigned_to)
            if task.created_by and task.created_by != request.user:
                recipients.add(task.created_by)
            for recipient in recipients:
                _notify(recipient,
                        f'Nova mensagem em: {task.title}',
                        mensagem=f'{request.user.get_full_name() or request.user.username}: {content[:80]}',
                        tipo='nova_mensagem', task=task)
        return redirect('tasks:detail', pk=task.pk)
    
    return render(request, 'tasks/message.html', {'task': task})


@login_required
def notifications_view(request):
    """Lista todas as notificações do usuário logado."""
    notifications = Notification.objects.filter(recipient=request.user)
    # Marcar todas como lidas ao abrir a página
    notifications.filter(lida=False).update(lida=True)
    return render(request, 'tasks/notifications.html', {'notifications': notifications})


@login_required
def mark_notification_read(request, pk):
    """Marca uma notificação específica como lida via AJAX."""
    notif = get_object_or_404(Notification, pk=pk, recipient=request.user)
    notif.lida = True
    notif.save()
    return JsonResponse({'ok': True})


@login_required
def unread_notifications_count(request):
    """Retorna o número de notificações não lidas do usuário logado."""
    count = Notification.objects.filter(recipient=request.user, lida=False).count()
    return JsonResponse({'count': count})


@login_required
def settings_view(request):
    """View de configurações do usuário"""
    if not hasattr(request.user, 'profile'):
        UserProfile.objects.create(user=request.user, role='admin' if request.user.is_superuser else 'colaborador')
    user_profile = request.user.profile
    
    if request.method == 'POST':
        # Atualizar configurações
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        
        user_profile.phone = request.POST.get('phone', user_profile.phone)
        user_profile.bio = request.POST.get('bio', user_profile.bio)
        user_profile.cep = request.POST.get('cep', user_profile.cep)
        user_profile.logradouro = request.POST.get('logradouro', user_profile.logradouro)
        user_profile.numero = request.POST.get('numero', user_profile.numero)
        user_profile.complemento = request.POST.get('complemento', user_profile.complemento)
        user_profile.bairro = request.POST.get('bairro', user_profile.bairro)
        user_profile.cidade = request.POST.get('cidade', user_profile.cidade)
        user_profile.estado = request.POST.get('estado', user_profile.estado)
        user_profile.save()
        
        return redirect('tasks:settings')
    
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'tasks/settings.html', context)


@login_required
def kanban_view(request):
    """Visualização Kanban de Tarefas por Status"""
    if not hasattr(request.user, 'profile'):
        UserProfile.objects.create(user=request.user, role='admin' if request.user.is_superuser else 'colaborador')
    user_profile = request.user.profile

    # Filtrar tarefas baseado no role do usuário
    if user_profile.role == 'gestor':
        all_tasks = Task.objects.filter(created_by=request.user)
    elif user_profile.role == 'colaborador':
        all_tasks = Task.objects.filter(assigned_to=request.user)
    else:
        all_tasks = Task.objects.all()

    context = {
        'tarefas_abertas': all_tasks.filter(status='aberta').select_related('assigned_to', 'created_by'),
        'tarefas_alocadas': all_tasks.filter(status='alocada').select_related('assigned_to', 'created_by'),
        'tarefas_concluidas': all_tasks.filter(status='concluida').select_related('assigned_to', 'created_by'),
        'tarefas_finalizadas': all_tasks.filter(status='finalizada').select_related('assigned_to', 'created_by'),
    }
    return render(request, 'tasks/kanban.html', context)


@login_required
def calendar_view(request):
    """Visualização Calendário de Tarefas por Data de Vencimento"""
    from datetime import date
    import json

    if not hasattr(request.user, 'profile'):
        UserProfile.objects.create(user=request.user, role='admin' if request.user.is_superuser else 'colaborador')
    user_profile = request.user.profile

    # Filtrar tarefas com due_date baseado no role
    if user_profile.role == 'gestor':
        tasks_with_dates = Task.objects.filter(created_by=request.user, due_date__isnull=False)
    elif user_profile.role == 'colaborador':
        tasks_with_dates = Task.objects.filter(assigned_to=request.user, due_date__isnull=False)
    else:
        tasks_with_dates = Task.objects.filter(due_date__isnull=False)

    # Preparar eventos para o FullCalendar (formato JSON)
    events = []
    for task in tasks_with_dates:
        # Cor baseada na prioridade
        color_map = {
            'urgente': '#ef4444',  # red
            'alta': '#f97316',     # orange
            'normal': '#3b82f6',   # blue
            'baixa': '#22c55e',    # green
        }
        color = color_map.get(task.priority, '#6b7280')

        events.append({
            'id': task.pk,
            'title': task.title,
            'start': task.due_date.isoformat(),
            'url': f'/tasks/{task.pk}/',
            'backgroundColor': color,
            'borderColor': color,
        })

    context = {
        'events_json': json.dumps(events),
    }
    return render(request, 'tasks/calendar.html', context)


# ─────────────────────────────────────
# GESTÃO DE ÁREAS DO PRÉDIO (GESTOR)
# ─────────────────────────────────────

def _is_gestor_or_admin(user):
    """Verifica se o usuário é Gestor ou Admin."""
    profile = getattr(user, 'profile', None)
    return profile and profile.role in ('gestor', 'admin')


@login_required
def area_list_view(request):
    """Lista todas as áreas do prédio."""
    if not _is_gestor_or_admin(request.user):
        return redirect('tasks:dashboard')
    areas = AreaPredio.objects.all()
    return render(request, 'tasks/area_list.html', {'areas': areas})


@login_required
def area_create_view(request):
    """Cria uma nova área do prédio."""
    if not _is_gestor_or_admin(request.user):
        return redirect('tasks:dashboard')
    from django.contrib.auth.models import User as AuthUser

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        descricao = request.POST.get('descricao', '').strip()
        andar = request.POST.get('andar', '').strip()
        responsavel_id = request.POST.get('responsavel')
        ativo = request.POST.get('ativo') == 'on'

        if not nome:
            return render(request, 'tasks/area_form.html', {
                'error': 'O nome da área é obrigatório.',
                'users': AuthUser.objects.all(),
                'form_action': 'create',
            })

        responsavel = AuthUser.objects.filter(pk=responsavel_id).first() if responsavel_id else None
        AreaPredio.objects.create(
            nome=nome, descricao=descricao, andar=andar,
            responsavel=responsavel, ativo=ativo
        )
        return redirect('tasks:area_list')

    return render(request, 'tasks/area_form.html', {
        'users': AuthUser.objects.all(),
        'form_action': 'create',
    })


@login_required
def area_edit_view(request, pk):
    """Edita uma área do prédio."""
    if not _is_gestor_or_admin(request.user):
        return redirect('tasks:dashboard')
    from django.contrib.auth.models import User as AuthUser

    area = get_object_or_404(AreaPredio, pk=pk)

    if request.method == 'POST':
        area.nome = request.POST.get('nome', area.nome).strip()
        area.descricao = request.POST.get('descricao', area.descricao).strip()
        area.andar = request.POST.get('andar', area.andar).strip()
        responsavel_id = request.POST.get('responsavel')
        area.responsavel = AuthUser.objects.filter(pk=responsavel_id).first() if responsavel_id else None
        area.ativo = request.POST.get('ativo') == 'on'
        area.save()
        return redirect('tasks:area_list')

    return render(request, 'tasks/area_form.html', {
        'area': area,
        'users': AuthUser.objects.all(),
        'form_action': 'edit',
    })


@login_required
def area_delete_view(request, pk):
    """Desativa (soft-delete) ou exclui uma área do prédio."""
    if not _is_gestor_or_admin(request.user):
        return redirect('tasks:dashboard')
    area = get_object_or_404(AreaPredio, pk=pk)
    if request.method == 'POST':
        area.delete()
        return redirect('tasks:area_list')
    return render(request, 'tasks/area_confirm_delete.html', {'area': area})
