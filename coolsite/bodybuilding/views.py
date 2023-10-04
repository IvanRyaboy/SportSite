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
    exercises = title.exercises.all()
    context = {
        'menu': menu,
        'title': title,
        'muscle_id': muscle_id,
        'exercises': exercises
    }
    return render(request, 'bodybuilding/muscle.html', context=context)


def show_exercise(request, exercise_id):
    exercise = Exercise.objects.get(pk=exercise_id)
    context = {
        'menu': menu,
        'exercise': exercise
    }
    return render(request, 'bodybuilding/exercise.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
