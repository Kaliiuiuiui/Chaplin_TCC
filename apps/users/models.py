from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Especialidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Especialidade"
        verbose_name_plural = "Especialidades"

class ActivityLog(models.Model):
    admin_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='admin_logs')
    target_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='target_logs')
    action = models.CharField(max_length=255)
    role_old = models.CharField(max_length=50, blank=True, null=True)
    role_new = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.admin_user} -> {self.action} on {self.target_user} at {self.timestamp}"

    class Meta:
        verbose_name = "Log de Atividade"
        verbose_name_plural = "Logs de Atividades"

class UserProfile(models.Model):
    """Extensão do modelo User do Django com informações adicionais"""
    
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('gestor', 'Gestor do Prédio'),
        ('lider', 'Líder de Equipe'),
        ('colaborador', 'Colaborador'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='colaborador')
    especialidade = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, null=True, blank=True, related_name='profissionais')
    phone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    
    # Endereço (ViaCEP)
    cep = models.CharField(max_length=9, blank=True)
    logradouro = models.CharField(max_length=255, blank=True)
    numero = models.CharField(max_length=20, blank=True)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)

    # Autenticação de Dois Fatores (2FA)
    two_factor_enabled = models.BooleanField(default=False, verbose_name='2FA Ativo')
    totp_secret = models.CharField(max_length=64, blank=True, verbose_name='Chave TOTP')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.get_role_display()})"
    
    class Meta:
        verbose_name = "Perfil de Usuário"
        verbose_name_plural = "Perfis de Usuários"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
