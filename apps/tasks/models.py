from django.db import models
from django.contrib.auth.models import User

class TipoProblem(models.Model):
    """Modelo para Tipos de Problemas Predefinidos"""
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome
        
    class Meta:
        verbose_name = "Tipo de Problema"
        verbose_name_plural = "Tipos de Problemas"

class Task(models.Model):
    """Modelo de Tarefa de Manutenção"""
    
    PRIORITY_CHOICES = [
        ('baixa', 'Baixa'),
        ('normal', 'Normal'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]
    
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('alocada', 'Alocada'),
        ('concluida', 'Concluída'),
        ('finalizada', 'Finalizada'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberta')
    
    # Relacionamentos
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tasks_created')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks_assigned')
    
    # Datas
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    # Localização e Tipo
    location = models.CharField(max_length=200, blank=True)
    tipo_problema = models.ForeignKey(TipoProblem, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarefas')
    
    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"
    
    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        ordering = ['-created_at']


class TaskEvidence(models.Model):
    """Modelo para Evidências de Conclusão de Tarefa"""
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='evidences')
    photo = models.ImageField(upload_to='evidences/', blank=True, null=True)
    description = models.TextField(blank=True)
    tempo_gasto = models.CharField(max_length=50, blank=True, help_text="Ex: 2 horas, 30 minutos")
    materiais_utilizados = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Evidência - {self.task.title}"
    
    class Meta:
        verbose_name = "Evidência"
        verbose_name_plural = "Evidências"


class Message(models.Model):
    """Modelo para Mensagens/Chat por Tarefa"""
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Mensagem de {self.sender.username} em {self.task.title}"
    
    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"
        ordering = ['created_at']
