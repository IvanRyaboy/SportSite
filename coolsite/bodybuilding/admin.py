from django.contrib import admin
from .models import *


@admin.register(Muscle)
class MuscleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'about')
    list_display_links = ('id', 'name')


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'about')
    filter_horizontal = ['muscles']
