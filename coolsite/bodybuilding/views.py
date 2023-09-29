from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

menu = ['Главное меню', 'О сайте', 'Мышечные группы']


def index(request):
    muscles = Muscle.objects.all()
    context = {
        'menu': menu,
        'title': "Главное меню",
        'muscles': muscles
    }
    return render(request, 'bodybuilding/index.html', context=context)


def show_muscle(request, muscle_id):
    title = Muscle.objects.get(pk=muscle_id)
    context = {
        'menu': menu,
        'title': title.name,
        'muscle_id': muscle_id
    }
    return render(request, 'bodybuilding/muscle.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
