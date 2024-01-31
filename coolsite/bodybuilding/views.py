from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormView, FormMixin

from .forms import *
from .models import *

menu = [{'title': 'Мышечные группы', 'url_name': 'muscles'},
        {'title': 'Упражнения', 'url_name': 'exercises'}]


class MainPage(ListView):
    model = Recipe
    template_name = 'bodybuilding/index.html'
    context_object_name = 'recipes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        return context


class Muscles(ListView):
    model = Muscle
    template_name = 'bodybuilding/muscles.html'
    context_object_name = 'muscles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Мышечные группы'
        return context


class Exercises(ListView):
    model = Exercise
    template_name = 'bodybuilding/exercises.html'
    context_object_name = 'exercises'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Упражнения'
        return context


class Recipes(ListView):
    model = Recipe
    template_name = 'bodybuilding/recipes.html'
    context_object_name = 'recipes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Рецепты'
        return context


class ShowMuscle(ListView):
    model = Muscle
    template_name = 'bodybuilding/muscle.html'
    context_object_name = 'muscle'

    def get_queryset(self):
        return Muscle.objects.get(slug=self.kwargs['muscleSlug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = str(context['muscle'].name)
        context['exercises'] = context['muscle'].exercises.all()
        return context


class ShowExercise(ListView):
    model = Exercise
    template_name = 'bodybuilding/exercise.html'
    context_object_name = 'exercise'

    def get_queryset(self):
        return Exercise.objects.get(slug=self.kwargs['exerciseSlug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = str(context['exercise'].name)
        return context


class ShowRecipe(ListView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'bodybuilding/recipe.html'

    def get_queryset(self):
        return Recipe.objects.get(slug=self.kwargs['recipeSlug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = str(context['recipe'].name)
        return context


class ShowSportNutrition(ListView):
    model = SportNutrition
    context_object_name = 'sportNutrition'
    template_name = 'bodybuilding/nutrition.html'

    def get_queryset(self):
        return SportNutrition.objects.get(slug=self.kwargs['spotrNutritionSlug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = str(context['sportNutrition'].name)
        return context


class Registration(CreateView, FormMixin):
    form_class = RegisterUserForm
    template_name = 'bodybuilding/registration.html'
    success_url = reverse_lazy('home')


class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'bodybuilding/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
