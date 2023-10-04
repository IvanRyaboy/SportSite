from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', index),
    path('muscle/<int:muscle_id>/', showMuscle, name='muscle'),
    path('exercise/<int:exercise_id>/', showExercise, name='exercise'),
    path('recipe/<int:recipe_id>/', showRecipe, name='recipe'),
    path('admin/', admin.site.urls),
]
