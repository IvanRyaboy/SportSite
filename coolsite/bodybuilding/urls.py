from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', MainPage.as_view()),
    path('muscles/', Muscles.as_view(), name='muscles'),
    path('exercises/', Exercises.as_view(), name='exercises'),
    path('recipes/', Recipes.as_view(), name='recipes'),
    path('muscles/<slug:muscleSlug>/', ShowMuscle.as_view(), name='muscle'),
    path('exercises/<slug:exerciseSlug>/', ShowExercise.as_view(), name='exercise'),
    path('recipe/<slug:recipeSlug>/', ShowRecipe.as_view(), name='recipe'),
    path('nutrition/<slug:sportNutritionSlug>/', ShowSportNutrition.as_view(), name='sportNutrition'),
    path('admin/', admin.site.urls),
]
