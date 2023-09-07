from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .functions import *

menu = ['Главное меню', 'О сайте', 'Мышечные группы']
muscles = Muscle.objects.all()


def index(request):
    relations = AllRelations()
    context = {
        'menu': menu,
        'title': "Главное меню",
        'relations': relations
    }
    return render(request, 'bodybuilding/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
