from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', index),
    path('muscle/<int:muscle_id>/', show_muscle, name='muscle'),
    path('exercise/<int:exercise_id>/', show_exercise, name='exercise'),
    path('recipe/<int:recipe_id>/', show_recipe, name='recipe'),
    path('admin/', admin.site.urls),
]
