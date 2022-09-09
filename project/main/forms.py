from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:# в этом классе указываем дополнительные настройки
        model = Task #показываем с какой моделью мы работаем
        fields = ["nameofdishes", "task"]#указываем какие поля должны присутствовать в самой формочке
        widgets = {"nameofdishes": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название блюда'
        }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }