from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', index),
    path('muscle/<int:muscle_id>/', show_muscle, name='muscle'),
    path('exercise/<int:exercise_id>/', show_exercise, name='exercise'),
    path('admin/', admin.site.urls),
]
