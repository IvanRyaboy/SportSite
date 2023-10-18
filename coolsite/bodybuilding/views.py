from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

menu = [{'title': 'Мышечные группы', 'url_name': 'muscles'},
        {'title': 'Упражнения', 'url_name': 'exercises'},]


def index(request):
    muscles = Muscle.objects.all()
    recipes = Recipe.objects.all()
    sportNutrition = SportNutrition.objects.all()
    context = {
        'menu': menu,
        'title': "Главное меню",
        'muscles': muscles,
        'recipes': recipes,
        'sportNutrition': sportNutrition
    }
    return render(request, 'bodybuilding/index.html', context=context)


def muscles(request):
    muscles = Muscle.objects.all()
    context = {
        'menu': menu,
        'muscles': muscles
    }
    return render(request, 'bodybuilding/muscles.html', context=context)


def exercises(request):
    exercises = Exercise.objects.all()
    context = {
        'menu': menu,
        'exercises': exercises
    }
    return render(request, 'bodybuilding/exercises.html', context=context)


def show_muscle(request, muscleSlug):
    title = Muscle.objects.get(slug=muscleSlug)
    exercises = title.exercises.all()
    context = {
        'menu': menu,
        'title': title,
        'muscleSlug': muscleSlug,
        'exercises': exercises
    }
    return render(request, 'bodybuilding/muscle.html', context=context)


def show_exercise(request, exerciseSlug):
    exercise = Exercise.objects.get(slug=exerciseSlug)
    context = {
        'menu': menu,
        'exercise': exercise
    }
    return render(request, 'bodybuilding/exercise.html', context=context)


def show_recipe(request, recipeSlug):
    recipe = Recipe.objects.get(slug=recipeSlug)
    context = {
        'menu': menu,
        'recipe': recipe
    }
    return render(request, 'bodybuilding/recipe.html', context=context)


def show_sportNutrition(request, sportNutritionSlug):
    sportNutrition = SportNutrition.objects.get(slug=sportNutritionSlug)
    context = {
        'menu': menu,
        'sportNutrition': sportNutrition
    }
    return render(request, 'bodybuilding/nutrition.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
