from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DishesForm(ModelForm):
    class Meta:# в этом классе указываем дополнительные настройки
        model = Dishes #показываем с какой моделью мы работаем
        fields = ['nameofdishes', 'description', 'howTOcook', 'category_id']#указываем какие поля должны присутствовать в самой формочке
        widgets = {"nameofdishes": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название блюда'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "howTOcook": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание готовки'
            }),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]