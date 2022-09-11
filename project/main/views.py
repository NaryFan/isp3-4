from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import DishesForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import logging
import asyncio
from asgiref.sync import sync_to_async


logger = logging.getLogger('main')


def home(request):
    logger.info("Good work")
    return render(request, 'main/home_page2.html', {'title': 'О готовке'})


@login_required(login_url='login_page')
def index(request):
    return render(request, 'main/home.html', {'title': 'О готовке'})


@login_required(login_url='login_page')
def about(request):
    return render(request, 'main/about.html')


@login_required(login_url='login_page')
def create(request):
    error = ''
    if request.method == 'POST':
        form = DishesForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("Блюдо было успешно создано!")
            return redirect('menu_page')
        else:
            logger.error("Форма заполнения была неверной")
            error = 'Форма заполнения была неверной'

    form = DishesForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def update(request, pk):
    dish = asyncio.run(get_dishes_id(pk))
    form = DishesForm(instance=dish)

    if request.method == 'POST':
        form = DishesForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('menu_page')
        else:
            logger.error("Форма заполнения была неверной")
            error = 'Форма была неверной'
    context = {
        'form': form
    }
    return render(request, 'main/change_dish.html', context)


@sync_to_async
def get_dishes_id(pk):
    dish = Dishes.objects.get(id=pk)
    return dish


def delete(request, pk):
    dish = asyncio.run(get_dishes_id(pk))

    if request.method == 'POST':
        dish.delete()
        return redirect('menu_page')

    context = {
        'form': dish
    }
    return render(request, 'main/menu_page.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                logger.info("Регистрация прошла успешно!")
                return redirect('popup_window')
        else:
            form = CreateUserForm()

    contex = {'form': form}
    return render(request, 'main/register_page.html', contex)


"""Проверка набора учета данных с authenticate"""


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
     if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            """с помощью метода login и выполняется вход """
            login(request, user)
            logger.info("Вход был успешно выполнен!")
            return redirect('home')
        else:
            logger.error("Пароль или имя пользователя был введен неправильно!")
            messages.info(request, 'Пароль или имя пользователя был введён неправильно!')

     contex = {}
     return render(request, 'main/login_page.html', contex)


def logout_user(request):
    logout(request)
    return redirect('login_page')


def popup(request):
    return render(request, 'main/popup_window.html')


@login_required(login_url='login_page')
def menu(request):
    # получаем все объекты из класса
    dishes = asyncio.run(get_obj_order_by())
    return render(request, 'main/menu_page.html', {'dishes': dishes})


@sync_to_async
def get_obj_order_by():
    dishes = Dishes.objects.order_by('-id')
    return dishes