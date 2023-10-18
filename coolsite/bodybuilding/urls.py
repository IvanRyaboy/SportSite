from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', index),
    path('muscles/', muscles, name='muscles'),
    path('exercises/', exercises, name='exercises'),
    path('muscles/<slug:muscleSlug>/', show_muscle, name='muscle'),
    path('exercises/<slug:exerciseSlug>/', show_exercise, name='exercise'),
    path('recipe/<slug:recipeSlug>/', show_recipe, name='recipe'),
    path('nutrition/<slug:sportNutritionSlug>/', show_sportNutrition, name='sportNutrition'),
    path('admin/', admin.site.urls),
]
