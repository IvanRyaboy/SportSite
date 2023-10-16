from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', index),
    path('muscles/', muscles, name='muscles'),
    path('exercises/', exercises, name='exercises'),
    path('muscles/<int:muscle_id>/', show_muscle, name='muscle'),
    path('exercises/<int:exercise_id>/', show_exercise, name='exercise'),
    path('recipe/<int:recipe_id>/', show_recipe, name='recipe'),
    path('nutrition/<int:sportNutrition_id>/', show_sportNutrition, name='sportNutrition'),
    path('admin/', admin.site.urls),
]
