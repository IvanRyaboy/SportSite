from django.contrib import admin
from .models import *


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'about')


@admin.register(Muscle)
class MuscleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'about')
    list_display_links = ('id', 'name')
    filter_horizontal = ['exercises']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
