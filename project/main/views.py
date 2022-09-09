from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from .forms import TaskForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm


def index(request):
    tasks = Task.objects.order_by('-id')  # получаем все оъекты из класса
    return render(request, 'main/home.html', {'title': 'О готовке', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

def register(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateUserForm()

    contex = {'form': form}
    return render(request, 'main/register_page.html', contex)


def login(request):
    contex = {}
    return render(request, 'main/login_page.html', contex)