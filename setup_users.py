from django.contrib.auth.models import User
from apps.users.models import UserProfile

users_data = [
    ('admin', 'admin@chaplin.com', 'admin123', 'admin', True),
    ('gestor', 'gestor@chaplin.com', 'gestor123', 'gestor', False),
    ('lider', 'lider@chaplin.com', 'lider123', 'lider', False),
    ('colaborador', 'colaborador@chaplin.com', 'colaborador123', 'colaborador', False),
]

for username, email, password, role, is_superuser in users_data:
    user, created = User.objects.get_or_create(username=username, defaults={'email': email})
    user.email = email
    user.set_password(password)
    user.is_superuser = is_superuser
    user.is_staff = is_superuser
    user.save()
    
    # Profile is created by signal, just update it
    profile = user.profile
    profile.role = role
    profile.save()
    
    status = "Criado" if created else "Atualizado"
    print(f"Usuário {username} ({role}) {status} com sucesso.")
