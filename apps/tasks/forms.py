from django import forms
from .models import Task, TaskEvidence

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'location', 'due_date',
                  'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-orange-500', 'placeholder': 'Título da tarefa'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-orange-500', 'rows': 4}),
            'priority': forms.Select(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-orange-500'}),
            'location': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-orange-500', 'placeholder': 'Ex: Sala 302, Corredor B...'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-orange-500'}),
            'cep': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-orange-500', 'placeholder': '00000-000', 'maxlength': '9', 'id': 'task_cep'}),
            'logradouro': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-orange-500 bg-gray-50', 'readonly': 'readonly', 'id': 'task_logradouro'}),
            'numero': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-orange-500', 'placeholder': 'Número', 'id': 'task_numero'}),
            'complemento': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-orange-500', 'placeholder': 'Apto, sala, bloco...', 'id': 'task_complemento'}),
            'bairro': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-orange-500 bg-gray-50', 'readonly': 'readonly', 'id': 'task_bairro'}),
            'cidade': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-orange-500 bg-gray-50', 'readonly': 'readonly', 'id': 'task_cidade'}),
            'estado': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-orange-500 bg-gray-50', 'readonly': 'readonly', 'id': 'task_estado', 'maxlength': '2'}),
        }

class TaskEvidenceForm(forms.ModelForm):
    class Meta:
        model = TaskEvidence
        fields = ['photo', 'description']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'rows': 3}),
        }
