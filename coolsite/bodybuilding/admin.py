from django.contrib import admin
from .models import *


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'about')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Muscle)
class MuscleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'about')
    list_display_links = ('id', 'name')
    filter_horizontal = ['exercises']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(SportNutrition)
class SportNutritionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(CalorieCount)
class CalorieCountAdmin(admin.ModelAdmin):
    list_display = ('calorie', 'date')

